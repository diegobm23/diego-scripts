import pandas as pd

estudantes = ['Maria', 'Ana', 'João']
notas = [7, 10, 8]

matematica = pd.Series(data=notas, index=estudantes)

print(matematica)

curso = pd.DataFrame(
    {
        "Alunos": ['Maria', 'Ana', 'João'],
        "Matemática": [7, 10, 8],
        "Física": [8, 10, 8],
        "Português": [10, 10, 7]
    }
)

print(curso["Matemática"].mean())
print(curso.describe())