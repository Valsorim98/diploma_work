#!/usr/bin/env python3
# -*- coding: utf8 -*-

import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox
import emoji

from database import Database

class GUI():
    """Class GUI.
    """

# Region attributes.

    __root = None
    """Root window instance.
    """

    __search_btn = None
    """Search button.
    """

    __main_label = None
    """Main label.
    """

    __city_label = None
    """City label.
    """

    __stars_label = None
    """Stars label.
    """

    __amenities_label = None
    """Amenities label.
    """

    __price_label = None
    """Price label.
    """

    __city_combobox = None
    """Combobox for city entry.
    """

    __stars_combobox = None
    """Combobox for stars entry.
    """

    __price_combobox = None
    """Combobox for price entry.
    """

    __wi_fi_checkbox = None
    """Checkbox for wi-fi.
    """

    __ac_checkbox = None
    """Checkbox for air conditioner.
    """

    __bar_checkbox = None
    """Checkbox for bar.
    """

    __restaurant_checkbox = None
    """Checkbox for restaurant.
    """

    __pets_checkbox = None
    """Checkbox for allow pets.
    """

    __wi_fi_var = None
    """Boolean variable for Wi-fi.
    """

    __ac_var = None
    """Boolean variable for air conditioner.
    """

    __bar_var = None
    """Boolean variable for bar.
    """

    __restaurant_var = None
    """Boolean variable for restaurant.
    """

    __pets_var = None
    """Boolean variable for allow pets.
    """

    __database = None
    """Database abstraction.
    """

# End region attributes.

# Region constructor.

    def __init__(self):
        """Constructor for GUI class.
        """

        self.__main_form()

        self.__main_labels()

        self.__main_comboboxes()

        self.__main_checkboxes()

        self.__main_button()

        self.__positioning()

        self.run()

# End region constructor.

# Region public methods.

    def run(self):
        """Run the main loop.
        """

        self.__root.mainloop()

# End region public methods.

