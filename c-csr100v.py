#resconf-put.py 
import json 
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://10.10.0.254/restconf/data/ietf-interfaces:interfaces/interface=Loopback8"

headers = { "Accept": "application/yang-data+json", "Content-type":"application/yang-data+json"
}
basicauth = ("admin", "cisco") 
yangConfig = {
    "ietf-interfaces:interface": { 
        "name": "Loopback8",
        "description": "Loopback8", 
        "type": "iana-if-type:softwareLoopback", 
        "enabled": True,
        "ietf-ip:ipv4": { 
            "address": [
                {
                    "ip": "10.10.1.8",
                    "netmask": "255.255.0.0"
                }
          ]
        },
        "ietf-ip:ipv6": {}
    }
}

resp = requests.post(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299): 
    print("LOOPBACK INTERFACE CREATION.....STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message:{}'.format(resp.status_code,resp.json()))

api_url = "https://10.10.0.254/restconf/data/Cisco-IOS-XE-native:native/ip/route"

headers = { "Accept": "application/yang-data+json", "Content-type":"application/yang-data+json"
}
basicauth = ("admin", "cisco") 
yangConfig = {
    "Cisco-IOS-XE-native:route": {
        "ip-route-interface-forwarding-list": [
            {
                "prefix": "0.0.0.0",
                "mask": "0.0.0.0",
                "fwd-list": [
                    {
                        "fwd": "Loopback8"
                    }
                ]
            }
        ]
    }
}

resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299): 
    print("DEFAULT ROUTE ADDITION.......STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message:{}'.format(resp.status_code,resp.json()))

api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing-state/routing-instance=default/ribs/rib=ipv4-default/routes"

resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print("SHOWING ROUTING TABLE.......STATUS OK: {}".format(resp.status_code))
print(json.dumps(resp.json(),indent=4))