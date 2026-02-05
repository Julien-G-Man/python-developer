"""
AssemblyAI is a powerful AI API platform for automatic speech recognition.
This script uploads audio files and starts the transcription process using AssemblyAI
"""

import requests

headers = {"authorization": "api_key"}

# upload audio file 
upload_response = requests.post(
    'https://assemblyai.com/v2/upload',
    headers=headers,
    files={'file': open('sample.mp3', 'rb')}
)
audio_url = upload_response.json()['upload_url']

# Transcribe
transcript_response = requests.post(
    'https://assemblyai.com/v2/transcript',
    headers=headers,
    json={'audio_url': audio_url}
)
transcipt_id = transcript_response.json()['id']