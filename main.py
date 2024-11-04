# https://developer.riotgames.com/docs/lol

import json

from modes.classic import CLASSIC
from modes.aram import ARAM
from modes.ultbook import ULTBOOK

PATCH = '14.21.1'
Classic = CLASSIC(PATCH)
Aram = ARAM(PATCH)
UltBook = ULTBOOK(PATCH)

mode_guide = {
    'classic': Classic,
    'aram': Aram,
    'ultbook': UltBook
}

# Image_URL = 'https://ddragon.leagueoflegends.com/cdn/{PATCH}/img/item/{ITEM_ID}.png'

class Main:
    def __init__(self):

        self.lanes = [
            'Top',
            'Jungle',
            'Mid',
            'ADC',
            'Support'
        ]

    def generateBuildFiles(self):
        for lane in self.lanes:
            build = Classic.CreateBuild(isSupport = lane == 'Support', isJungle = lane == 'Jungle')
            ult_build = UltBook.CreateBuild()

            with open(f'builds/classic_{lane}.json', 'w') as f:
                json.dump(build, f, indent=4)
            
            with open(f'builds/ultbook_{lane}.json', 'w') as f:
                json.dump(ult_build, f, indent=4)

        for i in range(3):
            with open(f'builds/aram_{i + 1}.json', 'w') as f:
                json.dump(Aram.CreateBuild(), f, indent=4)

    def CreateBuild(self, mode='', lane='mid'):
        build = mode_guide[mode].CreateBuild(isSupport=lane=='Support', isJungle=lane=='Jungle')
        build['lane'] = lane
        print(build)
        return build

if __name__ == '__main__':
    main = Main()
    main.generateBuildFiles()