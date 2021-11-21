#!/usr/bin/env python3
# -*- coding: utf8 -*-

from pymongo import MongoClient
import certifi

class Database():
    """Class database.
    """

# Region attributes.

    __client = None
    """Connect as a client.
    """

    suitable_hotels = None
    """The found hotels.
    """

# End region.

# Region constructor.

    def __init__(self, user_preferences):
        """Constructor for database class.
        """

        self.__user_preferences = user_preferences

        self.__get_documents()

# End region.

# Region private methods.

    def __connection_database(self):
        """Method to connect to the database.
        """

        # Use SSL for the connection to the cluster.
        ca = certifi.where()

        # MongoDB URL to connect to the cluster.
        url = "mongodb+srv://analytics:analytics-password@mflix.jkfp1.mongodb.net/Hotels?retryWrites=true&w=majority"

        # Connect to the database with the cluster URL and SSL.
        self.__client = MongoClient(url, tlsCAFile=ca)

        return self.__client["Hotels"]

    def __get_documents(self):
        """Method to search for the hotels in the database with the user preferences.
        """

        # Pass the method that connects to the database.
        db = self.__connection_database()

        # Pass the collection with the hotels.
        collection = db["Hotel_Info"]

        # Get all the documents from the collection.
        read_collection = collection.find({})

        # Flag for a suitable hotel.
        suitable_hotel = False

        # Hotel counter.
        num_hotels = 0

        # Dict for found hotels.
        found_hotels = {}

        # Prints all hotels in the town from user preferences.
        for hotel in read_collection:

            # Create dict with the given preferences to search in the database.
            __searchdb = {}

            # If the user didn't specify any preferences print all hotels.
            if self.__user_preferences["Town"] == 0 and self.__user_preferences["Star Rating"] == 0 and self.__user_preferences["Amenities"]["Wi-fi"] == 0 and self.__user_preferences["Amenities"]["Air Conditioner"] == 0 and self.__user_preferences["Amenities"]["Bar"] == 0 and self.__user_preferences["Amenities"]["Restaurant"] == 0 and self.__user_preferences["Amenities"]["Allow Pets"] == 0 and self.__user_preferences["Price"] == 0:
                print(hotel)
                num_hotels += 1

            # If there are any given preferences to search with them.
            else:

                # Search by town.
                if self.__user_preferences["Town"] != 0:
                    __searchdb["Town"] = self.__user_preferences["Town"]

                # Search by star rating.
                if self.__user_preferences["Star Rating"] != 0:
                    __searchdb["Star Rating"] = self.__user_preferences["Star Rating"]

                # Search by wi-fi.
                if self.__user_preferences["Amenities"]["Wi-fi"] != 0:
                    __searchdb["Wi-fi"] = True

                # Search by air conditioner.
                if self.__user_preferences["Amenities"]["Air Conditioner"] != 0:
                    __searchdb["Air Conditioner"] = True

                # Search by bar.
                if self.__user_preferences["Amenities"]["Bar"] != 0:
                    __searchdb["Bar"] = True

                # Search by restaurant.
                if self.__user_preferences["Amenities"]["Restaurant"] != 0:
                    __searchdb["Restaurant"] = True

                # Search by pets.
                if self.__user_preferences["Amenities"]["Allow Pets"] != 0:
                    __searchdb["Allow Pets"] = True

                # Search by price.
                if self.__user_preferences["Price"] != 0:
                    __searchdb["Price"] = self.__user_preferences["Price"]

            # Iterate on every key - value pair from __searchdb dict.
            for key, value in __searchdb.items():

                if (key, value) in hotel.items():
                    suitable_hotel = True

                elif key == "Price":

                    if value == "Up to 30 BGN":
                        if hotel["Price"] <= 30:
                            suitable_hotel = True

                        else:
                            suitable_hotel = False
                            break

                    elif value == "31-50 BGN":
                        if hotel["Price"] >= 31 and hotel["Price"] <= 50:
                            suitable_hotel = True

                        else:
                            suitable_hotel = False
                            break

                    elif value == "51-70 BGN":
                        if hotel["Price"] >= 51 and hotel["Price"] <= 70:
                            suitable_hotel = True

                        else:
                            suitable_hotel = False
                            break

                    elif value == "71-100 BGN":
                        if hotel["Price"] >= 71 and hotel["Price"] <= 100:
                            suitable_hotel = True

                        else:
                            suitable_hotel = False
                            break

                    elif value == "More than 100 BGN":
                        if hotel["Price"] > 100:
                            suitable_hotel = True

                        else:
                            suitable_hotel = False
                            break

                    # If the input price is different from the options in the dropdown menu, to look for hotels up to the given price.
                    else:
                        # Convert string to int.
                        hotel_price = int(__searchdb["Price"])

                        if hotel["Price"] <= hotel_price:
                            suitable_hotel = True

                        else:
                            suitable_hotel = False

                else:
                    suitable_hotel = False
                    break

            # Print only the hotels that coincide with all the user preferences and append them to found_hotels dict.
            if suitable_hotel == True:
                print(hotel)
                num_hotels += 1
                found_hotels.update({num_hotels:hotel})

        # For testing.
        print(__searchdb)
        print(f"{num_hotels} hotels found.")
        print(f"\nFound hotels: {found_hotels}")

        # Make found_hotels dict as a class attribute to be able to get it outside of the class.
        self.suitable_hotels = found_hotels

# End region.
