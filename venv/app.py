from flask import Flask, render_template, request, send_from_directory
from flask_socketio import SocketIO, emit, send
from gui import GUI
from morsecoder import MorseIdentifier
from threading import Thread
import socket, keyboard

app = Flask(__name__)
conn = SocketIO(app)
translater = MorseIdentifier()

class App():
    global window,translater
    def __init__(self):
        self.IP = socket.gethostbyname(socket.gethostname())

    @app.route('/')
    def mainPage():
        return render_template('morse.html')

    @conn.on('connect')
    def askForConfirm():
        print("Hi")
        window.userConfirmation(request.headers.get('User-Agent'))
    
    @conn.on('key')
    def addKey(key):
        translater.add(key)
        window.addSequence(key)
    
    @conn.on('enter')
    def enter():
        sequence, result = translater.translateMorse(translater.sequence)
        if window.isTypeOn: keyboard.write(result)
        window.addLetters(result,bold=True)
        window.clearSeq()
    
    @conn.on('backspace')
    def backspace(data):
        if translater.sequence == "":
            keyboard.press_and_release('backspace')
        print('Backspace: ' + translater.sequence)
        if not data['clock']: translater.sequence = translater.sequence[:-1]
        else: 
            print("Caps locking: " + translater.sequence)
            translater.sequence = translater.sequence[:-2]
        window.clearSeq(clearSeq=False)
        window.addSequence(translater.sequence)
        print('Result:' + translater.sequence)
    
    @app.route('/scripts/<path:path>')
    def sendJS(path):
        return send_from_directory('js',path)

    @app.route('/static/<path:path>')
    def sendStatic(path):
        return send_from_directory('static',path)

    def start(self):
        print('a')
        window.statusText.set(window.statusText.get()+"Server IP: " + self.IP+":1791")
        app.run(host=self.IP,port=1791)
        conn.run()
    
    def confirmUser(self):
        print("User Confirmed")
        emit('approved')

    def clear(self):
        translater.sequence = ""
        translater.letters = ""

if __name__ == "__main__":
    appObj = App()
    window = GUI(appObj)
    appThread = Thread(target=appObj.start,daemon=True)
    appThread.start()
    window.run()