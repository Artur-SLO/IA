from src.covid_data import Covid_Data
from datetime import date

PATH = "../data/covid.csv"
data = Covid_Data(PATH)

data.print()

N = 5000
print(f"=== Cidades do estado com mais de {N} casos ===\n")
data.highest_score(N)

print("\n=== Numero de casos intervalar ===\n")
data.interval(date(2025, 5, 5), date(2026, 5, 11))

N = 10
print(f"\n=== Top {N} cidades ===")
data.top(N, date(2023, 5, 5), date(2026, 5, 11))

print(f"\n=== Porcentagens {N} cidades ===")
data.percentages(N)

print("\n=== Media e Desvio Padrão ===")
data.meanstd()
