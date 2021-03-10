from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

from random import uniform
import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def get_img_link(self):
        # Get the user query from Text_query
        query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and the first image link
        page = wikipedia.page(query)
        img_link = page.images[round(uniform(0, 10))]
        return img_link

    def download_img(self):
        # Download the image
        req = requests.get(self.get_img_link())
        imgpath = 'files/img.jpg'
        with open(imgpath, 'wb') as file:
            file.write(req.content)
        return imgpath

    def set_img(self):
        # Set the image in the image widget
        self.manager.current_screen.ids.img.source = self.download_img()
        self.ids.img.opacity = 1
        # self.ids.img.reload()
        # print(dir(self.ids.img))


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
