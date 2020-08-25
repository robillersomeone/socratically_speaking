import pandas as pd

def most_common_words(dialogue, frequency):
    '''
    '''

    df_most_common = pd.DataFrame(ordered_counts[:10], columns=['word', 'frequency'])
    df_most_common.plot(kind='bar', x='word', title='top 10 most common words')