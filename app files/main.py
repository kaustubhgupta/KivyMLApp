from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.size = (400,600)

Builder_string = '''
ScreenManager:
    Main:
<Main>:
    name : 'main'
    MDLabel:
        text: 'Music Genre Predictor'
        halign: 'center'
        pos_hint: {'center_y':0.8}
        font_style: 'H2'

    MDBoxLayout:

        MDSlider:
            pos_hint: {'center_y':0.7}
            halign: 'center'
            min: 0.0000009
            max: 0.0001
            value: 0.0001
            hint: False
            id: slide_value

        MDLabel:
            text: ''
            halign: 'center'
            pos_hint: {'center_y':0.5}
            id: sample_text

        MDRaisedButton:
            pos_hint: {'center_x':0.5, 'center_y':0.1}
            text: 'Predict'
            on_press: app.predict()
'''

class Main(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Main(name='main'))

class MainApp(MDApp):
    def build(self):
        self.help_string = Builder.load_string(Builder_string)
        return self.help_string

    def predict(self):
        self.help_string.get_screen('main').ids.sample_text.text = str(self.help_string.get_screen('main').ids.slide_value.value)
MainApp().run()

# https://kivymlapp.herokuapp.com/predict?acousticness=0.344719513&danceability=0.758067547&energy=0.323318405&instrumentalness=0.0166768347&liveness=0.0856723112&speechiness=0.0306624283&tempo=101.993&valence=0.443876228