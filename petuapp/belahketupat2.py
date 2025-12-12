from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image


class HitungBelahKetupatApp(App):
    def build(self):
        root = FloatLayout()

        # Background image
        background = Image(source="11.png", 
                          fit_mode='fill',
                          size_hint=(1, 1), 
                          pos_hint={'x': 0, 'y': 0})
        root.add_widget(background)

        # Layout konten utama di tengah layar
        self.layout = BoxLayout(orientation='vertical',
                                padding=10,
                                spacing=10,
                                size_hint=(None, None),
                                size=(450, 650),  # Disesuaikan untuk 3 input
                                pos_hint={'center_x': 0.5, 'center_y': 0.5})
        root.add_widget(self.layout)

        # Judul
        judul = Label(
            text="BELAH KETUPAT",
            size_hint=(1, None),
            height=50,
            color=(0, 0, 0, 1),
            font_size='24sp',
            bold=True
        )
        self.layout.add_widget(judul)

        # Gambar belah ketupat - TEPAT DI TENGAH
        self.image_belahketupat = Image(source="belahketupat.png",
                                   size_hint=(None, None),
                                   size=(250, 200),
                                   pos_hint={"center_x": 0.5, "center_y": 0.5},
                                   fit_mode='contain')
        self.layout.add_widget(self.image_belahketupat)

        # Label rumus luas belah ketupat
        rumus = Label(
            text="Rumus : L = ½ × d1 × d2",
            size_hint=(1, None),
            height=35,
            color=(0, 0, 0, 1),
            font_size='18sp'
        )
        self.layout.add_widget(rumus)

        # Input diagonal 1 (d1)
        self.input_d1 = TextInput(
            hint_text="Masukkan diagonal 1 (d1)",
            multiline=False,
            input_filter="float",
            size_hint=(None, None),
            size=(250, 50),
            pos_hint={"center_x": 0.5}
        )
        self.layout.add_widget(self.input_d1)

        # Input diagonal 2 (d2)
        self.input_d2 = TextInput(
            hint_text="Masukkan diagonal 2 (d2)",
            multiline=False,
            input_filter="float",
            size_hint=(None, None),
            size=(250, 50),
            pos_hint={"center_x": 0.5}
        )
        self.layout.add_widget(self.input_d2)
        
        # Tombol hitung
        tombol_hitung = Button(text="Hitung Luas Belah Ketupat",
                              size_hint=(None, None),
                              size=(250, 50),
                              pos_hint={"center_x": 0.5},
                              background_color=(0.2, 0.6, 0.2, 1))
        tombol_hitung.bind(on_press=self.hitung_luas)
        self.layout.add_widget(tombol_hitung)

        # Hasil luas
        self.label_hasil = TextInput(
            hint_text="Luas akan muncul di sini",
            multiline=False,
            readonly=True,
            size_hint=(None, None),
            size=(250, 50),
            pos_hint={"center_x": 0.5},
            background_color=(1, 1, 0.9, 1)
        )
        self.layout.add_widget(self.label_hasil)

        return root

    def hitung_luas(self, instance):
        try:
            d1 = float(self.input_d1.text)
            d2 = float(self.input_d2.text)
            luas = 0.5 * d1 * d2
            self.label_hasil.text = f"Luas Belah Ketupat: {luas:.2f}"
        except:
            self.label_hasil.text = "Input harus berupa angka!"


if __name__ == "__main__":
    HitungBelahKetupatApp().run()