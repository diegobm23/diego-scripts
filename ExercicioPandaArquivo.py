import pandas as pd

cereais = pd.read_csv("/home/diegobm23/projetos-diegobm23/diego-scripts/Datasets/cereal.csv")

print(cereais.info())

calorias = cereais.calories
sodio = cereais.sodium

calorias_mean = round(calorias.mean(), 2)
sodio_max = sodio.max()

print("\n************************************")
print("A média de calorias é: " + calorias_mean.astype(str))
print("A maior concetração de sódio é: " + sodio_max.astype(str))
print("************************************")
