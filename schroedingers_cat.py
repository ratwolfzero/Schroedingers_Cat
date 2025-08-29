import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from qutip import coherent, mesolve, destroy, wigner, Qobj
import random

# --- Parameters ---
N = 30                   # Hilbert space dimension for accuracy
alpha = 2.0              # Coherent state amplitude
timesteps = 200          # Total animation frames
t_total = 20             # Total time in units
t_decohere_start = 10.0  # Time when decoherence starts
t_static_end = 2.0       # Time until static initial state display ends
gamma = 0.05             # Decoherence rate
kerr_strength = 0.1      # Kerr nonlinearity strength for twisting

# --- Time lists ---
tlist_total = np.linspace(0, t_total, timesteps)
dt = tlist_total[1] - tlist_total[0]  # Exact dt from tlist

# --- Operators ---
a = destroy(N)

# --- Initial Schrödinger cat state ---
psi1 = coherent(N, alpha)
psi2 = coherent(N, -alpha)
cat = (psi1 + psi2).unit()
initial_rho = cat * cat.dag()  # Store initial density matrix

# --- Hamiltonians ---
# Kerr Hamiltonian for phase 1 twisting
H_twist = kerr_strength * (a.dag() * a)**2
# Zero Hamiltonian for static display
H_static = Qobj(np.zeros((N, N)), dims=[[N], [N]])
# Zero Hamiltonian for phase 2
H_decohere = Qobj(np.zeros((N, N)), dims=[[N], [N]])

# --- Collapse operators for decoherence ---
c_ops_decoherence = [np.sqrt(gamma) * a]

# --- Phase space grid ---
x = np.linspace(-5, 5, 130)  # Increased resolution
p = np.linspace(-5, 5, 130)  # Increased resolution

# --- Precompute phase 1: static period + twisting ---
frames_phase1 = np.where(tlist_total < t_decohere_start)[0]
rho_rot = []
if len(frames_phase1) > 0:
    # Split phase 1 into static and twisting periods
    t_static_frames = np.where(tlist_total[frames_phase1] <= t_static_end)[0]
    t_twist_frames = np.where(tlist_total[frames_phase1] > t_static_end)[0]

    # Static period: no evolution
    for _ in t_static_frames:
        rho_rot.append(initial_rho)  # Append initial state for static period

    # Twisting period: evolve from t=2 to t=10
    if len(t_twist_frames) > 0:
        t_twist = tlist_total[frames_phase1][t_twist_frames] - t_static_end
        result_rot = mesolve(H_twist, initial_rho, t_twist, c_ops=[])
        rho_rot.extend(result_rot.states)

# --- Flags and state tracking ---
collapse_state = None
decoherence_started = False
rho_prev = rho_rot[-1] if rho_rot else initial_rho

# --- Prepare figure ---
fig, ax = plt.subplots(figsize=(6, 6))


def update(frame):
    global collapse_state, decoherence_started, rho_prev

    ax.clear()
    t = tlist_total[frame]

    if collapse_state is not None:
        rho_t = collapse_state
        title = "Box opened → wavefunction collapsed"
    else:
        # Determine phase
        if t >= t_decohere_start:
            if not decoherence_started:
                decoherence_started = True
                rho_prev = initial_rho  # Reset to initial state at start of phase 2
        else:
            decoherence_started = False  # Reset flag for animation repeat

        if not decoherence_started:
            # Phase 1: static or coherent evolution
            idx = frame if frame < len(rho_rot) else -1
            rho_t = rho_rot[idx]
            if t <= t_static_end:
                title = f"Static initial state (t={t:.2f})"
            else:
                title = f"Coherent evolution → spiral fringes & blob distortion (t={t:.2f})"
        else:
            # Phase 2: decoherence
            result = mesolve(H_decohere, rho_prev, [
                             0, dt], c_ops=c_ops_decoherence)
            rho_t = result.states[-1]
            rho_prev = rho_t
            title = f"Decoherence → interference fading (t={t:.2f})"

    # Compute Wigner function and plot
    W = wigner(rho_t, x, p)
    max_abs_W = np.max(np.abs(W))
    ax.contourf(x, p, W, 200, cmap="RdBu_r", vmin=-max_abs_W, vmax=max_abs_W)
    ax.set_xlabel("x")
    ax.set_ylabel("p")
    ax.set_title(title)
    ax.set_aspect('equal')

    # Label blobs during static phase
    if t <= t_static_end and collapse_state is None:
        ax.text(2, 0, 'Alive', color='black', fontsize=10, ha='center')
        ax.text(-2, 0, 'Dead', color='black', fontsize=10, ha='center')

    # Label collapsed state
    if collapse_state is not None:
        # Check which state the system collapsed to
        if np.allclose(collapse_state.full(), (psi1 * psi1.dag()).full(), atol=1e-6):
            ax.text(2, 0, 'Alive', color='black', fontsize=10, ha='center')
        elif np.allclose(collapse_state.full(), (psi2 * psi2.dag()).full(), atol=1e-6):
            ax.text(-2, 0, 'Dead', color='black', fontsize=10, ha='center')


def on_key(event):
    global collapse_state
    if event.key == 'o' and collapse_state is None:
        collapse_state = random.choice([psi1*psi1.dag(), psi2*psi2.dag()])
        print("Box opened! Wavefunction collapsed.")


# Connect key event
fig.canvas.mpl_connect('key_press_event', on_key)

# Run animation
interval = (t_total / timesteps) * 1000  # ms per frame
ani = FuncAnimation(fig, update, frames=timesteps,
                    interval=interval, repeat=True)

# Save as GIF
#fps = timesteps / t_total   # frames per second
#ani.save("schrodinger_cat.gif", writer="pillow", fps=fps)


plt.show()
