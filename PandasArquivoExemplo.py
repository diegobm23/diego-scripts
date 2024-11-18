import pandas as pd

prouni = pd.read_csv("/home/diegobm23/projetos-diegobm23/diego-scripts/Datasets/cursos-prouni.csv")
print(prouni)
print("\n**********\n")

print(prouni.dtypes)
print("\n**********\n")

print(prouni.info())
print("\n**********\n")

print(prouni.head(15))
print("\n**********\n")

print(prouni.tail(15))
print("\n**********\n")

# Exporta o .csv para excel na pasta do projeto.
#prouni.to_excel("cursos-prouni.xlsx", sheet_name="cursos", index=False)

# Exporta o .csv para json na pasta do projeto.
#prouni.to_json("cursos-prouni.json")

# Subconjuntos
nota_curso = prouni[ ["nota_integral_ampla", "curso_busca"] ]
print(nota_curso.head(15))
print("\n**********\n")

# Seleção de linhas
sul = prouni[ prouni["uf_busca"].isin(["PR", "SC", "RS"]) ]
print(sul.head(15))
print("\n**********\n")

baratos = prouni[ prouni.mensalidade < 300 ][ ["curso_busca", "mensalidade"] ]
print(baratos.head(15))
print("\n**********\n")

nota_alta = prouni.loc[prouni.nota_integral_ampla > 700, ["curso_busca", "nota_integral_ampla"]]
print(nota_alta.head(15))
print("\n**********\n")

# Criação de colunas
nota_alta["Nota"] = nota_alta.nota_integral_ampla / 10
print(nota_alta.head(15))
print("\n**********\n")

# Agrupamentos
grupo_notas = prouni[["curso_busca", "nota_integral_ampla"]].groupby("curso_busca").mean()
print(grupo_notas.sort_values("nota_integral_ampla", ascending=False))
print("\n**********\n")

# Removendo linhas com valores NaN
prouni_limpo = prouni.dropna()
print(prouni_limpo)

# Removendo colunas com valores NaN
prouni_limpo = prouni.dropna(axis=1)
print(prouni_limpo)

# Coloca zero em todas as celulas com NaN
prouni_limpo = prouni.fillna(0)
print(prouni_limpo)

# Coloca a média em todas as células com NaN de uma coluna
prouni_limpo = prouni["nota_integral_ampla"].fillna(prouni.nota_integral_ampla.mean())
print(prouni_limpo)