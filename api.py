from censusgeocoder import *
import numpy as np

import yelp_fetcher
import predict

current_latitude = None
current_longitude = None

current_categories = None

current_businesses = None
current_regresssion = None

def set_address(address, categories):
    cg = CensusGeocode()
    res = cg.onelineaddress(address)
    current_latitude = res[0]['2010 Census Blocks'][0]['CENTLAT']
    current_longitude = res[0]['2010 Census Blocks'][0]['CENTLAT']

    current_categories = categories
    
    current_businesses = yelp_fetcher.get_businesses(current_latitude, current_longitude], categories)

    current_regression = predict.get_regression(current_businesses, current_categories)

def get_current_businesses():
    return current_businesses

def get_scores(demographics):
    return []
