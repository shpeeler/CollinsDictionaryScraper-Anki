from .util.util import Util
import requests
import time

class CollinsDictionary(object):

    base_url = 'https://www.collinsdictionary.com/dictionary/french-english/conjugation/{}'

    def __init__(self, sleep=1.5):
        self.sleep = sleep

    def request(self, verb):
        """
        requests the page for given verb
        """

        time.sleep(self.sleep)
        url = str(self.base_url).format(verb)

        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError as e:
            Util.write(str(e))
            return None

        return response.content
