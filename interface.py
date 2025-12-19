from os import system, name
from calculo_prob import cls
import calculo_prob as cp

calculos= {
    'Média aritimética':cp.media_aritimetica,
    'Probabilidade simples':cp.permu_simp,  #dicionario com os tipos de calculos e as funções desses calculos
    'Permutação simples':cp.permu_simp,
    'Arranjo simples':cp.arranjo_simp,
    'Combinação simples':cp.comb_simp,
    'Erro-padrão':cp.erro_padrao,
    'Distribuição padrão':cp.distribuicao_padrao,
    'Distribuição binomial':cp.distr_binom,
    'Média aritimética com intervalo simetrico bicaudal':cp.media_aritimetica_com_intervalo_simetrico_bicaudal,
}

quant= list(calculos.keys()) #faz uma lista com as chaves do dicionario
funcao= list(calculos.values()) #faz uma lista com as funções do dicionario

while True:
    
    cls()

    for i, opcao in enumerate(quant, 1): #enumerate retorna uma tupla, por exemplo: (1, 'Probabilidade simples')
        print(f'[{i}] {opcao}')
    print(f'[{len(quant)+1}] Sair\n\n')

    try:
        escolha= int(input('Digite o numero da opção\n'
                           'Opção:'))
        cls()

    except ValueError:

        #tratamento simples para uma entrada string
        print('\n')
        print('Digite um numero inteiro\n'
              'pressione qualquer tecla para continuar')
        input()
        cls()
        continue

    if escolha== len(quant)+1: # como a opção de saida é sempre a ultima, é mais prático chamar o len(quant)
                                #que devolve numero de opções com funções, e acrescentar +1
        break

    elif 1<= escolha <= len(quant): #caso o mumero da escolha seja de 1 a (numero da ultima opção de calculo)

        try:
            indice= escolha-1

            resultado= funcao[indice]() #chama a função pelo numero que o usuário escolheu
            
            cls()
            print(f'O resultado da conta de {quant[indice]} é: {resultado}')
            print('Aperte qualquer tecla para continuar')
            input()
        
        except ValueError:
            
            #tratamento simples para erros nas entradas da função escolhida
            print('\n')
            print('Leia as perguntas com atenção\n'
                  'Digite apenas numeros\n'
                  'Respoda apenas com "s" para sim e "n" para não\n\n'
                  'pressione qualquer tecla para continuar')
            input()
    
    else:
        
        #solução simples para entradas com numeros fora do escopo de opções
        print('Escolha um numero associado as opções exibidas\n'
              'pressione qualquer tecla para continuar')
        input()
        cls()
