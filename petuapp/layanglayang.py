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
            # Warna pink pastel (RGB 255,183,197)
            Color(1, 0.72, 0.77, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class HitungLayangApp(App):
    def build(self):
        self.layout = ColoredBoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        # Judul
        self.judul = Label(
            text="Mengitung Luas Layang-layang",
            font_size=32,
            bold=True,
            color=(0, 0, 0, 1),
            size_hint=(1, None),
            height=60
        )
        self.layout.add_widget(self.judul)

        # Gambar layang-layang
        self.image_layang = Image(
            source="cobagambarly.png",
            size=(800, 400),
            size_hint=(None, None),
            pos_hint={"center_x": 0.5}
        )
        self.layout.add_widget(self.image_layang)

         # Rumus
        self.rumus = Label(
            text="Rumus: L = 0.5 × d1 × d2  ",
            font_size=20,
            color=(0, 0, 0, 1)
        )
        self.layout.add_widget(self.rumus)

        # Input diagonal 1
        self.input_d1 = TextInput(
            hint_text="Masukkan diagonal 1",
            multiline=False,
            input_filter="float",
            size=(220, 50),
            size_hint=(None, None),
            pos_hint={"center_x": 0.5}
        )
        self.layout.add_widget(self.input_d1)

        # Input diagonal 2
        self.input_d2 = TextInput(
            hint_text="Masukkan diagonal 2",
            multiline=False,
            input_filter="float",
            size=(220, 50),
            size_hint=(None, None),
            pos_hint={"center_x": 0.5}
        )
        self.layout.add_widget(self.input_d2)

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
            d1 = float(self.input_d1.text)
            d2 = float(self.input_d2.text)
            luas = 0.5 * d1 * d2
            self.label_hasil.text = f"Luas Layang-Layang: {luas}"
        except:
            self.label_hasil.text = "Input harus berupa angka!"

if __name__ == "__main__":
    HitungLayangApp().run() 
