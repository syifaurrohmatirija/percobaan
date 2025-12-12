from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.metrics import sp, dp
from kivy.core.window import Window
from kivy.graphics import Rectangle


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(20)
        )

        label_judul = Label(
            text='MENU BANGUN DATAR',
            font_size=sp(32),
            size_hint=(1, 0.2)
        )
        layout.add_widget(label_judul)

        btn_trapesium = Button(
            text='TRAPESIUM',
            font_size=sp(28),
            size_hint=(1, 0.2)
        )
        btn_trapesium.bind(on_press=lambda x: setattr(self.manager, 'current', 'trapesium'))
        layout.add_widget(btn_trapesium)

        self.add_widget(layout)


class TrapesiumScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ===== BACKGROUND Gambar pada SCREEN =====
        with self.canvas.before:
            self.bg = Rectangle(source='bg Trapesium.jpeg', size=self.size, pos=self.pos)
        self.bind(size=self.update_bg, pos=self.update_bg)

        # ===== LAYOUT UTAMA =====
        layout = BoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(15)
        )

        # Judul
        judul = Label(
            text='HITUNG LUAS TRAPESIUM',
            font_size=sp(32),
            color=(1, 0, 0, 1),
            size_hint=(1, 0.15)
        )
        layout.add_widget(judul)

        # Gambar trapesium
        gambar = Image(
            source='trapesium.png',
            size_hint=(1, None),
            height=Window.height * 0.25,
            allow_stretch=True,
            keep_ratio=True
        )
        layout.add_widget(gambar)

        # Rumus
        rumus = Label(
            text='Rumus: L = ½ × (a + b) × tinggi',
            font_size=sp(18),
            color=(0, 0, 0, 1),
            size_hint=(1, 0.1)
        )
        layout.add_widget(rumus)

        # Input a
        self.input_a = TextInput(
            hint_text='Masukkan sisi atas trapesium (a)',
            multiline=False,
            input_filter='float',
            size_hint=(0.8, None),
            height=dp(40),
            pos_hint={'center_x': 0.5}
        )
        layout.add_widget(self.input_a)

        # Input b
        self.input_b = TextInput(
            hint_text='Masukkan sisi bawah trapesium (b)',
            multiline=False,
            input_filter='float',
            size_hint=(0.8, None),
            height=dp(40),
            pos_hint={'center_x': 0.5}
        )
        layout.add_widget(self.input_b)

        # Input tinggi
        self.input_tinggi = TextInput(
            hint_text='Masukkan tinggi trapesium',
            multiline=False,
            input_filter='float',
            size_hint=(0.8, None),
            height=dp(40),
            pos_hint={'center_x': 0.5}
        )
        layout.add_widget(self.input_tinggi)

        # Tombol hitung
        tombol_hitung = Button(
            text='Hitung Luas',
            size_hint=(0.6, None),
            height=dp(45),
            pos_hint={'center_x': 0.5}
        )
        tombol_hitung.bind(on_press=self.hitung_luas)
        layout.add_widget(tombol_hitung)

        # Label hasil
        self.label_hasil = Label(
            text='Luas muncul di sini',
            font_size=sp(20),
            color=(0, 0, 0, 1),
            size_hint=(1, 0.1)
        )
        layout.add_widget(self.label_hasil)

        # Tombol BACK ke menu
        btn_back = Button(
            text='KEMBALI KE MENU',
            font_size=sp(20),
            size_hint=(0.6, None),
            height=dp(45),
            pos_hint={'center_x': 0.5}
        )
        btn_back.bind(on_press=lambda x: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def hitung_luas(self, instance):
        try:
            a = float(self.input_a.text)
            b = float(self.input_b.text)
            t = float(self.input_tinggi.text)
            luas = 0.5 * (a + b) * t
            self.label_hasil.text = f'Luas Trapesium: {luas:.2f}'
        except ValueError:
            self.label_hasil.text = 'Input harus angka!'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(TrapesiumScreen(name='trapesium'))
        return sm


if __name__ == '__main__':
    MyApp().run()