import requests
from IIFLapis import IIFLClient


def iiflholdings():
    headers = {
        "Ocp-Apim-Subscription-Key": "fc714d8e5b82438a93a95baa493ff45b",
        "Content-Type": "application/json"
    }
    data = {
        "head": {
            "appName": "IIFLMarARPIT  G",
            "userId": "IYSqCaIb7Nl",
            "password": "jUxmFGAW8xp",
            "key": "LIsgACEaIdPgxTTNDjzmFMrHUUgVQpJP",
            "requestCode": "IIFLMarRQHoldingV2",
            "osName": "WEB",
            "appVer": "1.0"
        },
        "body": {
            "ClientCode": "ARPITJUL"
        }
    }
    r = requests.post(url="https://dataservice.iifl.in/openapi/prod/Holding", headers=headers, data=data)
    print(r.status_code)
    print(r.content)


def get_iifl_client():
    client = IIFLClient(client_code="ARPITJUL", passwd="TVlogin@13", dob="19910716",
                        email_id="goyal.arpit.91@gmail.com", contact_number="8861094754")
    client.client_login()  # For Customer Login
    # P = client.holdings("ARPITJUL")
    # print(P)
    return client
