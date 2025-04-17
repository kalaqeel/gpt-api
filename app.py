from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# أضف مفتاح OpenAI الخاص بك هنا
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask-gpt", methods=["POST"])
def ask_gpt():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "Question is required"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        answer = response['choices'][0]['message']['content']
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
