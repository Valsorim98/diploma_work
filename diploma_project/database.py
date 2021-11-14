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
        """Method to get the existing documents in the collection.
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

            if self.__user_preferences["Town"] == db_town_hotel and self.__user_preferences["Star Rating"] == db_stars_hotel:
                print(hotel)

        # Iterate through all documents and print them.
        # for document in read_collection:
        #     print(document)

# End region.
