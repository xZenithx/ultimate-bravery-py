import requests
import json
import random

class Items:
    def __init__(self, patch, map = '11'):
        self.patch = patch
        self.map = map
        self.items_uri = f'https://ddragon.leagueoflegends.com/cdn/{self.patch}/data/en_US/item.json'
        self.items_data = []
        self.items = []
        self.items_legendary = []
        self.items_boots = []
        self.items_starters = []
        self.items_jungle = []
        self.items_support = []

        # Make a GET request to the URL
        response = requests.get(self.items_uri)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON data
            data = json.loads(response.text)
            self.items_data = data['data']
        else:
            print('Failed to retrieve data')
        
        # Add items to list
        for item in self.items_data:
            if self.isItemValid(item):
                self.items.append(item)

        for item in self.items:
            if self.isItemLegendary(item):
                self.items_legendary.append(item)
            if self.isItemBoots(item):
                self.items_boots.append(item)
            if self.isItemStarter(item):
                self.items_starters.append(item)
            if self.isItemJungle(item):
                self.items_jungle.append(item)
            if self.isItemSupport(item):
                self.items_support.append(item)

    def isItemValid(self, item):
        item_data = self.items_data[item]
        if not 'maps' in item_data:
            return False
        if not self.map in item_data['maps']:
            return False
        if item_data['maps'][self.map] == False:
            return False
        if 'inStore' in item_data and item_data['inStore'] == False:
            return False

        return True

    def isItemLegendary(self, item):
        item_data = self.items_data[item]

        if not 'depth' in item_data:
            return False
        if item_data['depth'] != 3:
            return False

        return True

    def isItemBoots(self, item):
        item_data = self.items_data[item]
        if not 'tags' in item_data:
            return False
        if not 'Boots' in item_data['tags']:
            return False
        if item == '1001':
            return False

        return True

    def isItemStarter(self, item):
        item_data = self.items_data[item]

        if self.map != '12':
            # Cull
            if item == '1083':
                return True
            # Dark Seal
            if item == '1082':
                return True

        if not 'tags' in item_data:
            return False
        if not 'Lane' in item_data['tags']:
            return False
        if 'Consumable' in item_data['tags']:
            return False
        if not 'plaintext' in item_data:
            return False
        if not 'starting' in item_data['plaintext']:
            return False

        return True

    def isItemJungle(self, item):
        item_data = self.items_data[item]
        if not 'tags' in item_data:
            return False
        if not 'Jungle' in item_data['tags']:
            return False
        # nexus blitz
        if item_data['maps']['21'] == True:
            return False

        return True
    
    def isItemSupport(self, item):
        item_data = self.items_data[item]

        if not 'from' in item_data:
            return False
        if not '3867' in item_data['from']:
            return False

        return True

    def RandomLegendary(self):
        return self.items_data[random.choice(self.items_legendary)]

    def RandomJungle(self):
        return self.items_data[random.choice(self.items_jungle)]

    def RandomStarter(self):
        return self.items_data[random.choice(self.items_starters)]

    def RandomSupport(self):
        return self.items_data[random.choice(self.items_support)]

    def RandomBoots(self):
        return self.items_data[random.choice(self.items_boots)]


    def RandomBuild(self, isSupport = False, isJungle = False):
        starter = ""

        build = []

        if isJungle:
            starter = self.RandomJungle()['name']
        elif isSupport:
            starter = self.items_data['3865']['name']
            build.append(self.RandomSupport()['name'])
        else:
            starter = self.RandomStarter()['name']

        build.append(self.RandomBoots()['name'])

        while len(build) <= 5:
            random_item = self.RandomLegendary()['name']
            if not random_item in build:
                build.append(random_item)
        
        return {
            'starter': starter,
            'item_1': build[0],
            'item_2': build[1],
            'item_3': build[2],
            'item_4': build[3],
            'item_5': build[4],
            'item_6': build[5]
        }