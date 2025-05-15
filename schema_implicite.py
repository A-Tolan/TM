import numpy as np
import matplotlib.pyplot as plt

# Paramètres
L = 1.0
T = 0.1
N = 100
M = 1000

h = L / N
tau = T / M
x = np.linspace(0, L, N+1)
t = np.linspace(0, T, M+1)
lambda_ = tau / h**2

# Fonctions initiales
def f1(x): return np.sin(2*np.pi*x)
def f2(x): return np.where(x <= 0.5, 2*x, 2*(1 - x))

# Construction de la matrice A tridiagonale
main_diag = (1 + 2*lambda_) * np.ones(N-1)
off_diag = -lambda_ * np.ones(N-2)
A = np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)

# Résolution avec schéma implicite
def solve_implicit(f):
    u = np.zeros((M+1, N+1))
    u[0, :] = f(x)
    for n in range(M):
        rhs = u[n, 1:N]
        u[n+1, 1:N] = np.linalg.solve(A, rhs)
    return u

# Résolution pour f1 et f2
u1 = solve_implicit(f1)
u2 = solve_implicit(f2)

# Affichage
def plot_solution(u, title):
    plt.figure(figsize=(8,5))
    for n_plot in [0, int(M*0.25), int(M*0.5), int(M*0.75), M]:
        plt.plot(x, u[n_plot, :], label=f't = {t[n_plot]:.3f}')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('u(x,t)')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_solution(u1, "Schéma implicite – f₁(x) = sin(2πx)")
plot_solution(u2, "Schéma implicite – f₂(x) en triangle")
