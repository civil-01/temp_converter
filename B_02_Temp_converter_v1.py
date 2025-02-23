from tkinter import *
from functools import partial  # To prevent unwanted windows
import all_constants as c
import conversion_rounding as cr


class Converter:
    """
    Temperature conversion tool (°C to °F or °F tp °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.all_calculations_list = [['10.0°F is -12°C', '10.0°F is -12°C', '20.0°F is -7°C', '20.0°F is -7°C',
                                       '30.0°F is -1°C', '30.0°F is -1°C', '40.0°F is 4°C', '40.0°F is 4°C',
                                       '50.0°F is 10°C', '50.0°F is 10°C', '60.0°F is 16°C', '60.0°F is 16°C']
]

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Arial", "16", "bold"))
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and then press " \
                       "one of the buttons to convert it from centigrade " \
                       "to Fahrenheit."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame, font=("Arial", "16", "bold"))
        self.temp_entry.grid(row=2)

        error = "Please enter a number"
        self.answer_error = Label(self.temp_frame, text=error,
                                  fg="#004c99")
        self.answer_error.grid(row=3)

        # conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # button list (button text | bg colour | command | column)
        button_details_list = [
            ["To Celsius", "#990099", lambda: self.check_temp(c.ABS_ZERO_FAHRENHEIT), 0, 0],
            ["To Fahrenheit", "#009900", lambda: self.check_temp(c.ABS_ZERO_CELSIUS), 0, 1],
            ["Help / Info", "#CC6600", self.to_help, 1, 0],
            ["History / Export", "#004C99", "", 1, 1]
        ]

        # List to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Ariel", "12", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # retrieve help button
        self.to_help_button = self.button_ref_list[2]

        # retrieve 'history / export' button and disable it at the start ref at 3 which is line 4 as it starts at line 0
        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)

    def check_temp(self, min_temp, ):
        """
        Checks temperature is valid and either invokes a calculation
        function or shows a custom error
        """

        # Retrieve temperature to be converted
        to_convert = self.temp_entry.get()

        print("to convert", to_convert)

        # reset label and entry box (if we had an error)
        self.answer_error.config(fg="#004C99", font=("Arial", "13", "bold"))
        self.temp_entry.config(bg="#FFFFFF")

        error = f"Enter a number more than / equal to {min_temp}"
        has_errors = "no"

        try:
            to_convert = float(to_convert)
            if to_convert >= min_temp:
                error = ""
                self.convert(min_temp, to_convert)
            else:
                # error = "Too Low"
                pass

        except ValueError:
            # error = "please enter a number"
            pass

        # display the error if necessary
        if error != "":
            self.answer_error.config(text=error, fg="#9C0000")
            self.temp_entry.config(bg="#f4CCCC")
            self.temp_entry.delete(0, END)
        else:
            self.convert(min_temp, to_convert)

    def convert(self, min_temp, to_convert):
        """
        Converts temperatures and updates answer label. Also stores
        calculations for export / history feature
        """

        if min_temp == c.ABS_ZERO_CELSIUS:
            answer = cr.to_fahrenheit(to_convert)
            answer_statement = f"{to_convert}°C is {answer}°F"
        else:
            answer = cr.to_celsius(to_convert)
            answer_statement = f"{to_convert}°F is {answer}°C"

        # enable history export button as soon as we have a valid calculation
        self.to_history_button.config(state=NORMAL)

        self.answer_error.config(text=answer_statement)
        self.all_calculations_list.append(answer_statement)
        print(self.all_calculations_list)

    def to_help(self):
        DisplayHelp(self)


class DisplayHelp:

    def __init__(self, partner):
        # setup dialogue box amd background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_button.config(state=DISABLED)

        # if users press cross at the top, closes help
        #  and releases help box
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        self.help_text_label = Label(self.help_frame,
                                     text="help text goes here", wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # list and loop to set the background colour on
        # everything except buttons
        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        """
        Closes help dialogue box (and enable help button)
        """
        # put help button back to normal
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
