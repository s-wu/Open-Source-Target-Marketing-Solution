import numpy as np
from sklearn.linear_model import LinearRegression

import yelp_fetcher
import census_data

def get_features(latitude, longitude):
    demographics = census_data.getTractDemographics(x=longitude, y=latitude)
    return np.array([ v for k, v in sorted(demographics.items()) ])

def get_regression(businesses):

    features = []
    target = []
    for b in businesses:
        latitude, longitude = b['latitude'], b['longitude']
        try:
            features.append(get_features(latitude, longitude))
            target.append(b['review_count'])
        except Exception:
            pass
    features = np.vstack(features)
    target = np.array(target)

    reg = LinearRegression()
    reg.fit(features, target)
    return reg

if __name__ == '__main__':
    WIL = (39.7390720,-75.5397880)
    categories = ['sushi']
    businesses = yelp_fetcher.get_businesses(WIL[0], WIL[1], categories)
    print businesses

    print get_regression(businesses)
