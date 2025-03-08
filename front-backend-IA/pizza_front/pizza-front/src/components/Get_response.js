const userRequest = "Where can I find a pizza near me?";

fetch('http://127.0.0.1:8000/api/ai-response/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    user_request: userRequest
  })
})
  .then(response => response.json())
  .then(data => {
    console.log('Response:', data);
    // Affiche la réponse de l'IA et les informations supplémentaires
    document.getElementById("response-message").innerText = data.response_message;
    document.getElementById("extra-info").innerText = JSON.stringify(data.extra_info, null, 2);
  })
  .catch(error => {
    console.error('Error:', error);
  });
