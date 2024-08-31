import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Check for blank entries
    if not text_to_analyze.strip():
        return {
            'status_code': 400,
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    try:
        response = requests.post(url, headers=headers, json=input_json)

        # Check if the response status code is 400
        if response.status_code == 400:
            return {
                'status_code': 400,
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        # Convert response text into a dictionary
        response_json = response.json()

        # Check if the response contains 'emotionPredictions'
        if 'emotionPredictions' not in response_json or len(response_json['emotionPredictions']) == 0:
            return {
                'status_code': response.status_code,
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        emotions = response_json['emotionPredictions'][0]['emotion']

        # Extract the relevant emotions
        required_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        emotion_scores = {emotion: emotions.get(emotion, 0) for emotion in required_emotions}

        # Ensure all values in emotion_scores are numeric
        if all(isinstance(score, (int, float)) for score in emotion_scores.values()):
            # Find the dominant emotion
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            return {
                'status_code': response.status_code,
                'anger': emotion_scores['anger'],
                'disgust': emotion_scores['disgust'],
                'fear': emotion_scores['fear'],
                'joy': emotion_scores['joy'],
                'sadness': emotion_scores['sadness'],
                'dominant_emotion': dominant_emotion
            }
        else:
            return {
                'status_code': response.status_code,
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

    except Exception as e:
        # Handle exceptions and return None values with a status code
        return {
            'status_code': 500,
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
