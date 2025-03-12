### Description des actions :

1. **`get_panier`** : Cette méthode récupère ou crée un panier pour l'utilisateur. Si l'utilisateur est connecté, le panier est associé à son compte. Sinon, un panier est créé pour une session anonyme.

2. **`add_pizza_to_card`** : Ajoute un produit au panier. Si le produit n'existe pas, il est créé et ajouté au panier. Ensuite, la quantité du produit dans le panier est mise à jour selon les données fournies.

3. **`delete_pizza_from_card`** : Supprime un produit du panier en fonction des données fournies.

4. **`update_pizza_from_card`** : Met à jour la quantité d'un produit dans le panier. Si la quantité est mise à 0, le produit est supprimé du panier.

5. **`read_card`** : Récupère l'ensemble des produits du panier et renvoie les informations sous forme de réponse JSON.

6. **`order`** : Crée une commande basée sur le contenu du panier, en associant chaque produit du panier à la commande. Après cela, les produits sont supprimés du panier.

7. **`order_history`** : Récupère l'historique des commandes d'un utilisateur. Si l'utilisateur est connecté, l'historique de ses commandes est renvoyé. Si `all=true` est passé en paramètre, toutes les commandes sont renvoyées.

### Exemple de requêtes HTTP :

- **Ajouter un produit au panier :**
  - Méthode : `POST`
  - URL : `/panier/add_pizza_to_card/`
  - Données :
    ```json
    {
      "nom": "Pizza Margherita",
      "localisation": "Italie",
      "image": "image_url",
      "prix": 12.99,
      "taille": "M",
      "quantite": 2
    }
    ```

- **Supprimer un produit du panier :**
  - Méthode : `POST`
  - URL : `/panier/delete_pizza_from_card/`
  - Données :
    ```json
    {
      "nom": "Pizza Margherita",
      "localisation": "Italie",
      "prix": 12.99,
      "taille": "M"
    }
    ```

- **Mettre à jour la quantité d'un produit dans le panier :**
  - Méthode : `POST`
  - URL : `/panier/update_pizza_from_card/`
  - Données :
    ```json
    {
      "nom": "Pizza Margherita",
      "localisation": "Italie",
      "prix": 12.99,
      "taille": "M",
      "quantite": 3
    }
    ```

- **Consulter le panier :**
  - Méthode : `GET`
  - URL : `/panier/read_card/`

- **Passer une commande :**
  - Méthode : `POST`
  - URL : `/panier/order/`

- **Voir l'historique des commandes :**
  - Méthode : `GET`
  - URL : `/panier/order_history/`
