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
    
    try:
        response = requests.post(url, headers=headers, json=input_json)
        
        # Convert response text into a dictionary
        response_json = response.json()
        
        # Log the entire response for debugging
        #print("Response Status Code:", response.status_code)
        #print("Response JSON:", response_json)
        
        # Extract emotion predictions
        if 'emotionPredictions' in response_json and len(response_json['emotionPredictions']) > 0:
            emotions = response_json['emotionPredictions'][0]['emotion']
            
            # Extract the relevant emotions
            required_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
            emotion_scores = {emotion: emotions.get(emotion, 0) for emotion in required_emotions}
            
            # Log emotion scores for debugging
            #print("Emotion Scores:", emotion_scores)
            
            # Ensure all values in emotion_scores are numeric
            if all(isinstance(score, (int, float)) for score in emotion_scores.values()):
                # Find the dominant emotion
                dominant_emotion = max(emotion_scores, key=emotion_scores.get)
                
                # Return the result in the required format
                result = (
                    f" Response Status Code:{response.status_code}\n"
                    f"Emotion Scores:\n"
                    f"  Anger: {emotion_scores['anger']}\n"
                    f"  Disgust: {emotion_scores['disgust']}\n"
                    f"  Fear: {emotion_scores['fear']}\n"
                    f"  Joy: {emotion_scores['joy']}\n"
                    f"  Sadness: {emotion_scores['sadness']}\n"
                    f"Dominant Emotion: {dominant_emotion}"
                )
                return result
            else:
                return "Error: Non-numeric values found in emotion scores"
        else:
            return "No emotion predictions found in response"
    except Exception as e:
        return f"An error occurred: {str(e)}"
