import requests
import json


# returns entire data from specific endpoint as python dictionary
def get_endpoint(param):
    API_ENDPOINT = f'https://disease.sh{param}'

    try:
        response = requests.get(API_ENDPOINT)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)

    response_dict = json.loads(response.text)

    return response_dict


# returns country specific data as python dictionary
def covid_country(country):
    stats = get_endpoint(f'/v3/covid-19/countries/{country}')

    keys = ['country', 'active', 'critical', 'deaths', 'recovered', 'tests', 'today', 'cases']
    data = {x:stats[x] for x in keys if x in stats}

    return(data)

