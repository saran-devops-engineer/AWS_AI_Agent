const sendMessage = async () => {
    const userInput = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");
    const message = userInput.value.trim();

    if (!message) return;

    // Display user's message
    chatBox.innerHTML += `<div class="user">🧑 You: ${message}</div>`;
    userInput.value = "";

    try {
        const response = await fetch("http://localhost:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });

        const data = await response.json();
        chatBox.innerHTML += `<div class="bot">🤖 Bot: ${data.response}</div>`;
    } catch (error) {
        console.error("Fetch error:", error);
        chatBox.innerHTML += `<div class="bot">🤖 Bot: ❌ Failed to connect to backend.</div>`;
    }

    chatBox.scrollTop = chatBox.scrollHeight;
};

// Submit on button click
document.getElementById("submitBtn").onclick = sendMessage;

// ✅ Submit on Enter key
document.getElementById("userInput").addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        e.preventDefault(); // Prevent newline in input box
        sendMessage();
    }
});
