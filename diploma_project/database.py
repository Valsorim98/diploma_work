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

        # Prints all hotels in the town from user preferences.
        for hotel in read_collection:

            # Get the data for each hotel from the database.
            db_town_hotel = hotel["Town"]
            db_stars_hotel = hotel["Star Rating"]
            db_price_hotel = hotel["Price"]

            # Create a dict for each hotels' amenities and append it.
            db_amenities_hotel = {"Wi-fi": 0, "Air Conditioner": 0, "Bar": 0, "Restaurant": 0, "Allow Pets": 0}

            db_wifi_hotel = hotel["Wi-fi"]
            db_amenities_hotel["Wi-fi"] = db_wifi_hotel

            db_ac_hotel = hotel["Air Conditioner"]
            db_amenities_hotel["Air Conditioner"] = db_ac_hotel

            db_bar_hotel = hotel["Bar"]
            db_amenities_hotel["Bar"] = db_bar_hotel

            db_restaurant_hotel = hotel["Restaurant"]
            db_amenities_hotel["Restaurant"] = db_restaurant_hotel

            db_pets_hotel = hotel["Allow Pets"]
            db_amenities_hotel["Allow Pets"] = db_pets_hotel

            # Prints out each hotel's amenities.
            # print(db_amenities_hotel)

            # Create flags for every preference and search the db only for True flags.
            town_flag = False
            rating_flag = False
            wifi_flag = False
            ac_flag = False
            bar_flag = False
            restaurant_flag = False
            pets_flag = False
            price_flag = False

            # If the user didn't specify any preferences print all hotels.
            if self.__user_preferences["Town"] == 0 and self.__user_preferences["Star Rating"] == 0 and self.__user_preferences["Amenities"]["Wi-fi"] == 0 and self.__user_preferences["Amenities"]["Air Conditioner"] == 0 and self.__user_preferences["Amenities"]["Bar"] == 0 and self.__user_preferences["Amenities"]["Restaurant"] == 0 and self.__user_preferences["Amenities"]["Allow Pets"] == 0 and self.__user_preferences["Price"] == 0:
                print(hotel)

            # If there are any given preferences to search with them.
            else:

                # Search by town.
                if self.__user_preferences["Town"] == db_town_hotel:
                    town_flag = True
                    # print(hotel)

                elif self.__user_preferences["Town"] == 0:
                    pass

                # Search by star rating.
                if self.__user_preferences["Star Rating"] == db_stars_hotel:
                    rating_flag = True

                elif self.__user_preferences["Star Rating"] == 0:
                    pass

                # Search by amenities.
                if self.__user_preferences["Amenities"]["Wi-fi"] == 0:
                    pass

                elif self.__user_preferences["Amenities"]["Wi-fi"] == True:
                    pass

                if self.__user_preferences["Amenities"]["Air Conditioner"] == 0:
                    pass

                if self.__user_preferences["Amenities"]["Bar"] == 0:
                    pass

                if self.__user_preferences["Amenities"]["Restaurant"] == 0:
                    pass

                if self.__user_preferences["Amenities"]["Allow Pets"] == 0:
                    pass

                elif self.__user_preferences["Amenities"] == db_amenities_hotel:
                    pass

                # Search by price.
                if self.__user_preferences["Price"] == 0:
                    pass

                elif self.__user_preferences["Price"] == db_price_hotel:
                    pass

        # Iterate through all documents and print them.
        # for document in read_collection:
        #     print(document)

# End region.
