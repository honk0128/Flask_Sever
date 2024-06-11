from pytube import YouTube

# step 1: 영상 + 오디오 다운로드
# video_url = "https://www.youtube.com/watch?v=K1SCQzHrWAI"
# yt = YouTube(video_url)
# stream = yt.streams.get_highest_resolution()
# stream.download(output_path='.', filename='book.mp4') # 현재 폴더에 저장

# video_url = "https://www.youtube.com/watch?v=3-sOsFQGHhg" # 김치찌게 망치
# yt = YouTube(video_url)
# stream = yt.streams.get_highest_resolution()
# stream.download(output_path='.', filename='kimchi.mp4') # 현재 폴더에 저장

# step 2: 오디오 다운로드
# video_url = "https://www.youtube.com/watch?v=K1SCQzHrWAI"
# yt = YouTube(video_url)
# audio_stream = yt.streams.filter(only_audio=True).first()
# audio_stream.download(output_path='.', filename='book.mp3')

'''
activate ai
cd whisper
python Pytube.py
'''