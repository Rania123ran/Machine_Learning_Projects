# 🖼️ Image Classifier (CIFAR-10)

Ce projet est un **classificateur d’images** basé sur un réseau de neurones convolutionnel (CNN) entraîné sur le jeu de données **CIFAR-10**.  
Il reconnaît des objets appartenant à **10 classes différentes** comme : avion, voiture, oiseau, chat, chien, cheval, etc.

---

## 🎯 Objectif du projet
L’objectif est de construire et d’entraîner un modèle capable d’identifier automatiquement le contenu d’une image parmi les 10 catégories du dataset CIFAR-10.

---

## 🧠 Jeu de données : CIFAR-10
Le jeu de données contient :
- **60 000 images** de taille **32x32 pixels**
- **10 classes** :
  `Plane`, `Car`, `Bird`, `Cat`, `Deer`, `Dog`, `Frog`, `Horse`, `Ship`, `Truck`

Les données sont déjà incluses dans TensorFlow :
```python
from tensorflow.keras import datasets
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()
