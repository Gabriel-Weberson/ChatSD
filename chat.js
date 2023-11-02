function sendMessage() {
    const messageInput = document.getElementById('message');
    const chatMessages = document.getElementById('chat-messages');

    if (messageInput.value.trim() === '') {
        return;
    }

    // Envia a mensagem para o servidor
    // Aqui você pode usar a lógica de envio de mensagens do chat_server.py

    // Exibe a mensagem na janela do chat
    const message = document.createElement('div');
    message.classList.add('message');
    message.textContent = messageInput.value;
    chatMessages.appendChild(message);

    // Limpa o campo de entrada
    messageInput.value = '';
}
