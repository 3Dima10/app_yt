"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
# from pytube import YouTube


class youtdolw(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label("Введите URL : ", style=Pack(padding=(0, 5)))

        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        name_label2 = toga.Label("Ведите путь : ", style=Pack(padding=(0,5)))

        self.name_input2 = toga.TextInput(style=Pack(flex=1))

        name_box2 = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box2.add(name_label2)
        name_box2.add(self.name_input2)

        button = toga.Button("BUTTON", on_press=self.say_hello, style=Pack(padding=5))

        main_box.add(name_box)
        main_box.add(name_box2)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        # print(f"Hello, {self.name_input.value}")
        # self.main_window.info_dialog(f"Hello, {self.name_input.value}", "FTK")
        from pytube import YouTube


        yt = YouTube(str(self.name_input.value))
        stream = yt.streams.get_by_itag(22) #выбираем по тегу, в каком формате будем скачивать.
        
        if not self.name_input2.value:
            stream.download()

        div = str(self.name_input2.value)

        stream.download(output_path=fr"{div}") #загружаем видео.
            

        self.main_window.info_dialog(f"Info", "Видео загружено")
        


def main():
    return youtdolw()
