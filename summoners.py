import requests
import json
import random

class Summoners:
    def __init__(self, patch, mode = 'CLASSIC'):
        self.patch = patch
        self.mode = mode
        self.summoners_uri = f'https://ddragon.leagueoflegends.com/cdn/{self.patch}/data/en_US/summoner.json'
        self.summoners_data = []
        self.summoners = {}

        # Make a GET request to the URL
        response = requests.get(self.summoners_uri)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON data
            data = json.loads(response.text)
            self.summoners_data = data
        else:
            print('Failed to retrieve data')

        for summoner in self.summoners_data['data'].values():
            if summoner['id'] in self.summoners:
                continue
            if not 'modes' in summoner:
                continue
            if not mode in summoner['modes']:
                continue
            if summoner['id'] == 'SummonerSmite':
                continue
            
            self.summoners[summoner['id']] = summoner
    
    def RandomSummoner(self, amount=1, isJungle=False):
        value = {}

        if isJungle:
            value[f'summoner_1'] = 'Smite'

        summoners = random.sample(list(self.summoners.values()), isJungle == True and 1 or amount)

        for summoner in summoners:
            value[f'summoner_{len(value) + 1}'] = summoner['name']
            
        return value