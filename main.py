from random import randint
from colorama import Fore


def jogarDados():
    numDado = randint(2, 12)
    return numDado


def primeiraRegra(dados):
    if dados == 7 or dados == 11:
        return True
    elif dados == 2 or dados == 3 or dados == 12:
        return False


def segundaRegra(dados, ponto):
    while dados:
        numDado = jogarDados()
        print(f'{Fore.CYAN}Seu novo lançamento tem o valor: {Fore.MAGENTA}{numDado}'
              f'{Fore.YELLOW} e seu primeiro lançamento tem o valor {Fore.MAGENTA}{dados}')
        print(f'{Fore.GREEN}=' * 80)

        if numDado == 7:
            print(f'{Fore.RED}Infelizmente você perdeu! Tente da próxima vez :(')
            break
        elif ponto == numDado:
            print()
            print(f"{Fore.GREEN}#" * 29 + ' PARABÉNS VOCÊ GANHOU ' + '#' * 29)
            break


def encontrarPontos(dados):
    pontos = [4, 5, 6, 8, 9, 10]
    for i in pontos:
        if i == dados:
            ponto = i
            segundaRegra(dados, ponto)
            break


def principal(dados):
    verification = dados != 7 or dados != 11 or dados != 2 or dados != 3 or dados != 12
    if primeiraRegra(dados):
        print()
        print(f"{Fore.GREEN}#" * 29 + ' PARABÉNS VOCÊ GANHOU ' + '#' * 29)
    elif primeiraRegra(dados) == False:
        print(f'{Fore.RED}Infelizmente você perdeu! Tente da próxima vez :(')
    elif verification:
        print(f'{Fore.BLUE}Se você tirar o mesmo resultado do seu primeiro lançamento você vence!!\n'
              f'-> E se lançar o valor 7 você perde!\n')
        encontrarPontos(dados)


if __name__ == "__main__":
    print(f"{Fore.RED}=" * 30 + ' REGRAS ' + '=' * 30)
    print(
        f'Se, na primeira jogada, você tirar 7 ou 11, você um "sortudo" e ganhou\n Se você tirar 2, 3 ou 12 na '
        f'primeira jogada, que "azar"!! ')
    print('=' * 70)
    print(f'\n{Fore.GREEN}Lançando os dados...')
    valorDado = jogarDados()
    print(f'{Fore.CYAN}Você lançou os dados e obteve o valor: {Fore.MAGENTA}{valorDado}')
    principal(valorDado)
