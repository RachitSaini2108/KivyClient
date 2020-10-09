from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        return Button(text='Hello World')

    import socket
    import pyttsx3
    engine = pyttsx3.init()
    Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        Server.connect(("192.168.1.4", 2108))
        Server.send("Hello Bitch".encode('utf-8'))
    except Exception as e:
        print(e)
    while True:
        messageToSpeak = Server.recv(1024).decode('utf-8')
        engine.say(messageToSpeak)
        engine.runAndWait()

TestApp().run()
