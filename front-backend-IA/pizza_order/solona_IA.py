import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_ai_response(user_request):
    driver = uc.Chrome()
    response_message = ""
    options = []

    try:
        driver.get("https://chat.openai.com/")
        time.sleep(5)  # Attendre que la page charge

        # Attendre la zone de saisie
        wait = WebDriverWait(driver, 15)
        text_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.ProseMirror")))

        # Message de l'utilisateur
        message = f"Tu vas jouer un rôle maintenant. Tu es un chatbot dans une plateforme de service de vente pizza, recommandation pizza, qui répond avec satisfaction à la demande de l'utilisateur. Voici la demande de l'utilisateur : {user_request}"

        text_input.send_keys(message, Keys.ENTER)

        # Attendre la réponse
        time.sleep(60)

        # Extraire la réponse de l'IA
        messages = driver.find_elements(By.CSS_SELECTOR, "div.markdown")
        if messages:
            response_text = messages[-1].text
            # Filtrage pour récupérer le message et les options
            if "message" in response_text and "options" in response_text:
                response_message = response_text.split("message:")[1].split("options:")[0].strip()
                options_raw = response_text.split("options:")[1].strip()
                options = options_raw.split("\n")  # Assuming each option is on a new line.
        else:
            response_message = "Désolé, aucune réponse de l'IA."
    except Exception as e:
        response_message = "Une erreur s'est produite."
        print(f"Erreur: {e}")
    finally:
        driver.quit()

    return response_message, options