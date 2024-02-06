from kivy.core.window import Window
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField
from kivy.core.text import LabelBase
from kivymd.font_definitions import theme_font_styles

from data import *
from libs.uix.root import Root

Window.size = (Window.height / 3.465, Window.height)

result, dial, dial_img, res_len, mode = [], [], [], [], []


class MainApp(MDApp, TouchBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None
        self.menu_2 = None
        self.menu = None
        self.orientation = "vertical"
        self.src_list = src_list
        LabelBase.register(
            name="Teko",
            fn_regular="Teko-Regular.ttf")
        theme_font_styles.append('Teko')
        self.theme_cls.font_styles["Teko"] = [
            "Teko",
            16,
            False,
            0.15,
        ]

    def build(self):
        self.root = Root()
        self.root.push("main_screen")
#        self.root.add_widget(Builder.load_file("assets/splashScreen.kv"))

        self.title = "MAKSIZ"
        self.theme_cls.primary_palette = 'Orange'
        self.theme_cls.theme_style = "Dark"

#    def on_start(self):
#        Clock.schedule_once(self.load_ms, 1)
#
#    def load_ms(self, *args):
#        self.root.push("main_screen")

    def open_dialog(self, src_img=None, src_v=None):
        dial_img.clear()
        dial_img.append(src_img)
        dial.clear()
        dial.append(src_v)
        self.dialog = Popup(title='',
                            background_color='white',
                            title_color='#333333',
                            title_size='10sp',
                            separator_height='0dp',
                            content=(ItemDialog()),
                            auto_dismiss=False,
                            size_hint=(.98, .92),
                            )
        self.dialog.open()

    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)

    def count_result(self, from_callback=0, src_res=None):
        if src_res is None:
            src_res = []

        self.root.load_screen('result')

        img_adder = self.root.get_screen('result').target
        img_adder.clear_widgets()

        if len(result) != 0:
            if from_callback == 0:
                if mode[-1] == 2:
                    if result[-1] in set1_sub:
                        src_res.append('assets/search/results/5.jpg')

                    if result[-1] in set2_sub:
                        src_res.append('assets/search/results/1.jpg')
                        src_res.append('assets/search/results/2.jpg')
                        src_res.append('assets/search/results/6.jpg')

                    if result[-1] in set3_sub:
                        src_res.append('assets/search/results/7.jpg')

                elif mode[-1] == 1:
                    if result[-1] in set1_cas:
                        src_res.append('assets/search/results/5.jpg')

                    if result[-1] in set2_cas:
                        src_res.append('assets/search/results/1.jpg')
                        src_res.append('assets/search/results/2.jpg')
                        src_res.append('assets/search/results/6.jpg')

                    if result[-1] in set3_cas:
                        src_res.append('assets/search/results/7.jpg')

                else:
                    res_len.append(1)
                    img_adder.add_widget(MDLabel(
                        text='К сожалению, результат поиска не дал результатов',
                        font_size='38sp',
                        font_style='Teko',
                        pos_hint={"center_x": .5, "center_y": .5},
                        size_hint=(1, None),
                        height="540dp",
                        halign='center'
                    ))
                result.clear()

            elif from_callback == 1:
                tmp_res = []
                varbs = [l701, l702, l703, l705, l706, l707]
                for var in varbs:
                    if result[-1] in var:
                        tmp_res.append(var[0])

                for tmp in tmp_res:
                    src_res.append('assets/search/results/' + tmp + '.jpg')
            elif from_callback == 2:
                pass
            else:
                pass

            src_res = list(set(src_res))
            res_len.append(len(src_res))
            for item in src_res:
                img_adder.add_widget(Image(
                    size_hint=(1, 1.4),
                    source=item,
                    allow_stretch=True,
                    keep_ratio=True,
                    # height="540dp",
                ))
        else:
            res_len.append(1)
            img_adder.add_widget(MDLabel(
                text='К сожалению, результат поиска не дал результатов',
                font_size='38sp',
                font_style='Teko',
                pos_hint={"center_x": .5, "center_y": .5},
                size_hint=(1, None),
                height="540dp",
                halign='center'
            ))
        result.clear()

    ###########################

    def build_view(self):
        self.menu = MDDropdownMenu(
            position="top",
            border_margin=dp(24),
            hor_growth="left",
            caller=self.root.get_screen('search2_2').ids.otrasl,
            elevation=1,
            width_mult=8,
            background_color='black',
            items=[
                {
                    "text": item,
                    "height": dp(45),
                    'font_style': 'Teko',
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=item: self.set_item(x),
                } for item in ddn_otrasl
            ]
        )
        self.menu.bind()

    # def build_view_2(self):
    #     self.menu_2 = MDDropdownMenu(
    #         position="top",
    #         border_margin=dp(24),
    #         hor_growth="left",
    #         caller=self.root.get_screen('search2_3').ids.stuff,
    #         elevation=1,
    #         width_mult=8,
    #         background_color='black',
    #         items=[
    #             {
    #                 "text": item,
    #                 "height": dp(45),
    #                 'font_style': 'Caption',
    #                 "viewclass": "OneLineListItem",
    #                 "on_release": lambda x=item: self.set_item(x),
    #             } for item in ddn_do
    #         ]
    #     )
    #     self.menu.bind()

    def set_item(self, text_item):
        if str(self.root.current_screen) == "<Screen name='search2_2'>":
            self.root.get_screen('search2_2').ids.otrasl.text = text_item
            self.menu.dismiss(self.menu)
        else:
            self.root.get_screen('search2_3').ids.stuff.text = text_item
            self.menu_2.dismiss(self.menu_2)

        result.clear()
        result.append(text_item)
        self.count_result(from_callback=1)
        self.root.current = 'result'

    def form_result(self):
        lst = ['c11', 'c12', 'c13', 'c21', 'c22', 'c31', 'c32', 'c41', 'c42']
        lst_res, src_res = [], []
        for i in lst:
            lst_res.append(self.root.get_screen('search5').ids[i].active)

        if lst_res[8]:
            src_res = ['assets/search/results/1.jpg',
                       'assets/search/results/2.jpg']
        else:
            if lst_res[7]:
                src_res = ['assets/search/results/6.jpg']
            else:
                if lst_res[6]:
                    src_res = ['assets/search/results/5.jpg',
                               'assets/search/results/7.jpg']
                else:
                    if lst_res[5]:
                        src_res = ['assets/search/results/1.jpg',
                                   'assets/search/results/2.jpg',
                                   'assets/search/results/6.jpg']
                    else:
                        src_res = ['assets/search/results/1.jpg',
                                   'assets/search/results/2.jpg',
                                   'assets/search/results/5.jpg',
                                   'assets/search/results/6.jpg',
                                   'assets/search/results/7.jpg']
        if True in lst_res:
            result.append('form')
            self.count_result(from_callback=2, src_res=src_res)
            self.root.current = 'result'
        else:
            src_res.clear()
            self.count_result(from_callback=2)
            self.root.current = 'result'

    def upload_img(self):
        lay = self.root.get_screen('result').target
        print(res_len)
        print(result)
        lay.size_hint = (1, res_len[-1] * .8)


