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
            Color(1, 0.72, 0.77, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


class HitungLayangApp(App):
    def build(self):
        layout = ColoredBoxLayout(orientation="vertical", padding=15, spacing=10)

        # judul
        layout.add_widget(Label(
            text="Mengitung Luas Layang-layang",
            font_size="26sp",
            bold=True,
            color=(0,0,0,1),
            size_hint_y=None,
            height="50dp"
        ))

        layout.add_widget(Image(
            source="cobagambarly.png",
            size_hint=(1, .4),     # otomatis sesuai HP
            keep_ratio=True,
            allow_stretch=True
        ))

        layout.add_widget(Label(
            text="Rumus: L = 0.5 × d1 × d2",
            font_size="18sp",
            color=(0,0,0,1)
        ))

        self.d1 = TextInput(
            hint_text="Masukkan diagonal 1",
            multiline=False,
            input_filter="float",
            size_hint=(1, None),
            height="45dp"
        )
        layout.add_widget(self.d1)

        self.d2 = TextInput(
            hint_text="Masukkan diagonal 2",
            multiline=False,
            input_filter="float",
            size_hint=(1, None),
            height="45dp"
        )
        layout.add_widget(self.d2)

        tombol = Button(
            text="Hitung Luas",
            size_hint=(1, None),
            height="50dp"
        )
        tombol.bind(on_press=self.hitung)
        layout.add_widget(tombol)

        self.output = Label(
            text="Luas akan muncul di sini",
            font_size="18sp"
        )
        layout.add_widget(self.output)

        return layout

    def hitung(self, *args):
        try:
            d1=float(self.d1.text)
            d2=float(self.d2.text)
            self.output.text=f"Luas: {0.5*d1*d2}"
        except:
            self.output.text="Masukkan angka!"


if __name__ == "__main__":
    HitungLayangApp().run()
