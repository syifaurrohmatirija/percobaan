from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp

from Tampilan_Kedua import TampilanMenuapp
from trapesium import TrapesiumScreen

Window.clearcolor = 1, 0.96, 0.86, 1


class ImageButton(ButtonBehavior, Image):
    pass


class HalamanAwal(Screen):
    pass


class PETUapp(App):

    def ganti_ke_menu(self, *args):
        self.manager.current = "menu"

    def build(self):
        self.manager = ScreenManager()

        screen_w, screen_h = Window.size
        is_landscape = screen_w > screen_h

        # ==========================
        # FUNGSI RESPONSIF LEVEL 5
        # ==========================
        def font_responsive(base):
            return sp(base * (screen_h / 800))

        def padding_responsive():
            return dp(screen_h * 0.03)

        def spacing_responsive():
            return dp(screen_h * 0.025)

        # ==========================
        # HALAMAN 1 (AWAL)
        # ==========================
        awal = HalamanAwal(name="awal")

        layout_awal = BoxLayout(
            orientation="vertical",
            padding=padding_responsive(),
            spacing=spacing_responsive()
        )

        judul = Label(
            text="Welcome to PETUapp",
            font_size=font_responsive(55),
            font_name="BACK TO SCHOOL.otf",
            color=(1, 0.41, 0.71, 1)
        )

        # Button PLAY responsif
        if is_landscape:
            btn_w, btn_h = 0.30, 0.22
        else:
            btn_w, btn_h = 0.45, 0.33

        tombol_play = ImageButton(
            source="play.jpeg",
            size_hint=(btn_w, btn_h),
            pos_hint={"center_x": 0.5},
            allow_stretch=True,
            keep_ratio=True
        )
        tombol_play.bind(on_press=self.ganti_ke_menu)

        layout_awal.add_widget(judul)
        layout_awal.add_widget(tombol_play)

        awal.add_widget(layout_awal)

        # ==========================
        # HALAMAN 2 (MENU)
        # ==========================
        menu = TampilanMenuapp(name="menu")

        # ==========================
        # HALAMAN 3 (TRAPESIUM)
        # ==========================
        trapesium = TrapesiumScreen(name="TrapesiumScreen")

        # Masukkan semua screen
        self.manager.add_widget(awal)
        self.manager.add_widget(menu)
        self.manager.add_widget(trapesium)

        return self.manager


PETUapp().run()