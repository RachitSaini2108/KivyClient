import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from plyer import tts
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):

    def SPEAK(self, instance):
        Text = self.TextToSpeak.text
        tts.speak(Text)

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2

        self.TextToSpeak = TextInput(text="Enter Text To Speak", multiline=False)
        self.add_widget(self.TextToSpeak)

        self.Speak = Button(text="SPEAK")
        self.add_widget(self.Speak)
        self.Speak.bind(on_press=self.SPEAK)


class MyApp(App):

    def build(self):
        return MyGrid()


MyApp().run()
