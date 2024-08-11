from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detection():
    textToAnalyze = request.args['textToAnalyze']
    
    results = emotion_detector(textToAnalyze)

    if results['joy'] is None:
        return "Invalid text! Please try again!"
    
    system_response = (
        f"<p>For the given statement, the system response is "
        f"<br> 'Anger': {results['anger']}, "
        f"<br> 'Disgust': {results['disgust']}, "
        f"<br> 'Fear': {results['fear']}, "
        f"<br> 'Joy': {results['joy']}, "
        f"<br> and 'Sadness': {results['sadness']}. "
        f"<br> The dominant emotion is <b>{results['dominant emotion']}</b>.</p>"
    )
    
    return system_response

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
