# Server-Side Streaming gRPC Demo

This demo showcases **Server-Side Streaming**. In this pattern, the client sends one request, and the server returns a stream of multiple responses. This is ideal for live updates, logs, or real-time data feeds.



## 🏃 How to Run

1.  **Start the Streaming Server:**
    ```bash
    python stream_server.py
    ```
2.  **Run the Streaming Client (in a new terminal):**
    ```bash
    python stream_client.py
    ```

## 💡 Use Case
The server simulates a multi-step process (e.g., "Connecting...", "Processing...", "Done") and yields each status update to the client immediately without closing the connection.