from flask import Flask, request, jsonify

app = Flask(__name__)


# The Webhook Endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON data sent by the sender
    data = request.json

    print("--- Webhook Received ---")
    print(f"Payload: {data}")

    # Returning a 200 OK status lets the sender know you got the message
    return jsonify({"status": "success"}), 200


if __name__ == '__main__':
    # Running on port 5000 by default
    app.run(port=5000)