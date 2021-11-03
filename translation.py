import os 
from googletrans import Translator
from collections import defaultdict


def clean_linebreaks(sentences):
    # Clean sentences from line break char
    return [line for line in ''.join(sentences).split('\n') if line.strip() != '']


def convert_data(translated, header, textmarker_data):
    for translation in translated:
        textmarker_data['title'] = header.title
        textmarker_data['ulr'] = header.ulr
        textmarker_data['sentence'] = translation.origin
        textmarker_data['translation'] = translation.translation
    
    return textmarker_data
        

input_dir = r'C:\Users\Maxi\Desktop\中文课\textmarker_history'
split_seq = ['\n', '\n']
textmaker_data = defaultdict()

for history_file in os.listdir(input_dir):
    if history_file.endswith('.txt'):
            with open(os.path.join(input_dir, history_file), encoding='utf8') as f:
                lines = f.readlines()
                idx_split = [(i, i+len(split_seq))
                             for i in range(len(lines)) if lines[i:i+len(split_seq)] == split_seq]
                
                header = lines[:idx_split[0][0]]
                sentences = lines[idx_split[0][1]:]
                header = clean_linebreaks(header)
                sentences = clean_linebreaks(sentences)
                
                translator = Translator()
                trans_sentences = translator.translate(sentences)
                textmarker_data= convert_data(trans_sentences, header)
                
print('Translations finished!')





