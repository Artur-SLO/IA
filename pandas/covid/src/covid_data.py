import pandas as pd

class Covid_Data:
    def __init__(self, PATH, nrows=-1):
        self.nrows = nrows
        if self.nrows == -1:
            self.data = pd.read_csv(PATH, sep=";", on_bad_lines="skip")
        else:
            self.data = pd.read_csv(PATH, sep=";", on_bad_lines="skip", nrows=self.nrows)
        self.data = self.data[self.data['Bairro'] != 'Não Encontrado']
        self.nrows = len(self.data)
        self.data['DataDiagnostico'] = pd.to_datetime(self.data['DataDiagnostico'], errors='coerce')

    def highest_score(self, N):
        unique_data = self.data['Municipio'].value_counts()
        unique_data = unique_data[unique_data > N]
        unique_data = unique_data.sort_index()
        print(unique_data)

    def interval(self, start, end):
        start_dt = pd.to_datetime(start)
        end_dt = pd.to_datetime(end)

        mask = (self.data['DataDiagnostico'] >= start_dt) & (self.data['DataDiagnostico'] <= end_dt)

        total = len(self.data[mask])

        print(f"Between {start} and {end}\n{total} cases, {(total / self.nrows * 100):.2f}% of cases")

    def top(self, N, start, end):
        start_dt = pd.to_datetime(start)
        end_dt = pd.to_datetime(end)
        data = self.data

        mask = (data['DataDiagnostico'] >= start_dt) & (data['DataDiagnostico'] <= end_dt)
        top = data[mask]
        top = top['Municipio'].value_counts()
        top = top.head(N)
        print(top)

    def percentages(self, N):
        hospitalized = (
            self.data[(self.data['FicouInternado'] == 'Sim') & (self.data['Classificacao'] == 'Confirmados')]
            ['Municipio']
            .value_counts()
            .head(N)
            .div(len(self.data))
            .mul(100)
        )

        deaths = (
            self.data.dropna(subset=['DataObito'])
            ['Municipio']
            .value_counts()
            .head(N)
            .div(len(self.data))
            .mul(100)
        )

        hospitalized_dead = (
            self.data[(self.data['FicouInternado'] == 'Sim') & (self.data['Classificacao'] == 'Confirmados') & (self.data['DataObito'].notna())]
            ['Municipio']
            .value_counts()
            .head(N)
            .div(len(self.data))
            .mul(100)
        )

        print("\nConfirmados e Hospitalizados:\n")
        print(hospitalized.to_string(float_format='{:,.3f}%'.format))

        print("\nObitos:\n")
        print(deaths.to_string(float_format='{:,.3f}%'.format))

        print("\nHospitalizado e Obito:\n")
        print(hospitalized_dead.to_string(float_format='{:,.3f}%'.format))

    def meanstd(self):
        death = (
            self.data[self.data['DataObito'].notna()]
            ['IdadeNaDataNotificacao']
            .str.extract('(\\d+)')[0]
            .astype(int)
        )
        death_without_disease = (
            self.data[
                (self.data['DataObito'].notna()) &
                (self.data['ComorbidadePulmao'] == 'Não') &
                (self.data['ComorbidadeCardio'] == 'Não') &
                (self.data['ComorbidadeRenal'] == 'Não') &
                (self.data['ComorbidadeDiabetes'] == 'Não') &
                (self.data['ComorbidadeTabagismo'] == 'Não') &
                (self.data['ComorbidadeObesidade'] == 'Não')
            ]['IdadeNaDataNotificacao']
            .str.extract(r'(\d+)')[0]
            .astype(int)
        )

        print(f"Media Idade: {death.mean():.3f}")
        print(f"Desvio Padrão Idade: {death.std():.3f}")
        print(f"Mortes sem comorbidades: {len(death_without_disease) / len(death) * 100:.3f}%")

    def print(self):
        data = self.data
        data.info()
        print(data[['Bairro', 'Municipio', 'DataObito']])
        # print(data['DataDiagnostico'])
