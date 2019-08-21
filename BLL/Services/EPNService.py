import requests
import json
from BLL.Exeptions.EpnWrongAuthException import EpnWrongAuthException
from BLL.Exeptions.EpnOfferNotFoundException import EpnOfferNotFoundException


class EPNService:

    def __init__(self, user, group):
        self.user = user
        self.group = group

    @staticmethod
    def __build_request_data(user, vk_items: list):

        data = {
            "user_api_key": "" + user.epn_api_token,
            "user_hash": "" + user.epn_hash,
            "api_version": 1,
            "requests": {

            }
        }

        counter = 0

        for item in vk_items:
            data["requests"]["rq_" + str(counter)] = {
                "action": "offer_info",
                "lang": "ru",
                "id": "" + item[1],
                "currency": "USD"

            }

            counter = + 1

        return data

    @staticmethod
    def __send_request(user, vk_items: list):

        data = EPNService.__build_request_data(user, vk_items)
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post("http://api.epn.bz/json", data=json.dumps(data), headers=headers)

        print(response.status_code)

        if "error" in response.json():
            if response.json()["error"] == 'Bad auth data!':
                raise EpnWrongAuthException("Wrong auth data!")
            # if "rq_0" in response.json():
            #     print("ok")
            #     if response.json()["result"]["rq_0"]["error"] == 'Offer not found':
            #         raise EpnOfferNotFoundException("Offer not found!")

    def create_deeplinks(self, vk_items: list):

        response = EPNService.__send_request(self.user, vk_items)

        deeplinks = list()

        counter = 0
        for item in response.json()["results"]:

            sale = (response.json()["results"]["rq_" + str(counter)]["offer"]["sale_price"] / response.json()["results"]["rq_" + str(counter)]["offer"]["price"])

            if sale < 0.1:
                sale = int(sale * 10)
            elif sale >= 0.1:
                sale = int(sale * 100)

            deeplink = {
                "image": response.json()["results"]["rq_" + str(counter)]["offer"]["picture"],
                "title": vk_items[counter][0],
                "url": response.json()["results"]["rq_" + str(counter)]["offer"]["url"],
                "price": response.json()["results"]["rq_" + str(counter)]["offer"]["sale_price"],
                "sale": sale,
                "group_id": self.group.id,
                "user_id": self.group.user_id
            }

            deeplinks.append(deeplink)
            counter = + 1

        return deeplinks
