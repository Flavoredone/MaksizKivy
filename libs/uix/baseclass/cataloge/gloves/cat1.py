from kivy.uix.screenmanager import Screen
from kivymd.uix.behaviors import TouchBehavior


class Gl1(Screen, TouchBehavior):
    # changing screens also can be done in python
    def on_touch_move(self, touch):
        if touch.x - touch.ox > 300:
            self.manager.pop()
    pass
