import pandas as pd
from collections import OrderedDict, defaultdict
import requests

#World Bank indicators of interest for pulling
indicators_default = ['NY.GDP.MKTP.KD.ZG', 'NV.IND.TOTL.KD.ZG', 'FP.CPI.TOTL.ZG', 'PX.REX.REER', 'NE.IMP.GNFS.KD.ZG']

#list of countries of interest
country_default = OrderedDict([('Ukraine', 'UA'), ('Poland', 'PL'), ('Russia', 'RU'), ('Germany', 'DE'), ('United States', 'US')])
payload = {'format': 'json', 'per_page': 500, 'date': '2010:2019'}


def pull_data(countries=country_default, indicators=indicators_default):
    ''' Pulls data from the World Bank API
    Input:
        country_default (dict): list of countries for viz
        indicators (list): list of indicators for viz
    Output:
        list (dict): list containing the pulled data
    '''
    #prepare country data for World Bank API
    #the API uses ISO-2 country codes separated by ;
    country_filter = list(countries.values())
    country_filter = [x.lower() for x in country_filter]
    country_filter = ';'.join(country_filter)

    data_frames = [] #stores the data frames with the indicator data of interest

    #pull data from World Bank API
    # store results in data_frames
    for indicator in indicators:
        url = 'http://api.worldbank.org/v2/countries/' + country_filter +\
            '/indicators/' + indicator
    
        try:
            r = requests.get(url, params=payload)
        except:
            print('could not load data', indicator)

        data = defaultdict(list)

        for entry in r.json()[1]:
        #check if country is already in dictionary
        # if so, append the new x and y values to the lists 
            if data[entry['country']['value']]:
                data[entry['country']['value']][0].append(int(entry['date']))
                data[entry['country']['value']][1].append(float(entry['value']))
            else:
                data[entry['country']['value']] = [[],[]]
        
        data_frames.append(data)
        return data_frames

df = pull_data()
print(df)

     
