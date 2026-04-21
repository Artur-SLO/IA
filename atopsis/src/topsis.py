import numpy as np

class Topsis:
    def __init__(self, matrix, criteria, weights=None):
        self.matrix = np.array(matrix, dtype=float)

        self.criteria = criteria
        if isinstance(criteria, (int, float, str)):
            self.criteria = np.full(self.matrix.shape[1], int(criteria))

        """
            Para o exercicio proposto os pesos não são utilizados de forma direta na fase TOPSIS
            porém é uma possibilidade oferecida pelo algoritmo
        """
        self.weights = weights
        if weights is not None:
            self.weights = np.array(weights, dtype=float)

    def run(self, normalize=True):
        # Normalização
        if normalize:
            norm = np.sqrt(np.sum(self.matrix**2, axis=0))
            norm = np.where(norm == 0, 1e-10, norm) # Evitar divisão por zero
            norm_matrix = self.matrix / norm
        else:
            norm_matrix = self.matrix

        # Ponderação da matriz
        weighted_matrix = norm_matrix
        if self.weights is not None:
            weighted_matrix = norm_matrix * self.weights

        # Calculo dos ideais Positivos e Negativos
        ideal_pos, ideal_neg = [], []
        for i in range(weighted_matrix.shape[1]):
            col = weighted_matrix[:, i]
            if self.criteria[i] == 1: # Beneficio
                ideal_pos.append(np.max(col))
                ideal_neg.append(np.min(col))
            else: # Custo
                ideal_pos.append(np.min(col))
                ideal_neg.append(np.max(col))

        ideal_pos = np.array(ideal_pos)
        ideal_neg = np.array(ideal_neg)

        # Distâncias euclidianas
        d_pos = np.sqrt(np.sum((weighted_matrix - ideal_pos)**2, axis=1))
        d_neg = np.sqrt(np.sum((weighted_matrix - ideal_neg)**2, axis=1))

        # Coeficiente de proximidade
        denominator = d_pos + d_neg
        denominator = np.where(denominator == 0, 1e-10, denominator)
        closeness = d_neg / denominator

        return closeness
