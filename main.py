from kivy.lang import Builder
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, WipeTransition
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.animation import Animation
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import Image
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField
from data import *

# Window.fullscreen = False

Window.size = (375, 812)

result = []
dial, dial_img = [], []


##########################################################
# Catalogue stuff

class ItemDialog(BoxLayout, TouchBehavior):
    target = ObjectProperty()


class CustomGrid(MDGridLayout, TouchBehavior):
    def __init__(self, *args, **kw):
        super(CustomGrid, self).__init__(**kw)
        self.cols = 1
        self.spacing = '10dp'
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
                self.size_hint = (1, 1.2)
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
            if self.count:
                Animation(size_hint=(self.size_hint_x * 2, self.size_hint_y * 2), d=.3).start(self)
                self.count = False
            else:
                Animation(size_hint=(self.size_hint_x / 2, self.size_hint_y / 2), d=.3).start(self)
                self.count = True
        # self.parent.update_from_scroll()


# Catalogue stuff
##########################################################


class MainApp(MDApp):
    dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_2 = None
        self.menu = None
        self.screen_manager = ScreenManager(transition=WipeTransition())
        self.orientation = "vertical"
        self.src_list = src_list

    def build(self):
        self.title = "MAKSIZ"
        self.theme_cls.primary_palette = 'Orange'
        self.theme_cls.theme_style = "Dark"

        # self.screen_manager.add_widget(Builder.load_file("splashScreen.kv"))

        for item in self.src_list:
            self.screen_manager.add_widget(Builder.load_file(item))

        return self.screen_manager

    # def on_start(self):
    #     self.fps_monitor_start()
    #     Clock.schedule_once(self.change_screen, 8)

    # def change_screen(self, *args):
    #     self.screen_manager.current = "MainScreen"

    def open_dialog(self, src_img=None, src_v=None):
        # path = r'assets/certif/pdf/1.pdf'
        # for android
        # subprocess.Popen(["open", path])
        dial_img.clear()
        dial_img.append(src_img)
        dial.clear()
        dial.append(src_v)
        # if not self.dialog:
        self.dialog = MDDialog(
            title="",
            radius=[20, 20, 20, 20],
            type="custom",
            md_bg_color='#1C1B1F',
            # content_cls=Item(x_size=self.x, y_size=self.y),
            content_cls=ItemDialog(),
            buttons=[
                MDFlatButton(
                    text="ВЕРНУТЬСЯ",
                    theme_text_color="Custom",
                    text_color='white',
                    on_release=self.dialog_close
                ),
            ],
        )
        self.dialog.open()

    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)

    def count_result(self, from_callback=0, src_res=None):
        if src_res is None:
            src_res = []
        img_adder = self.screen_manager.get_screen('search_result').target
        img_adder.clear_widgets()

        if len(result) != 0:
            if from_callback == 0:

                if result[-1] in (set1_cas and set2_cas) or (set1_sub and set2_sub):
                    src_res = ['assets/search/results/1.jpg',
                               'assets/search/results/2.jpg',
                               'assets/search/results/5.jpg',
                               'assets/search/results/6.jpg']

                elif result[-1] in set1_cas or set1_sub:
                    src_res = ['assets/search/results/5.jpg']

                elif result[-1] in set2_cas or set2_sub:
                    src_res = ['assets/search/results/1.jpg',
                               'assets/search/results/2.jpg',
                               'assets/search/results/6.jpg']

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
            for item in src_res:
                img_adder.add_widget(Image(
                    size_hint=(1, None),
                    source=item,
                    allow_stretch=True,
                    keep_ratio=True,
                    height="500dp",
                ))
        else:
            img_adder.add_widget(MDLabel(
                text='К сожалению, результат поиска не дал результатов',
                font_size='38sp',
                pos_hint={"center_x": .5, "center_y": .5},
                size_hint=(1, None),
                height="500dp",
                halign='center'
            ))
        result.clear()

    ###########################

    def build_view(self):
        self.menu = MDDropdownMenu(
            position="top",
            border_margin=dp(24),
            hor_growth="left",
            caller=self.screen_manager.get_screen('search2_2').ids.otrasl,
            elevation=1,
            width_mult=8,
            background_color='white',
            items=[
                {
                    "text": item,
                    # "secondary_text": item[15:],
                    "height": dp(45),
                    'font_style': 'Caption',
                    # 'secondary_font_style': 'Caption',
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=item: self.set_item(x),
                } for item in ddn_otrasl
            ]
        )
        self.menu.bind()

    def build_view_2(self):
        self.menu_2 = MDDropdownMenu(
            position="top",
            border_margin=dp(24),
            hor_growth="left",
            caller=self.screen_manager.get_screen('search2_3').ids.stuff,
            elevation=1,
            width_mult=8,
            background_color='white',
            items=[
                {
                    "text": item,
                    # "secondary_text": item[15:],
                    "height": dp(45),
                    'font_style': 'Caption',
                    # 'secondary_font_style': 'Caption',
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=item: self.set_item(x),
                } for item in ddn_do
            ]
        )
        self.menu.bind()

    def set_item(self, text_item):
        if str(self.screen_manager.current_screen) == "<Screen name='search2_2'>":
            self.screen_manager.get_screen('search2_2').ids.otrasl.text = text_item
            self.menu.dismiss(self.menu)
        else:
            self.screen_manager.get_screen('search2_3').ids.stuff.text = text_item
            self.menu_2.dismiss(self.menu_2)

        result.clear()
        result.append(text_item)
        self.count_result(from_callback=1)
        self.screen_manager.current = 'search_result'

    def form_result(self):
        lst = ['c11', 'c12', 'c13', 'c21', 'c22', 'c31', 'c32', 'c41', 'c42']
        lst_res, src_res = [], []
        for i in lst:
            lst_res.append(self.screen_manager.get_screen('search5').ids[i].active)

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
        for i in lst_res:
            if i:
                result.append('form')
                self.count_result(from_callback=2, src_res=src_res)
                self.screen_manager.current = 'search_result'
            else:
                src_res = []
                self.count_result(from_callback=2)
                self.screen_manager.current = 'search_result'


