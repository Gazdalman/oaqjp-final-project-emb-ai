import requests

def emotion_detector(text):

  url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
  headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
  input = { "raw_document": { "text": text } }

  response = requests.post(url, json=input, headers=headers)

  return response.text
