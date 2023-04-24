from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        f = request.files['fileip']
        f.save('x-rays/'+secure_filename(f.filename))
        return ''+f.filename

if __name__ == '__main__':
    app.run()
