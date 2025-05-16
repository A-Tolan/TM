# Résolution Analytique de l'Équation de la Chaleur

Ce projet a pour objectif de résoudre analytiquement l'équation de la chaleur en utilisant différents schémas numériques. L'objectif principal est de comparer l'efficacité de ces schémas en termes de précision, de stabilité et de performance.

## Description

L'équation de la chaleur est une équation aux dérivées partielles (EDP) fondamentale en physique et en mathématiques appliquées. Ce projet explore plusieurs méthodes numériques pour résoudre cette EDP, notamment :

- **Schéma explicite** : Méthode simple mais conditionnellement stable.
- **Schéma implicite** : Méthode stable mais plus coûteuse en calcul.
- **Schéma de Crank-Nicolson** : Compromis entre précision et stabilité.

## Objectifs

1. Implémenter les différents schémas numériques pour résoudre l'équation de la chaleur.
2. Comparer les résultats obtenus avec une solution analytique de référence.
3. Évaluer les performances des schémas en termes de :
    - Temps de calcul.
    - Précision des résultats.
    - Stabilité numérique.

## Structure du Projet

- **Code** : Les implémentations des différents schémas sont disponibles dans des fichiers Python.
- **Données** : Les paramètres de simulation (conditions initiales, conditions aux limites, etc.) sont configurables.
- **Résultats** : Les comparaisons des schémas sont présentées sous forme de graphiques et de tableaux.

## Prérequis

- Python 3.x
- Bibliothèques nécessaires : `numpy`, `matplotlib`

## Utilisation

1. Clonez le dépôt :
    ```bash
    git clone < https://github.com/A-Tolan/TM.git >
    cd < TM >
    ```


## Résultats Attendus

Les résultats incluront :
- Une comparaison graphique des solutions obtenues par chaque schéma.
- Une analyse des erreurs par rapport à la solution analytique.
- Une discussion sur les avantages et inconvénients de chaque méthode.


