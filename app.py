from flask import Flask, render_template, request
import pyttsx3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run-tts', methods=['POST'])
def run_tts():
    # Get the text from the input field
    text = request.form.get('text')

    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Speak the input text
    engine.say(text)
    engine.runAndWait()

    return "Speech completed."


if __name__ == '__main__':
    app.run(debug=True)
