from __future__ import print_function
import requests as req

def main():
    #http://api.tradeskillmaster.com/v1/item/US/khazgoroth?format=json&apiKey=odfIR8Qtfy1q7R2Ee27a9rNO_WN_M97w * 25
    #http://api.tradeskillmaster.com/v1/item/US/khazgoroth/137274?format=json&apiKey=odfIR8Qtfy1q7R2Ee27a9rNO_WN_M97w
    getalluri = "http://api.tradeskillmaster.com/v1/item/US/khazgoroth/" + str(137274)
    payload = {'format': 'json', 'apiKey': 'odfIR8Qtfy1q7R2Ee27a9rNO_WN_M97w'}
    r = req.get(getalluri, params=payload)
    response = r.json()
    print(r.url)
    print(response)
    print(response["SubClass"])
    print("pass")

if __name__ == "__main__":
    main()