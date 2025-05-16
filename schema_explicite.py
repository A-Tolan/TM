import numpy as np
import matplotlib.pyplot as plt

# Paramètres
L = 1.0      # longueur de la barre
T = 0.1      # temps final
N = 100      # nombre de points spatiaux
M = 1000     # nombre de pas de temps

h = L / N
tau = T / M
x = np.linspace(0, L, N+1)
t = np.linspace(0, T, M+1)

lambda_ = tau / h**2
print(f"lambda = {lambda_:.4f}")

# Vérification de stabilité
if lambda_ > 0.5:
    print("WARNING: Schéma potentiellement instable (lambda > 0.5)")

# Fonctions initiales
def f1(x):
    return np.sin(2 * np.pi * x)

def f2(x):
    return np.where(x <= 0.5, 2*x, 2*(1 - x))

# Construction de la matrice A (tridiagonale)
I = np.eye(N-1)
A = np.diag([-2]*(N-1)) + np.diag([1]*(N-2), 1) + np.diag([1]*(N-2), -1)
M_explicit = I + lambda_ * A

# Fonction de résolution avec schéma explicite vectorisé
def solve_explicit(f):
    u = np.zeros((M+1, N+1))
    u[0, :] = f(x)
    for n in range(0, M):
        u_next = np.dot(M_explicit, u[n, 1:N])
        u[n+1, 1:N] = u_next
    return u

# Résolution pour f1 et f2
u_f1 = solve_explicit(f1)
u_f2 = solve_explicit(f2)

# Affichage
def plot_solution(u, title, filename):
    plt.figure(figsize=(8,5))
    for n_plot in [0, int(M*0.25), int(M*0.5), int(M*0.75), M]:
        plt.plot(x, u[n_plot, :], label=f't = {t[n_plot]:.3f}')
    plt.xlabel("x")
    plt.ylabel("u(x,t)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig(filename)
    plt.close()


# Tracer les deux cas
plot_solution(u_f1, "Évolution de u(x,t) avec f₁(x) = sin(2πx)","explicite_solution_f1.png")
plot_solution(u_f2, "Évolution de u(x,t) avec f₂(x) en triangle","explicite_solution_f2.png")


