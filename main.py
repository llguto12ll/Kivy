import kivy
from kivy.app import App
from kivy.uix.label import Label

class myApp(App):
    def build(self):
        return Label(text='Oi')

if __name__ == '__main__':
    App=myApp()
    App.run()


