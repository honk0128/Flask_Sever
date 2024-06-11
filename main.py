from flask import Flask, request, render_template
from flask_cors import CORS
import tool

app = Flask(__name__)  # __name__ == '__main__'
CORS(app)

@app.get('/') # GET, http://localhost:5000
def index():
  return 'OpenAI 웹 서비스 접속'

@app.get('/translator') # GET, http://localhost:5000/translator
def translator():
  return '번역 서비스 접속'

app.run(host='0.0.0.0', port=5000, debug=True) # 어디서나 접속, debug=True: 소스 변경시 자동 재시작

'''
activate ai
python main.py
'''