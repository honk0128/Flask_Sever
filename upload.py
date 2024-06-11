from flask import Flask, request, redirect, flash, render_template
from werkzeug.utils import secure_filename
from PIL import Image
import os

import cx_Oracle
import os
os.putenv('NLS_LANG', 'KOREAN_KOREA.KO16MSWIN949')

conn = cx_Oracle.connect('kd/1234@127.0.0.1:1521/XE')
cs = conn.cursor()

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # 플래시 메시지에 필요
app.config['UPLOAD_FOLDER'] = 'storage'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif', 'txt', 'hwp', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'tar', 'gz', 'ipynb', 'doc', 'sql'}


    
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def is_image(filename):
    return filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif'}

def create_thumbnail(image_path, thumbnail_path, width, height):
    with Image.open(image_path) as img:
        img.thumbnail((width, height))
        img.save(thumbnail_path, "JPEG")

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    file_size = len(file.read())  
    file.seek(0) # 파일 포인터를 처음으로 이동  
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(original_path)

        if is_image(filename):
            name, ext = os.path.splitext(filename)  # 파일명과 확장자를 분리
            thumbnail_filename = f"{name}_t{ext}"   # 새로운 파일명 생성
            thumbnail_path = os.path.join(app.config['UPLOAD_FOLDER'], thumbnail_filename)
            create_thumbnail(original_path, thumbnail_path, 200, 150)    
        print(thumbnail_path, "and", app.config['UPLOAD_FOLDER'], "and", file_size)

        cs.execute("""
                    INSERT INTO pytest (testno, aprofile_img, aprofile_imgsave, aprofile_thum, aprofile_size)
                    VALUES (pytest_seq.nextval, :1, :2, :3, :4)
                    """, (filename, filename, thumbnail_filename, file_size))

        cs.close()
        conn.commit()
        conn.close()
        return 'File successfully uploaded'
    else:
        flash('File type not allowed')
        return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)

