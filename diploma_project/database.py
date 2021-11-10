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
            db_town_hotel = hotel["Town"]

            if self.__user_preferences["Town"] == db_town_hotel:
                print(hotel)

        # Iterate through all documents and print them.
        # for document in read_collection:
        #     print(document)

# End region.
