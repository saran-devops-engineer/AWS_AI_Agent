from flask import Flask, request, jsonify
from flask_cors import CORS
from intent_router import extract_intent_from_message, handle_intent

app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "*"}})  # Allow any origin for /chat

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        # CORS preflight response
        response = jsonify({'message': 'CORS preflight OK'})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST")
        return response

    try:
        user_message = request.json.get("message", "")
        print("🔵 Incoming message:", user_message)

        if not user_message:
            return jsonify({"response": "❌ No message provided."}), 400

        intent = extract_intent_from_message(user_message)
        print("🟢 Detected intent:", intent)

        response_text = handle_intent(intent, user_message)
        print("🟣 Response from handler:", response_text)

        response = jsonify({"response": response_text})
        response.headers.add("Access-Control-Allow-Origin", "*")  # 🔥 Add this
        return response

    except Exception as e:
        print("🔴 Exception:", str(e))
        response = jsonify({"response": f"❌ Backend error: {str(e)}"})
        response.headers.add("Access-Control-Allow-Origin", "*")  # 🔥 Add this too
        return response, 500

if __name__ == "__main__":
    app.run(debug=True)
