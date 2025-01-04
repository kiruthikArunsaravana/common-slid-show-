from flask import Flask, render_template
import os
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/')
def index():
    media_folder = os.path.join('static', 'media')
    media_files = os.listdir(media_folder) if os.path.exists(media_folder) else []
    media_files = [file for file in media_files if file.endswith(('.jpg', '.png', '.mp4'))]
    return render_template('index.html', media_files=media_files)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000')

if __name__ == '__main__':
    Timer(1, open_browser).start()  # Delay browser launch slightly to avoid overlap
    app.run(host='0.0.0.0', port=5000, debug=True)
   

