from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

class HitungTrapesiumApp(App):
    def build(self):
        root = FloatLayout()

        background = Image(source="3.png", 
                          fit_mode='fill',
                          size_hint=(1, 1), 
                          pos_hint={'x': 0, 'y': 0})
        root.add_widget(background)

        self.layout = BoxLayout(orientation='vertical',
                                padding=10,
                                spacing=10,
                                size_hint=(None, None),
                                size=(450, 700),
                                pos_hint={'center_x': 0.5, 'center_y': 0.5})
        root.add_widget(self.layout)

        judul = Label(
            text="TRAPESIUM",
            size_hint=(1, None),
            height=50,
            color=(0, 0, 0, 1),
            font_size='24sp',
            bold=True
        )
        self.layout.add_widget(judul)

        self.image_trapesium = Image(source="trapesium.png",
                                   size_hint=(None, None),
                                   size=(250, 200),
                                   pos_hint={"center_x": 0.5, "center_y": 0.5},  # ← INI YANG BIKIN TENGAH
                                   fit_mode='contain')
        self.layout.add_widget(self.image_trapesium)

        rumus = Label(
            text="Rumus : L = ½ × (a + b) × tinggi",
            size_hint=(1, None),
            height=35,
            color=(0, 0, 0, 1),
            font_size='18sp'
                     )
        self.layout.add_widget(rumus)

        self.input_a = TextInput(
            hint_text="Masukkan sisi atas (a)",
            multiline=False,
            input_filter="float",
            size_hint=(None, None),
            size=(250, 50),
            pos_hint={"center_x": 0.5}
                    )
        self.layout.add_widget(self.input_a)

        self.input_b = TextInput(
            hint_text="Masukkan sisi bawah (b)",
            multiline=False,
            input_filter="float",
            size_hint=(None, None),
            size=(250, 50),
            pos_hint={"center_x": 0.5}
                    )
        self.layout.add_widget(self.input_b)

        self.input_tinggi = TextInput(
            hint_text="Masukkan tinggi trapesium",
            multiline=False,
            input_filter="float",
            size_hint=(None, None),
            size=(250, 50),
            pos_hint={"center_x": 0.5}
        )
        self.layout.add_widget(self.input_tinggi)

        # Tombol hitung
        tombol_hitung = Button(text="Hitung Luas Trapesium",
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
            sisi_a = float(self.input_a.text)
            sisi_b = float(self.input_b.text)
            tinggi = float(self.input_tinggi.text)
            luas = 0.5 * (sisi_a + sisi_b) * tinggi
            self.label_hasil.text = f"Luas Trapesium: {luas:.2f}"
        except:
            self.label_hasil.text = "Input harus berupa angka!"

if __name__ == "__main__":
    HitungTrapesiumApp().run()