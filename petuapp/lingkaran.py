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
            # Warna ungu mirip gambar (RGB 128, 102, 255)
            Color(0.75, 0.65, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class HitungLingkaranApp(App):
    def build(self):
        self.layout = ColoredBoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        # Judul
        self.judul = Label(
            text="Mengitung Luas Lingkaran",
            font_size=32,
            bold=True,
            color=(0, 0, 0, 1),
            size_hint=(1, None),
            height=60
        )
        self.layout.add_widget(self.judul)

        # Gambar lingkaran
        self.image_lingkaran = Image(
            source="cobagambarlingkaran.png",   # pastikan nama file sesuai
            size=(800, 400),
            size_hint=(None, None),
            pos_hint={"center_x": 0.5}
        )
        self.layout.add_widget(self.image_lingkaran)

         # Rumus
        self.rumus = Label(
            text="Rumus: L = 3.14 × r × r ",
            font_size=20,
            color=(0, 0, 0, 1)
        )
        self.layout.add_widget(self.rumus)


        # Input jari-jari
        self.input_jari = TextInput(
            hint_text="Masukkan jari-jari",
            multiline=False,
            input_filter="float",
            size=(200, 50),
            size_hint=(None, None),
            pos_hint={"center_x": 0.5}
        )
        self.layout.add_widget(self.input_jari)

        # Tombol hitung
        tombol_hitung = Button(
            text="Hitung Luas",
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={"center_x": 0.5}
        )
        tombol_hitung.bind(on_press=self.hitung_luas)
        self.layout.add_widget(tombol_hitung)

        # Label hasil
        self.label_hasil = Label(text="Luas akan muncul di sini")
        self.layout.add_widget(self.label_hasil)

        return self.layout

    def hitung_luas(self, instance):
        try:
            jari = float(self.input_jari.text)
            phi = 3.14
            luas = phi * jari * jari
            self.label_hasil.text = f"Luas Lingkaran: {luas}"
        except:
            self.label_hasil.text = "Input harus berupa angka!"

if __name__ == "__main__":
    HitungLingkaranApp().run()
