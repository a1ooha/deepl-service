from flask import Flask, request, jsonify
from translatepy import Translator
from translatepy.translators import DeeplTranslate

app = Flask(__name__)


@app.route("/translate", methods=["POST"])
def translate():
    try:
        text = request.json["text"]
        target_lang = request.json["target_lang"]
        source_lang = request.json["source_lang"]

        translator = Translator(services_list=[DeeplTranslate])
        result = translator.translate(text, target_lang, source_lang)

        return jsonify({"code": 200, "data": str(result)})
    except Exception as e:
        return jsonify({"code": 500, "msg": str(e)})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
