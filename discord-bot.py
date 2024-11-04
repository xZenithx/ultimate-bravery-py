import discord
import os
from adjectives import get_random_adjective
from dotenv import load_dotenv
from discord.ext import commands
from main import Main

PATCH = '14.21.1'

load_dotenv()

bot = commands.Bot()
main = Main()

mode_options = [
    discord.OptionChoice(name="Classic", value="classic"),
    discord.OptionChoice(name="ARAM", value="aram"),
    discord.OptionChoice(name="Ultimate Spellbook", value="ultbook")
]
lane_options = [
    discord.OptionChoice(name="Top Lane", value="Top Lane"),
    discord.OptionChoice(name="Jungle", value="Jungle"),
    discord.OptionChoice(name="Mid Lane", value="Mid Lane"),
    discord.OptionChoice(name="ADC", value="ADC"),
    discord.OptionChoice(name="Support", value="Support"),
]

emoji_dict = {
    'zombieward': 1293165830300897280,
    'waterwalking': 1293165816933646337,
    'aftershock': 1293165809069199421,
    'unsealedspellbook': 1293165801125183539,
    'unflinching': 1293165792308891728,
    'ultimatehunter': 1293165781529526302,
    'triumph': 1293165768913190954,
    'treasurehunter': 1293165761451266068,
    'transcendence': 1293165752794353716,
    'timewarptonic': 1293165739548872775,
    'summonaery': 1293165727016161390,
    'suddenimpact': 1293165718598062120,
    'sorcery': 1293165712243953705,
    'secondwind': 1293165705503440989,
    'scorch': 1293165699170041957,
    'revitalize': 1293165692681715713,
    'resolve': 1293165686318698559,
    'relentlesshunter': 1293165680929013771,
    'presstheattack': 1293165675879075881,
    'presenceofmind': 1293165669394939904,
    'predator': 1293165662096851014,
    'precision': 1293165656514232461,
    'phaserush': 1293165649962602548,
    'overgrowth': 1293165642408529920,
    'nullifyingorb': 1293165636654071869,
    'nimbuscloak': 1293165630937239582,
    'shieldbash': 1293165558228979753,
    'manaflowband': 1293165478906171494,
    'magicalfootwear': 1293165471704678423,
    'lethaltempo': 1293165463035056149,
    'legendhaste': 1293165455263006813,
    'legendbloodline': 1293165446446710895,
    'legendalacrity': 1293165437873422386,
    'laststand': 1293165432332877824,
    'kleptomancy': 1293165424447590431,
    'jackofalltrades': 1293165418843734080,
    'inspiration': 1293165403643838504,
    'ingenioushunter': 1293165391966900268,
    'hextechflashtraption': 1293165384660287588,
    'hailofblades': 1293165376745635885,
    'guardian': 1293165368927457300,
    'tasteofblood': 1293165349767872552,
    'graspoftheundying': 1293165341211627663,
    'glacialaugment': 1293165333888237598,
    'ghostporo': 1293165326510325813,
    'gatheringstorm': 1293165318671171604,
    'fontoflife': 1293165309242376224,
    'fleetfootwork': 1293165297108385792,
    'firststrike': 1293165250681769994,
    'eyeballcollection': 1293165240246075393,
    'electrocute': 1293165225180139530,
    'domination': 1293165214551769150,
    'demolish': 1293165203227148318,
    'darkharvest': 1293165192657768488,
    'cutdown': 1293165182893293619,
    'coupdegrace': 1293165172575309845,
    'cosmicinsight': 1293165160646840413,
    'conqueror': 1293165149183803454,
    'conditioning': 1293165136449638503,
    'cheapshot': 1293165041964679198,
    'celerity': 1293165013694939136,
    'cashback': 1293165001900556299,
    'boneplating': 1293164988877242369,
    'biscuitdelivery': 1293164975409332305,
    'arcanecomet': 1293164937794818170,
    'approachvelocity': 1293164921055612991,
    'tripletonic': 1293164905175711824,
    'absorblife': 1293164890789253120,
    'absolutefocus': 1293164485066096690
}

