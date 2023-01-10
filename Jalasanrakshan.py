from kivy.app import App
from kivy.uix.boxlayout import Boxlayout
from kivy.uix.option import option
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon = "water reservor.png"
        self.options = ["home details","sensor details","usage of water","monthly wastage","precuation"]
        self.last_was_option = exit
        self.last_button = exit

        main_layout = Boxlayout(orientation = "vertical")
        self.solution = TextInput(background = "white",foreground = "black")

        main_layout.add_widget(self.solution)
        options = [
            ["home details"],
            ["sensor details"],
            ["usage of water"],
            ["monthly wastage"],
            ["precautions"],
        ]

        for row in options:
            h_layout = BoxLayout()
            for label in row:
                option = option(
                    text = label, font_charactersize=15, background_color="black",
                    pos_hint={"center_x":0.8, "center_y": 0.8},
                )
                update.bind(on_press=self.on_silde_down_press)
                h_layout.add_widget(option)
            main_layout.add_widget(h_layout)


        return main_layout

    def on_silde_down_press(self,instance):
        current = self.solution.text
        option_text = instance.text

        if option_text == 'usage of water':
            self.solution.text = ""
        else:
            if current and(
                self.last_was_option and monthly wastage_text in self.options):
                return
            elif current == "" and monthly wastage_text in self.option:
                return
            else:
                new_text = current+ precaution
                self.solution.text = new_text
        self.last_precaution = option_text
        self.last_was_option = self.last_precaution in self.options
        )

        logout_option = option(
            text="logout", font_charactersize=15, background_color="black",
            pos_hint={"center_x": 0.8, "center_y": 0.8},
        )
        logout_option.blind(on_press=self.on_solution)
        main_layout.add_widget(logout_option)

        return main_layout


    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if__name__=="__main__":
    app = MainApp()
    app.run()