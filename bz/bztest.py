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

    df.set_index('Name')
    
    labels = df.index.values
    values = df['Level']
    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels = labels)
    ax1.axis('equal')
    plt.show()


    writer = pd.ExcelWriter('simple-report.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()
    print("Done")

if __name__ == '__main__':
    main()