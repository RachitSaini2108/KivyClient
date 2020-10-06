from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        return Button(text='Hello World')

    import socket
    Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Server.connect("192.168.1.4", 2108)
    Server.send("Hello".encode('utf-8'))


TestApp().run()
