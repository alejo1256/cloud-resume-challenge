window.addEventListener('DOMContentLoaded', (event) => {
    initVisitorCounter();
});

const functionApi = 'https://lcnoq6v8l8.execute-api.us-east-1.amazonaws.com/prod/visitor';
const websocketApi = 'wss://7rsap298hb.execute-api.us-east-1.amazonaws.com/prod';

const initVisitorCounter = () => {
    // 1. First, do a traditional fetch to get the initial count immediately
    fetch(functionApi)
        .then(response => response.json())
        .then(response => {
            document.getElementById('counter').innerText = response.count;
            // 2. Once the initial count is loaded, establish WebSocket for real-time updates
            connectWebSocket();
        }).catch(error => {
            console.log("REST API error:", error);
            // Fallback: Try WebSocket even if REST fails
            connectWebSocket();
        });
}

const connectWebSocket = () => {
    const socket = new WebSocket(websocketApi);

    socket.onopen = () => {
        console.log("WebSocket connection established.");
    };

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        console.log("Real-time update received:", data);
        if (data.count) {
            document.getElementById('counter').innerText = data.count;
        }
    };

    socket.onclose = (event) => {
        console.log("WebSocket connection closed. Reconnecting in 5 seconds...");
        setTimeout(connectWebSocket, 5000);
    };

    socket.onerror = (error) => {
        console.log("WebSocket error:", error);
        socket.close();
    };
}
