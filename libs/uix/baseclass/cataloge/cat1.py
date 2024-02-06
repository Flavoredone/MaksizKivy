from kivy.uix.screenmanager import Screen
from kivymd.uix.behaviors import TouchBehavior


class Cat1(Screen, TouchBehavior):
    # changing screens also can be done in python
    def on_touch_move(self, touch):
        # print(touch.x - touch.ox)
        if touch.x - touch.ox > 300:
            self.manager.pop()
    pass
