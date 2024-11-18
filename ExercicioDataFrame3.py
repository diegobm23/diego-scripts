import pandas as pd

cereais = pd.read_csv("/home/diegobm23/projetos-diegobm23/diego-scripts/Datasets/cereal.csv")

media_calorias = cereais[["mfr", "calories"]].groupby("mfr").mean()
qtde_fabricantes = cereais["mfr"].nunique()
qtde_por_tipo = cereais[["type", "name"]].groupby("type").count()
qtde_tipo_c = cereais[(cereais.type == "C") & (cereais.protein == 1)]["name"].count()
qtde_rice = cereais[cereais["name"].str.contains("Rice")]["name"].count()

print("Média de calorias por fabricante")
print(media_calorias)
print("\n**********\n")
print("Total de fabricantes: ", qtde_fabricantes)
print("\n**********\n")
print("Quantidade de produtos por tipo")
print(qtde_por_tipo)
print("\n**********\n")
print("Quantidade de produtos do tipo C com apenas 1 proteína: ", qtde_tipo_c)
print("Quantidade de produtos com a palavra Rice no nome: ", qtde_rice)
