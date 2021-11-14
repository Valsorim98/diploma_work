#!/usr/bin/env python3
# -*- coding: utf8 -*-

import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox

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

        self.__create_form()

        self.__create_labels()

        self.__create_comboboxes()

        self.__create_checkboxes()

        self.__create_button()

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

    def __create_form(self):
        """Method to create the GUI form.
        """

        # Create the window for GUI.
        self.__root = tk.Tk()

        # Set window name.
        self.__root.title("Hotel finder")

        # Prevents resizing.
        self.__root.resizable(False, False)

        # Set window size.
        root_width = 600
        root_height = 600

        # Place the window in the center of the screen.
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (root_width/2))
        y_cordinate = int((screen_height/2) - (root_height/2))
        self.__root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))

        # Set window background colour.
        self.__root.configure(bg="#A37CF7")

    def __searchdb_command(self):
        """Method to get the user input to search in the database.
        """

        __user_preferences = self.__user_preferences()

        # Call Database class.
        self.__database = Database(__user_preferences)

    def __create_labels(self):
        """Method to create the labels.
        """

        self.__main_label = tk.Label(text="Looking for a hotel?\nYou are at the right place!", fg="white", bg="#A37CF7")
        self.__main_label.config(font=("Courier", 12))

        self.__city_label = tk.Label(self.__root, text="City:", fg="white", bg="#A37CF7")
        self.__city_label.config(font=("Courier", 10))

        self.__stars_label = tk.Label(self.__root, text="Stars:", fg="white", bg="#A37CF7")
        self.__stars_label.config(font=("Courier", 10))

        self.__amenities_label = tk.Label(self.__root, text="Amenities:", fg="white", bg="#A37CF7")
        self.__amenities_label.config(font=("Courier", 10))

        self.__price_label = tk.Label(self.__root, text="Price:", fg="white", bg="#A37CF7")
        self.__price_label.config(font=("Courier", 10))

    def __create_comboboxes(self):
        """Method to create the comboboxes.
        """

        self.__city_combobox = Combobox(self.__root, width=25)
        self.__city_combobox['values'] = ['Burgas', 'Dobrich', 'Lovech', 'Montana', 'Pleven', 'Plovdiv', 'Razgrad', 'Ruse',
                                            'Shumen', 'Silistra', 'Sliven', 'Sofia', 'Stara Zagora', 'Svishtov', 'Targovishte', 'Varna', 'Veliko Turnovo', 'Vraca']

        self.__stars_combobox = Combobox(self.__root, width=25)
        self.__stars_combobox['values'] = [1, 2, 3, 4, 5]

        self.__price_combobox = Combobox(self.__root, width=25)
        self.__price_combobox['values'] = ["Up to 30 BGN", "31-50 BGN", "51-70 BGN", "71-100 BGN", "More than 100 BGN"]

    def __create_checkboxes(self):
        """Method to create the checkboxes.
        """

        self.__wi_fi_var = BooleanVar()
        self.__wi_fi_checkbox = Checkbutton(self.__root, text="Wi-fi", bg="#A37CF7", variable=self.__wi_fi_var)

        self.__ac_var = BooleanVar()
        self.__ac_checkbox = Checkbutton(self.__root, text="Air Conditioner", bg="#A37CF7", variable=self.__ac_var)

        self.__bar_var = BooleanVar()
        self.__bar_checkbox = Checkbutton(self.__root, text="Bar", bg="#A37CF7", variable=self.__bar_var)

        self.__restaurant_var = BooleanVar()
        self.__restaurant_checkbox = Checkbutton(self.__root, text="Restaurant", bg="#A37CF7", variable=self.__restaurant_var)

        self.__pets_var = BooleanVar()
        self.__pets_checkbox = Checkbutton(self.__root, text="Allow Pets", bg="#A37CF7", variable=self.__pets_var)

    def __create_button(self):
        """Method to create the button.
        """

        self.__search_btn = tk.Button(
            text="Search",
            width=15,
            height=2,
            fg="white",
            bg="#6DA536",
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
