from .collinsdictionary import CollinsDictionary

class Requester(CollinsDictionary):

    def __init__(self, sleep=1.5):
        super().__init__()

    def request_page(self, verb):
        return self.request(verb)