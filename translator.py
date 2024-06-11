from flask import Flask, request, render_template
from flask_cors import CORS
import tool

app = Flask(__name__)  # __name__ == '__main__'
CORS(app)

@app.get('/translator') # GET, http://localhost:5000/translator
def translator_form():
  return render_template('translator.html') # /templates/translator.html

@app.post('/translator') # POST, http://localhost:5000/translator
def translator_proc():
  # print("POST 요청 발생함.")
  data = request.json
  sentence = data['sentence']
  language = data['language']
  age = data['age']
  
  sentence = tool.remove_empty_lines(sentence)
  # print(sentence)
  prompt = f'아래 문장을 {age}살 수준의 {language}로 번역해줘.\n\n{sentence}'
  # print('->prompt: ' + prompt)
  
  format = '''
  {
    "res": "번역된 문장"
  }
  '''
  
  response = tool.answer('너는 번역기야', prompt, format)
  # print(response) # {'res': 'Hello. Good morning.'}
  
  # return '{"res": "POST 요청 처리함"}'
  return response


app.run(host='0.0.0.0', port=5000, debug=True) # 어디서나 접속, debug=True: 소스 변경시 자동 재시작

'''
activate ai
python translator.py
'''