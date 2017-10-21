from flask import Flask, render_template, request, redirect, send_from_directory
from modules.run import *
from hashlib import md5
from modules.variables import *

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login_page.html')


@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html')


@app.route('/choose_dl_destination', methods=['POST', 'GET'])
def choose_dl_destination():
    decision = request.form['decision']
    if decision == "eva":
        return render_template('download_eva.html')
    elif decision == "local":
        return render_template('download_foreign.html')


@app.route('/download_eva', methods=['POST', 'GET'])
def download_eva():
    artist = request.form['artist']
    album = request.form['album']
    hd = request.form['hd']
    url = request.form['url']
    web_main(work_dir, hd_music_dir, artist, album, url, hd)
    return "yay"


@app.route('/download_local', methods=['POST', 'GET'])
def download_local():
    artist = request.form['artist']
    album = request.form['album']
    hd = "n"
    url = request.form['url']

    web_main(others_work_dir, hd_music_dir, artist, album, url, hd)
    return "yay"


@app.route('/login_digest', methods=['POST', 'GET'])
def login_digest():
    username = request.form['username']
    password = request.form['password']
    correct_hash = '9cd9550491104e2d0a8d57805ca76836'
    input_hash = md5(password).hexdigest()
    message = "Go Fuck Yourself"
    if username == "evoosa" and input_hash == correct_hash:
        return redirect('/home')
    else:
        return message



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969, threaded=True, debug=False)
