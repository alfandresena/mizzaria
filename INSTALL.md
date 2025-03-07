# Création, Activation et Installation

## 1. Créer l’environnement virtuel
Dans le dossier du projet (**`mizzaria`**), crée un environnement virtuel :
```bash
cd /chemin/vers/mizzaria
python -m venv venv
```
Le dossier **`venv`** contiendra l'environnement virtuel.

## 2. Ajouter à `.gitignore`
Crée ou édite le fichier `.gitignore` dans le dossier racine de ton projet (ici **`mizzaria`**) et ajoute la ligne suivante pour ignorer l'environnement virtuel :
```
venv/
```

## 3. Activer l’environnement virtuel
- **Windows** :
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac** :
  ```bash
  source venv/bin/activate
  ```

## 4. Installer les dépendances
Une fois l’environnement activé, installe les dépendances définies dans **`requirements.txt`** :
```bash
pip install -r requirements.txt
```

## 5. Vérifier l'installation
Vérifie que les bibliothèques sont correctement installées :
```bash
pip list
```
