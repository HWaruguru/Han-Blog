import requests
def get_quote():
    '''
    Function that gets the json response to our url request
    '''
    url = "http://quotes.stormconsultancy.co.uk/random.json"
    response = requests.get(url)
    quote = response.json()
    return quote
