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
        for slot in primary_tree['slots']:
            random_rune = random.choice(slot['runes'])
            runes.append(random_rune)

        random_slots = random.sample(secondary_tree['slots'][1:], 2)

        for slot in random_slots:
            random_rune = random.choice(slot['runes'])
            runes.append(random_rune)
        
        return {
            'rune_primary_1': runes[0]['name'],
            'rune_primary_2': runes[1]['name'],
            'rune_primary_3': runes[2]['name'],
            'rune_primary_4': runes[3]['name'],
            'rune_secondary_1': runes[4]['name'],
            'rune_secondary_2': runes[5]['name'],
            'rune_extra_1': random.randrange(1, 4),
            'rune_extra_2': random.randrange(1, 4),
            'rune_extra_3': random.randrange(1, 4)
        }
