import pytest
import math

# Ex 1-)
# Crie uma função que receba dois números e retorne o maior deles.
def higher_number(num1, num2):
    return max(num1, num2)
# Teste estático
def test_higher_number():
    assert higher_number(1, 2) == 2
    assert higher_number(2, 1) == 2
# Teste dinâmico
@pytest.mark.parametrize("num1, num2", [(1, 2), (2, 1), (0, 0), (-1, -2), (-2, -1)])
def test_higher_number(num1, num2):
    assert higher_number(num1, num2) == max(num1, num2)

# Ex 2-)
# Calcule a média aritmética dos valores contidos em uma lista.
def arithmetic_average(arr):
    sum_1 = sum(arr)
    return int(sum_1 / len(arr))

# Teste
def test_arithmetic_average():
    assert arithmetic_average([2, 4, 6]) == 4
    assert arithmetic_average([7, 2, 14]) == 7
    assert arithmetic_average([0, 34, 2, 76]) == 28

# Ex 3-)
# Escreva uma função imprima na tela um quadrado feito de asteriscos de lado de tamanho n
def generate_square(n):
    squares = []
    for i in range(n):
        line = n * '*'
        squares.append(line)
    return '\n'.join(squares)

print(generate_square(5))

# Teste
def test_generate_square():
    assert generate_square(5) == '*****\n*****\n*****\n*****\n*****'
    assert generate_square(2) == '**\n**'
    assert generate_square(1) == '*'
    
# Ex 4-)
# Retorne o maior nome
def biggest_name(arr):
    maior_nome = ''
    for nome in arr:
        if len(nome) > len(maior_nome):
            maior_nome = nome
    return maior_nome

# Teste
def test_biggest_name():
    arr = ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]
    assert biggest_name(arr) == "Fernanda"

# Ex 5-)
"""
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Crie uma função que retorne dois valores em uma tupla contendo a quantidade
de latas de tinta a serem compradas e o preço total a partir do tamanho de uma
parede (em m²).
"""

def paint_calculation(m2):
    litros = m2 / 3
    latas = litros / 18
    latas = math.ceil(latas)
    preco_total = latas * 80
    return (latas, preco_total)

# Teste
def test_paint_calculation():
    m2 = 54
    expected_output = (1, 80)
    assert paint_calculation(m2) == expected_output

    m2 = 55
    expected_output = (2, 160)
    assert paint_calculation(m2) == expected_output

# Ex 6-)
# Crie uma função que receba 3 lados de um triangulo e informe qual tipo de triangulo é formado
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return 'Triângulo Equilátero: três lados iguais'
        elif a == b or a == c or b == c:
            return 'Triângulo Isósceles: quaisquer dois lados iguais'
        else:
            return 'Triângulo Escaleno: três lados diferentes'
    else:
        return 'Não é um triângulo'

# Teste
def test_is_triangle():
    assert is_triangle(4, 4, 4) == 'Triângulo Equilátero: três lados iguais'
    assert is_triangle(4, 4, 5) == 'Triângulo Isósceles: quaisquer dois lados iguais'
    assert is_triangle(3, 4, 5) == 'Triângulo Escaleno: três lados diferentes'
    assert is_triangle(1, 2, 3) == 'Não é um triângulo'