##########################################################
# certif stuff

class ItemDialog(BoxLayout, TouchBehavior):
    target = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'


class CustomGrid(MDGridLayout, TouchBehavior):

    def __init__(self, *args, **kw):
        super(CustomGrid, self).__init__(**kw)
        self.cols = 1
        self.spacing = '5dp'
        self.count = True
        self.source = dial_img[-1]
        self.col = dial

        if self.col[-1] == 1:
            self.size_hint = (1, 1)
            self.add_widget(Image(
                pos_hint={"center_x": .5, "center_y": .5},
                source=self.source,
                allow_stretch=True,
                keep_ratio=True,
            ))
        elif self.col[-1] == 2:
            for i in range(2):
                self.size_hint = (1, 1.1)
                self.add_widget(Image(
                    pos_hint={"center_x": .5, "center_y": .5},
                    source=self.source[:19] + f'_{i}.jpg',
                    size_hint=(1, 1),
                    allow_stretch=True,
                    keep_ratio=True,
                ))
        elif self.col[-1] == 3:
            for i in range(3):
                self.size_hint = (1, 1.8)
                self.add_widget(Image(
                    pos_hint={"center_x": .5, "center_y": .5},
                    source=self.source[:19] + f'_{i}.jpg',
                    size_hint=(1, 1),
                    allow_stretch=True,
                    keep_ratio=True,
                ))

    ###################################################

    def on_touch_down(self, touch):

        if self.collide_point(*touch.pos):
            touch.grab(self)
            # if touch.is_single_tap:
            x = self.size_hint_x
            y = self.size_hint_y
            if self.count:
                Animation(size_hint=(x * 2, y * 2), d=.3).start(self)
                self.count = False
            else:
                Animation(size_hint=(x / 2, y / 2), d=.3).start(self)
                self.count = True


# certif stuff
##########################################################


##########################################################
# Dropdown menu stuff


class ComboEdit(MDTextField):
    options = ListProperty(('',))

    def __init__(self, **kw):
        ddn = self.drop_down = DropDown()
        ddn.bind(on_select=self.on_select)
        ddn.max_height = 600
        super(ComboEdit, self).__init__(**kw)

    def on_options(self, instance, value):
        ddn = self.drop_down
        ddn.clear_widgets()
        for option in value:
            but = MDRaisedButton(text=option,
                                 md_bg_color='#1C1B1F',
                                 text_color="white",
                                 font_name="Teko",
                                 height='36sp',
                                 on_press=lambda btn: ddn.select(btn.text))
            ddn.add_widget(but)

    def on_select(self, instance, value):
        self.text = value
        result.clear()
        result.append(value)


class MainView(FloatLayout):
    tmp_list = []

    def on_text(self, instance, value):
        if self.list == 'cas':
            self.tmp_list = all_cas
            mode.append(1)
        elif self.list == 'substance':
            self.tmp_list = all_substance
            mode.append(2)
        try:
            if value == '':
                instance.options = []
            else:
                tmp = []
                cnt = len(value)
                for v in self.tmp_list:
                    if value.lower() == v[0:cnt]:
                        tmp.append(v)
                instance.options = list(set(tmp))
            instance.drop_down.open(instance)
        except:
            pass


# Dropdown menu stuff
##########################################################

class ResGrid(MDGridLayout, TouchBehavior):
    count = True

    def on_touch_down(self, touch):
        tmp = .8 * res_len[-1]
        if self.count:
            Animation(size_hint=(2, tmp * 2), d=.2).start(self)
            self.count = False
        else:
            Animation(size_hint=(1, tmp), d=.2).start(self)
            self.count = True


if __name__ == "__main__":
    MainApp().run()
