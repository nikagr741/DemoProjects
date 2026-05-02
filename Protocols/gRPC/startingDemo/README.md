```markdown
# Unary gRPC Demo (Starting Project)

This project demonstrates the simplest form of gRPC communication: **Unary RPC**. The client sends a single request to the server and gets a single response back, similar to a traditional REST API call but over HTTP/2.

## 🏃 How to Run

1.  **Start the Server:**
    ```bash
    python server.py
    ```
2.  **Run the Client (in a new terminal):**
    ```bash
    python client.py
    ```

## 🔍 What's happening?
- The client sends a `HelloRequest` containing a name.
- The server processes the request and returns a `HelloReply` with a greeting message.