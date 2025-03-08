import React, {useState} from 'react';
import axios from 'axios';

const PizzaOrderForm = () => {
    const [userRequest, setUserRequest] = useState('');
    const [responseMessage, setResponseMessage] = useState('');
    const [options, setOptions] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/create-order/', {user_request: userRequest});
            setResponseMessage(response.data.response_message);
            setOptions(response.data.options);

        } catch(error) {
            console.error('Error:', error);
        }
    };
    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>Que voulez-vous ?</label>
                <input
                 type='text'
                 value={userRequest}
                 onChange={(e) => setUserRequest(e.target.value)}
                 placeholder='Entrez votre demande ...'
                />
            </form>
            {responseMessage && <p>Message de l'IA: {responseMessage}</p>}
            {options.length > 0 && (
                <ul>
                    {options.map((option, index) => (
                        <li key={index}>{option}</li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default PizzaOrderForm;