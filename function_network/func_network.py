import requests
import json

class Path:
    def find_path(start, api_path):
        return f"{start}/{api_path}"

hparameter = { 'Authorization': 'ApiKey' ,
            'Content-Type': 'application/json',
}

dparameter = {
    "workID":"testWork"
}

url = Path.find_path("https://google.com", "/v1/getWorkDraft/")
reponse = requests.get(url, headers=hparameter, data=dparameter)
print(reponse.status_code)


# class JS:
#     def jprint(obj):
#         text = json.dumps(obj, sort_keys=True)
#         return text