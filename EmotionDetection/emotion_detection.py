import requests
import json

def emotion_detector(text):

  url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
  headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
  input = { "raw_document": { "text": text } }

  response = requests.post(url, json=input, headers=headers)

  formatted_response = json.loads(response.text)
  emotions = formatted_response['emotionPredictions'][0]['emotion']

  dominant_emotion = max(emotions, key=emotions.get)

  anger_score = emotions['anger']
  disgust_score = emotions['disgust']
  fear_score = emotions['fear']
  joy_score = emotions['joy']
  sadness_score = emotions['sadness']


  return {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
  }
