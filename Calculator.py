import kivy


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 400)
Config.set('graphics', 'heigth', 500)
from kivy.core.window import Window
Window.clearcolor = (.62, .36, .92, 1)
class Calculator(App):
    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if (self.formula == "0" ):
            self.formula = ""

        self.formula += str(instance.text)
        self.update_label()

    def add_method (self, instance):
        if ( str(instance.text).lower() == "×"):
            self.formula += "*"
        else:
            self.formula += str(instance.text)

        self.update_label()
    
    def add_method1 (self, instance):
        if ( str(instance.text) == "÷"):
            self.formula += "/"
        else:
            self.formula += str(instance.text)
        
        self.update_label()

    def add_method2 (self, instance):
        if ( str(instance.text) == "−"):
            self.formula += "-"
        else:
            self.formula += str(instance.text)
        
        self.update_label()

    def calc_result(self, instance):
        if ( str(instance.text) == "C/="):
            self.formula += "="
        else:
            self.lbl.text = str(eval(self.lbl.text))
            self.formula = "0"


    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation = 'vertical', padding = 5)
        gl = GridLayout(cols = 4, spacing = 2.5)
        self.lbl = Label(text = "0", font_size = 50, halign = 'right', text_size = (400-80, 500/2))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text = "1", on_press = self.add_number,
        background_color = [.62, .36, .92, 1], background_normal = '',
         background_down = '',font_size = 35))
        gl.add_widget(Button(text = "2", on_press = self.add_number,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))
        gl.add_widget(Button(text = "3", on_press = self.add_number,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))
        gl.add_widget(Button(text = "×", on_press = self.add_method,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))

        gl.add_widget(Button(text = "4", on_press = self.add_number,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))
        gl.add_widget(Button(text = "5", on_press = self.add_number,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))
        gl.add_widget(Button(text = "6", on_press = self.add_number,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))
        gl.add_widget(Button(text = "−", on_press = self.add_method2,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))

        gl.add_widget(Button(text = "7", on_press = self.add_number,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))
        gl.add_widget(Button(text = "8", on_press = self.add_number,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))
        gl.add_widget(Button(text = "9", on_press = self.add_number,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))
        gl.add_widget(Button(text = "+", on_press = self.add_method,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))
        gl.add_widget(Button(text = ".", on_press = self.add_number,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))
        gl.add_widget(Button(text = "0", on_press = self.add_number,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))
        gl.add_widget(Button(text = "С/=", on_press = self.calc_result,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))
        gl.add_widget(Button(text = "÷", on_press = self.add_method1,
         background_color = [.62, .36, .92, 1], background_normal = '',
          background_down = '',font_size = 35))

        bl.add_widget(gl)
        return bl

if __name__ == "__main__":
    Calculator().run()
