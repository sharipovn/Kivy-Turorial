import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    #Initilizie
    def __init__(self,**kwargs):
        #call gridlayout constructor
        super(MyGridLayout,self).__init__(**kwargs)
        #Set columns
        self.cols=2
        #Add widgets
        self.add_widget(Label(text="Name: "))
        self.name=TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Favorite Pizza : "))
        self.pizza=TextInput(multiline=False)
        self.add_widget(self.pizza)
        
        self.add_widget(Label(text="Favorite Colour : "))
        self.color=TextInput(multiline=False)
        self.add_widget(self.color)

        #Create a Submit Button
        self.submit=Button(text="Submit",font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self,insatance):
        name=self.name.text
        pizza=self.pizza.text
        color=self.color.text

        #print(f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!')
        self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!'))

        #clear input boxes
        self.name.text="" 
        self.pizza.text=""
        self.color.text=""
class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
