import requests
import json

CLIENT_ACCESS_TOKEN="161afc65624d4d36b85798b9928ad9ea"
FACEBOOK_GRAPH_URL="https://graph.facebook.com/v2.8/"
FACEBOOK_ACCESS_TOKEN="EAAFt7gldi4wBAKV9MgATGUdzV518oH9KeFLt7vJI7SaQ9xKIS2vMVO4yaZBkjs5WP0JnFg2SpHheo8KMdt7cLKZAw4UrgewkTiN4UZBpM3T5RYl0ZByMZC1j3PUbmuuwiRndXSVAMxIYD7Uv6igfnLrVCvcOQZCon1GrQY7Wg20wZDZD"


def match_found(me, other):
    ''' match_found notifies through facebook messaging user 'me' that they can share a route with user 'other'
    me.keys() == ['id']
    other.keys() == ['id', 'source', 'destination', 'datetime']
    '''
    r = requests.get(FACEBOOK_GRAPH_URL + other['id'] +"?fields=first_name,last_name&access_token=" + FACEBOOK_ACCESS_TOKEN)
    if r.status_code != 200:
        return -1
    p = requests.get(FACEBOOK_GRAPH_URL + other['id'] +"?fields=profile_pic&access_token=" + FACEBOOK_ACCESS_TOKEN)
    if p.status_code != 200:
        print("image not found")

    namefile = r.json()
    data = {
    "name": namefile['first_name'] + " " + namefile['last_name'],
    "source": other['source'],
    "destination": other['destination'],
    "datetime": other['datetime']
    } 
    if p.status_code == 200:
        data['pic'] = p.json()['profile_pic']
    print(data)

    text = data['name'] + " wants a ride from " + data['source'] +" to " + data['destination'] +" for " + data['datetime'] + " . Message them to schedule pickup!"
    payload = {
        "recipient": {
        "id": me['id']
        },
        "message": {
            "text":  text
        }
    }
    url = "https://graph.facebook.com/v2.8/me/messages?access_token=" + FACEBOOK_ACCESS_TOKEN
    headers = {"Content-Type": "application/json" }
    p = requests.post(url, headers=headers, data=json.dumps(payload))

    print("n")

    payload["message"] = {
        "attachment": {
        "type": "image",
        "payload": {
            "url": data['pic'] 
            }
        }
    }

    p = requests.post(url, headers=headers, data=json.dumps(payload))
    print(p.status_code)
    print(p.json())
