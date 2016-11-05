import numpy as np
from sklearn.linear_model import LinearRegression

import yelp_fetcher
import census_data

LOCATION = (39.7390720,-75.5397880)

def get_features(x, y):
    demographics = census_data.getTractDemographics(x, y)
    return np.array([ v for k, v in sorted(demographics.items()) ])

def predict(latitude, longitude, categories):
    businesses = yelp_fetcher.get_businesses(latitude, longitude, categories)
    print businesses

    features = []
    target = []
    for b in businesses:
        y, x = b['latitude'], b['longitude']
        features.append(get_features(x, y))
        target.append(b['review_count'])
    features = np.vstack(features)
    target = np.array(target)
    print features, target

    reg = LinearRegression()
    reg.fit(features, target)
    print reg.coef_
    return reg

if __name__ == '__main__':
    predict(LOCATION[0], LOCATION[1], ['sushi'])
