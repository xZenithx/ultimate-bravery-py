# https://developer.riotgames.com/docs/lol

import json

from modes.classic import CLASSIC
from modes.aram import ARAM
from modes.ultbook import ULTBOOK

PATCH = '14.19.1'

# Image_URL = 'https://ddragon.leagueoflegends.com/cdn/{PATCH}/img/item/{ITEM_ID}.png'



Classic = CLASSIC(PATCH)
Aram = ARAM(PATCH)
UltBook = ULTBOOK(PATCH)

lanes = [
    'Top',
    'Jungle',
    'Mid',
    'ADC',
    'Support'
]

for lane in lanes:
    build = Classic.CreateBuild(isSupport = lane == 'Support', isJungle = lane == 'Jungle')
    ult_build = UltBook.CreateBuild()

    with open(f'builds/classic_{lane}.json', 'w') as f:
        json.dump(build, f, indent=4)
    
    with open(f'builds/ultbook_{lane}.json', 'w') as f:
        json.dump(ult_build, f, indent=4)