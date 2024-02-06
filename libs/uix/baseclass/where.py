from kivy.uix.screenmanager import Screen
from kivymd.uix.behaviors import TouchBehavior


class Where(Screen, TouchBehavior):
    # changing screens also can be done in python
    def on_touch_move(self, touch):
        if touch.x - touch.ox > 100:
            self.manager.push('main_screen', 'right')
    pass
