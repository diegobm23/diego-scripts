import pandas as pd

cereais = pd.read_csv("/home/diegobm23/projetos-diegobm23/diego-scripts/Datasets/cereal.csv")

trix_sugar = cereais[cereais.name == "Trix"]["sugars"].iloc[0]
quaker_potass = cereais[cereais.name == "Quaker Oatmeal"]["potass"].iloc[0]
max_sodium = cereais[cereais.sodium == cereais.sodium.max()]["name"].iloc[0]
diets = cereais[cereais.fat == 0][["name", "calories"]]

print("\n***************************************")
print("Trix - sugar: " + trix_sugar.astype(str))
print("Quaker Oatmeal - potass: " + quaker_potass.astype(str))
print("Max sodium: " + max_sodium)
print("***************************************")
print(diets)
print("***************************************")

# Salva o DataFrame em excel
#diets.to_excel("diets.xlsx", sheet_name="diets", index=False)