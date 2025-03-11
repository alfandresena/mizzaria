from rapidfuzz import process, fuzz
import spacy


nlp = spacy.load("fr_core_news_md")


suggestions = [
  "Je veux commander une pizza Margherita avec mozzarella et basilic à Antananarivo.",
  "Où trouver une pizzeria spécialisée en Pepperoni à Mahajanga ?",
  "Je cherche une pizzeria qui propose des pizzas vegan à Tsiadana.",
  "Montre-moi les pizzerias disponibles à Analakely.",
  "Quelles sont les pizzas Quatre Fromages disponibles à Antsakaviro ?",
  "Je veux commander une pizza aux champignons et fromage.",
  "Où sont les pizzerias ouvertes à Nosy Be à partir de 19h ?",
  "Je veux manger une pizza carrée",
  "J'ai envie de manger une pizza cuite au feu de bois",
  "Quelles pizzerias font des pizzas aux crevettes ?",
  "Pizzerias ouvertes à Mahamasina en ce moment.",
  "Trouve-moi les pizzerias qui font des pizzas au poulet.",
  "Pizza GM pas chères",
  "Pizza au jambon et olives avec sauce tomate.",
  "Pizzeria spécialisée en Vegan à Diego.",
  "Où acheter une pizza BBQ Chicken pas chère à Toamasina ?",
  "Je veux voir les pizzas aux fruits de mer disponibles à Ankatso.",
  "Indique-moi une pizzeria qui fait des pizzas Napolitaines à Ampasampito.",
  "Meilleure pizzeria à Tsiadana pour une pizza extra-large.",
  "Trouver une pizzeria ouverte à Anlakely avec livraison.",
  "Quel pizzeria fait la meilleure pizza sans porc à Ivandry ?"
]

def detect_intent(prompt):
  doc = nlp(prompt.lower())
  

  intent_pizzeria = {"chercher", "trouver", "localiser", "où", "lister", "indique", "montre", "disponible", "à"}
  intent_pizza = {"manger", "commander", "aimer", "vouloir", "prendre", "désirer", "acheter", "gouter", "envie"}
  
  if any(token.lemma_ in intent_pizzeria for token in doc):
    return "pizzeria"
  elif any(token.lemma_ in intent_pizza for token in doc):
    return "pizza"
  
  return "inconnu"


def suggest_longer_prompt(prompt, subset, limit=3, score_min=30):

  results = process.extract(prompt.lower(), subset, limit=limit, scorer=fuzz.ratio)
  return [match[0] for match in sorted(results, key=lambda x: x[1], reverse=True) if match[1] > score_min]


def combined_suggestions(prompt, limit=3, score_min=30):
  intent = detect_intent(prompt)

  if intent == "pizza":
    filtered_suggestions = [s for s in suggestions if "pizza" in s.lower()]
  elif intent == "pizzeria":
    filtered_suggestions = [s for s in suggestions if "pizzeria" in s.lower()]
  else:
    filtered_suggestions = suggestions

  return suggest_longer_prompt(prompt, filtered_suggestions, limit=limit, score_min=score_min)

