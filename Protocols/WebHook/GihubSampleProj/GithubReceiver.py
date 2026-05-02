from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json

    # Extracting details from the GitHub payload
    repo_name = data.get('repository', {}).get('full_name')
    pusher = data.get('pusher', {}).get('name')
    commit_msg = data.get('head_commit', {}).get('message')

    print("\n--- New GitHub Event Received! ---")
    print(f"Repo: {repo_name}")
    print(f"Pushed by: {pusher}")
    print(f"Commit Message: {commit_msg}")

    return jsonify({"status": "success"}), 200


if __name__ == '__main__':
    app.run(port=5000)