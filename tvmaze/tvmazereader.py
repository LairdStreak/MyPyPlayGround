import requests
import json
from pprint import pprint



def main():
    seriesidlist = ['21845','5495']
    episodes = []
    for identity in seriesidlist:
        urlPath = 'http://api.tvmaze.com/shows/{value}/episodes'.format(value=identity)
        response = read_seriesEpisodes(urlPath)
        episodes.append(response)
    
    #pprint(episodes)
    return episodes


    # infoUri = 'http://api.tvmaze.com/shows/{value}'.format(value=identity)
    #    urlPath = 'http://api.tvmaze.com/shows/{value}/episodes'.format(value=identity)
    #    response = read_seriesEpisodes(urlPath)
    #    return response
        #pprint(response)
        #read_seriesInfo(infoUri)
        #read_seriesEpisodes(urlPath)
    

def read_seriesInfo(uri):
    response = requests.get(uri)
    data = json.loads(response.content)
    print(data['name'])
    print('\n')

def read_seriesEpisodes(uri):
    response = requests.get(uri)
    data = json.loads(response.content)
    content = []
    for record in data:
        name = record['name']
        releasedate = record['airdate']
        summary = record['summary']
        info = {
        "name":  name,
        "releasedate": releasedate,
        "summary":  summary,
        }
        content.append(info)
    return content

if __name__ == '__main__':
    main()