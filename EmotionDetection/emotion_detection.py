import requests # Import the requests library
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header) # Send a post request
    formatted_response = json.loads(response.text)

    label = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = label['anger']
    disgust_score = label['disgust']
    fear_score = label['fear']
    joy_score = label['joy']
    sadness_score = label['sadness']

    dominant_emotion = max(label, key=label.get)

    return {
       
        'dominant_emotion': dominant_emotion
            }

print(emotion_detector('I hate working long hours'))


#    python3.11 emotion_detection.py 
    
# git add .
# git config --global user.email "tatosc@msn.com"
# git config --global user.name "tatosc123"
# git commit -m " last commit"
# git push
