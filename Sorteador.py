import random

def sorteador():
    entrada = input("Digite os itens separados por vírgula: ")
    itens = [item.strip() for item in entrada.split(",") if item.strip()]
    
    if itens:
        escolhido = random.choice(itens)
        print(f"\n🎉 Sorteado: {escolhido}")
    else:
        print("Você precisa digitar pelo menos um item!")

# Executar
sorteador()
