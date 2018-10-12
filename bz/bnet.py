import requests
import requests.auth
from datetime import datetime, timezone


def get_access_token():
    
    TOKEN_URL = "https://us.battle.net/oauth/token"
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "client_credentials"}
    response = requests.post(TOKEN_URL,
                             auth=client_auth,
                             data=post_data)
    token_json = response.json()
    return token_json["access_token"]

def get_guildnews(token):
    head = {'Authorization': 'Bearer {}'.format(token)}
    guild_uri = "https://us.api.blizzard.com/wow/guild/dathremar/WhiteHand?fields=news"
    # https://us.api.blizzard.com/wow/guild/realm-blah/guild-blah/?fields=news
    response = requests.get(guild_uri,headers=head)
    guild_data = response.json()
    print(guild_data)

def get_token_price(token):
    head = {'Authorization': 'Bearer {}'.format(token)}
    tokenuri = 'https://us.api.blizzard.com/data/wow/token/?namespace=dynamic-us'
    response = requests.get(tokenuri,headers=head)
    tokenData = response.json()
    ts = int(tokenData["last_updated_timestamp"]) / 1000
    dt = datetime.fromtimestamp(ts, timezone.utc)
    goldPrice = int(tokenData["price"]) / 10000
    print("Token Gold Price {0} on Date {1}".format(goldPrice, dt))

def main():
    token = get_access_token()
    get_guildnews(token)
    # get_token_price(token)
    # print(get_access_token())

if __name__ == '__main__':
    main()