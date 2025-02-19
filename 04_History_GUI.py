from tkinter import *
from functools import partial  # To prevent unwanted windows


class Converter:
    """
    Temperature conversion tool (°C to °F or °F to °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                        text="History / Export",
                                        bg="#CC6600",
                                        fg="#FFFFFF",
                                        font=("Arial", "14", "bold"), width=12,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)

    def to_history(self):
        ExportHistory(self)


class ExportHistory:

    def __init__(self, partner):
        # setup dialogue box amd background colour
        background = "#ffe6cc"
        self.history_box = Toplevel()

        # disable history button
        partner.to_history_button.config(state=DISABLED)

        # if users press cross at the top, closes history
        #  and releases history box
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box, width=300,
                                   height=200)
        self.history_frame.grid()

        self.history_heading_label = Label(self.history_frame,
                                           text="history / Info",
                                           font=("Arial", "14", "bold"))
        self.history_heading_label.grid(row=0)

        self.history_text_label = Label(self.history_frame,
                                        text="history text goes here", wraplength=350,
                                        justify="left")
        self.history_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.history_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # list and loop to set the background colour on
        # everything except buttons
        recolour_list = [self.history_frame, self.history_heading_label,
                         self.history_text_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_history(self, partner):
        """
        Closes history dialogue box (and enable history button)
        """
        # put history button back to normal
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
