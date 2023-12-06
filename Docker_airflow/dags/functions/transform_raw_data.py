"""
The transform_data function is defined in this module. 
The function is very specific for the transformations that are required for the current occasion and is not characterized by high level of abstraction.
This function loads the data from a json and transforms them in a file with a newline delimited json format.
The output newline delimited json as a file, is required from bigquery in order to load the data in a table.
The file containing the data is loaded from a url that is passed as input argument.
The file should contain a single quote json.
The flatten function is also used for the transformations.
"""
import requests
import json
import ast
import pandas as pd
import os
import io
from functions.flatten_json import flatten


def transform_data(url):
    """
    This function takes a url that corresponds to a file and transforms the data in the desired format.
    Args:
        url: url for the respective file to be loaded. Should be a string.
    Returns:
        A file with a newlined delimited json that can be loaded in a bigquery table
    """

    # load the data from the url provided
    resp = requests.get(url)

    # use the ast library to handle the single quote json
    # payload is in the "list" key of the json dictionary provided
    raw_data = ast.literal_eval(resp.text)['list']

    # initialize empty payload
    payload = []

    for subscription in raw_data:
        flattened_data = flatten(subscription) # use flatten function that we have defined in order to flatten the dictionary
        for key, value in flattened_data.items(): # here we want to convert values into strings. This is needed for booleans.
            if type(value) != list: # there are values that are arrays, we do not want to convert to string as they might be easier to parse with their current format in sql later.
                flattened_data[key] = str(value)
        flattened_data_json = json.dumps(flattened_data)
        payload.append(flattened_data_json)

    payload_json_str = '\n'.join(payload) #convert the json into a newline delimtied json

    payload_as_file = io.StringIO(payload_json_str) # wrap the json as a file 

    return payload_as_file