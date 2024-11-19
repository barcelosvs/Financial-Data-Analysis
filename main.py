import os
import scripts.data_extraction as data_extraction
import scripts.data_analysis as data_analysis
import scripts.data_visualization as data_visualization

def main():
    print("1. Coletando os dados...")
    data_extraction.download_stock_data("AAPL", "2020-01-01", "2023-01-01")
    print("Dados coletados e salvos em 'data/'")

    print("2. Processando os dados...")
    data_analysis.process_data("data/AAPL_data.csv")
    print("Dados processados e salvos em 'data/'")

    print("3. Gerando gráficos...")
    data_visualization.create_graph("data/AAPL_data_processed.csv")
    print("Gráficos gerados e salvos em 'outputs/'")

if __name__ == "__main__":
    if not os.path.exists("data"):
        os.makedirs("data") 
    if not os.path.exists("outputs"):
        os.makedirs("outputs")  
    main()
