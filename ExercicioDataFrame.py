import pandas as pd

comidas_favoritas = pd.DataFrame(
    {
        "Nome": ["Pizza", "Batata frita", "Sorvete"],
        "Tipo": ["Prato principal", "Entrada", "Sobre-mesa"],
        "Preço": [45.5, 12.9, 8.5]
    }
)

precos = comidas_favoritas["Preço"]

print(comidas_favoritas.describe())
print("\n***************************")
print("A soma dos preços é: " + precos.sum().astype(str))
print("A média dos preços é: " + precos.mean().astype(str))
print("***************************")
