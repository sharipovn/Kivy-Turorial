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
        self.cols=1

        #create a second gridlayout
        self.top_grid=GridLayout()
        self.top_grid.cols=2
        
        #Add widgets
        self.top_grid.add_widget(Label(text="Name: "))
        self.name=TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Favorite Pizza : "))
        self.pizza=TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)
        
        self.top_grid.add_widget(Label(text="Favorite Colour : "))
        self.color=TextInput(multiline=False)
        self.top_grid.add_widget(self.color)


        #Add the new top_grid to our app
        self.add_widget(self.top_grid)


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
