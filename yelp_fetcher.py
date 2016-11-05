import io, json
import math
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

''' Returns Yelp rating of area

Aggregates review counts for top 20 businesses in the region

Params:
    categories - list of Yelp's: https://www.yelp.com/developers/documentation/v2/all_category_list
    radius  - in meters
'''
def get_businesses(latitude, longitude, categories, radius=5000, mesh_size=1):
    # read API keys
    with io.open('secrets/yelp_secret.json') as cred:
        creds = json.load(cred)
        auth = Oauth1Authenticator(**creds)
        client = Client(auth)

    client = Client(auth)

    businesses = {}

    mesh_dist = float(radius) / mesh_size

    params = {
            'limit': 5,
            'offset': 0,
            'sort': 0,
            'category_filter': ','.join(categories),
            'radius_filter': mesh_dist,
            }

    meters_to_latitude = 1. / (111000)
    meters_to_longitude = 1. / (111321 * math.cos(math.radians(latitude)))
    for i in range(-mesh_size / 2, mesh_size / 2 + 1):
        for j in range(-mesh_size / 2, mesh_size / 2 + 1):
            try:
                response = client.search_by_coordinates(
                        latitude + i * mesh_dist * meters_to_latitude,
                        longitude + j * mesh_dist * meters_to_longitude,
                        **params)
                for business in response.businesses:
                    businesses[business.id] = business
            except Exception as e:
                pass
                #print e.message
    return [
            {
                'name': b.name,
                'review_count': b.review_count,
                'rating': b.rating,
                'latitude': b.location.coordinate.latitude,
                'longitude': b.location.coordinate.longitude,
                'score': b.review_count,
            }
            for b in businesses.values()
            ]

if __name__ == '__main__':
    print get_businesses(39.7467431,-75.5448359,['sushi'])
