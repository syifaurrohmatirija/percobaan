from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LuasBangunDatar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        # Dropdown pilihan bangun datar
        self.spinner = Spinner(
            text='Pilih Bangun Datar',
            values=('Persegi', 'Persegi Panjang', 'Segitiga', 'Trapesium', 'Belah Ketupat', 'Jajar Genjang', 'Layang Layang', 'Lingkaran'),
            size_hint=(1, None), height=44
        )
        self.spinner.bind(text=self.update_input_fields)
        self.add_widget(self.spinner)

        # Layout input
        self.input_layout = BoxLayout(orientation='vertical', size_hint=(1, None), height=150)
        self.add_widget(self.input_layout)

        # Tombol hitung
        self.btn_hitung = Button(text='Hitung Luas', size_hint=(1, None), height=50)
        self.btn_hitung.bind(on_press=self.hitung_luas)
        self.add_widget(self.btn_hitung)

        # Label hasil
        self.hasil = Label(text='Hasil luas akan muncul di sini.', size_hint=(1, None), height=40)
        self.add_widget(self.hasil)

    def update_input_fields(self, spinner, text):
        self.input_layout.clear_widgets()

        if text == 'Persegi':
            self.sisi = TextInput(hint_text='Masukkan panjang sisi', input_filter='float')
            self.input_layout.add_widget(self.sisi)

        elif text == 'Persegi Panjang':
            self.panjang = TextInput(hint_text='Masukkan panjang', input_filter='float')
            self.lebar = TextInput(hint_text='Masukkan lebar', input_filter='float')
            self.input_layout.add_widget(self.panjang)
            self.input_layout.add_widget(self.lebar)

        elif text == 'Segitiga':
            self.alas = TextInput(hint_text='Masukkan alas', input_filter='float')
            self.tinggi = TextInput(hint_text='Masukkan tinggi', input_filter='float')
            self.input_layout.add_widget(self.alas)
            self.input_layout.add_widget(self.tinggi)

        elif text == 'Trapesium':
            self.sisi_atas = TextInput(hint_text='Masukan sisi atas', input_filter='float')
            self.sisi_bawah = TextInput(hint_text='Masukkan sisi bawah', input_filter='float')
            self.tinggi = TextInput(hint_text='Masukkan tinggi', input_filter='float')
            self.input_layout.add_widget(self.sisi_atas)
            self.input_layout.add_widget(self.sisi_bawah)
            self.input_layout.add_widget(self.tinggi)

        elif text == 'Belah Ketupat':
            self.diagonal_1 = TextInput(hint_text='Masukkan diagonal 1', input_filter='float')
            self.diagonal_2 = TextInput(hint_text='Masukkan diagonal 2', input_filter='float')
            self.input_layout.add_widget(self.diagonal_1)
            self.input_layout.add_widget(self.diagonal_2) 

        elif text == 'Jajar Genjang':
            self.alas = TextInput(hint_text='Masukkan alas', input_filter='float')
            self.tinggi = TextInput(hint_text='Masukkan tinggi', input_filter='float')
            self.input_layout.add_widget(self.alas)
            self.input_layout.add_widget(self.tinggi)

        elif text == 'Layang Layang':
            self.diagonal_1 = TextInput(hint_text='Masukkan diagonal 1', input_filter='float')
            self.diagonal_2 = TextInput(hint_text='Masukkan diagonal 2', input_filter='float')
            self.input_layout.add_widget(self.diagonal_1)
            self.input_layout.add_widget(self.diagonal_2)

        elif text == 'Lingkaran':
            self.jari_jari = TextInput(hint_text='Masukkan jari jari', input_filter='float')
            self.input_layout.add_widget(self.jari_jari)

    def hitung_luas(self, instance):
        bangun = self.spinner.text

        try:
            if bangun == 'Persegi':
                sisi = float(self.sisi.text)
                luas = sisi * sisi

            elif bangun == 'Persegi Panjang':
                p = float(self.panjang.text)
                l = float(self.lebar.text)
                luas = p * l

            elif bangun == 'Segitiga':
                a = float(self.alas.text)
                t = float(self.tinggi.text)
                luas = 0.5 * a * t

            elif bangun == 'Trapesium':
                a = float(self.sisi_atas.text)
                b = float(self.sisi_bawah.text)
                t = float(self.tinggi.text)
                luas = 0.5*(a+b)*t

            elif bangun == 'Belah Ketupat':
                d1 = float(self.diagonal_1.text)
                d2 = float(self.diagonal_2.text)
                luas = 0.5*d1*d2

            elif bangun == 'Jajar Genjang':
                a = float(self.alas.text)
                t = float(self.tinggi.text)
                luas = a*t

            elif bangun == 'Layang Layang':
                d1 = float(self.diagonal_1.text)
                d2 = float(self.diagonal_2.text)
                luas = 0.5*d1*d2

            elif bangun == 'Lingkaran':
                22/7 = float(self.phi.text)
                r = float(self.jari_jari.text)
                luas = 22/7*r*r

            else:
                self.hasil.text = "Pilih bangun datar terlebih dahulu!"
                return

            self.hasil.text = f"Luas = {luas}"

        except:
            self.hasil.text = "Input tidak valid! Harap masukkan angka."

class LuasApp(App):
    def build(self):
        return LuasBangunDatar()

if __name__ == '__main__':
    LuasApp().run()
