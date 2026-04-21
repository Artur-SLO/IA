import csv

class Parameters:
    def __init__(self, PATH):
        with open(PATH, 'r') as f:
            params = {
                row['Param'].strip(): row['Valor'].strip()
                for row in csv.DictReader(f)
                if row.get('Param') and row.get('Valor')
            }

        self.type_avg = 1 if params.get('avg_tipo', 'B').upper() == 'B' else 0
        self.type_std = 1 if params.get('std_tipo', 'C').upper() == 'B' else 0
        self.weight_avg = float(params.get('avg_peso', 0.5))
        self.weight_std = float(params.get('std_peso', 0.5))

    def print(self):
        print("Paramenters: ")
        print(f"Type avg: {'B' if self.type_avg == 1 else 'C'}")
        print(f"Type std: {'B' if self.type_std == 1 else 'C'}")
        print(f"Weight avg: {self.weight_avg}")
        print(f"Weight std: {self.weight_std}\n")

    def get_type_avg(self):
        return self.type_avg

    def get_type_std(self):
        return self.type_std

    def get_weight_avg(self):
        return self.weight_avg

    def get_weight_std(self):
        return self.weight_std
