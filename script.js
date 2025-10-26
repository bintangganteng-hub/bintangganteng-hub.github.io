const chatLog = document.getElementById('chatLog');
const userInput = document.getElementById('userInput');

const apiKey = 'AIzaSyDIF622TSXxQWdfCmdHZEZI4M3mMffGf-c'; // Ganti dengan API key Anda
const apiUrl = 'https://api.openai.com/v1/engines/davinci-codex/completions'; // Contoh API endpoint

function addMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    messageElement.classList.add(sender);
    messageElement.textContent = message;
    chatLog.appendChild(messageElement);
    chatLog.scrollTop = chatLog.scrollHeight; // অটো স্ক্রোল নিচে
}

async function sendMessage() {
    const message = userInput.value;
    if (message.trim() === '') return;

    addMessage(message, 'user');
    userInput.value = '';

    try {
        // Kirim permintaan ke API
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                prompt: message,
                max_tokens: 150
            })
        });

        const data = await response.json();
        const reply = data.choices[0].text.trim();
        addMessage(reply, 'chatbot');
    } catch (error) {
        console.error('Error:', error);
        addMessage('Maaf, terjadi kesalahan.', 'chatbot');
    }
}
