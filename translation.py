import os 
from googletrans import Translator
from collections import defaultdict
from export_to_anki import data_to_csv


def clean_linebreaks(sentences):
    # Clean sentences from line break char
    return [line for line in ''.join(sentences).split('\n') if line.strip() != '']


def convert_data(translated, header, textmarker_data):
    for translation in translated:
        textmarker_data['sentence'].append(translation.origin)
        textmarker_data['translation'].append(translation.text)
        textmarker_data['title'].append(header[2])
        textmarker_data['ulr'].append(header[1][header[1].rfind(' ') + 1:])  # Cut out only the url
        
    return textmarker_data
        

input_dir = r'C:\Users\Maxi\Desktop\中文课\textmarker_history'
split_seq = ['\n', '\n']
textmarker_data = defaultdict(list)

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
                textmarker_data = convert_data(
                    trans_sentences, header, textmarker_data)

data_to_csv(textmarker_data, input_dir)

print('Translations finished!')