def RuneEmojiString(rune: str):
    return rune.lower().replace(' ', '').replace(':', '')

def GetEmoji(emojistr: str):
    if not RuneEmojiString(emojistr) in emoji_dict:
        print('Unknown emoji: ' + RuneEmojiString(emojistr))
        return ''
    return '<:' + RuneEmojiString(emojistr) + ':' + str(emoji_dict[RuneEmojiString(emojistr)]) + '>'

@bot.slash_command(
  name="build",
)
async def build(
    ctx: discord.ApplicationContext,
    mode: discord.Option(str, 'Choose a mode', choices=mode_options), # type: ignore
    lane: discord.Option(str, 'Pick a lane', choices=lane_options, required=False) # type: ignore
):
    build = main.CreateBuild(mode=mode, lane=lane)
    embed = discord.Embed()
    embed.set_author(name=f'{build['mode']}')
    embed.set_footer(text="by Zenith")
    if 'champion' in build:
        embed.title = f'{get_random_adjective()} {build['champion']} | {build['lane']}'
        embed.set_thumbnail(url=f'https://ddragon.leagueoflegends.com/cdn/{PATCH}/img/champion/{build['champion'].replace('\'', '')}.png')
    
    
    embed.description = f'''
[**{build['summoner_1']}**, **{build['summoner_2']}**]

[{GetEmoji(build['rune_primary']['name'])}] **{build['rune_primary']['name']}**
> {GetEmoji(build['rune_primary']['1'])}**{build['rune_primary']['1']}**
> {GetEmoji(build['rune_primary']['2'])}{build['rune_primary']['2']}
> {GetEmoji(build['rune_primary']['3'])}{build['rune_primary']['3']}
> {GetEmoji(build['rune_primary']['4'])}{build['rune_primary']['4']}

[{GetEmoji(build['rune_secondary']['name'])}] **{build['rune_secondary']['name']}**
> {GetEmoji(build['rune_secondary']['1'])}{build['rune_secondary']['1']}
> {GetEmoji(build['rune_secondary']['2'])}{build['rune_secondary']['2']}

[**Extras**]
> {build['rune_extra']['1']}, {build['rune_extra']['2']}, {build['rune_extra']['3']}
'''
    if 'starter' in build:
        embed.description += f'''
[**Starter**]
> {build['starter']}
'''

    embed.description += f'''
[**Items**]
> {build['item_1']}
> {build['item_2']}
> {build['item_3']}
> {build['item_4']}
> {build['item_5']}
> {build['item_6']}
'''
    

    await ctx.respond(embed=embed)


bot.run(os.getenv('DISCORD_TOKEN'))

#     string = f'''
# [**{build['mode']}**]
# [**{build['lane']}**]
# '''

#     letters = ["Q", "W", "E"]
#     random_letters = random.sample(letters, 3)
#     result = " > ".join(random_letters)

#     if 'champion' in build:
#         string += f'''
# [**{build['champion']}**]
# '''
#     string += f'''
# [**{build['summoner_1']}**, **{build['summoner_2']}**]
# [**{result}**]

# [**{build['rune_primary']['name']}**]
# > **{build['rune_primary']['1']}**
# > {build['rune_primary']['2']}
# > {build['rune_primary']['3']}
# > {build['rune_primary']['4']}

# [**{build['rune_secondary']['name']}**]
# > {build['rune_secondary']['1']}
# > {build['rune_secondary']['2']}

# [**Extras**]
# > {build['rune_extra']['1']}, {build['rune_extra']['2']}, {build['rune_extra']['3']}
# '''
#     if 'starter' in build:
#         string += f'''
# [**Starter**]
# > {build['starter']}
# '''

#     string += f'''
# [**Items**]
# > {build['item_1']}
# > {build['item_2']}
# > {build['item_3']}
# > {build['item_4']}
# > {build['item_5']}
# > {build['item_6']}
# '''