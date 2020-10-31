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
        pos_hint: {'center_y':0.9}
        font_style: 'H3'

    MDLabel:
        text: 'Acousticness'
        pos_hint: {'center_y':0.75}

    MDTextField:
        hint_text: '(0.0000009491-0.99579650)'
        width: 100
        size_hint_x: None
        pos_hint: {'center_y':0.75, 'center_x':0.5}

    MDLabel:
        text: 'Danceability'
        pos_hint: {'center_y':0.70}

    MDLabel:
        text: 'Energy'
        pos_hint: {'center_y':0.65}

    MDLabel:
        text: 'Instrumentalness'
        pos_hint: {'center_y':0.6}

    MDLabel:
        text: 'Liveness'
        pos_hint: {'center_y':0.55}

    MDLabel:
        text: 'Speechiness'
        pos_hint: {'center_y':0.50}

    MDLabel:
        text: 'Tempo'
        pos_hint: {'center_y':0.45}

    MDLabel:
        text: 'Valence'
        pos_hint: {'center_y':0.40}

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
        self.help_string.get_screen('main').ids.sample_text_1.text = str(self.help_string.get_screen('main').ids.slide_value_1.value)
        self.help_string.get_screen('main').ids.sample_text_2.text = str(self.help_string.get_screen('main').ids.slide_value_2.value)

MainApp().run()

# https://kivymlapp.herokuapp.com/predict?acousticness=0.344719513&danceability=0.758067547&energy=0.323318405&instrumentalness=0.0166768347&liveness=0.0856723112&speechiness=0.0306624283&tempo=101.993&valence=0.443876228