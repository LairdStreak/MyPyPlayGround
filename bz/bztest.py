from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.common.utility import util
from pyblizzard.pyblizzard import PyBlizzard
from pyblizzard.wow.enum.characterprofilefield import CharacterProfileField
from pyblizzard.wow.enum.pvpbracket import PvpBracket
import pandas as pd
import xlsxwriter
import matplotlib.pyplot as plt
import time



def GetWoWRaces(pybz):
    print('Getting character races...')
    pyb_races = pybz.wow.get_data_character_races()
    return pyb_races

def GetWoWClasses(pybz):
    print('Getting character classes...')
    pyb_classes = pybz.wow.get_data_character_classes()
    return pyb_classes    

def main():
    pybz = PyBlizzard("", Region.US, Locale.US)
    toon_races = pd.DataFrame(GetWoWRaces(pybz))
    toon_classes = pd.DataFrame(GetWoWClasses(pybz))
     # GUILD PROFILE
    print('Getting guild profile...')
    guild_profile = pybz.wow.get_guild_profile("dathremar", "WhiteHand")
    data = pd.DataFrame(guild_profile['members'])
    list = []
    for index, row in data.iterrows():
        raceint = row['character']['race']
        classint = row['character']['class']
        race = [i for i in toon_races.races if i['id'] == raceint][0]['name']
        toonclass = [i for i in toon_classes.classes if i['id'] == classint][0]['name']
        list.append({'Name' : row['character']['name'], 'Level' : row['character']['level'], 'Race' : race, 'Class' : toonclass, 'achievementPoints' : row['character']['achievementPoints']})

    df = pd.DataFrame.from_records(list)  
    writer = pd.ExcelWriter('simple-report.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()
    output = df.to_html()
    print(output)
    print("Done")

if __name__ == '__main__':
    main()