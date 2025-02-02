from flask import Flask, request, jsonify

from test import PtEnTranslator

# from googletrans import Translator
from flasgger import Swagger
import os
from flask_cors import CORS


app_root = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(app_root, "Models/model.onnx")
translator_geez = PtEnTranslator(model_path)

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)
# translator_english = Translator()
target_language_geez = "en"
target_language_english = "am"


@app.route("/")
def hello_world():
    return "Hello This is Geez-to-Amharic translation!"


@app.route("/translate/geez", methods=["POST"])
def translate_geez():
    try:
        ge = request.json.get("geez_text")
        results, duration = translator_geez.predict(ge)
        return jsonify({"translatedText": results})
    except Exception as e:
        return jsonify({"error": str(e)})


# @app.route('/translate/english', methods=['POST'])
# def translate_english():
#     try:
#         en_text = request.json.get('english_text')
#         translation = translator_english.translate(src="en", dest=target_language_english, text=en_text)
#         return jsonify({"translatedText": translation.text})
#     except Exception as e:
#         return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
