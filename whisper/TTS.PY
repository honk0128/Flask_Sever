from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="해외 주식 세금 안내입니다. 해외 주식은 양도 소득세를 매년 5월에 정산해야하며 250만원 까지는 세금을 할당하지 않습니다.",
)

response.stream_to_file("output.mp3")

'''
python TTS.py
'''