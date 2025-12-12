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
    def __init__(self, **kwargs):  # ✅ Diperbaiki
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=dp(20),
            padding=dp(20)
        )

        # BARIS 1 (3 gambar)
        baris1 = BoxLayout(
            orientation="horizontal",
            spacing=dp(15),
            size_hint_y=None,
            height=Window.height * 0.25
        )

        # Gambar dengan fungsi klik
        tombol_persegi = ImageButton(source="persegi.jpeg", size_hint=(1, 1), allow_stretch=True, keep_ratio=True)
        tombol_persegi.bind(on_press=lambda x: setattr(self.manager, "current", "PersegiScreen"))
        
        tombol_pp = ImageButton(source="persegipanjang.jpeg", size_hint=(1, 1), allow_stretch=True, keep_ratio=True)
        tombol_pp.bind(on_press=lambda x: setattr(self.manager, "current", "PersegiPanjangScreen"))
        
        tombol_trapesium = ImageButton(source="trapesium.jpeg", size_hint=(1, 1), allow_stretch=True, keep_ratio=True)
        tombol_trapesium.bind(on_press=lambda x: setattr(self.manager, "current", "TrapesiumScreen"))

        baris1.add_widget(tombol_persegi)
        baris1.add_widget(tombol_pp)
        baris1.add_widget(tombol_trapesium)

        # BARIS 2 (4 gambar)
        baris2 = BoxLayout(
            orientation="horizontal",
            spacing=dp(10),  # Lebih kecil spacing
            size_hint_y=None,
            height=Window.height * 0.25
        )

        tombol_segitiga = ImageButton(source="segitiga.jpeg", size_hint=(1, 1), allow_stretch=True, keep_ratio=True)
        tombol_segitiga.bind(on_press=lambda x: setattr(self.manager, "current", "SegitigaScreen"))
        
        tombol_layang = ImageButton(source="layanglayang.jpeg", size_hint=(1, 1), allow_stretch=True, keep_ratio=True)
        tombol_layang.bind(on_press=lambda x: setattr(self.manager, "current", "LayangLayangScreen"))
        
        tombol_lingkaran = ImageButton(source="lingkaran.jpeg", size_hint=(1, 1), allow_stretch=True, keep_ratio=True)
        tombol_lingkaran.bind(on_press=lambda x: setattr(self.manager, "current", "LingkaranScreen"))

        baris2.add_widget(tombol_segitiga)
        baris2.add_widget(tombol_layang)
        baris2.add_widget(tombol_lingkaran)

        # BARIS 3 (HOME & BACK)
        baris3 = BoxLayout(
            orientation="horizontal",
            spacing=dp(20),
            size_hint_y=None,
            height=Window.height * 0.15
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