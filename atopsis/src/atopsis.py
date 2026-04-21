import numpy as np
from src.topsis import Topsis

class Atopsis:
    def __init__(self, matrix_avg, matrix_std, params):
        self.m_avg = matrix_avg
        self.m_std = matrix_std
        self.params = params

    def run(self):
        # Definição dos critérios (1 ou 0)
        criteria_avg = self.params.get_type_avg()
        criteria_std = self.params.get_type_std()

        # TOPSIS nas Médias
        topsis_avg = Topsis(self.m_avg.get_matrix(), criteria_avg)
        closeness_avg = topsis_avg.run(normalize=True)

        # TOPSIS nos Desvios
        topsis_std = Topsis(self.m_std.get_matrix(), criteria_std)
        closeness_std = topsis_std.run(normalize=True)

        # Aplicação dos pesos
        w_avg = self.params.get_weight_avg()
        w_std = self.params.get_weight_std()

        # Os pesos são aplicados fora do TOPSIS para seguir o modelo do artigo
        matrix_c_weighted = np.column_stack((
            closeness_avg * w_avg,
            closeness_std * w_std
        ))

        # Topsis na Matriz Global (closeness_avg | closeness_std)
        global_criteria = [1, 1] # Sempre deve ser um criterio de beneficio
        topsis_global = Topsis(matrix_c_weighted, global_criteria)
        global_closeness = topsis_global.run(normalize=False)

        # Definição do Ranking Final
        ranking = sorted(
            zip(self.m_avg.algorithms, global_closeness),
            key=lambda x: x[1],
            reverse=True
        )

        return ranking