# Region private methods.

    def __main_form(self):
        """Method to create the main GUI form.
        """

        # Create the window for GUI.
        self.__root = tk.Tk()

        # Set window name.
        self.__root.title("Hotel finder")

        # Prevents resizing.
        self.__root.resizable(False, False)

        # Set window size.
        _root_width = 600
        _root_height = 600

        # Place the window in the center of the screen.
        _screen_width = self.__root.winfo_screenwidth()
        _screen_height = self.__root.winfo_screenheight()
        _x_cordinate = int((_screen_width/2) - (_root_width/2))
        _y_cordinate = int((_screen_height/2) - (_root_height/2))
        self.__root.geometry("{}x{}+{}+{}".format(_root_width, _root_height, _x_cordinate, _y_cordinate))

        # Set window background colour.
        self.__root.configure(bg="#1C86EE")

    def __results_form(self, found_hotels):
        """Method to show create a new form with the hotel results.
        """

        _found_hotels = found_hotels

        _root_results = Toplevel(self.__root)
        _root_results.title("Search results")
        _root_results.resizable(False, False)

        _root_results_width = 750
        _root_results_height = 750

        _screen_width = _root_results.winfo_screenwidth()
        _screen_height = _root_results.winfo_screenheight()
        _x_cordinate = int((_screen_width/2) - (_root_results_width/2))
        _y_cordinate = int((_screen_height/2) - (_root_results_height/2))
        _root_results.geometry("{}x{}+{}+{}".format(_root_results_width, _root_results_height, _x_cordinate, _y_cordinate))

        _root_results.configure(bg="#1C86EE")



        # ME and INDIAN:

        # Create frame on the root window.
        # dont need that
        # _frame=Frame(_root_results, bg="#1C86EE")
        # _frame.pack(fill=BOTH, expand="yes")

        # Create canvas on the frame.
        _canvas = Canvas(_root_results, bg="#1C86EE", bd=0, highlightthickness=0, relief='ridge')
        _canvas.pack(side=LEFT, expand=True, fill=BOTH)

        # Create the scrollbar on the frame.
        _scrollbar = Scrollbar(_root_results, orient="vertical", command=_canvas.yview)
        _scrollbar.pack(side=RIGHT, fill=Y)

        # Create label on the canvas.
        # _main_label = Label(_canvas, text="Results", fg="white", bg="#1C86EE", font=("arial", 20), pady=20)
        # _main_label.pack()

        # Make the canvas scrollable.
        _canvas.config(yscrollcommand=_scrollbar.set)
        _canvas.bind('<Configure>', lambda e: _canvas.configure(scrollregion=_canvas.bbox("all")))

        # Create a frame on the canvas.
        frame_in_canvas = Frame(_canvas, bg="#1C86EE", pady=30)

        # Populate the frame on the canvas with the text boxes.
        # Coords start with (x, y).
        _canvas.create_window((240,0), window=frame_in_canvas, anchor="nw")

        # Create a text box for every found hotel.
        for hotel in _found_hotels.values():

            # For star emoji:
            star = emoji.emojize(":star:")

            # Starting message.
            msg = f'''\nCity: {hotel["Town"]}\nName: {hotel["Hotel"]}\nStars: '''
            stars_msg = ""

            # Add number of stars equal to the star rating of the hotel.
            for i in range (hotel["Star Rating"]):
                stars_msg = stars_msg + star

            price_msg = hotel["Price"]

            # Concatenate strings.
            message = msg + stars_msg + f"\nPrice: {price_msg} BGN"

            # Concatenate string with wi-fi.
            if hotel["Wi-fi"] == True:
                wi_fi_msg = "\nWi-fi: Yes"
                message = message + wi_fi_msg
            else:
                wi_fi_msg = "\nWi-fi: No"
                message = message + wi_fi_msg

            # Concatenate string with air conditioner.
            if hotel["Air Conditioner"] == True:
                ac_msg = "\nAir conditioner: Yes"
                message = message + ac_msg
            else:
                ac_msg = "\nAir conditioner: No"
                message = message + ac_msg

            # Concatenate string with bar.
            if hotel["Bar"] == True:
                bar_msg = "\nBar: Yes"
                message = message + bar_msg
            else:
                bar_msg = "\nBar: No"
                message = message + bar_msg

            # Concatenate string with restaurant.
            if hotel["Restaurant"] == True:
                restaurant_msg = "\nRestaurant: Yes"
                message = message + restaurant_msg
            else:
                restaurant_msg = "\nRestaurant: No"
                message = message + restaurant_msg

            # Concatenate string with pets.
            if hotel["Allow Pets"] == True:
                pets_msg = "\nAllow pets: Yes"
                message = message + pets_msg
            else:
                pets_msg = "\nAllow pets: No"
                message = message + pets_msg

            text_box = Text(frame_in_canvas, height=11, width=32, font=("Courier", 10, "italic"))
            text_box.pack(pady=10)
            text_box.insert('end', message)
            # Make the text box not editable.
            text_box.config(state='disabled')

            text_box.tag_add("star", "4.7", "4.15")
            text_box.tag_config("star", background="white", foreground="red")

        # Focus the newly created form.
        _root_results.after(1, lambda: _root_results.focus_force())

    def __searchdb_command(self):
        """Method to get the user input to search in the database.
        """

        __user_preferences = self.__user_preferences()

        # Call Database class.
        self.__database = Database(__user_preferences)
        _found_hotels = self.__database.suitable_hotels

        # Create a new form with the results.
        self.__results_form(found_hotels=_found_hotels)

    def __main_labels(self):
        """Method to create the labels in main form.
        """

        self.__main_label = tk.Label(text="Looking for a hotel?\nYou are at the right place!", fg="white", bg="#1C86EE")
        self.__main_label.config(font=("Courier", 12))

        self.__city_label = tk.Label(self.__root, text="City:", fg="white", bg="#1C86EE")
        self.__city_label.config(font=("Courier", 10))

        self.__stars_label = tk.Label(self.__root, text="Stars:", fg="white", bg="#1C86EE")
        self.__stars_label.config(font=("Courier", 10))

        self.__amenities_label = tk.Label(self.__root, text="Amenities:", fg="white", bg="#1C86EE")
        self.__amenities_label.config(font=("Courier", 10))

        self.__price_label = tk.Label(self.__root, text="Price:", fg="white", bg="#1C86EE")
        self.__price_label.config(font=("Courier", 10))

    def __main_comboboxes(self):
        """Method to create the comboboxes in main form.
        """

        self.__city_combobox = Combobox(self.__root, width=25)
        self.__city_combobox['values'] = ['Burgas', 'Dobrich', 'Lovech', 'Montana', 'Pleven', 'Plovdiv', 'Razgrad', 'Ruse',
                                            'Shumen', 'Silistra', 'Sliven', 'Sofia', 'Stara Zagora', 'Svishtov', 'Targovishte', 'Varna', 'Veliko Turnovo', 'Vraca']

        self.__stars_combobox = Combobox(self.__root, width=25)
        self.__stars_combobox['values'] = [1, 2, 3, 4, 5]

        self.__price_combobox = Combobox(self.__root, width=25)
        self.__price_combobox['values'] = ["Up to 30 BGN", "31-50 BGN", "51-70 BGN", "71-100 BGN", "More than 100 BGN"]

    def __main_checkboxes(self):
        """Method to create the checkboxes in main form.
        """

        self.__wi_fi_var = BooleanVar()
        self.__wi_fi_checkbox = Checkbutton(self.__root, text="Wi-fi", fg="white", bg="#1C86EE", selectcolor="#1C86EE", variable=self.__wi_fi_var)

        self.__ac_var = BooleanVar()
        self.__ac_checkbox = Checkbutton(self.__root, text="Air Conditioner", fg="white", bg="#1C86EE", selectcolor="#1C86EE", variable=self.__ac_var)

        self.__bar_var = BooleanVar()
        self.__bar_checkbox = Checkbutton(self.__root, text="Bar", fg="white", bg="#1C86EE", selectcolor="#1C86EE", variable=self.__bar_var)

        self.__restaurant_var = BooleanVar()
        self.__restaurant_checkbox = Checkbutton(self.__root, text="Restaurant", fg="white", bg="#1C86EE", selectcolor="#1C86EE", variable=self.__restaurant_var)

        self.__pets_var = BooleanVar()
        self.__pets_checkbox = Checkbutton(self.__root, text="Allow Pets", fg="white", bg="#1C86EE", selectcolor="#1C86EE", variable=self.__pets_var)

    def __main_button(self):
        """Method to create the button in main form.
        """

        self.__search_btn = tk.Button(
            text="Search",
            font="Helvetica 9 bold",
            width=15,
            height=2,
            fg="black",
            bg="#F0FFFF",
            command=self.__searchdb_command)

    def __positioning(self):
        """Method to adjust the positioning of the labels, entries and button.
        """

        # Configure the grid.
        # The first column is twice as big as the second one.
        self.__root.columnconfigure(0, weight=2)
        self.__root.columnconfigure(1, weight=1)
        self.__root.columnconfigure(2, weight=2)

        # Positions of the labels.
        self.__main_label.grid(row=0, column=1, pady=30, sticky=W)

        self.__city_label.grid(row=1, column=0, pady=10, sticky=E)

        self.__stars_label.grid(row=2, column=0, pady=10, sticky=E)

        self.__amenities_label.grid(row=3, column=0, pady=10, sticky=E)

        self.__price_label.grid(row=5, column=0, pady=10, sticky=E)

        # Positions of the comboboxes.
        self.__city_combobox.grid(row=1, column=1, padx=40, sticky=W)

        self.__stars_combobox.grid(row=2, column=1, padx=40, sticky=W)

        self.__price_combobox.grid(row=5, column=1, padx=40, sticky=W)

        # Positions of the checkboxes.
        self.__wi_fi_checkbox.grid(row=3, column=1, padx=40, sticky=W)

        self.__ac_checkbox.grid(row=3, column=1, padx=10)

        self.__bar_checkbox.grid(row=4, column=1, padx=40, sticky=W)

        self.__restaurant_checkbox.grid(row=4, column=1, padx=10)

        self.__pets_checkbox.grid(row=4, column=1, padx=10, sticky=E)

        # Position of the search button.
        self.__search_btn.grid(row=6, column=1, padx=70, pady=30, sticky=W)

    def __user_preferences(self):
        """Method to get the user preferences and store them in a dictionary.

        Returns:
            dict: The user preferences.
        """

        # Create a default dict.
        __searchdb_dict = {"Town": 0, "Star Rating": 0, "Amenities": {"Wi-fi": 0, "Air Conditioner": 0, "Bar": 0, "Restaurant": 0, "Allow Pets": 0}, "Price": 0}

        # Get the inputs.
        __city_input = self.__city_combobox.get()
        # Lowercase the string and capitalize only the first letter of every word.
        __city_input = __city_input.lower().title()

        __stars_input = self.__stars_combobox.get()

        __price_input = self.__price_combobox.get()

        # Append the dict with the entries.
        if __city_input != "":
            __searchdb_dict["Town"] = __city_input

        if __stars_input != "":
            __stars_input = int(__stars_input)
            __searchdb_dict["Star Rating"] = __stars_input

        # Check if the checkboxes are checked.
        if self.__wi_fi_var.get() == True:
            __searchdb_dict["Amenities"]["Wi-fi"] = True

        if self.__ac_var.get() == True:
            __searchdb_dict["Amenities"]["Air Conditioner"] = True

        if self.__bar_var.get() == True:
            __searchdb_dict["Amenities"]["Bar"] = True

        if self.__restaurant_var.get() == True:
            __searchdb_dict["Amenities"]["Restaurant"] = True

        if self.__pets_var.get() == True:
            __searchdb_dict["Amenities"]["Allow Pets"] = True

        if __price_input != "":
            __searchdb_dict["Price"] = __price_input

        # for testing
        print(__searchdb_dict)

        return __searchdb_dict

# End region private methods.
