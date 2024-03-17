from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivymd.uix.textfield import MDTextField
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivy.uix.popup import Popup

Window.size = (360,800)

class User:
    def __init__(self):
        self.address = ""
        self.password = ""
        self.first_name = ""
        self.middle_name = ""
        self.last_name = "" 
        self.balance = 0

class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = User()

    def createAccount(self):
        create = self.get_screen("fifth")
        self.user.address = create.ids.create_address.text
        self.user.first_name = create.ids.first_name.text
        self.user.middle_name = create.ids.middle_name.text
        self.user.last_name = create.ids.last_name.text

        self.address = self.user.address
        self.first_name = self.user.first_name
        self.middle_name = self.user.middle_name
        self.last_name = self.user.last_name
    def confirmPassword(self):
        create = self.get_screen("sixth")
        self.user.create_password = create.ids.create_password.text
        self.user.confirm_password = create.ids.confirm_password.text
        self.createAccount()
        if self.user.create_password != self.user.confirm_password:
            print("Invalid Password!")
            return False
        elif self.user.address == "" or self.user.first_name == "" or self.user.middle_name == "" or self.user.last_name == "" or self.user.create_password == "" or self.user.confirm_password == "":
            print("Fill out the information!")
            return False
        else:
            return True
    def onButtonPress(self):
        if self.confirmPassword():
            self.createAccount()
            self.current = 'fourth'
            print({self.user.address, self.user.first_name, self.user.middle_name, self.user.last_name, self.user.create_password}) 
    def login(self):
        login = self.get_screen("third")
        self.createAccount()
        self.confirmPassword()
        self.address = login.ids.address.text
        self.password = login.ids.password.text
        if self.address != self.user.address:
            print("Invalid email!")
            return False
        elif self.password != self.user.create_password:
            print("Invalid password!")
            return False
        elif self.address == "" or self.password == "":
            return False
        else:
            print("You have successfully logged in!")
            return True
    def btnlogin(self):
        if self.login():
            self.createAccount()
            self.current = 'fourth'
    def depositBal(self):    
        create = self.get_screen("depop")
        depositAmount = float(create.ids.depositinput.text)
        self.user.balance += depositAmount
        self.update()
    def update(self):
        main = self.get_screen('fourth')
        main.ids.balance.text = f'₱{self.user.balance:.2f}'
    def withdrawBal(self):
        create = self.get_screen("withdrop")
        withdrawAmount = float(create.ids.withdrawinput.text)
        self.user.balance -= withdrawAmount
        self.update()

class Paradise(MDApp):
    def build(self):
        return WindowManager()
if __name__=='__main__':
    Paradise().run()