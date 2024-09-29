
from items import Items as items
from runes import Runes as runes
from champions import Champions as champions
from summoners import Summoners as summoners

class CLASSIC:
    def __init__(self, patch):
        self.display = 'Classic'
        self.patch = patch
        self.Items = items(self.patch)
        self.Runes = runes(self.patch)
        self.Champions = champions(self.patch)
        self.Summoners = summoners(self.patch)
    
    def CreateBuild(self, isJungle=False, isSupport=False):
        build = {}
        build['mode'] = self.display
        build['champion'] = self.Champions.RandomChamp()['name']
        build = build | self.Summoners.RandomSummoner(amount=2, isJungle=isJungle)
        build = build | self.Runes.RandomRunes()
        build = build | self.Items.RandomBuild(isSupport=isSupport, isJungle=isJungle)

        return build
