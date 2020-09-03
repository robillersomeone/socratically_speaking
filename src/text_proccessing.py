# text processing

import re

########################
# parsing raw txt files
########################

# apology ends with 'End of the Project Gutenberg EBook of Apology, by Plato'
# dialogue starts on line 469

# crito ends with 'End of this Project Gutenberg Etext of Crito, by Plato'


# symposium ends with 'End of the Project Gutenberg EBook of Symposium, by Plato'

########################
# identifying speakers
########################

def format_two_speakers(dialogue):
    '''
    for crito only
    '''
    return [x.replace("CRITO:", "CRITOtalking").replace("SOCRATES:", "SOCRATEStalking").lower() for x in dialogue.split()]
  

def speakers_said(dialogue):
    '''
    case in point symposium

    get text from speaker said format
    '''

################ 
# text cleaning
################

def count_questions(dialogue):
    '''
    count the number of '?' in a dialgoue
    '''
    pass

def no_punctuation(dialogue):
    '''
    fix method to take puncuation out
    '''
    cleaned_words = []
    for word in dialogue:
        s = re.sub(r'[^\w]','',word) 
        cleaned_words.append(s)
    return cleaned_words
crito = no_punctuation(format_words()) 

def stems_and_lemmas(dialogue):
    '''
    get lemmas of words
    '''
    pass