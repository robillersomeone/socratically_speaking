# get dialogues

import requests

urls = {
    'apology' : 'http://www.gutenberg.org/cache/epub/1656/pg1656.txt',
    'crito' : 'http://www.gutenberg.org/cache/epub/1657/pg1657.txt',
    'euthyphro' : 'http://www.gutenberg.org/cache/epub/1642/pg1642.txt',
    'gorgias' : 'http://www.gutenberg.org/cache/epub/1672/pg1672.txt',
    'symposium' : 'http://www.gutenberg.org/cache/epub/1600/pg1600.txt',
    'phaedo' : 'http://www.gutenberg.org/cache/epub/1658/pg1658.txt'


}


############################
# save text in data folder
############################

def save_txt(dialogue):
    '''
    params
    ------
    dialogue : str
        name of dialogue
    returns
    -------
    None
        outputs a .txt file of the dialogue in the /data dir

    '''
    # look up the url
    dialogue_url = urls[dialogue]

    dialogue_text = requests.get(dialogue_url).text[:]

    with open(f'../data/raw/{dialogue}.txt', 'w') as f:
        f.write(dialogue_text)

save_txt('phaedo')