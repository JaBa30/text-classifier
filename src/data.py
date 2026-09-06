import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df = df.dropna(subset=['text', 'label'])
    df['text'] = df['text'].astype(str).str.lower().str.strip()
    df = df[df['text'] != ""]
    df = df.drop_duplicates(subset=['text'], keep='first')
    return df
