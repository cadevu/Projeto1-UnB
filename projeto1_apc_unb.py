input()
restaurante={}
mesas_ocupadas={}
n_comandos=0
total_mesas={}
mesas_ocupadas={}
mesas_ocupadas['soma']=0
total_cadeiras={}
pessoas_total={}
total_pessoas={}
correcao=0

while True: # break point e recebe a area e as mesas e cadeiras
    
    teste=list(input().split())
    if teste[0]== '--ATENDIMENTO':
        break    
    area=teste[0]
    cadeiras= int(teste[2])
    mesas=int(teste[1])
    if area not in restaurante: # adicionar a área no dicionário restaurantes 
        restaurante[area]={}
        restaurante = {key: val for key, val in sorted(restaurante.items(), key = lambda ele: ele[0])} # ordenar as mesas de acordo com o número de cadeiras
    if cadeiras not in restaurante[area]: # adicionar o tipo de mesa no dicionario da area 
        restaurante[area][cadeiras]=0
        restaurante[area] = {key: val for key, val in sorted(restaurante[area].items(), key = lambda ele: ele[0])}
    restaurante[area][cadeiras]= mesas
    if area not in total_mesas: #armazena o número total de mesas
        total_mesas[area]= {}
        total_mesas = {key: val for key, val in sorted(total_mesas.items(), key = lambda ele: ele[0])}
    if cadeiras not in total_mesas[area]: 
        total_mesas[area][cadeiras]=0
        total_mesas[area] = {key: val for key, val in sorted(total_mesas[area].items(), key = lambda ele: ele[0])}
    soma_mesas= total_mesas[area][cadeiras] + mesas
    total_mesas[area][cadeiras]= soma_mesas
    if area not in total_cadeiras:
        total_cadeiras[area]=0
    total_cadeiras[area]= cadeiras + total_cadeiras[area]
    soma_pessoas_area= cadeiras*mesas
    if area not in pessoas_total:
        pessoas_total[area]=0
    pessoas_total[area]= soma_pessoas_area + pessoas_total[area]
def fechamento_restaurante(): #comando final de fechamento do restaurante
    print('Restaurante fechado.')
    print('Balanco final de mesas:')
    for area in restaurante:
        print(area + ':')
        for n_cadeiras in restaurante[area]:
            print(f' {total_mesas[area][n_cadeiras]} mesas de {n_cadeiras} cadeiras.')
    print(f'Um total de {mesas_ocupadas["soma"]} pessoas visitaram o restaurante hoje.')
    print('Bom descanso!')
def comando_1():   # alocação de pessoas em determinada mesa em determinada área 
    flag= False
    frase_qtd= list(input().split())
    qtd_pessoas= int(frase_qtd[4])    
    for area in restaurante:
        if area == frase_qtd[8]:
            for n_mesas in restaurante[area]: #n_mesas = chaves do dicionario restaurante[area]
                if int(frase_qtd[4])<= n_mesas and restaurante[area][n_mesas]!=0 :
                   
                    mesas_ocupadas['soma']= mesas_ocupadas['soma'] + qtd_pessoas                    
                    flag=True
                    print(f'Um grupo de {frase_qtd[4]} pessoas ocupou uma mesa de {n_mesas} lugares na area {frase_qtd[8]}.')
                    restaurante[area][n_mesas]=restaurante[area][n_mesas] - 1 #retira a mesa das mesas disponiveis
                    if frase_qtd[8] not in mesas_ocupadas:
                        mesas_ocupadas[frase_qtd[8]]=[]
                    tempo_permanencia=(((2* int ( frase_qtd[4]))+2) + n_comandos) 
                    mesas_ocupadas[frase_qtd[8]].append([int(frase_qtd[4]),n_mesas,tempo_permanencia]) #número de pessoas,numero de cadeiras da mesa, tempo de permanencia
                    if area not in total_pessoas:
                        total_pessoas[area]=0
                    total_pessoas[area]= total_pessoas[area] + qtd_pessoas
                    break                   
            if flag==False:        
                print('Nao foi possivel levar o grupo de clientes para uma mesa.')
    
def comando_2():    #relação de quantas mesas estão ocupadas 
    for area in restaurante:
        if area not in mesas_ocupadas:
            for sublista in restaurante[area]:
                print (f'{area}: (0 de {sum(total_mesas[area].values())} mesas)')
                break
        else:
            total_ocupadas= len(mesas_ocupadas[area])
            for sublista in restaurante[area]:
               print(f'{area}: ({total_ocupadas} de {sum(total_mesas[area].values())} mesas)')
               break
def comando_3(): #relatório de quantas pessoas há no restaurante no momento
    for area in restaurante:
        if area not in mesas_ocupadas:
            for sublista in restaurante[area]:
                print (f'{area}: (0 de {pessoas_total[area]} pessoas)')
                break
        else:
               print(f'{area}: ({total_pessoas[area]- correcao} de {pessoas_total[area]} pessoas)')    # colocar um contador no mesas_ocupadas[area][indice de cadeiras em cada mesa]
def comando_4(): # adicionar ou remover mesas em determinada area 
    frase_cmd4= list(input().split()) #comando = [1] , n de mesas = [3] n de cadeiras = [6] area = [11]
    area4= frase_cmd4[11]
    tipo_mesa= int (frase_cmd4[6])
    mesas4=int(frase_cmd4[3])
    if frase_cmd4[1]== 'adicionar':
        if tipo_mesa not in restaurante[area4]:
            restaurante[area4][tipo_mesa]=0
        if tipo_mesa not in total_mesas[area4]:
            total_mesas[area4][tipo_mesa]= 0
        restaurante[area4][tipo_mesa]= restaurante[area4][tipo_mesa] + mesas4
        total_mesas[area4][tipo_mesa]= total_mesas[area4][tipo_mesa] + mesas4
        pessoas_total[area4]= pessoas_total[area4] + (tipo_mesa * mesas4 )
        total_cadeiras[area4]= total_cadeiras[area4] + tipo_mesa
        print(f'{mesas4} mesas de {tipo_mesa} cadeiras adicionadas com sucesso na area {area4}.')
    else:
        restaurante[area4][tipo_mesa]= restaurante[area4][tipo_mesa] -mesas4
        total_mesas[area4][tipo_mesa]= total_mesas[area4][tipo_mesa] -mesas4
        pessoas_total[area4]= pessoas_total[area4] - (tipo_mesa * mesas4 )
        total_cadeiras[area4]= total_cadeiras[area4] - tipo_mesa
        print(f'{mesas4} mesas de {tipo_mesa} cadeiras removidas com sucesso na area {area4}.')
comando=input() 
while True:
    if comando=='-1':
        fechamento_restaurante()
        break
    if comando =='1':
        n_comandos=n_comandos+1 
        comando_1()        
    if comando =='2':
        n_comandos=n_comandos+1 
        comando_2()        
    if comando =='3':
        n_comandos=n_comandos+1 
        comando_3()
    if comando =='4':
        n_comandos=n_comandos+1 
        comando_4()
    for area in mesas_ocupadas: #relação tempo de permanencia descrito no projeto
        if area != 'soma':
            for sublista in mesas_ocupadas[area]:
                if sublista[2]<=n_comandos+1:
                    restaurante[area][sublista[1]]=restaurante[area][sublista[1]] + 1
                    del(mesas_ocupadas[area][0])
                    total_pessoas[area]=total_pessoas[area]- sublista[0]
                    break
    comando=input()            
            