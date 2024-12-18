// Toggle chat window visibility
function toggleChat() {
    const chatWindow = document.getElementById('chat-window');
    chatWindow.style.display = chatWindow.style.display === 'block' ? 'none' : 'block';
}

// Send a message to the chatbot
function sendMessage() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value.trim();
    if (message) {
        displayMessage('You', message);
        userInput.value = '';

        // Simulate chatbot response (simple logic)
        setTimeout(() => {
            const botReply = getBotResponse(message);
            displayMessage('Chatbot', botReply);
        }, 1000);
    }
}

// Display messages in the chat window
function displayMessage(sender, message) {
    const chatContent = document.getElementById('chat-content');
    const msgDiv = document.createElement('div');
    msgDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatContent.appendChild(msgDiv);
    chatContent.scrollTop = chatContent.scrollHeight;
}

// Simple chatbot responses
function getBotResponse(userMsg) {
    const responses = {
        hello: "Hi! How can I assist you today?",
        help: "Sure! You can ask me about our services, pricing, or support.",
        goodbye: "Goodbye! Have a great day!",
    };

    const msg = userMsg.toLowerCase();

    if (responses[msg]) return responses[msg];
    return "I'm not sure I understand that. Can you try again?";
}
