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

This simulation models a quantum analog of the cat state using a **coherent state superposition** in a harmonic oscillator, visualized through the **Wigner function in phase space**.

It demonstrates:

* Coherent evolution under a Kerr Hamiltonian → twisting interference patterns.
* Decoherence due to environmental interactions → fading quantum interference.
* Interactive collapse via key press → mimicking measurement.

---

## 🧮 Mathematical Background

The simulation is based on a quantum harmonic oscillator with a Hilbert space dimension:

$$
N = 30
$$

### Initial Cat State

The Schrödinger cat state is a superposition of two coherent states:

$$
|\psi\rangle = \frac{1}{\sqrt{2}} \left( |\alpha\rangle + |-\alpha\rangle \right), \quad \alpha = 2.0
$$

where $|\alpha\rangle$ and $|-\alpha\rangle$ are coherent states with amplitudes $\alpha$ and $-\alpha$.

The density matrix is:

$$
\rho_0 = |\psi\rangle\langle\psi|
$$

The **Wigner function** $W(x, p)$ represents the quantum state in phase space, computed over a grid $x, p \in [-5, 5]$.

* Two Gaussian peaks → “alive” ($x \approx 2$) and “dead” ($x \approx -2$).
* Interference fringes → signature of quantum superposition.

![initiaö](initial_state.png)

---

### Simulation Phases

#### 1. Coherent Evolution (t = 2 → 10)

The state evolves under a **Kerr Hamiltonian**:

$$
H_{\text{Kerr}} = \kappa (a^\dagger a)^2, \quad \kappa = 0.1
$$

* Non-linear shearing causes interference fringes to **twist into spirals**.
* Gaussian blobs **distort** in phase space.

![Coherent](coherent_evolution.png)

---

#### 2. Decoherence (t = 10 → 20)

After resetting to $\rho_0$, decoherence is applied via **amplitude damping**:

$$
c = \sqrt{\gamma} a, \quad \gamma = 0.05
$$

* No Hamiltonian applied ($H = 0$).
* Interference fringes **fade away**, leaving stationary blobs.
* System resembles a **classical mixture**.

![Decoherence](decoherence.png)

---

#### 3. Collapse

Pressing **“o”** collapses the wave function to:

* $|\alpha\rangle\langle\alpha|$ → alive ($x \approx 2$)
* $|-\alpha\rangle\langle-\alpha|$ → dead ($x \approx -2$)

The plot updates with a single labeled blob: **Alive** or **Dead**.

![Collapse](alive.png)

---

### What the Simulation Shows

* **t = 0 → 2 (Static Display):**
  Two blobs (“Alive” at $x \approx 2$, “Dead” at $x \approx -2$) with straight fringes.
* **t = 2 → 10 (Coherent Evolution):**
  Kerr Hamiltonian twists fringes into spirals, blobs distort.
* **t = 10 → 20 (Decoherence):**
  Fringes fade, blobs remain stationary.

### Interactive Collapse

* Press **“o”** → collapse to one outcome (Alive or Dead).

### Visualization

* Wigner function plotted with:

  * **Red–blue colormap** (`RdBu_r`)
  * **Colorbar**
  * Light gray background + grid

---

## 🔍 Interpreting the Results

* **Static Phase (t=0 → 2):**

$$
W(x, p) \approx W_{\text{alive}}(x-2, p) + W_{\text{dead}}(x+2, p) + \text{interference terms}
$$

* **Coherent Evolution (t=2 → 10):**
  Non-linear dynamics twist fringes + shear blobs → isolated quantum behavior.

* **Decoherence (t=10 → 20):**

$$
\rho \approx \frac{1}{2} \left( |\alpha\rangle\langle\alpha| + |-\alpha\rangle\langle-\alpha| \right)
$$

Fringes disappear, leaving a **classical mixture**.

* **Collapse (press “o”):**
  Single blob remains, labeled Alive or Dead.

---

## 🌌 Quantum Interpretations

The simulation touches on key interpretations:

* **Copenhagen:** Collapse on measurement (“o” key).
* **Decoherence:** Phase 2 → environment destroys interference.
* **Other views:** Many-Worlds, Bohmian Mechanics, QBism also consistent, though not explicitly modeled.

---

## 📚 References

* N. Lambert, E. Giguère, P. Menczel, B. Li, P. Hopf, G. Suárez, M. Gali, J. Lishman, R. Gadhvi, R. Agarwal, A. Galicia, N. Shammah, P. Nation, J. R. Johansson, S. Ahmed, S. Cross, A. Pitchford, F. Nori, QuTiP 5: The Quantum Toolbox in Python, arXiv:2412.04705 (2024). <https://arxiv.org/abs/2412.04705>.
QuTiP: [https://qutip.org](https://qutip.org)
* Schrödinger, E. (1935). *The Present Situation in Quantum Mechanics.*
* Zurek, W. H. (2003). *Decoherence and the Transition from Quantum to Classical.*
