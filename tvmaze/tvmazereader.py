import requests
import json
from pprint import pprint

seriesidlist = ['21845','5495']

def main():
    for identity in seriesidlist:
        infoUri = 'http://api.tvmaze.com/shows/{value}'.format(value=identity)
        urlPath = 'http://api.tvmaze.com/shows/{value}/episodes'.format(value=identity)
        read_seriesInfo(infoUri)
        read_seriesEpisodes(urlPath)
        #print(urlPath)
    #//print("here")

def read_seriesInfo(uri):
    response = requests.get(uri)
    data = json.loads(response.content)
    print(data['name'])
    print('\n')

def read_seriesEpisodes(uri):
    response = requests.get(uri)
    data = json.loads(response.content)
    for record in data:
        name = record['name']
        releasedate = record['airdate']
        summary = record['summary']
        print("{} {} {}".format(name, releasedate, summary))


if __name__ == '__main__':
    main()