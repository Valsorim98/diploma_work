#!/usr/bin/env python3
# -*- coding: utf8 -*-

import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import Calendar
from functools import partial
import datetime
from datetime import date
import emoji

from database import Database

class GUI():
    """Class GUI.
    """

# Region attributes.

    __root = None
    """Root window instance for main form.
    """

    __results_canvas = None
    """Canvas on results form.
    """

    __eng_button = None
    """Button to change language to English.
    """

    __bul_button = None
    """Button to change language to Bulgarian.
    """

    __search_btn = None
    """Search button.
    """

    __main_label = None
    """Main label.
    """

    __name_label = None
    """Name label.
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

    __name_entry = None
    """Name entry.
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

    __chosen_language = "english"
    """Chosen language from the main form. English by default.
    """

# End region attributes.

# Region constructor.

    def __init__(self):
        """Constructor for GUI class.
        """

        self.__main_form()

        self.__positioning()

        self.__run()

# End region constructor.

# Region private methods.

    def __run(self):
        """Run the main loop.
        """

        self.__root.mainloop()

    def __change_language_eng(self):
        """Method to change the language to English.
        """

        self.__chosen_language = "english"

        self.__root.title("Hotel finder")

        self.__main_label.config(text="Looking for a hotel?\nYou are at the right place!")
        self.__name_label.config(text="Name:")
        self.__city_label.config(text="City:")
        self.__city_combobox['values'] = ['Burgas', 'Dobrich', 'Lovech', 'Montana', 'Pleven', 'Plovdiv', 'Razgrad', 'Ruse',
                                            'Shumen', 'Silistra', 'Sliven', 'Sofia', 'Stara Zagora', 'Svishtov', 'Targovishte', 'Varna', 'Veliko Turnovo', 'Vraca']
        self.__stars_label.config(text="Stars:")
        self.__amenities_label.config(text="Amenities:")
        self.__price_label.config(text="Price up to:")

        self.__wi_fi_checkbox.config(text="Wi-fi")
        self.__ac_checkbox.config(text="Air Conditioner")
        self.__ac_checkbox.grid(row=4, column=1, padx=10)
        self.__bar_checkbox.config(text="Bar")
        self.__restaurant_checkbox.config(text="Restaurant")
        self.__pets_checkbox.config(text="Allow Pets")

        self.__price_combobox['values'] = ["Up to 30 BGN", "31-50 BGN", "51-70 BGN", "71-100 BGN", "More than 100 BGN"]

        self.__search_btn.config(text="Search")

    def __change_language_bul(self):
        """Method to change the language to Bulgarian.
        """

        self.__chosen_language = "bulgarian"

        self.__main_label.config(text="Търсите хотел?\nВие сте на правилното място!")
        self.__name_label.config(text="           Име:")
        self.__city_label.config(text="Град:")
        self.__city_combobox['values'] = ['Бургас', 'Варна', 'Велико Търново', 'Враца', 'Добрич', 'Ловеч', 'Монтана', 'Плевен', 'Пловдив', 'Разград', 'Русе',
                                            'Свищов', 'Силистра', 'Сливен', 'София', 'Стара Загора', 'Търговище', 'Шумен']
        self.__stars_label.config(text="Звезди:")
        self.__amenities_label.config(text="Удобства:")
        self.__price_label.config(text="Цена до:")

        self.__wi_fi_checkbox.config(text="Интернет")
        self.__ac_checkbox.config(text="Климатик")
        self.__ac_checkbox.grid(row=4, column=1, padx=(0,30))
        self.__bar_checkbox.config(text="Бар")
        self.__restaurant_checkbox.config(text="Ресторант")
        self.__pets_checkbox.config(text="С дом. любимци")

        self.__price_combobox['values'] = ["До 30 лева", "31-50 лева", "51-70 лева", "71-100 лева", "Над 100 лева"]

        self.__search_btn.config(text="Търсене")

    def __onreturn_main(self, event):
        """When on main form, calls searchdb_command method on 'Return' button click.
        """

        self.__searchdb_command()

    def __onreturn_reserve(self, calendar, hotel_name, name_entry, room_capacity, days_entered, reservation_form):
        """When on reserve room form, calls reserve_room_command method on 'Return' button click.
        """

        self.__reserve_room_command(calendar, hotel_name, name_entry, room_capacity, days_entered, reservation_form)

    def __onreturn_review(self, city, hotel_name, _name_entry, _service_scale, _food_scale, _feedback, _root_review):
        """When on review form, calls submit_review_command on 'Return' button click.
        """

        self.__submit_review_command(city, hotel_name, _name_entry, _service_scale, _food_scale, _feedback, _root_review)

    def __on_mousewheel_results(self, event):
        self.__results_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def __main_form(self):
        """Method to create the main GUI form.
        """

        # Create the window for GUI.
        self.__root = tk.Tk()

        # Set window name.
        self.__root.title("Hotel finder")
        if self.__chosen_language != "english":
            self.__root.title("Търсене на хотели")

        # Prevents resizing.
        self.__root.resizable(False, False)

        # Set window size.
        _root_width = 600
        _root_height = 600

        # Place the window in the center of the screen.
        _screen_width = self.__root.winfo_screenwidth()
        _screen_height = self.__root.winfo_screenheight()
        _x_coordinate = int((_screen_width/2) - (_root_width/2))
        _y_coordinate = int((_screen_height/2) - (_root_height/2))
        self.__root.geometry("{}x{}+{}+{}".format(_root_width, _root_height, _x_coordinate, _y_coordinate))

        # Set window background colour.
        self.__root.configure(bg="#1C86EE")

        # Create buttons to change the language.
        self.__eng_button = tk.Button(self.__root, text='English', command=self.__change_language_eng)
        self.__bul_button = tk.Button(self.__root, text='Български', command=self.__change_language_bul)

        # Create the labels in the main form.
        self.__main_label = tk.Label(text="Looking for a hotel?\nYou are at the right place!", fg="white", bg="#1C86EE", font=("Courier", 14))
        self.__name_label = tk.Label(self.__root, text="Name:", fg="white", bg="#1C86EE", font=("Courier", 11))
        self.__city_label = tk.Label(self.__root, text="City:", fg="white", bg="#1C86EE", font=("Courier", 11))
        self.__stars_label = tk.Label(self.__root, text="Stars:", fg="white", bg="#1C86EE", font=("Courier", 11))
        self.__amenities_label = tk.Label(self.__root, text="Amenities:", fg="white", bg="#1C86EE", font=("Courier", 11))
        self.__price_label = tk.Label(self.__root, text="Price up to:", fg="white", bg="#1C86EE", font=("Courier", 11))

        # Create the entry in the main form.
        self.__name_entry = tk.Entry(self.__root, width=28)

        # Create the comboboxes in the main form.
        self.__city_combobox = Combobox(self.__root, width=25)
        self.__city_combobox['values'] = ['Burgas', 'Dobrich', 'Lovech', 'Montana', 'Pleven', 'Plovdiv', 'Razgrad', 'Ruse',
                                            'Shumen', 'Silistra', 'Sliven', 'Sofia', 'Stara Zagora', 'Svishtov', 'Targovishte', 'Varna', 'Veliko Turnovo', 'Vraca']

        self.__stars_combobox = Combobox(self.__root, width=25)
        self.__stars_combobox['values'] = [1, 2, 3, 4, 5]

        self.__price_combobox = Combobox(self.__root, width=25)
        self.__price_combobox['values'] = ["Up to 30 BGN", "31-50 BGN", "51-70 BGN", "71-100 BGN", "More than 100 BGN"]

        # Create the checkboxes in the main form.
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

        # Create the search button in the main form.
        self.__search_btn = tk.Button(
            self.__root,
            text="Search",
            font="Helvetica 9 bold",
            width=15,
            height=2,
            fg="black",
            bg="white",
            command=self.__searchdb_command)

        # On 'Return' button click to click the 'Search' button on main form.
        self.__root.bind("<Return>", self.__onreturn_main)

    def __results_form(self, found_hotels):
        """Method to create a results GUI form with the found hotels.

        Args:
            found_hotels (dict): All of the found hotels, searched by the user preferences.
        """

        _found_hotels = found_hotels

        _root_results = Toplevel(self.__root)
        _root_results.title("Search results")
        if self.__chosen_language != "english":
            _root_results.title("Резултати от търсенето")
        _root_results.resizable(False, False)

        _root_results_width = 750
        _root_results_height = 750

        _screen_width = _root_results.winfo_screenwidth()
        _screen_height = _root_results.winfo_screenheight()
        _x_coordinate = int((_screen_width/2) - (_root_results_width/2))
        _y_coordinate = int((_screen_height/2) - (_root_results_height/2))
        _root_results.geometry("{}x{}+{}+{}".format(_root_results_width, _root_results_height, _x_coordinate, _y_coordinate))

        _root_results.configure(bg="#1C86EE")

        # Create canvas over root.
        self.__results_canvas = Canvas(_root_results, bg="#1C86EE", bd=0, highlightthickness=0, relief='ridge')
        self.__results_canvas.pack(side=LEFT, expand=True, fill=BOTH)

        # Create the scrollbar on root.
        _scrollbar = Scrollbar(_root_results, orient="vertical", command=self.__results_canvas.yview)
        _scrollbar.pack(side=RIGHT, fill=Y)

        # Link the scrollbar to the canvas to make it active.
        self.__results_canvas.config(yscrollcommand=_scrollbar.set)
        self.__results_canvas.bind('<Configure>', lambda e: self.__results_canvas.configure(scrollregion=self.__results_canvas.bbox("all")))

        # Bind mouse wheel activation to the scrollbar in canvas.
        self.__results_canvas.bind_all("<MouseWheel>", self.__on_mousewheel_results)

        # Create a frame on the canvas.
        _frame_on_canvas = Frame(self.__results_canvas, bg="#1C86EE", pady=30)

        # Populate the frame on the canvas with the text boxes.
        # Coords start with (x, y).
        self.__results_canvas.create_window((0,0), window=_frame_on_canvas, anchor="nw", width=750)

        # Configure the grid.
        _frame_on_canvas.columnconfigure(0, weight=1)
        _frame_on_canvas.columnconfigure(1, weight=2)
        _frame_on_canvas.columnconfigure(2, weight=1)

        if self.__chosen_language == "english":
            _main_label = Label(_frame_on_canvas, text="Results", fg="white", bg="#1C86EE", font=("arial", 20))
            _main_label.grid(row=0, column=1, padx=112, pady=(0,20), sticky=E)
        else:
            _main_label = Label(_frame_on_canvas, text="Намерени хотели", fg="white", bg="#1C86EE", font=("arial", 20))
            _main_label.grid(row=0, column=1, padx=(0,45), pady=(0,20), sticky=E)

        row_counter = 1

        # Create a text box for every found hotel.
        for hotel in _found_hotels.values():

            # For star emoji:
            star = emoji.emojize(":star:")

            'Stara Zagora', 'Svishtov', 'Targovishte', 'Varna', 'Veliko Turnovo', 'Vraca'

            # Starting message.
            if self.__chosen_language == "english":
                msg = f'''\n     City: {hotel["Town"]}\n     Name: {hotel["Hotel"]}\n     Stars: '''
            else:
                # Change the name of the towns to Bulgarian if thats the chosen language.
                if hotel["Town"] == "Burgas":
                    hotel["Town"] = "Бургас"
                if hotel["Town"] == "Dobrich":
                    hotel["Town"] = "Добрич"
                if hotel["Town"] == "Lovech":
                    hotel["Town"] = "Ловеч"
                if hotel["Town"] == "Montana":
                    hotel["Town"] = "Монтана"
                if hotel["Town"] == "Pleven":
                    hotel["Town"] = "Плевен"
                if hotel["Town"] == "Plovdiv":
                    hotel["Town"] = "Пловдив"
                if hotel["Town"] == "Razgrad":
                    hotel["Town"] = "Разград"
                if hotel["Town"] == "Ruse":
                    hotel["Town"] = "Русе"
                if hotel["Town"] == "Shumen":
                    hotel["Town"] = "Шумен"
                if hotel["Town"] == "Silistra":
                    hotel["Town"] = "Силистра"
                if hotel["Town"] == "Sliven":
                    hotel["Town"] = "Сливен"
                if hotel["Town"] == "Sofia":
                    hotel["Town"] = "София"
                if hotel["Town"] == "Stara Zagora":
                    hotel["Town"] = "Стара Загора"
                if hotel["Town"] == "Svishtov":
                    hotel["Town"] = "Свищов"
                if hotel["Town"] == "Targovishte":
                    hotel["Town"] = "Търговище"
                if hotel["Town"] == "Varna":
                    hotel["Town"] = "Варна"
                if hotel["Town"] == "Veliko Turnovo":
                    hotel["Town"] = "Велико Търново"
                if hotel["Town"] == "Vraca":
                    hotel["Town"] = "Враца"
                msg = f'''\n     Град: {hotel["Town"]}\n     Име: {hotel["Hotel"]}\n     Звезди: '''

            stars_msg = ""

            # Add number of stars equal to the star rating of the hotel.
            for i in range (hotel["Star Rating"]):
                stars_msg = stars_msg + star

            price_msg = hotel["Price"]

            # Concatenate strings.
            if self.__chosen_language == "english":
                message = msg + stars_msg + f"\n     Price: {price_msg} BGN"
            else:
                message = msg + stars_msg + f"\n     Цена: {price_msg} лева"

            # Concatenate string with wi-fi.
            if hotel["Wi-fi"] == True:
                if self.__chosen_language == "english":
                    wi_fi_msg = "\n     Wi-fi: Yes"
                else:
                    wi_fi_msg = "\n     Интернет: Да"
                message = message + wi_fi_msg
            else:
                if self.__chosen_language == "english":
                    wi_fi_msg = "\n     Wi-fi: No"
                else:
                    wi_fi_msg = "\n     Интернет: Не"
                message = message + wi_fi_msg

            # Concatenate string with air conditioner.
            if hotel["Air Conditioner"] == True:
                if self.__chosen_language == "english":
                    ac_msg = "\n     Air conditioner: Yes"
                else:
                    ac_msg = "\n     Климатик: Да"
                message = message + ac_msg
            else:
                if self.__chosen_language == "english":
                    ac_msg = "\n     Air conditioner: No"
                else:
                    ac_msg = "\n     Климатик: Не"
                message = message + ac_msg

            # Concatenate string with bar.
            if hotel["Bar"] == True:
                if self.__chosen_language == "english":
                    bar_msg = "\n     Bar: Yes"
                else:
                    bar_msg = "\n     Бар: Да"
                message = message + bar_msg
            else:
                if self.__chosen_language == "english":
                    bar_msg = "\n     Bar: No"
                else:
                    bar_msg = "\n     Бар: Не"
                message = message + bar_msg

            # Concatenate string with restaurant.
            if hotel["Restaurant"] == True:
                if self.__chosen_language == "english":
                    restaurant_msg = "\n     Restaurant: Yes"
                else:
                    restaurant_msg = "\n     Ресторант: Да"
                message = message + restaurant_msg
            else:
                if self.__chosen_language == "english":
                    restaurant_msg = "\n     Restaurant: No"
                else:
                    restaurant_msg = "\n     Ресторант: Не"
                message = message + restaurant_msg

            # Concatenate string with pets.
            if hotel["Allow Pets"] == True:
                if self.__chosen_language == "english":
                    pets_msg = "\n     Allow pets: Yes"
                else:
                    pets_msg = "\n     С дом. любимци: Да"
                message = message + pets_msg
            else:
                if self.__chosen_language == "english":
                    pets_msg = "\n     Allow pets: No"
                else:
                    pets_msg = "\n     С дом. любимци: Не"
                message = message + pets_msg

            # Create and fill the text boxes with the found hotels.
            _text_box = Text(_frame_on_canvas, height=11, width=32, font=("Courier", 10, "italic"))
            _text_box.grid(row=row_counter, padx=30, pady=10, column=1, sticky=E)
            _text_box.insert('end', message)
            # Make the text box not editable.
            _text_box.config(state='disabled')

            # Change color of stars.
            _text_box.tag_add("star", "4.12", "4.18")
            _text_box.tag_config("star", background="white", foreground="red")

            if self.__chosen_language == "english":
                _reserve_btn = tk.Button(
                _frame_on_canvas,
                text="Reserve a room",
                font="Helvetica 9 bold",
                width=18,
                height=2,
                fg="black",
                bg="white",
                # Use partial to be able to pass the hotel name variable.
                command=partial(self.__reserve_room_form, hotel_name=hotel["Hotel"], results_form=_root_results))

                _reserve_btn.grid(row=row_counter, column=2, padx=(0,30), pady=50, sticky=NW)

                _review_btn = tk.Button(
                _frame_on_canvas,
                text="Leave a review",
                font="Helvetica 9 bold",
                width=18,
                height=2,
                fg="black",
                bg="white",
                command=partial(self.__review_form, city=hotel["Town"], hotel_name=hotel["Hotel"], results_form=_root_results))

                _review_btn.grid(row=row_counter, column=2, padx=(0,30), pady=(120,0), sticky=NW)
            else:
                _reserve_btn = tk.Button(
                _frame_on_canvas,
                text="Резервиране на стая",
                font="Helvetica 9 bold",
                width=18,
                height=2,
                fg="black",
                bg="white",
                # Use partial to be able to pass the hotel name variable.
                command=partial(self.__reserve_room_form, hotel_name=hotel["Hotel"], results_form=_root_results))

                _reserve_btn.grid(row=row_counter, column=2, padx=(0,30), pady=50, sticky=NW)

                _review_btn = tk.Button(
                _frame_on_canvas,
                text="Дайте мнение",
                font="Helvetica 9 bold",
                width=18,
                height=2,
                fg="black",
                bg="white",
                command=partial(self.__review_form, city=hotel["Town"], hotel_name=hotel["Hotel"], results_form=_root_results))

                _review_btn.grid(row=row_counter, column=2, padx=(0,30), pady=(120,0), sticky=NW)

            row_counter += 1

        # Focus the newly created form.
        _root_results.after(1, lambda: _root_results.focus_force())

    def __reserve_room_form(self, hotel_name, results_form):
        """Method to create the reserve room GUI form.

        Args:
            hotel_name (str): The name of the chosen hotel for reservation.
            results_form (tkform): The results form.
        """

        _root_reservation = Toplevel(self.__root, bg="#1C86EE")
        if self.__chosen_language == "english":
            _root_reservation.title("Reservation")
        else:
            _root_reservation.title("Резервация")
        _root_reservation.resizable(False, False)

        _root_reservation_width = 600
        _root_reservation_height = 600

        _screen_width = _root_reservation.winfo_screenwidth()
        _screen_height = _root_reservation.winfo_screenheight()
        _x_coordinate = int((_screen_width/2) - (_root_reservation_width/2))
        _y_coordinate = int((_screen_height/2) - (_root_reservation_height/2))
        _root_reservation.geometry("{}x{}+{}+{}".format(_root_reservation_width, _root_reservation_height, _x_coordinate, _y_coordinate))

        # Focus the newly created form.
        _root_reservation.after(1, lambda: _root_reservation.focus_force())

        # Destroy the results form.
        results_form.destroy()

        # Configure the grid.
        _root_reservation.columnconfigure(0, weight=1)
        _root_reservation.columnconfigure(1, weight=1)
        _root_reservation.columnconfigure(2, weight=1)

        if self.__chosen_language == "english":
            _main_label = Label(_root_reservation, text="Select accommodation date", fg="white", bg="#1C86EE", font=("Courier", 16))
        else:
            _main_label = Label(_root_reservation, text="Изберете дата за настаняване", fg="white", bg="#1C86EE", font=("Courier", 16))

        _main_label.grid(row=0, column=1, padx=20, pady=(60,0))

        # Get current date.
        _current_date = datetime.datetime.now()
        _current_year = _current_date.year
        _current_month = _current_date.month
        _current_day = _current_date.day

        # Create the calendar and pass the current date to be selected.
        _cal = Calendar(_root_reservation, selectmode = 'day',
               year = _current_year, month = _current_month,
               day = _current_day, date_pattern="dd-mm-yyyy")
        _cal.grid(row=1, column=1, padx=20, pady=(40,0))

        if self.__chosen_language == "english":
            _name_reservation_label = Label(_root_reservation, text="Enter name for reservation:", fg="white", bg="#1C86EE", font=("Courier", 14))
        else:
            _name_reservation_label = Label(_root_reservation, text="Въведете име за резервация:", fg="white", bg="#1C86EE", font=("Courier", 14))

        _name_reservation_label.grid(row=2, column=1, padx=(0,105), pady=(25,0))

        _name_entry = Entry(_root_reservation, width=20)
        _name_entry.grid(row=2, column=1, padx=(350,0), pady=(25,0))

        if self.__chosen_language == "english":
            _room_cap_label = Label(_root_reservation, text="Reserve a room for        people.", fg="white", bg="#1C86EE", font=("Courier", 14))
            _room_cap_combobox = Combobox(_root_reservation, width=8)
            _room_cap_combobox['values'] = [1, 2, 3, 4]
            _room_cap_combobox.grid(row=3,column=1, padx=(80,0), pady=(25,0))
        else:
            _room_cap_label = Label(_root_reservation, text="Резервирайте стая за        души.", fg="white", bg="#1C86EE", font=("Courier", 14))
            _room_cap_combobox = Combobox(_root_reservation, width=8)
            _room_cap_combobox['values'] = [1, 2, 3, 4]
            _room_cap_combobox.grid(row=3,column=1, padx=(125,0), pady=(25,0))

        _room_cap_label.grid(row=3, column=1, padx=(0,40), pady=(25,0))

        if self.__chosen_language == "english":
            _days_label = Label(_root_reservation, text="I would like to stay for        days.", fg="white", bg="#1C86EE", font=("Courier", 14))
            _days_label.grid(row=4, column=1, pady=(25,0))
            _days_combobox = Combobox(_root_reservation, width=8)
            _days_combobox['values'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            _days_combobox.grid(row=4, column=1, padx=(215,0), pady=(25,0))
        else:
            _days_label = Label(_root_reservation, text="Бих желал да остана за        дни.", fg="white", bg="#1C86EE", font=("Courier", 14))
            _days_label.grid(row=4, column=1, padx=(0,25), pady=(25,0))
            _days_combobox = Combobox(_root_reservation, width=8)
            _days_combobox['values'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            _days_combobox.grid(row=4, column=1, padx=(175,0), pady=(25,0))

        if self.__chosen_language == "english":
            _reserve_btn = Button(
                _root_reservation,
                text="Reserve",
                font="Helvetica 9 bold",
                width=15,
                height=2,
                fg="black",
                bg="white",
                command=partial(self.__reserve_room_command, calendar=_cal, hotel_name=hotel_name, name_entry=_name_entry, room_capacity=_room_cap_combobox,
                                days_entered=_days_combobox, reservation_form=_root_reservation))
        else:
            _reserve_btn = Button(
                _root_reservation,
                text="Резервиране",
                font="Helvetica 9 bold",
                width=15,
                height=2,
                fg="black",
                bg="white",
                command=partial(self.__reserve_room_command, calendar=_cal, hotel_name=hotel_name, name_entry=_name_entry, room_capacity=_room_cap_combobox,
                                days_entered=_days_combobox, reservation_form=_root_reservation))

        _reserve_btn.grid(row=5, column=1, pady=(25,0))

        # On 'Return' button click to click the 'Reserve' button on reservation form.
        _root_reservation.bind("<Return>", lambda reserve: self.__onreturn_reserve(_cal, hotel_name, _name_entry, _room_cap_combobox,
                            _days_combobox, _root_reservation))

    def __reserve_room_command(self, calendar, hotel_name, name_entry, room_capacity, days_entered, reservation_form):
        """Method to reserve a room.

        Args:
            calendar (tkcalendar): Calendar from tkinter.
            hotel_name (str): The name of the chosen hotel.
            name_entry (tkentry): The entered name from user for reservation.
            room_capacity (tkcombobox): The capacity of the chosen room for reservation.
            days_entered (tkcombobox): The days of stay at the hotel.
            reservation_form (tkform): The reservation form.
        """

        # Get the date selected on the calendar.
        _date = calendar.get_date()
        # Get the hotel name.
        _hotel_name = hotel_name
        # Get the name for reservation.
        _name_entered = name_entry.get()
        # Get the room capacity.
        _room_cap = room_capacity.get()
        # Get the days to stay in the hotel.
        _days_of_stay = days_entered.get()

        # Split the date into a list.
        _reservation_date = _date.split("-")

        # Convert the date into integers.
        _reserve_day = _reservation_date[0]
        _reserve_day = int(_reserve_day)

        _reserve_month = _reservation_date[1]
        _reserve_month = int(_reserve_month)

        _reserve_year = _reservation_date[2]
        _reserve_year = int(_reserve_year)

        # Get today's date in d/m/y format.
        _today = date.today()
        _today_format = _today.strftime("%d/%m/%Y")

        # Split the date into a list.
        _today_list = _today_format.split("/")

        # Convert the date into integers.
        _now_day = _today_list[0]
        _now_day = int(_now_day)

        _now_month = _today_list[1]
        _now_month = int(_now_month)

        _now_year = _today_list[2]
        _now_year = int(_now_year)

        # Flag to check if the given reservation date is in the past.
        _invalid_reserve_date = False

        # Checks for valid reservation date.
        if _reserve_year > _now_year:
            _invalid_reserve_date = False

        if _reserve_year < _now_year:
            _invalid_reserve_date = True

        if _reserve_year == _now_year:
            if _reserve_month < _now_month:
                _invalid_reserve_date = True
            if _reserve_month > _now_month:
                _invalid_reserve_date = False
            if _reserve_month == _now_month:
                if _reserve_day > _now_day:
                    _invalid_reserve_date = False
                if _reserve_day == _now_day:
                    _invalid_reserve_date = False
                if _reserve_day < _now_day:
                    _invalid_reserve_date = True

        # Contains digit flag.
        _contains_digit = False

        # Check if the entered values from the reserve form are valid.
        try:
            for symbol in _name_entered:
                if symbol.isdigit():
                    if self.__chosen_language == "english":
                        messagebox.showerror("Something went wrong", f"We were unable to reserve a room for hotel {_hotel_name}.\nPlease enter valid values.")
                    else:
                        messagebox.showerror("Нещо се обърка", f"Не успяхме да резервираме стая за хотел {_hotel_name}.\nМоля, въведете валидни стойности.")
                    reservation_form.after(1, lambda: reservation_form.focus_force())
                    _contains_digit = True
                    break
                if _invalid_reserve_date == True:
                    if self.__chosen_language == "english":
                        messagebox.showerror("Invalid date", f"We were unable to reserve a room for hotel {_hotel_name}.\nPlease enter a valid date.")
                    else:
                        messagebox.showerror("Невалидна дата", f"Не успяхме да резервираме стая за хотел {_hotel_name}.\nМоля, въведете валидна дата.")
                    reservation_form.after(1, lambda: reservation_form.focus_force())
                    break
            _name_entered = _name_entered.lower().title()
            #if (_room_cap != "") and (_days_of_stay != ""):
            _room_cap = int(_room_cap)
            _days_of_stay = int(_days_of_stay)
            if (_days_of_stay != "" and _days_of_stay >= 1 and _days_of_stay <= 14 and
                _room_cap != "" and _room_cap >= 1 and _room_cap <= 4 and
                _name_entered != "" and _contains_digit == False and _invalid_reserve_date == False):
                reservation_form.destroy()
                if self.__chosen_language == "english":
                    messagebox.showinfo("Reserved", f"Thank you for choosing hotel {_hotel_name}. We are expecting {_name_entered} on {_date}. Time of stay - {_days_of_stay} days.")
                else:
                    messagebox.showinfo("Резервирана е стая", f"Благодарим Ви, че избрахте хотел {_hotel_name}. Очакваме Ви, {_name_entered} на {_date}. Време за престой - {_days_of_stay} дена.")
            if _days_of_stay <= 0 or _days_of_stay >= 15 or _room_cap <= 0 or _room_cap >= 5 or _name_entered == "":
                if self.__chosen_language == "english":
                    messagebox.showerror("Something went wrong", f"We were unable to reserve a room for hotel {_hotel_name}.\nPlease enter valid values.")
                else:
                    messagebox.showerror("Нещо се обърка", f"Не успяхме да резервираме стая за хотел {_hotel_name}.\nМоля, въведете валидни стойности.")
                reservation_form.after(1, lambda: reservation_form.focus_force())
        except:
            if self.__chosen_language == "english":
                messagebox.showerror("Something went wrong", f"We were unable to reserve a room for hotel {_hotel_name}.\nPlease enter valid values.")
            else:
                messagebox.showerror("Нещо се обърка", f"Не успяхме да резервираме стая за хотел {_hotel_name}.\nМоля, въведете валидни стойности.")
            reservation_form.after(1, lambda: reservation_form.focus_force())

    def __review_form(self, city, hotel_name, results_form):
        """Method to create the review GUI form.

        Args:
            results_form (tkform): The results form.
        """

        _root_review = Toplevel(self.__root, bg="#1C86EE")
        if self.__chosen_language == "english":
            _root_review.title("Leave a review")
        else:
            _root_review.title("Обратна връзка")
        _root_review.resizable(False, False)

        _root_review_width = 600
        _root_review_height = 600

        _screen_width = _root_review.winfo_screenwidth()
        _screen_height = _root_review.winfo_screenheight()
        _x_coordinate = int((_screen_width/2) - (_root_review_width/2))
        _y_coordinate = int((_screen_height/2) - (_root_review_height/2))
        _root_review.geometry("{}x{}+{}+{}".format(_root_review_width, _root_review_height, _x_coordinate, _y_coordinate))

        # Configure the grid.
        _root_review.columnconfigure(0, weight=1)
        _root_review.columnconfigure(1, weight=1)
        _root_review.columnconfigure(2, weight=1)

        if self.__chosen_language == "english":
            _main_label = Label(_root_review, text="Tell us what you think", fg="white", bg="#1C86EE", font=("Courier", 14))
        else:
            _main_label = Label(_root_review, text="Споделете ни какво мислите", fg="white", bg="#1C86EE", font=("Courier", 14))

        _main_label.grid(row=0, column=1, pady=(50,0))

        if self.__chosen_language == "english":
            _name_label = Label(_root_review, text="Enter your name:", font=("Courier", 12), fg="white", bg="#1C86EE")
        else:
            _name_label = Label(_root_review, text="Вашето име:", font=("Courier", 12), fg="white", bg="#1C86EE")

        _name_label.grid(row=1, column=1, padx=(25,0), pady=(30,0), sticky=W)

        _name_entry = Entry(_root_review, width=28)
        _name_entry.grid(row=1, column=1, padx=(155,0), pady=(30,0))

        if self.__chosen_language == "english":
            _service_label = Label(_root_review, text="Evaluation of service:", font=("Courier", 12), fg="white", bg="#1C86EE")
        else:
            _service_label = Label(_root_review, text="Оценка на услугите:", font=("Courier", 12), fg="white", bg="#1C86EE")

        _service_label.grid(row=2, column=1, padx=(25,0), pady=(30,0), sticky=W)

        _service_scale = Scale(_root_review, from_=1, to=5, troughcolor="white", highlightbackground="#1C86EE", bg="#1C86EE", orient=HORIZONTAL)
        _service_scale.set(3)
        _service_scale.grid(row=2, column=1, padx=(225,0), pady=(15,0))

        if self.__chosen_language == "english":
            __food_label = Label(_root_review, text="How was the food?", font=("Courier", 12), fg="white", bg="#1C86EE")
        else:
            __food_label = Label(_root_review, text="Хареса ли Ви храната?", font=("Courier", 12), fg="white", bg="#1C86EE")

        __food_label.grid(row=3, column=1, padx=(25,0), pady=(30,0), sticky=W)

        _food_scale = Scale(_root_review, from_=1, to=5, troughcolor="white", highlightbackground="#1C86EE", bg="#1C86EE", orient=HORIZONTAL)
        _food_scale.set(3)
        _food_scale.grid(row=3, column=1, padx=(225,0), pady=(15,0))

        _feedback = Text(_root_review, height=9, width=42, font=("Courier", 12), wrap="word")
        _feedback.grid(row=4, column=1, pady=30)
        if self.__chosen_language == "english":
            _feedback.insert(INSERT, "We want to know more for your experience with us.")
        else:
            _feedback.insert(INSERT, "Искаме да знаем повече за престоя Ви при нас.")

        # Make the inserted text in the Text widget temporary.
        _feedback.bind("<Button-1>", lambda e: _feedback.delete(1.0, END))

        if self.__chosen_language == "english":
            _submit_button = Button(_root_review,
                text="Submit",
                font="Helvetica 9 bold",
                width=15,
                height=2,
                fg="black",
                bg="white",
                command=partial(self.__submit_review_command, city=city, hotel_name=hotel_name, name_entry=_name_entry, service_scale=_service_scale,
                                food_scale=_food_scale, feedback=_feedback, review_form=_root_review))
        else:
            _submit_button = Button(_root_review,
                text="Изпращане",
                font="Helvetica 9 bold",
                width=15,
                height=2,
                fg="black",
                bg="white",
                command=partial(self.__submit_review_command, city=city, hotel_name=hotel_name, name_entry=_name_entry, service_scale=_service_scale,
                                food_scale=_food_scale, feedback=_feedback, review_form=_root_review))

        _submit_button.grid(row=5, column=1)

        # Focus the newly created form.
        _root_review.after(1, lambda: _root_review.focus_force())

        # Destroy the results form.
        results_form.destroy()

        _root_review.bind("<Return>", lambda review: self.__onreturn_review(city, hotel_name, _name_entry, _service_scale, _food_scale, _feedback, _root_review))

    def __submit_review_command(self, city, hotel_name, name_entry, service_scale, food_scale, feedback, review_form):
        """Method to submit hotel reviews in a database collection.

        Args:
            hotel_name (str): The name of the chosen hotel to give a review.
            name_entry (str): Name of the user giving a review.
            service_scale (int): Evaluation of the service.
            food_scale (int): Evaluation of the food.
            feedback (str): Feedback for the hotel in free text.
            review_form (tkform): The review form.
        """

        # The name of the city of the chosen hotel.
        _city = city

        # Create dict to store the data for the review.
        _review_dict = {}

        # Get the name of the chosen hotel.
        _hotel_name = hotel_name
        # Get the name of the person giving a review.
        _name_entered = name_entry.get()
        # Get the evaluation of the service.
        _service_eval = service_scale.get()
        # Get the evaluation of the food.
        _food_eval = food_scale.get()
        # Get the free text feedback.
        _feedback = feedback.get(1.0, END)

        # Operate on strings.
        _name_entered = _name_entered.lower().title()
        _feedback = _feedback[:-1]

        # Append the dict with the data.
        _review_dict["Town"] = _city
        _review_dict["Hotel"] = _hotel_name
        _review_dict["Name"] = _name_entered
        _review_dict["Service"] = _service_eval
        _review_dict["Food"] = _food_eval

        # Contains digit flag.
        _contains_digit = False

        # Check if the entered values from the review form are valid.
        try:
            for symbol in _name_entered:
                if symbol.isdigit():
                    if self.__chosen_language == "english":
                        messagebox.showerror("Something went wrong", f"We were unable to get your review for hotel {_hotel_name}.\nPlease try again.")
                    else:
                        messagebox.showerror("Нещо се обърка", f"Не успяхме да въведем вашето мнение за хотел {_hotel_name}.\nМоля, опитайте отново.")
                    review_form.after(1, lambda: review_form.focus_force())
                    _contains_digit = True
                    break
            _name_entered = _name_entered.lower().title()
            _service_eval = int(_service_eval)
            _food_eval = int(_food_eval)
            if _name_entered != "" and _contains_digit == False:
                review_form.destroy()
                if _feedback == "We want to know more for your experience with us." or _feedback == "":
                    _review_dict["Additional info"] = "None"
                    self.__database.insert_review(_review_dict)
                    if self.__chosen_language == "english":
                        messagebox.showinfo("Review sent", f"Thank you for your feedback for hotel {_hotel_name}.\nFrom {_name_entered} - service evaluation: {_service_eval}, food evaluation: {_food_eval}, additional information: None.")
                    else:
                        messagebox.showinfo("Мнението Ви е изпратено", f"Благодарим Ви за вашето мнение за хотел {_hotel_name}.\nОт {_name_entered} - оценка на услугите: {_service_eval}, оценка на храната: {_food_eval}, допълнителна информация: Няма.")
                if _feedback != "We want to know more for your experience with us.":
                    _review_dict["Additional info"] = _feedback
                    self.__database.insert_review(_review_dict)
                    if self.__chosen_language == "english":
                        messagebox.showinfo("Review sent", f"Thank you for your feedback for hotel {_hotel_name}.\nFrom {_name_entered} - service evaluation: {_service_eval}, food evaluation: {_food_eval}, additional information: {_feedback}")
                    else:
                        messagebox.showinfo("Мнението Ви е изпратено", f"Благодарим Ви за вашето мнение за хотел {_hotel_name}.\nОт {_name_entered} - оценка на услугите: {_service_eval}, оценка на храната: {_food_eval}, допълнителна информация: {_feedback}")
            if _name_entered == "":
                if self.__chosen_language == "english":
                    messagebox.showerror("Something went wrong", f"We were unable to get your review for hotel {_hotel_name}.\nPlease enter your name.")
                else:
                    messagebox.showerror("Нещо се обърка", f"Не успяхме да въведем вашето мнение за хотел {_hotel_name}.\nМоля, въведете вашето име.")
                review_form.after(1, lambda: review_form.focus_force())
        except:
            if self.__chosen_language == "english":
                messagebox.showerror("Something went wrong", f"We were unable to get your review for hotel {_hotel_name}.\nPlease try again.")
            else:
                messagebox.showerror("Нещо се обърка", f"Не успяхме да въведем вашето мнение за хотел {_hotel_name}.\nМоля, опитайте отново.")
            review_form.after(1, lambda: review_form.focus_force())

    def __searchdb_command(self):
        """Method to get the user preferences stored in a dict and search in the database.
        """

        __user_preferences = self.__user_preferences()

        # Check if there are wrong user inputs.
        if (__user_preferences["Star Rating"] == "error") or (__user_preferences["Price"] == "error"):
            pass
        else:
            # Call Database class.
            self.__database = Database(__user_preferences)
            _found_hotels = self.__database.found_hotels

            # If the _found_hotels dict is not empty to create a results form and populate it with them.
            if _found_hotels:
                # Create a results form with the found hotels.
                self.__results_form(found_hotels=_found_hotels)
            # If it is empty to show a pop up message.
            else:
                if self.__chosen_language == "english":
                    messagebox.showerror("No hotels found", f"No hotels found for your preferences.\nPlease try again.")
                else:
                    messagebox.showerror("Няма намерени хотели", f"Няма намерени хотели по вашите изисквания.\nМоля, опитайте отново.")

    def __positioning(self):
        """Method to adjust the positioning of the labels, entries and buttons in the main form.
        """

        # Configure the grid.
        # The first column is twice as big as the second one.
        self.__root.columnconfigure(0, weight=2)
        self.__root.columnconfigure(1, weight=1)
        self.__root.columnconfigure(2, weight=2)

        # Positions of language change buttons.
        self.__eng_button.grid(row=0, column=0, padx=(10,0), pady=(10,0), sticky=NW)
        self.__bul_button.grid(row=0, column=0, padx=(65,0), pady=(10,0), sticky=NW)

        # Positions of the labels.
        self.__main_label.grid(row=0, column=1, padx=(0,75), pady=(60,40), sticky=W)
        self.__name_label.grid(row=1, column=0, pady=10, sticky=E)
        self.__city_label.grid(row=2, column=0, pady=10, sticky=E)
        self.__stars_label.grid(row=3, column=0, pady=10, sticky=E)
        self.__amenities_label.grid(row=4, column=0, pady=10, sticky=E)
        self.__price_label.grid(row=6, column=0, pady=20, sticky=E)

        # Position of the entry.
        self.__name_entry.grid(row=1, column=1, padx=50, sticky=W)

        # Positions of the comboboxes.
        self.__city_combobox.grid(row=2, column=1, padx=50, sticky=W)
        self.__stars_combobox.grid(row=3, column=1, padx=50, sticky=W)
        self.__price_combobox.grid(row=6, column=1, padx=50, pady=20, sticky=W)

        # Positions of the checkboxes.
        self.__wi_fi_checkbox.grid(row=4, column=1, padx=45, sticky=W)
        self.__ac_checkbox.grid(row=4, column=1, padx=10)
        self.__bar_checkbox.grid(row=5, column=1, padx=45, sticky=W)
        self.__restaurant_checkbox.grid(row=5, column=1, padx=143, sticky=W)
        self.__pets_checkbox.grid(row=5, column=1, padx=40, sticky=E)

        # Position of the search button.
        self.__search_btn.grid(row=7, column=1, padx=80, pady=30, sticky=W)

    def __user_preferences(self):
        """Method to get the user preferences from the main GUI form and store them in a dictionary.

        Returns:
            dict: The user preferences.
        """

        # Create a default dict.
        __searchdb_dict = {"Name": 0, "Town": 0, "Star Rating": 0, "Amenities": {"Wi-fi": 0, "Air Conditioner": 0, "Bar": 0, "Restaurant": 0, "Allow Pets": 0}, "Price": 0}

        # Get the inputs.
        __name_input = self.__name_entry.get()
        __city_input = self.__city_combobox.get()

        # Lowercase the string and capitalize only the first letter of every word of the name and city inputs.
        __name_input = __name_input.lower().title()
        __city_input = __city_input.lower().title()

        __stars_input = self.__stars_combobox.get()
        __price_input = self.__price_combobox.get()

        _show_error_flag = False

        # Append the dict with the entries.
        if __name_input != "":
            __searchdb_dict["Name"] = __name_input

        if __city_input != "":
            __searchdb_dict["Town"] = __city_input

        if __stars_input != "":
            try:
                __stars_input = int(__stars_input)
                __searchdb_dict["Star Rating"] = __stars_input
            except:
                __searchdb_dict["Star Rating"] = "error"
                _show_error_flag = True

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
            try:
                __price_input = int(__price_input)
                __searchdb_dict["Price"] = __price_input
            except:
                __searchdb_dict["Price"] = "error"
                _show_error_flag = True

        if _show_error_flag == True:
            if self.__chosen_language == "english":
                messagebox.showerror("Something went wrong", "Please enter valid values.")
            else:
                messagebox.showerror("Нещо се обърка", "Моля, въведете валидни стойности.")

        # for testing
        print(f"Searchdb dict: {__searchdb_dict}")

        return __searchdb_dict

# End region private methods.
