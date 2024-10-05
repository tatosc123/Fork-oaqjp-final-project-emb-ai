'''
from flask import Flask, render_template, request
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
'''
App route define
'''
@app.route("/emotionDetector")
def sent_analizer():
    """
    Analyzes the provided text and detects the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None :
        return 'Invalid text! Please try again!.'
    return response
@app.route("/")
def render_index_page():
    """
    Renders the index page.
    """
    return render_template('index.html')
if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000)
#
