import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock


class SocketClient:
    from plyer import tts
    import socket
    Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Server.connect(("192.168.1.4", 2108))

    def ReceiveTextToSpeak(self):
        TextToSpeak = SocketClient.Server.recv(1024).decode('utf-8')
        if TextToSpeak is not None:
            SocketClient.tts.speak(TextToSpeak)
            MyGrid.UpdateUI(None)
            return TextToSpeak


class MyGrid(GridLayout):

    def ReceiveTextCallback(self, instance):
        Clock.schedule_interval(SocketClient.ReceiveTextToSpeak, 1 / 30)

    def UpdateUI(self):
        self.message.text = SocketClient.ReceiveTextToSpeak(None)

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.message = Label(text="Hello World")
        self.add_widget(self.message)
        self.cols = 2
        self.rows = 1
        # VideoCapture()
        SocketClient()
        Clock.schedule_once(self.ReceiveTextCallback, 2)


class MyApp(App):
    def build(self):
        return MyGrid()


MyApp().run()
