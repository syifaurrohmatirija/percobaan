from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import sp, dp
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle


class BelahKetupatScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout utama (vertikal)
        layout = BoxLayout(
            orientation="vertical",
            padding=sp(20),
            spacing=sp(20)
        )

        # =====================
        # Judul halaman
        # =====================
        label1 = Label(
            text="HITUNG LUAS BELAH KETUPAT",
            font_size=sp(40),
            color=(1,0,0,1),
            size_hint=(1,0.2)
        )
        layout.add_widget(label1)

        # =====================
        # bagian isi
        # =====================

        # Image

        self.imagebelahketupat = Image(source = "belahketupat.png",
                               size_hint=(1, None),
                               height=dp(150),
                               allow_stretch=True,
                               keep_ratio=True)
        layout.add_widget(self.imagebelahketupat)

        # Rumus

        self.labelRumus = Label(text = "Rumus Luas Belah Ketupat = ½ × d1 × d2",
                           font_size=sp(18),
                           color=(0,0,0,1)
                           )
        layout.add_widget(self.labelRumus)

        # input text 1

        self.input_d1 = TextInput(hint_text="Masukkan diagonal 1 (d1)",
                                  multiline=False,
                                  input_filter="float",
                                  size_hint=(0.8,None),
                                  height= dp(45),
                                  pos_hint={"center_x": 0.5}
                                  )
        layout.add_widget(self.input_d1) 

        # input text 2

        self.input_d2 = TextInput(hint_text="Masukkan diagonal 2 (d2)",
                                   multiline=False,
                                   input_filter="float",
                                   size_hint=(0.8,None),
                                   height=dp(45),
                                   pos_hint={"center_x": 0.5}
                                   )
        layout.add_widget(self.input_d2)

        # tombol hitung

        self.tombolHitung = Button(text="Hitung Luas",
                              size_hint=(0.6, None),
                              height=dp(50),
                              pos_hint={"center_x":0.5}
                              )
        self.tombolHitung.bind(on_press=self.hitungLuas)
        layout.add_widget(self.tombolHitung)

        self.labelHasil = Label(text="Luas akan muncul di sini",
                           color= (0,0,0,1),
                           font_size=sp(18)
                           )
        layout.add_widget(self.labelHasil)

        # =====================
        # Tombol BACK & HOME
        # =====================
        tombol_layout = BoxLayout(
            orientation="horizontal",
            spacing=sp(20),
            size_hint=(1, 0.2)
        )

        btn_back = Button(
            text="BACK",
            font_size=sp(18),  # Smaller font
            size_hint=(None, None),  # Disable relative sizing
            size=(80, 40),  # Fixed small size (width, height)
            pos_hint={'top': 1, 'right': 1},  # Top-right corner
            on_release=self.go_back
        )

        tombol_layout.add_widget(btn_back)

        layout.add_widget(tombol_layout)

        self.add_widget(layout)

    # =====================
    # FUNGSI TOMBOL
    # =====================

    def go_back(self, *args):
        # Kembali ke halaman sebelumnya
        self.manager.current = "menu"   # ganti sesuai nama screen kamu

    def hitungLuas(self, instance):
        try:
            d1 = float(self.input_d1.text)
            d2 = float(self.input_d2.text)
            luas = 0.5 * d1 * d2
            self.label_hasil.text = f"Luas Belah Ketupat: {luas:.2f}"
        except:
            self.label_hasil.text = "Input harus angka!"

    App.get_running_app().stop()