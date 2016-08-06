#!/usr/local/env python
from Player import Player
from flask import Flask
app = Flask(__name__)
Music = Player('/home/archer/Documents/Gosrc/src/tmp/music-player/music/Baby.mp3')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/cmd/play')
def play():
    Music.Play()
    return "ok"

@app.route('/cmd/replay')
def replay():
    Music.Replay()
    return "ok"

@app.route('/cmd/pause')
def pause():
    Music.Pause()
    return "ok"

@app.route('/cmd/resume')
def resume():
    Music.Resume()
    return "ok"

@app.route('/cmd/forward')
def forward():
    Music.Forward()
    return "ok"

@app.route('/cmd/backward')
def backward():
    Music.Backward()
    return "ok"

@app.route('/cmd/stop')
def stop():
    Music.Stop()
    return 'ok'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9010)
