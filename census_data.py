from census import Census
from us import states
from censusgeocode import CensusGeocode
import numpy as np

census = Census("0893c0cbfcde7f65746eed7d176f18a27c862bbe", year=2014)
cg = CensusGeocode()

demo_ranges = {
    'male0-14': (3,6),
    'male15-34': (6,13),
    'male35-59': (13,18),
    'male60+': (18,26),
    'female0-14': (27,30),
    'female15-34': (30,37),
    'female35-59': (37,42),
    'female60+': (42,50)
    }
demo_vars = {}

for key in demo_ranges:
    demo_vars[key] = []
    first, last = demo_ranges[key]
    for i in range(first,last):
        demo_vars[key].append('B01001_'+str(i).zfill(3)+'E')

fields = np.hstack(demo_vars.values()).tolist()

def getTractDemographics(x, y):
    result = cg.coordinates(x=x, y=y)[0]['Census Tracts'][0]

    state_fips = int(result['STATE'])
    county_fips = int(result['COUNTY'])
    tract = int(result['TRACT'])

    data = census.acs5.state_county_tract(fields, state_fips, county_fips, tract)[0]
    res = {}

    for key in demo_vars:
        res[key] = 0
        for var in demo_vars[key]:
            res[key] += int(data[var])

    return res

print getTractDemographics(-76,41)

