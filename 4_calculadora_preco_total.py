# 4- Calculadora de Preço Total
# Objetivo: Calcular o preço total de uma compra e exibir todas as informações.

# Informações da compra conforme a atividade
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

# Cálculo do preço total e arredondamento para 2 casas decimais (moeda)
preco_total = round(preco_unitario * quantidade, 2)

# Exibição de todas as informações
print("--- Calculadora de Preço Total ---")
print(f"Produto: {nome_produto}")
# O ":.2f" garante que o preço unitário seja exibido com duas casas decimais
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print("-" * 30)
# O ":.2f" garante que o preço total seja exibido com duas casas decimais
print(f"Preço Total da Compra: R$ {preco_total:.2f}")
