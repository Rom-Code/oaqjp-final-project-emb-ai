from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector  # Ensure this import is correct

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_analyzer():
    '''
    This function handles GET requests to analyze emotions from the provided text.
    It uses the emotion_detector function and returns the results in a formatted response.
    '''
    # Retrieve the query parameter from the request
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Pass the text to the emotion_detector function and store the response
    result = emotion_detector(text_to_analyze)

    # Check if the dominant_emotion is None and respond accordingly
    if result.get('dominant_emotion') is None:
        response_str = "Invalid text! Please try again."
    else:
        # Format the dictionary response into a readable string
        emotions = [f"'{key}': {value}" for key, value in result.items() if value is not None]
        dominant_emotion = result.get('dominant_emotion', 'N/A')
        if emotions:
            emotion_str = ', '.join(emotions)
            response_str = (f"For the given statement, the system response is {emotion_str}. "
                            f"The dominant emotion is {dominant_emotion}.")
        else:
            response_str = "No emotion predictions found in response."

    # Return the formatted response as plain text
    return response_str

@app.route('/')
def render_index_page():
    '''
    This function serves the main page of the application.
    It renders the index.html template located in the templates folder.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    '''
    This function starts the Flask application and deploys it on localhost:5000.
    '''
    app.run(host="0.0.0.0", port=5000, debug=True)