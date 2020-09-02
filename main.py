from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy_garden.zbarcam import zbarcam


Builder.load_string('''

<FirstScreen>: ##########################################################################################

#:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol

BoxLayout:
    orientation: 'vertical'
    ZBarCam:
        id: zbarcam
        # optional, by default checks all types
        code_types: ZBarSymbol.QRCODE, ZBarSymbol.EAN13
    Label:
        size_hint: None, None
        size: self.texture_size[0], 50
        text: ', '.join([str(symbol.data) for symbol in zbarcam.symbols])
''')


class FirstScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(FirstScreen(name='prim'))

class TestCamera(App):
    def build(self):
        return sm


if __name__ == '__main__':
    TestCamera().run()
