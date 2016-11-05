from censusgeocode import *
import numpy as np

import yelp_fetcher
import predict

current_latitude = None
current_longitude = None

current_categories = None

current_businesses = None
current_regression = None

def set_address(address, categories):
    global current_latitude, current_longitude, current_categories, current_businesses, current_regression
    cg = CensusGeocode()
    res = cg.onelineaddress(address)
    current_latitude = res[0]['coordinates']['y']
    current_longitude = res[0]['coordinates']['x']

    current_categories = categories
    
    current_businesses = yelp_fetcher.get_businesses(current_latitude, current_longitude, categories)
    print current_businesses

    current_regression = predict.get_regression(current_businesses)

def get_current_businesses():
    global current_businesses
    return current_businesses

def get_scores(demographics):
    return []

if __name__ == '__main__':
    set_address('410 Memorial Drive, Cambridge, MA 02139', ['sushi'])
    print get_current_businesses()
    print current_regression.coef_
