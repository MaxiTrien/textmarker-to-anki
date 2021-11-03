import pandas as pd
import os


def data_to_csv(data, result_dir):
    df = pd.DataFrame(data) 
    df.to_csv(os.path.join(result_dir, 'textmarker.csv'), encoding='utf-8', 
              index=False, header=False)
    print('CSV file created.')
