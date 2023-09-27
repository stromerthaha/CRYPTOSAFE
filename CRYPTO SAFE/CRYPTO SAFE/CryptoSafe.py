import os
from flask import Flask,  request,jsonify,render_template
from werkzeug.utils import secure_filename
from dataProc import *
from Threads import *
from flask import send_file
import time
import zipfile
script = ''

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = set(['txt'])
UPLOAD_FOLDER1 = './'
ALLOWED_EXTENSIONS1 = {'zip'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER1'] = UPLOAD_FOLDER1

def resultE():
    return render_template('Encrypt/KeyResult.html')

def resultD():
    return render_template('Decrypt/DecryptResult.html')


@app.route('/enchome')
def enchome():
    return render_template('Encrypt/enchome.html')
@app.route('/dechome')
def dechome():
    return render_template('Decrypt/dechome.html')

@app.route('/encrypt/')
def EncryptInput():
  Segment()
  getInfo()
  Crypt()
  rag()
  zip_files()
  return resultE()

@app.route('/decrypt/')
def DecryptMessage():
  chandru()
  st=time.time()
  DeCrypt()
  et=time.time()
  print(et-st)
  trim()
  st=time.time()
  Merge()
  et=time.time()
  print(et-st)
  return resultD()

def start():
  content = open('./Secured.txt','r')
  content.seek(0)
  first_char = content.read(1) 
  if not first_char:
    return render_template('Encrypt/Empty.html')
  else:
    return render_template('Encrypt/confirm.html')

def start1():
    return render_template('Decrypt/deconfirm.html')
  
@app.route('/')
def index():
  return render_template('index.html')

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def allowed_file1(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS1

@app.route('/return-files-key/')
def return_files_key():
  try:
    return send_file('./test_files/stego_image.png',download_name='stego_image.png',as_attachment=True)
  except Exception as e:
    return str(e)

@app.route('/return-files-data/')
def return_files_data():
  try:
    return send_file('./Output.txt',download_name='Output.txt',as_attachment=True)
  except Exception as e:
    return str(e)


@app.route('/data/', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    if 'file' not in request.files:
      return render_template('Encrypt/Nofile.html')
    file = request.files['file']
    if file.filename == '':
      return render_template('Encrypt/Nofile.html')
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'Secured.txt'))
      return start()
    return render_template('Encrypt/Invalid.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    image = request.files['imageFile']
    filename = image.filename
    image.save(os.path.join('./test_files', 'cover_image.png'))
    return jsonify({'status': 'OK'})

@app.route('/download', methods=['POST'])
def download():
 try:
    return send_file('.//CryptoSafe.zip',download_name='CryptoSafe.zip',as_attachment=True)
 except Exception as e:
    return str(e)

@app.route('/data1/', methods=['GET', 'POST'])
def upload_file1():
  if request.method == 'POST':
    if 'file1' not in request.files:
      return render_template('Decrypt/Nofile.html')
    file = request.files['file1']
    if file.filename == '':
      return render_template('Decrypt/Nofile.html')
    if file and allowed_file1(file.filename):
      filename = secure_filename(file.filename)
      with zipfile.ZipFile(os.path.join(app.config['UPLOAD_FOLDER1'], filename), 'r') as zip_ref:
          zip_ref.extractall(os.path.join('./zip'))
      return start1()
    return render_template('Decrypt/Invalid.html')
  
@app.route('/upload_image1', methods=['POST'])
def upload_image1():
    image1 = request.files['imageFile1']
    filename = image1.filename
    image1.save(os.path.join('./test_files', 'stego_image.png'))
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
  app.run(debug=True)
