import numpy as np
import matplotlib.pyplot as plt

# Paramètres du problème
L, T, nx, nt, alpha = 1.0, 0.1, 50, 100, 1.0
dx, dt = L / (nx - 1), T / nt
x, t = np.linspace(0, L, nx), np.linspace(0, T, nt+1)
lambda_ = alpha * dt / dx**2

# Matrices A et B pour Crank-Nicholson
D = np.diag([-2]*nx) + np.diag([1]*(nx-1), 1) + np.diag([1]*(nx-1), -1)
D[0, :] = D[-1, :] = 0  # conditions de Dirichlet
I = np.eye(nx)
A, B = I - (lambda_/2) * D, I + (lambda_/2) * D

# Fonction pour résoudre et sauvegarder
def solve_and_save(f, title, filename):
    u = np.zeros((nt+1, nx))
    u[0, :] = f(x)
    u[:, 0] = u[:, -1] = 0  # conditions de Dirichlet
    for n in range(nt):
        b = np.dot(B, u[n, :])
        b[0] = b[-1] = 0
        u[n+1, :] = np.linalg.solve(A, b)
    plt.figure(figsize=(8, 5))
    for i in range(0, nt+1, nt//5):
        plt.plot(x, u[i, :], label=f"t = {t[i]:.3f}")
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("u(x,t)")
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

# Résolution pour les deux conditions initiales
solve_and_save(lambda x: np.sin(2 * np.pi * x), "Évolution avec Crank-Nicholson (f1(x))", "crank_evolution_f1.png")
solve_and_save(lambda x: np.where(x < 0.5, 2 * x, 2 * (1 - x)), "Évolution avec Crank-Nicholson (f2(x))", "crank_evolution_f2.png")
