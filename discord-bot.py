import discord
import os
import random
from adjectives import get_random_adjective
from dotenv import load_dotenv
from discord.ext import commands
from main import Main

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
        embed.title = f'{get_random_adjective().capitalize()} {build['champion']} | {build['lane']}'
        embed.set_thumbnail(url=f'https://ddragon.leagueoflegends.com/cdn/14.19.1/img/champion/{build['champion'].replace('\'', '')}.png')
    
    
    embed.description = f'''
[**{build['summoner_1']}**, **{build['summoner_2']}**]

[**{build['rune_primary']['name']}**]
> **{build['rune_primary']['1']}**
> {build['rune_primary']['2']}
> {build['rune_primary']['3']}
> {build['rune_primary']['4']}

[**{build['rune_secondary']['name']}**]
> {build['rune_secondary']['1']}
> {build['rune_secondary']['2']}

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