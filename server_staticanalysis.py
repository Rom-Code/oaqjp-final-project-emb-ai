"""
server.py

This module defines a Flask web application that provides emotion analysis functionality.
It has two routes:
1. /emotionDetector: Processes the provided text and returns the emotion analysis results.
2. /: Renders the main index page of the application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector  # Ensure this import is correct

# Create a Flask application instance
app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_analyzer():
    """
    Analyzes the emotions of the provided text and returns a formatted response.

    Retrieves the query parameter 'textToAnalyze' from the request, processes it
    using the emotion_detector function, and formats the response accordingly.
    
    Returns:
        str: A formatted string with the emotion analysis results or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Get the result from emotion_detector
    result = emotion_detector(text_to_analyze)

    # Check if the dominant_emotion is None and respond accordingly
    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again."

    # Format the response
    emotions = [f"'{key}': {value}" for key, value in result.items() if value is not None]
    dominant_emotion = result.get('dominant_emotion', 'N/A')
    if emotions:
        emotion_str = ', '.join(emotions)
        response_str = (f"For the given statement, the system response is {emotion_str}. "
                        f"The dominant emotion is {dominant_emotion}.")
    else:
        response_str = "No emotion predictions found in response."

    return response_str

@app.route('/')
def render_index_page():
    """
    Renders the main index page of the application.

    Returns:
        str: The HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    #Starts the Flask application and deploys it on localhost:5000.
    app.run(host="0.0.0.0", port=5000, debug=True)
