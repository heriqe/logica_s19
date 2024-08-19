# Exercício - Código para calcular gastos

gabriel = {
    'nome': 'Gabriel',
    'gastos': [49, 200, 9.99]
}

carol = {
    'nome': 'Carol',
    'gastos': [300, 420, 59.90, 33.80]
}

joao = {
    'nome': 'João',
    'gastos': [39.90, 23.50, 6.10, 19.50]
}

pessoas = [gabriel, carol, joao]

for pessoa in pessoas:
    nome = pessoa['nome']
    gastos = pessoa['gastos']
    total_gasto = int(sum(gastos))
    menor_gasto = int(min(gastos))
    maior_gasto = int(max(gastos))
    
    print(f"{nome}:")
    print(f"  Total gasto: R${total_gasto}")
    print(f"  Menor valor gasto: R${menor_gasto}")
    print(f"  Maior valor gasto: R${maior_gasto}")