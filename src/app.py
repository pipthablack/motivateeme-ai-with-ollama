from flask import Flask, jsonify
import ollama

def generate_motivational_text():
    """
    Generates a motivational quote using Ollama's Gemma model.
    """
    try:
        response = ollama.chat(
            model="gemma:2b",
            messages=[
                {"role": "system", "content": "You are a motivational speaker."},
                {"role": "user", "content": 
                 "Generate a powerful motivational quote in **10 lines or more**. "
                 "It should inspire people to take action and believe in themselves. "
                 "Keep it concise, impactful, and  more than 10 lines."}
            ]
        )

       
        quote = response["message"]["content"]
        quote_lines = quote.split('\n')
        limited_quote = '\n'.join(quote_lines[:10])
        return limited_quote

    except Exception as e:
        return f"Error generating motivational text: {str(e)}"

def create_app():
    """
    Creates and configures the Flask application.
    """
    app = Flask(__name__)

    @app.route('/motivation', methods=['GET'])
    def get_motivation():
        """
        API endpoint to fetch a daily motivational message.
        """
        return jsonify({"message": generate_motivational_text()})

    return app

