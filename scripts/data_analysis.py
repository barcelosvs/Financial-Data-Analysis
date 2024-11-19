import pandas as pd

def process_data(input_file):
    data = pd.read_csv(input_file, sep=",")
    
    if "Close" not in data.columns or "Date" not in data.columns:
        raise ValueError("As colunas esperadas não foram encontradas no arquivo. Verifique os dados.")

    data['Close'] = pd.to_numeric(data['Close'], errors='coerce')

    data.dropna(subset=['Close'], inplace=True)

    data.set_index("Date", inplace=True)

    data['Short_MA'] = data['Close'].rolling(window=20).mean()
    data['Long_MA'] = data['Close'].rolling(window=50).mean()

    data.to_csv(input_file.replace(".csv", "_processed.csv"))
