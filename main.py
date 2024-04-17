"""phi de Euler"""
# Se n = p^k, então phi(n) = p^k - p^(k-1)

import random
from math import floor, sqrt

# c = candidato a gerador
# d = divisores da ordem de Z (fatoração de Z)
# p = o grupo Z
# l = lista dos primos

# phi(n) = pi^(ei) - pi^(ei-1)

"1. calcular a distância de 1 até o primeiro elemento do grupo que satisfaz (x+1)(x-1) = 0 mod phi(n): gerando d"
"2. descobrir quem é o numero ao lado na lista dos coprimos com n, pois ele também atende x^2 = 1 mod n"
"3. pular de novo pro próximo numero após a distância d"
"4. adicionar esses numeros em lista e os multiplos também"


def group(n):
    from math import gcd
    for i in range(1, n):
        if gcd(i, n) > 1:
            continue
        for j in range(1, n):
            if gcd(j, n) > 1:
                continue
            print(f"{(i*j) % n:2}", end=" ")
        print()


def inverseGroup(n):
    p = phi(n)
    c = [cop(n)] # lista com os elementos do grupo n
    for i in range(len(c)-1):
        if c[i] % p == 0:
            d = i - 1


def phi(n):
    for p in primes(n):
        n *= (1 - 1 / p)
    return int(n)


def generator(n):
    cp = cop(n)  # recebe os coprimos de n
    while len(cp) > 0:  # enquanto a quantidade de elementos em cp forem maiores que zero, continua a tentar candidatos
        j = random.choice(cp)  # pseudoaleatoriedade dos elementos em Zn para pegar um candidato
        if is_generator(j, n) is True:  # se o candidato for gerador, retorna imeditamente
            return f"<{j}>"
        cp.remove(j)  # senão, o remove da lista e testa o próximo
    return False  # se não tiver gerador (não é cíclico), retorna False


def is_generator(c, p):  # Recebe os valores do candidato a gerador e do grupo Z
    l = []
    for i in cop(p):  # puxa os coprimos pela função cop(n) e cria um loop para cada um
        l.append(generator_try_d(c, i, p))  # retorna os valores do candidato, do fator e do grupo para a função generator_try_d e insere o valor True e/ ou False na lista
    if False in l:  # se existir algum elemento falso na lista, retorna False
        return False
    return True


def cop(n):
    l = []
    for i in range(2, n):
        if mdc(i, n) == 1:
            l.append(i)
    return l


def generator_try_d(c, d, p):  # Só testa um divisor por vez para o candidato a gerador
    if c ** (phi(p) // d) % p != 1:
        return True
    else:
        return False


def primes(n):
    l = []
    l.extend([p for p, _ in primes_by_trial(n)])  # adicionando à lista o primeiro elemento da tupla (o primo) e ignorando o valor do seu expoente
    return l


def primes_by_trial(n, p=[]):
    p.append(itrial(n))
    if itrial(n) == n:  # quando o último primo for igual a n, que é o último valor das divisões sucessivas de n por seu fator
        return [(i, p.count(i)) for i in set(p)]
    else:
        return primes_by_trial(n // p[-1], p)  # divide n pelo último primo adicionado


def itrial(n, nxt=2):
    assert nxt >= 2, "but the smallest prime is 2, isn't it?"
    assert n >= 2
    for nxt in range(nxt, floor(sqrt(n)) + 1):  # nxt (2) percorre a faixa de nxt até a raíz quadrada de n
        if divides(nxt, n):  # enquanto nxt não alcança o valor da raíz quadrada de n, verifica se nxt divide n
            return nxt  # caso divida, retorna nxt
    return n  # senão, retorna n


def is_prime(n):
    x = itrial(n)
    if x == n:
        return True
    else:
        return False


def divides(a, b):
    if b % a == 0:
        return True
    else:
        return False


def mdc(a, b): #por euclides, a divide b sucessivamente até o resto ser zero
    if b == 0: #se b (a mod b) for igual a zero, retorna a (último dividendo == m-1 ou antigo b)
        return a
    else: #atribui b-1 (a mod b) para variável a (a == n-1), atribuindo à posição de b o novo a mod b, assim, dividindo b antigo pelo resto
        return mdc(b, a % b)


n1 = int(input(''))
print(cop(n1))



