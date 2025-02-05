from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = "" 

    if request.method == "POST":
        sentence = request.form.get("sentence")  
        selected_language = request.form.get("language")  
        translator = Translator()
        try:
            translated = translator.translate(sentence, src='en', dest=selected_language)  
            translated_text = translated.text
        except Exception as e:
            translated_text = f"Error: {str(e)}"

    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
