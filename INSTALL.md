# Création, Activation et Installation

## 1. Créer l’environnement
```bash
python -m venv monenv
```

## 2. Ajouter à `.gitignore`
Crée ou édite `.gitignore` dans le dossier racine et ajoute :
```
monenv/
```

## 3. Activer l’environnement
- Windows : `monenv\Scripts\activate`
- Linux/Mac : `source monenv/bin/activate`

## 4. Installer les dépendances
```bash
pip install -r requirements.txt
```

## 5. Vérifier
```bash
pip list
```
