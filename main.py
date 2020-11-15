import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

#
class SocketClient:
    from plyer import tts
    import socket
    Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Server.connect(("192.168.1.4", 2108))

    def ReceiveTextToSpeak(self):
        TextToSpeak = SocketClient.Server.recv(1024).decode('utf-8')
        if TextToSpeak is not None:
            SocketClient.tts.speak(TextToSpeak)
            return TextToSpeak


# class VideoCapture:
#     import _pickle as pickle
#     import cv2
#     import struct
#     cap = cv2.VideoCapture(0)
#
#     def SendVideoStream(self):
#         ret, frame = VideoCapture.cap.read()
#         # Serialize frame
#         data = VideoCapture.pickle.dumps(frame)
#
#         # Send message length first
#         message_size = VideoCapture.struct.pack("L", len(data))
#
#         # Then data
#         SocketClient.Server.sendall(data)


class MyGrid(GridLayout):
    a = 0
    def UpdateGUI(self, instance):
        if SocketClient.ReceiveTextToSpeak(None) is not None:
            MyGrid.a = SocketClient.ReceiveTextToSpeak(None)
            self.message.text = str(MyGrid.a)

    def ReceiveTextCallback(self, instance):
        pass
        Clock.schedule_interval(SocketClient.ReceiveTextToSpeak, 1 / 30)
        # Clock.schedule_interval(VideoCapture.SendVideoStream, 1 / 30)

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.message = Label(text="Hello World")
        self.add_widget(self.message)
        self.cols = 2
        self.rows = 1
        # VideoCapture()
        SocketClient()
        Clock.schedule_once(self.ReceiveTextCallback, 2)
        Clock.schedule_interval(self.UpdateGUI, 1/1)


class MyApp(App):
    def build(self):
        return MyGrid()


MyApp().run()


