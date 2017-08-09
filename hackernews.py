"""
DOCSTRING
"""
import requests
import simplejson as json

def main():
    """doc string"""
    page = requests.get("https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty")
    jsonData = page.content
    print(page.status_code)
    jsonObject = json.loads(jsonData)

    # print the keys and values
    for key in jsonObject:
        #print("The key is ({}))".format(key))
        url = "https://hacker-news.firebaseio.com/v0/item/{}.json".format(key)
        recordDatapage = requests.get(url)
        recordData = recordDatapage.content
        jsonRecord = json.loads(recordData)
        print(jsonRecord["title"])

if __name__ == '__main__':
    main()