# Morse Code Typer
A program allowing you to type in Morse code.
Uses a Flask webserver/socket.io to communicate with a mobile device, passing data to a custom translator and GUI.

> What practical use does it have? None!

### Morse Code Guide
This program follows the international Morse Code syntax, which can be found [here](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/International_Morse_Code.svg/315px-International_Morse_Code.svg.png 'Wikimedia International Morse Code') and in the GUI.
There are some modifications to make Morse Code more keyboard-friendly:
- Spaces are emulated using the / key, with / marking a space between letters, // marking a space between words and /// marking a new line.
- A shift key is included to emulate the shift key on a keyboard, allowing uppercase and lowercase letters, and special characters such as ! and % when shift is combined with a number.
- An enter key is also included to translate the morse code input (most likely will be combined with a different system in the future).

### Features
- [X] Mobile website interface that connects with the computer
- [X] WebSocket connection using socket.io combined with Flask for a low-latency experience
- [X] GUI to access various settings, and to view the morse code output
- [X] Keyboard-friendly morse code translator

### Bugs/WIP
- [ ] Adding a "quick-return" feature to automatically translate letters from Morse Code
- [ ] Making an executable version of the program
- [ ] Completing status feature of GUI
- [ ] Adding punctuation characters
- [ ] Calculating typing speed

# How to use
1. After starting the app(source code or executable), go to IP:1791 on a mobile device. The IP can be found in the GUI menu.
2. An alert will pop up on the computer showing a conection request. Approve this.
3. You're now able to type morse code through your phone! Make sure to press the "Toggle Keyboard" button to translate the morse code into keyboard input. 

**NOTE:** Since the IP for Morse Code Typer is different from most IP adresses, saving the site as a bookmark or saving to the home screen is recommended.

## Running the source code
Run `python app.py`. Using a virtual environment is recommended
#### Dependencies
- `flask` for the web server
- `flask-socketio` to integrate socket.io
- `keyboard` to emulate keyboard input.
