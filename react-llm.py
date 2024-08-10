import openai

# Simulação de chamada para um modelo ReAct
def react_model(prompt):
    # Exemplo de raciocínio e ação combinados
    reasoning = "Para calcular o fatorial de um número, precisamos multiplicar todos os inteiros de 1 até o número. " \
                "Isso pode ser feito de maneira iterativa ou recursiva. A recursão é mais direta, pois a função chama " \
                "a si mesma até que o caso base seja atingido."
    
    # Ação: Geração do código com base no raciocínio
    code = """
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
"""
    return reasoning, code

# Entrada de exemplo
prompt = "Gerar o código para calcular o fatorial de um número."

# Simulação da chamada ao modelo
reasoning, code = react_model(prompt)

# Saída
print("Raciocínio do Modelo:")
print(reasoning)
print("\nCódigo Gerado:")
print(code)
