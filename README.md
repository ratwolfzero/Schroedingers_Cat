# Schrödinger’s Cat Simulation

This repository contains a **Python-based simulation of Schrödinger’s cat**, a famous quantum mechanics thought experiment, using the **QuTiP** library.

The simulation visualizes the quantum superposition of a cat being *alive* and *dead* in phase space via the **Wigner function**, showcasing:

* **Coherent evolution**
* **Decoherence**
* **Wave function collapse**

![Simulation](schrodinger_cat.gif)

---

## 📖 Overview

Erwin Schrödinger’s 1935 thought experiment illustrates the paradoxical nature of quantum superposition when applied to macroscopic objects:

* A cat is sealed in a box with a radioactive atom, a Geiger counter, and a vial of poison.
* If the atom decays (50% probability), the poison is released → the cat dies.
* Until observed, quantum mechanics suggests the cat exists in a **superposition of alive and dead**.

This simulation models a **quantum analog of the cat state** using a **coherent state superposition** in a harmonic oscillator, visualized through the **Wigner function in phase space**.

It demonstrates:

* Coherent evolution under a Kerr Hamiltonian → twisting interference patterns
* Decoherence due to environmental interactions → fading quantum interference
* Interactive collapse via key press → mimicking measurement

---

## 🧮 Mathematical Background

The simulation is based on a quantum harmonic oscillator with Hilbert space dimension:

$$
N = 30
$$

### Initial Cat State

The Schrödinger cat state is a superposition of two coherent states:

$$
|\psi_\text{cat}\rangle = \frac{1}{\sqrt{2 \,(1 + e^{-2|\alpha|^2})}} \Big( |\alpha\rangle + |-\alpha\rangle \Big), \quad \alpha = 2.0
$$

where $|\alpha\rangle$ and $|-\alpha\rangle$ are coherent states with amplitudes $\alpha$ and $-\alpha$.

The corresponding density matrix is:

$$
\rho_0 = |\psi_\text{cat}\rangle \langle \psi_\text{cat}|
$$

---

### Wigner Function

The **Wigner function** $W(x,p)$ represents the quantum state in phase space, computed over a grid:

$$
x, p \in [-5, 5]
$$

* Two Gaussian peaks → “Alive” ($x \approx 2$) and “Dead” ($x \approx -2$)
* Interference fringes → signature of quantum superposition

Decomposition of the Wigner function:

$$
W(x,p) = \frac{1}{\mathcal{N}^2} \Big[ W_\alpha(x,p) + W_{-\alpha}(x,p) + W_\text{interf}(x,p) \Big]
$$

where:

* $W_\alpha(x,p)$ = Wigner function of $|\alpha\rangle$
* $W_{-\alpha}(x,p)$ = Wigner function of $|-\alpha\rangle$
* $W_\text{interf}(x,p)$ = interference term
* $\mathcal{N}^2 = 2(1 + e^{-2|\alpha|^2})$

![initial](initial_state.png)

---

## Simulation Phases

### 1. Coherent Evolution (t = 2 → 10)

The state evolves under a **Kerr Hamiltonian**:

$$
H_\text{Kerr} = \kappa \, (a^\dagger a)^2, \quad \kappa = 0.1
$$

* Non-linear shearing causes interference fringes to **twist into spirals**
* Gaussian blobs **distort** in phase space

![Coherent](coherent_evolution.png)

---

### 2. Decoherence (t = 10 → 20)

After resetting to $\rho_0$, decoherence is applied via **amplitude damping**:

$$
c = \sqrt{\gamma} \, a, \quad \gamma = 0.05
$$

* No Hamiltonian applied ($H = 0$)
* Interference fringes **fade away**, leaving stationary blobs
* System resembles a **classical mixture**:

$$
\rho_\text{decoh} \approx \frac{1}{2} \Big( |\alpha\rangle \langle \alpha| + |-\alpha\rangle \langle -\alpha| \Big)
$$

![Decoherence](decoherence.png)

---

### 3. Collapse (Interactive Measurement)

Pressing **“o”** collapses the wave function to:

$$
|\psi_\text{cat}\rangle \to
\begin{cases}
|\alpha\rangle & \text{"Alive"} \\
|-\alpha\rangle & \text{"Dead"}
\end{cases}
$$

The plot updates with a single labeled blob: **Alive** or **Dead**.

![Collapse](alive.png)

---

## 🔍 Interpreting the Results

* **t = 0 → 2 (Static Display):**
  Two blobs (“Alive” at $x \approx 2$, “Dead” at $x \approx -2$) with straight interference fringes.

* **t = 2 → 10 (Coherent Evolution):**
  Kerr Hamiltonian twists fringes into spirals, blobs distort.

* **t = 10 → 20 (Decoherence):**
  Fringes fade, blobs remain stationary → classical mixture.

* **Collapse (press “o”):**
  Single blob remains, labeled Alive or Dead.

---

## 🌌 Quantum Interpretations

* **Copenhagen:** Collapse occurs on measurement (“o” key)
* **Decoherence:** Environmental interaction destroys interference (phase 2)
* **Other views:** Many-Worlds, Bohmian Mechanics, QBism also consistent but not explicitly modeled

---

## 📚 References

* N. Lambert et al., *QuTiP 5: The Quantum Toolbox in Python*, arXiv:2412.04705 (2024). [https://arxiv.org/abs/2412.04705](https://arxiv.org/abs/2412.04705)
* QuTiP: [https://qutip.org](https://qutip.org)
* Schrödinger, E. (1935). *The Present Situation in Quantum Mechanics.*
* Zeh, H. D. (1970). *On the Interpretation of Measurement in Quantum Theory.* *Foundations of Physics* 1, 69–76.
* Zurek, W. H. (2003). *Decoherence and the Transition from Quantum to Classical.* [https://doi.org/10.48550/arXiv.quant-ph/0306072](https://doi.org/10.48550/arXiv.quant-ph/0306072)

---

## ⚙️ Technical FAQ

**Q: Why are the red blobs darker during decoherence?**.

A: Visualization effect; darker red emphasizes remaining amplitude after interference fades.

**Q: Why do blobs shift slightly during decoherence?**.

A: Amplitude damping with $\gamma = 0.05$ can slightly move coherent states toward the origin.

**Q: Are the interference fringes correct?**.

A: Yes; sparse fringes reflect the Wigner function for $\alpha = 2.0$.

**Q: Is the time step accurate?**.

A: 200 timesteps over 20 units ($dt \approx 0.1$) is sufficient; increase for higher precision.

**Q: Is amplitude damping the only decoherence model?**.

A: In this simulation, yes. You can modify `c_ops_decoherence` for other models (e.g., dephasing).

**Q: Is the Wigner function normalized?**.

A: Yes, QuTiP’s `wigner` ensures normalization; colormap scaling is for plotting.

**Q: How does collapse work?**.

A: Pressing 'o' randomly selects $|\alpha\rangle$ or $|-\alpha\rangle$, simulating measurement.

**Q: Can accuracy be improved?**.  

A: Increase Hilbert space $N$ or grid resolution in $x,p$, at the cost of performance.
