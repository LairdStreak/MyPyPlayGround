from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.common.utility import util
from pyblizzard.pyblizzard import PyBlizzard
from pyblizzard.wow.enum.characterprofilefield import CharacterProfileField
from pyblizzard.wow.enum.pvpbracket import PvpBracket
import pandas as pd
import xlsxwriter
import matplotlib.pyplot as plt

def main():
    pybz = PyBlizzard("gfyjawteeb4wbzke674wbwzyjbpcahjv", Region.US, Locale.US)
    
     # GUILD PROFILE
    print('Getting guild profile...')
    guild_profile = pybz.wow.get_guild_profile("dathremar", "WhiteHand")
    data = pd.DataFrame(guild_profile['members'])
    list = []
    for index, row in data.iterrows():
        list.append({'Name' : row['character']['name'], 'Level' : row['character']['level']})

    df = pd.DataFrame.from_records(list)   
    df = df[df['Level'] > 115]
    #df.set_index('Name')
    #df.plot.bar()

    #plt.show()
    #print("done")
    writer = pd.ExcelWriter('simple-report.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()
        
    #for item in list:
    #    print(f"{item['Name']} - {item['Level']}")


    #for char in guild_profile['members']:
    #    print(f"{char['character']['name']} - {char['character']['level']}")
        # print(char['character']['level'])
    #util.print_response_object(guild_profile)



if __name__ == '__main__':
    main()