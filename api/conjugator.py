from .requester import Requester
from .util.util import Util 
from bs4 import BeautifulSoup
import re

requester = Requester()

class Conjugator():

    def get_verb_data(self, verb):
        if verb == None:
            return None

        response = requester.request_page(verb) # remove from here on add to separate class

        if response == None:
            return None

        bsoup = BeautifulSoup(response, 'html.parser')
        table = bsoup.find('div', attrs={'class':'columns2'})

        result = self.read_table(table)

        fullstring = ""

        # create string for field
        for tense, conjugation_list in result.items():
            fullstring += '<b>{}:</b><br>'.format(tense)

            for conjugation in conjugation_list:
                fullstring += '{}<br>'.format(conjugation)

            fullstring += '<br>'

        return fullstring

    def read_table(self, table): # remove from _init_ to separate class
        """
        reads every in the given table contained tense/conjugation
        returns it as dict(tense, list(conjugation))
        """

        conjugation_dict = dict()

        for entry in table:
            if entry == "\n":
                continue

            # tense as string
            # create method that e.g. swaps string a to string b - maybe read val from jsons
            tense = re.search(r'>(.*)<', str(entry.contents[1])).group(1)

            # conjugation table as object
            conjugations = entry.contents[3]
            
            # all conjugations for given tense as list
            conjugation_list = self.read_conjugations(conjugations)

            # append tense and full conjugation list to dict
            conjugation_dict.update({tense : conjugation_list})
            
        # return all the verbs conjugations as dictionart <tense, list(conjugations)>
        return conjugation_dict

    def read_conjugations(self, conjugations): # remove from _init_ to separate class
        """
        reads the given conjugations tables conjugations
        returns them as list(conjugation)
        """

        conjugation_list = list()

        for conjugation in conjugations.contents:
            if conjugation == "\n":
                continue

            # conjugation (pronoun + verb)
            result = re.search(r'>(.*)<', str(conjugation)).group(1)
            
            conjugation_list.append(result)

        return conjugation_list