import requests
import json
import random

class Runes:
    def __init__(self, patch):
        self.patch = patch
        self.runes_uri = f'https://ddragon.leagueoflegends.com/cdn/{self.patch}/data/en_US/runesReforged.json'
        self.runes_data = []
        self.runes = {}

        # Make a GET request to the URL
        response = requests.get(self.runes_uri)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON data
            data = json.loads(response.text)
            self.runes_data = data
        else:
            print('Failed to retrieve data')
        
        for rune in self.runes_data:
            if not rune['key'] in self.runes:
                self.runes[rune['key']] = rune
        
        # self.RandomRunes()

    def RandomRunes(self):
        rune_page = {}

        primary_tree = []
        secondary_tree = []
        # Choose two random trees
        random_trees = random.sample(list(self.runes.values()), 2)
        for random_tree in random_trees:
            if not primary_tree:
                primary_tree = random_tree
            else:
                secondary_tree = random_tree

        runes = []

        runes.append(primary_tree['name'])
        runes.append(secondary_tree['name'])

        for slot in primary_tree['slots']:
            random_rune = random.choice(slot['runes'])
            runes.append(random_rune)

        random_slots = random.sample(secondary_tree['slots'][1:], 2)

        for slot in random_slots:
            random_rune = random.choice(slot['runes'])
            runes.append(random_rune)
        
        return {
            'rune_primary': {
                'name': runes[0],
                '1': runes[2]['name'],
                '2': runes[3]['name'],
                '3': runes[4]['name'],
                '4': runes[5]['name']
            },
            'rune_secondary': {
                'name': runes[1],
                '1': runes[6]['name'],
                '2': runes[7]['name']
            },
            'rune_extra': {
                '1': random.randrange(1, 4),
                '2': random.randrange(1, 4),
                '3': random.randrange(1, 4)
            }
        }
