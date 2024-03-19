import json, urllib.parse, urllib.request, urllib.error

def get_tarot_definition(input):
    base_url = "https://tarotapi.dev/api/v1/cards/search"
    query = { 'q': input }
    encoded_query = urllib.parse.urlencode(query, quote_via=urllib.parse.quote)
    full_url = base_url + '?' + encoded_query
    print(full_url)
    try:
        with urllib.request.urlopen(full_url) as response:
            card_json = json.loads(response.read().decode('utf-8'))

            return card_json
    except urllib.error.URLError:
        print('Please check your spelling')

get_tarot_definition('the fool')