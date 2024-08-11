import requests
import json
def emotion_detector(text_to_analyse:str):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADER_DATA = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT_DATA = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, json=INPUT_DATA, headers=HEADER_DATA)

    if response.status_code == 400:
        emotions_data = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant emotion": None
        }
        return emotions_data

    formatted_response = json.loads(response.text)

    emotions_data = formatted_response["emotionPredictions"][0]["emotion"]

    max_score = max(emotions_data.values())
    max_score_emotion = [
        key for key, value in emotions_data.items() \
        if value == max_score
    ]
    emotions_data['dominant emotion'] = max_score_emotion[0]
    
    return emotions_data