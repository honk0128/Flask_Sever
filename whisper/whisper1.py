import os
import tool

from openai import OpenAI

client = OpenAI(
  api_key=os.getenv('OPENAI_API_KEY')
)

# MP3
# -----------------------------------------------------------------------------
# 한국어
# audio_file= open("./book.mp3", "rb")  # 유튜버
# transcript = client.audio.transcriptions.create(model='whisper-1', 
#                                      language='ko',
#                                      file=audio_file)

# audio_file= open("./진주_조개잡이_쿨.mp3", "rb") # 노래 정확도 떨어짐
# transcript = client.audio.transcriptions.create(model='whisper-1', 
#                                      language='ko',
#                                      file=audio_file)

# 영어
# audio_file= open("./I_Just_Called_To_Say_I_Love_you_Stevie_Wonder.mp3", "rb")
# transcript = client.audio.transcriptions.create(model='whisper-1', 
#                                      language='en',
#                                      file=audio_file)

# MP4, 최대 파일 크기 25 MB 지정됨, book.mp4 는 80MB가 넘어 에러가 발생됨
# -----------------------------------------------------------------------------
# 한국어
# audio_file= open("./book.mp4", "rb") # X Maximum content size limit (26214400) exceeded (26258790 bytes read)
# transcript = client.audio.transcriptions.create(model='whisper-1', 
#                                      language='ko',
#                                      file=audio_file)

# 영어
# audio_file= open("./Mind-blowing Artificial Intelligence Tools.mp4", "rb")
# transcript = client.audio.transcriptions.create(model='whisper-1', 
#                                      language='en',
#                                      file=audio_file)

print(type(transcript)) # <class 'openai.types.audio.transcription.Transcription'>
print(transcript.text)

'''
activate ai
python whisper1.py
'''