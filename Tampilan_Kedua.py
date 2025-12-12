from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.metrics import sp, dp


class ImageButton(ButtonBehavior, Image):
    pass


class TampilanMenuapp(Screen):

    def tekan_trapesium(self, *args):
        self.manager.current = "TrapesiumScreen"

    def _init_(self, **kwargs):
        super()._init_(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=dp(20),
            padding=dp(20)
        )

        

        # BARIS 1
        baris1 = BoxLayout(
            orientation="horizontal",
            spacing=dp(15),
            size_hint_y=None,
            height=Window.height * 0.28
        )

        gambar1 = ["persegi.jpeg", "persegipanjang.jpeg", "segitiga.jpeg"]
        for img in gambar1:
            baris1.add_widget(
                ImageButton(
                    source=img,
                    size_hint=(1, 1),
                    allow_stretch=True,
                    keep_ratio=True
                )
            )

        tombol_trapesium = ImageButton(
            source="trapesium.jpeg",
            size_hint=(1, 1),
            allow_stretch=True,
            keep_ratio=True
        )
        tombol_trapesium.bind(on_press=self.tekan_trapesium)
        baris1.add_widget(tombol_trapesium)

        # BARIS 2
        baris2 = BoxLayout(
            orientation="horizontal",
            spacing=dp(15),
            size_hint_y=None,
            height=Window.height * 0.28
        )

        gambar2 = ["layanglayang.jpeg", "lingkaran.jpeg",
                   "jajargenjang.jpeg", "belahketupat.jpeg"]

        for img in gambar2:
            baris2.add_widget(
                ImageButton(source=img,
                            size_hint=(1, 1),
                            allow_stretch=True,
                            keep_ratio=True)
            )

        # BARIS 3 (HOME & BACK)
        baris3 = BoxLayout(
            orientation="horizontal",
            spacing=dp(20),
            size_hint_y=None,
            height=Window.height * 0.17
        )

        btn_home = Button(
            text="HOME",
            font_size=sp(30),
            background_normal="",
            background_color=(1, 0.7, 0.9, 1)
        )
        btn_home.bind(on_press=lambda x: setattr(self.manager, "current", "awal"))

        btn_back = Button(
            text="BACK",
            font_size=sp(30),
            background_normal="",
            background_color=(1, 0.7, 0.9, 1)
        )
        btn_back.bind(on_press=lambda x: setattr(self.manager, "current", "awal"))

        baris3.add_widget(btn_home)
        baris3.add_widget(btn_back)

        layout.add_widget(baris1)
        layout.add_widget(baris2)
        layout.add_widget(baris3)

        self.add_widget(layout)