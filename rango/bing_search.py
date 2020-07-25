import requests
from .. import keys

URL = 'https://api.cognitive.microsoft.com/bing/v7.0/search'


def run_query(search_terms):
    L = []
    try:
        x = requests.get(URL, headers={'Ocp-Apim-Subscription-Key': BING_API_KEY}, params={"q": search_terms, 'count': 10})
        for i in x.json()["webPages"]['value']:
            L.append(i["url"])
    # Catch a URLError exception - something went wrong when connecting!
    except Exception as e:
        print("Error when querying the Bing API: ", e)

    # Return the list of results to the calling function.
    return L