from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle


class ColoredBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.90, 0.88, 0.97, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class HitungPersegiPanjangApp(App):
    def build(self):
        self.layout = ColoredBoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        # Judul
        self.judul = Label(
            text="Mengitung Luas Persegi Panjang",
            font_size=32,
            bold=True,
            color=(0, 0, 0, 1),
            size_hint=(1, None),
            height=60
        )
        self.layout.add_widget(self.judul)

        # Gambar
        self.image_persegi = Image(
            source="cobagambarpp.png",
            size=(800, 400),
            size_hint=(None, None),
            pos_hint={"center_x": 0.5}
        )
        self.layout.add_widget(self.image_persegi)

       # Rumus
        self.rumus = Label(
            text="Rumus: L = p × l",
            font_size=20,
            color=(0, 0, 0, 1)
        )
        self.layout.add_widget(self.rumus)

        # Input panjang
        self.panjang = TextInput(
            hint_text="Masukkan panjang",
            multiline=False,
            input_filter="float",
            size=(200, 50),
            size_hint=(None, None),
            pos_hint={"center_x": 0.5}
        )
        self.layout.add_widget(self.panjang)

        # Input lebar
        self.lebar = TextInput(
            hint_text="Masukkan lebar",
            multiline=False,
            input_filter="float",
            size=(200, 50),
            size_hint=(None, None),
            pos_hint={"center_x": 0.5}
        )
        self.layout.add_widget(self.lebar)

        # Tombol
        tombol_hitung = Button(
            text="Hitung Luas",
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={"center_x": 0.5}
        )
        tombol_hitung.bind(on_press=self.hitung_luas)
        self.layout.add_widget(tombol_hitung)

        # Hasil (Label, bukan TextInput)
        self.label_hasil = Label(
            text="Luas akan muncul di sini",
            font_size=20,
            color=(0, 0, 0, 1)
        )
        self.layout.add_widget(self.label_hasil)

        return self.layout

    def hitung_luas(self, instance):
        try:
            p = float(self.panjang.text)
            l = float(self.lebar.text)
            luas = p * l
            self.label_hasil.text = f"Luas persegi panjang: {luas}"
        except:
            self.label_hasil.text = "Input harus berupa angka!"

if __name__ == "__main__":
    HitungPersegiPanjangApp().run()
