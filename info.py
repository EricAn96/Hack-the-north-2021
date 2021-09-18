import requests
import json


# returns entire data from specific endpoint as python dictionary
def get_endpoint(param):
    API_ENDPOINT = f'https://disease.sh{param}'

    url_valid = True

    try:
        response = requests.get(API_ENDPOINT)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        url_valid = False
        print(err)

    response_dict = json.loads(response.text)

    return response_dict, url_valid


# returns country specific data as python dictionary
def covid_country(country):
    stats, url_valid = get_endpoint(f'/v3/covid-19/countries/{country}')

    keys = ['active', 'critical', 'deaths', 'recovered', 'tests', 'today', 'cases']
    data = {x:stats[x] for x in keys if x in stats}

    return data, url_valid
