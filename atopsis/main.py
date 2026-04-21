import csv
from src.matrix import Matrix
from src.parameters import Parameters
from src.atopsis import Atopsis

AVG_PATH = './avg_mat.csv'
STD_PATH = './std_mat.csv'
PAR_PATH = './params.csv'

def main():
    # Carregamento e Tratamento de Erros
    try:
        avg_matrix = Matrix(AVG_PATH)
        std_matrix = Matrix(STD_PATH)
        parameters = Parameters(PAR_PATH)
    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado. {e}")
        return
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return

    # Execução do Algoritmo
    atopsis = Atopsis(avg_matrix, std_matrix, parameters)
    ranking = atopsis.run()

    # Criação do arquivo de ranking
    ranking_by_name = sorted(ranking, key=lambda x: x[0])
    try:
        with open('resultado.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Algorithms', 'Coef'])
            for algorithm, score in ranking_by_name:
                formatted_score = f"{round(score, 2):g}"
                writer.writerow([algorithm, formatted_score])

    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

if __name__ == "__main__":
    main()
