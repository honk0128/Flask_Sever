from flask import Flask, request, render_template
from flask_cors import CORS
import tool

app = Flask(__name__)  # __name__ == '__main__'
CORS(app)

@app.get('/emotion') # GET, http://localhost:5000/emotion
def emotion_form():
  return render_template('emotion.html') # /templates/summary.html

@app.post('/emotion') # POST, http://localhost:5000/emotion
def emotion_proc():
  # print("POST 요청 발생함.")
  data = request.json
  article = data['article']
  
  article = tool.remove_empty_lines(article)
  # print(sentence)
  prompt = f'아래 뉴스가 호재인지 악재인지 알려줘.\n\n[뉴스]\n{article}'
  # print('->prompt: ' + prompt)
  
  format = '''
  {
    "res": "1 또는 0"
  }
  '''
  
  response = tool.answer('너는 증권 투자 권유 대행인 및 투자 컨설턴트야', prompt, format)
  # response = tool.answer('너는 요약 시스템이야', prompt, format, 'gpt-4-turbo')
  # response = tool.answer('너는 요약 시스템이야', prompt, format, 'gpt-4o')
  # print(response) # {'res': 'Hello. Good morning.'}
  
  # return '{"res": "POST 요청 처리함"}'
  return response


app.run(host='0.0.0.0', port=5000, debug=True) # 어디서나 접속, debug=True: 소스 변경시 자동 재시작

'''
activate ai
python emotion.py
'''