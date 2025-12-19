from math import factorial as fat
from os import system, name


def cls():
    '''
    Limpa o terminal
    '''
    system('cls' if name== 'nt' else 'clear')

def media_aritimetica():
    '''
    Pede uma lista de valores\n
    Divide a soma de todos os valores pela quantidade de valores\n
    Devolve a média aritimética
    '''
    som_val= 0

    val= float(input('Digite o valor\n'
                     'Valor:'))
    cls()

    contador= 0

    while val!= 0:
        contador+= 1
        som_val+= val

        cls()
        print('Digite 0 para parar\n')
        val= float(input('Digite o proximo valor\n'
                         'Valor:'))

        if val== 0:
            contador-= 1

    return som_val/contador

def prob_marginal():
    '''
    Pede a quantidadde de elementos n(e) e o tamanho do espaço amostral n(Ω)\n
    devolve a probabilidade marginal de n(e) dividido por n(Ω).
    '''

    eleme= int(input('Digite a quantidade de elementos\n'
                     'Quantidade:'))
    cls()

    espa_amost= int(input('Digite o tamanho do espaço amostral\n'
                          'Tamanho:'))
    cls()
    return (eleme/espa_amost)*100 

def permu_simp():
    '''
    Função que faz permutações simples.\n
    pergunta o numero (n) de elementos distintos\n
    Recebe a quantidade de elementos deverão ser usados no agrupameto\n
    Faz o calculo de permutação simples e devolve o resultado
    '''
    def fixo():
        '''
        pergunta se há elementos com posição fixa\n
        Se sim pergunta quantos\n
        Devolve a quantidade de de elementos com posição fixas.
        '''

        perg= input('Há elementos que tem posição fixa?\n'
                    '(s/n)\n'
                    'Resposta:')
        cls()

        if perg!= 's' or perg!= 'n':
            raise ValueError

        elif perg== 's':

            perg= int(input('Qual o numero de elementos com posição fixa?\n'
                             'Numero:'))
            cls()

            return perg
        
        else:
            return 0
    
    def junt():
        perg= input('Há elementos que aparecem juntos?\n'
                    '(s/n)\n'
                    'Resposta:')
        cls()

        if perg!= 's' or perg!= 'n':
            raise ValueError
        
        elif perg== 's':
            perg= int(input('Quantos elementos aparecem juntos?\n'
                         'Resposta:'))
            cls()
            
            return perg-1
        
        else:
            return 0
    
    cls()

    n= int(input('Digite o numero (n) de elementos\nNumero:'))
    cls()

    fixos= fixo()
    juntos= junt()

    
    
    return fat(n-juntos- fixos) #retorna a permutação no caso em que há elementos juntos mas não há fixos.
                            #e quando não há nem juntos nem fixos

def arranjo_simp():
        '''
        Pede o numero de elementos n(e) e de quantos em quantos eles devem ser arranjados (p)\n
        Retorna o arranjo simples
        '''

        def term_come():
            '''
            pergunta se o arranjoo deve começar ou terminar com elementos especificos\n
            Se sim, pergunta quantos e devolve o resultado. 
            '''
            perg= input('O arranjo deve começar ou terminar com elementos especificos?\n'
                        '(s/n)\n'
                        'Resposta:')
            cls()

            if perg!= 's' or perg!= 'n':
                raise ValueError

            elif perg== 's':
                perg2= int(input('Deve começar/terminar com quantos elementos especificos?\n'
                                'Quantidade:'))
                cls()

                return int((fat(eleme-perg2))/fat((eleme-perg2)-(arra-perg2)))
            
            else: 
                return

        def tem():
            '''
            pergunta se o arranjo deve ter algum elemento especifico\n
            Se sim, faz a conta e devolve o resultado.
            '''
            perg= input('O arranjo deve ter algum elemento especifico?\n'
                        '(s/n)\n'
                        'Resposta:')
            cls()

            if perg!= 's' or perg!= 'n':
                raise ValueError

            elif perg== 's':
                
                perg2= int(input('Quantos elementos especificos deve ter?\n'
                                 'Quantos:'))
                cls()

                return int((fat(eleme-perg2))/fat((eleme-perg2)-(arra-perg2)))
            
            else:
                return

        def nao_tem():

            perg= input('O arranjo não deve ter algum elemento especifico?\n'
                        '(s/n)\n'
                        'Resposta:')
            cls()

            if perg!= 's' or perg!= 'n':
                raise ValueError
            
            elif perg== 's':

                perg2= int(input('Quantos elementos não deve ter?\n'
                                 'Quantidade:'))
                cls()

                nao_ha= int(fat(eleme-perg2)/fat((eleme-perg2)-arra))
                
                return nao_ha
            
            else:
                return None
            

        eleme= int(input('Digite a quantidade de elementos\n'
                     'Quantidade:'))
        cls()

        arra= int(input('Digite de quantos em quantos quer arranja-los\n'
                        'Resposta:'))
        cls()

        termina_comeca= term_come()
        tem_elemento= tem()
        nao_tem_elemento= nao_tem()

        if termina_comeca!= None:
            return termina_comeca
        
        elif tem_elemento!= None:
            return tem_elemento
        
        elif nao_tem_elemento!= None:
            return nao_tem_elemento

        else:
            return int(fat(eleme)/fat(eleme-arra))

