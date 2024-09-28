from items import Items as items
from runes import Runes as runes
from champions import Champions as champions
from summoners import Summoners as summoners

class ULTBOOK:
    def __init__(self, patch):
        self.name = 'ULTBOOK'
        self.map = '11'
        self.patch = patch
        self.Champions = champions(self.patch)
        self.Items = items(self.patch, map=self.map)
        self.Runes = runes(self.patch)
        self.Summoners = summoners(self.patch, mode=self.name)
    
    def CreateBuild(self):
        build = {}
        build['champion'] = self.Champions.RandomChamp()['name']
        build = build | self.Summoners.RandomSummoner(amount=2)
        build = build | self.Runes.RandomRunes()
        build = build | self.Items.RandomBuild()

        return build
