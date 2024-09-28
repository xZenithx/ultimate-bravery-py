import requests
import json
import random

class Champions:
    def __init__(self, patch):
        self.patch = patch
        self.champions_uri = f'https://ddragon.leagueoflegends.com/cdn/{self.patch}/data/en_US/champion.json'
        self.champions_data = []
        self.champions = {}
        self.support_champions = []
        self.non_support_champions = []

        # Make a GET request to the URL
        response = requests.get(self.champions_uri)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON data
            data = json.loads(response.text)
            self.champions_data = data
        else:
            print('Failed to retrieve data')

        for champion in self.champions_data['data'].values():
            if not champion['id'] in self.champions:
                self.champions[champion['id']] = champion

        for champion in self.champions:
            if 'tags' in champion and 'Support' in champion['tags']:
                self.support_champions.append(champion)
            else:
                self.non_support_champions.append(champion)

    def RandomChamp(self, supportOnly = False, nonSupportOnly = False):
        if supportOnly == True:
            if self.support_champions:
                return random.choice(self.support_champions)
            else:
                return None
        elif nonSupportOnly == True:
            if self.non_support_champions:
                return random.choice(self.non_support_champions)
            else:
                return None
        elif self.champions:
            return random.choice(list(self.champions.values()))
        else:
            return None