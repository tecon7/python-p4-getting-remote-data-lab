import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
        response = requests.get(url)
        return response.content

    def load_json(self):
        people_list = []
        people = json.loads(self.get_response_body())
        for name in people:
            people_list.append(name)

        return people_list
