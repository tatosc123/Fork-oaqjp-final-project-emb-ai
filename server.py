from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/\emotionDetector")
def sent_analizer():
    # Retrive text to analize from the request arguments
    test_to_analize = request.args.get('testToAnalize')

    # Pass the text to the emotion detector function
    response = emotion_detector(text_to_analyze)
    
    # Extract the label and the score for the response

    label = ['emotionPredictions'][0]['emotion']

     return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
            }

app.route("/")
def render_index_page():
    return render_template('index.html')
if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000)
                    

