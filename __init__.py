from aqt import mw
from aqt.utils import showWarning
from anki.hooks import addHook
from anki.utils import stripHTMLMedia
from .api.requester import Requester
from .api.util.util import Util 
from .api.conjugator import Conjugator
from bs4 import BeautifulSoup
import re

config = Util.read_config()

conjugator = Conjugator()

def get_verb_data(editor):
    """
    reads verb information from collinsdictionary, parses the information and writes the tense/conjugations to
    the configured field
    """

    verb = stripHTMLMedia(editor.note.fields[editor.currentField])

    verb_data = conjugator.get_verb_data(verb)    

    # set field value
    for field in editor.note.keys():
        if field == config['field'] and verb_data != None:
            editor.note[field] = str(verb_data)

    # update gui elements
    mw.reset()

def verbLookupButton(buttons, editor):
    """
    creates a new button
    returns new set of buttons
    """

    editor._links['verb'] = get_verb_data
    icon = Util.get_icon_path() 

    return buttons + [editor._addButton(icon, 'verb', 'lookup verb data')]

addHook('setupEditorButtons', verbLookupButton)