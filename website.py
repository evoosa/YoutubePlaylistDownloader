from flask import Flask, render_template, request
from modules.run import *
from hashlib import md5

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login_page.html')


@app.route('/download', methods=['POST', 'GET'])
def download():
    artist = request.form['artist']
    album = request.form['album']
    hd = request.form['hd']
    url = request.form['url']
    work_dir = "c:\\users\\evoosa\\desktop\\music\\"
    hd_music_dir = "F:\\Music"
    web_main(work_dir, hd_music_dir, artist, album, url, hd)
    return "yay"


@app.route('/login_digest', methods=['POST', 'GET'])
def login_digest():
    username = request.form['username']
    password = request.form['password']
    correct_hash = '9cd9550491104e2d0a8d57805ca76836'
    input_hash = md5(password).hexdigest()
    message = "Go Fuck Yourself"
    if username == "evoosa" and input_hash == correct_hash:
        return render_template('get_params.html')
    else:
        return message


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969, debug=False)