##########################################################
# Dropdown menu stuff

class ComboEdit(MDTextField, MainApp):
    options = ListProperty(('',))
    '''
    :data:`options` defines the list of options that will be displayed when
    touch is released from this widget.
    '''

    def __init__(self, **kw):
        ddn = self.drop_down = DropDown()
        ddn.bind(on_select=self.on_select)
        super(ComboEdit, self).__init__(**kw)

    def on_options(self, instance, value):
        ddn = self.drop_down
        ddn.clear_widgets()
        for option in value:
            but = MDRaisedButton(text=option,
                                 md_bg_color='#1C1B1F',
                                 width=dp(50),
                                 text_color="white",
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
        elif self.list == 'substance':
            self.tmp_list = all_substance

        if value == '':
            instance.options = []
        else:
            tmp = []
            cnt = len(value)
            # for v in self.list:
            for v in self.tmp_list:
                # if value in v:
                if value == v[0:cnt]:
                    tmp.append(v)
            instance.options = list(set(tmp))
        try:
            instance.drop_down.open(instance)
        except:
            pass


# Dropdown menu stuff
##########################################################

class ResGrid(MDGridLayout, TouchBehavior):
    count = True

    # def on_touch_down(self, touch):
    #     if self.count:
    #         Animation(size_hint_x=(self.size_hint_x * 2), size_hint_y=10, d=.3).start(self)
    #         self.count = False
    #     else:
    #         Animation(size_hint_x=(self.size_hint_x / 2), size_hint_y=2, d=.3).start(self)
    #         self.count = True


MainApp().run()