def comb_simp():
    '''
    Pede o numero de elementos n(e) e a quantidade em que quer agrupa-los (p)\n
    Devolve o numero de possibilidades, ignorando a ordem, em que pode agrupa-los.
    '''

    eleme= int(input('Digite o numero de elementos\n'
                     'Numero:'))
    cls()

    quant_grup= int(input('Quer agrupa-los em quantos?\n'
                          'Quantos por grupo:'))
    cls()

    num= 1

    inicio= eleme-quant_grup

    if inicio==0:
        inicio= 1

    for n in range(inicio+1, eleme+1, 1):
        num*= n

    return num/fat(quant_grup)

def distr_binom ():
    '''
    função para calculo de distribuição binomial\n
    Pede as seguintes informações apara fazer a conta\n
    n= numero total de itens\n
    x= numero de itens selecionados\n
    p= probabilidade de ocorrencia do evento\n
    '''

    n= int(input('Digite o numero total de itens\n'
                 'Numero:'))
    cls()

    x= int(input('Digite o numero de itens selecionados\n'
                 'Numero:'))
    cls()

    p= float(input('Digite a probabilidade de ocorrencia de evento\n'
                   'Exmplo: 0.9 pois é igual a 90%\n'
                   'Probabilidade:'))
    cls()

    fa_n= fat(int(n)); fa_x= fat(int(x)); fa_nx= fat(int(n-x)) #a função fat() só aceita numeros inteiros
                                                            #por isso converti para int
    fracao= fa_n/(fa_x*fa_nx)
    return fracao* (p**x) *((1-p)**(n-x))

def erro_padrao() -> float:
    '''
    Pede o desvio padrão e o numero de elementos a amostra n(Ω).\n
    Devolve o erro-padrão.
    '''

    desvi_padr= float(input('Digite o valor do desvio padrão\n'
                            'Valor:'))
    cls()

    num_elem= int(input('Digite o numero de elementos da amostra\n'
                        'Numero:'))
    cls()

    erro_pad= desvi_padr/(num_elem**(1/2))

    return erro_pad

def probabilidade_de_Z(z):
    '''
    Recebe o valor dde Z e Retorna sua probabilidade
    '''
    from math import erf, sqrt
    return 0.5*(1+erf(z/sqrt(2)))
 
def distribuicao_padrao():

    '''
    Pede os valores da média aritimética obtida X, média aritimética desejada φ(fi), e do desvio padrão.\n
    Retorna o valor de Z e pergunta se deseja a probabilidade.
    '''

    X= float((input('Digite o valor da média aritimética obtida\n'
                  'Valor de x:')))
    cls()

    fi= float(input('Digite o valor da média aritimética desejada\n'
                  'Valor de fi(φ):'))
    cls()

    desvi_pad= float(input('Digite o valor do desvio padrão\n'
                           'Valor:'))
    cls()

    val_Z= (X-fi)/desvi_pad

    perg= input(f'O valor de Z é {val_Z}\n'
                'Quer receber a probabilidade?\n'
                '(s/n)\n'
                'Resposta:')
    cls()

    if perg== 's':
        return probabilidade_de_Z(val_Z)
    
    else:
        return

def media_aritimetica_com_intervalo_simetrico_bicaudal():
    '''
    Pede a média aritimética desejada φ(fi)\n
    Pede o valor de Z, do desvio padrão e da quantidade de elementos na amostra.\n
    Retorna Z inferior e Z superior 
    '''
    media_dese= float(input('Digite o valor da média aritimética desejada\n'
                            'Valor de φ(fi):'))
    cls()

    val_Z= float(input('Digite o valor de Z\n'
                       'Valor de Z:'))
    cls()

    desv_pad= float(input('Digite o valor do desvio padrão\n'
                          'Valor do desvio padrão:'))
    cls()

    num_ele= int(input('Digite a quantidade de elementos da amostra\n'
                       'Quantidade:'))
    cls()

    Z_superior= media_dese+val_Z*(desv_pad/(num_ele**(1/2)))
    Z_inferior= media_dese-val_Z*(desv_pad/(num_ele**(1/2)))

    return f'Z superior:{str(Z_superior)}\nZ inferior:{str(Z_inferior)}'
