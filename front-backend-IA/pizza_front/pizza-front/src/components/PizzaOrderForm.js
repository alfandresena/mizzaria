import React, { useState } from 'react';
import axios from 'axios';

const PizzaOrderForm = () => {
    const [userRequest, setUserRequest] = useState('');
    const [responseMessage, setResponseMessage] = useState(''); // Stocker la réponse de l'IA

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/create-order/', {
                user_request: userRequest
            });

            // Mettre à jour la réponse affichée
            setResponseMessage(response.data.response_message);

        } catch (error) {
            console.error('Erreur:', error);
            setResponseMessage("Erreur lors de la communication avec l'IA.");
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>Que voulez-vous ?</label>
                <input
                    type="text"
                    value={userRequest}
                    onChange={(e) => setUserRequest(e.target.value)}
                    placeholder="Entrez votre demande ..."
                />
                <button type="submit">Envoyer</button>
            </form>

            {/* Afficher la réponse de l'IA */}
            {responseMessage && (
                <div>
                    <h3>Réponse de l'IA :</h3>
                    <p>{responseMessage}</p>
                </div>
            )}
        </div>
    );
};

export default PizzaOrderForm;
