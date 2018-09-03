from pyblizzard.common.enum.locale import Locale
from pyblizzard.common.enum.region import Region
from pyblizzard.common.utility import util
from pyblizzard.pyblizzard import PyBlizzard
from pyblizzard.wow.enum.characterprofilefield import CharacterProfileField
from pyblizzard.wow.enum.pvpbracket import PvpBracket

def main():
    pybz = PyBlizzard("gfyjawteeb4wbzke674wbwzyjbpcahjv", Region.US, Locale.US)
    # CHARACTER PROFILE
    # print('Getting character profile...')
    # character_profile = pybz.wow.get_character_profile("khazgoroth", "Gnomeifix", CharacterProfileField.TALENTS, CharacterProfileField.ITEMS)
    # util.print_response_object(character_profile)


     # GUILD PROFILE
    print('Getting guild profile...')
    guild_profile = pybz.wow.get_guild_profile("dathremar", "WhiteHand")
    for char in guild_profile['members']:
        print(f"{char['character']['name']} - {char['character']['level']}")
        # print(char['character']['level'])
    #util.print_response_object(guild_profile)



if __name__ == '__main__':
    main()