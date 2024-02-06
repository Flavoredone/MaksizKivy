import json
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from libs.applibs import utils


class Root(ScreenManager):
    history = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
#        Window.bind(on_keyboard=self._handle_keyboard)
        with open("screens.json") as f:
            self.screens_data = json.load(f)

#    def _handle_keyboard(self, instance, key, *args):
#        if key == 27:
#            self.pop()
#            return True

    def load_screen(self, screen_name):
        if not self.has_screen(screen_name):
            screen = self.screens_data[screen_name]
            Builder.load_file(screen["kv"])
            exec(screen["import"])
            screen_object = eval(screen["object"])
            screen_object.name = screen_name
            self.add_widget(screen_object)

    def push(self, screen_name, side="left"):
        if self.current != screen_name:
            self.history.append({"name": screen_name, "side": side})

        self.load_screen(screen_name)
        self.transition.direction = side
        self.current = screen_name

    def push_replacement(self, screen_name, side="left"):
        self.history.clear()
        self.push(screen_name, side)

    def pop(self):
        if not len(self.history) > 1:
            return

        cur_side = self.history.pop()["side"]
        prev_screen = self.history[-1]

        if cur_side == "left":
            side = "right"
        elif cur_side == "right":
            side = "left"
        elif cur_side == "up":
            side = "down"
        elif cur_side == "down":
            side = "up"

        self.transition.direction = side
        self.current = prev_screen["name"]
