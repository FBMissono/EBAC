import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys



sns.set_theme()  


def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao = 'nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).unstack().plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    return None
    
print('O nome do nosso script é: ', sys.argv[0])  

mes1 = sys.argv[1]

mes2 = sys.argv[2]  

mes3 = sys.argv[3]  

mes4 = sys.argv[4]  

mes5 = sys.argv[5]  
  
print('Mês de referência é: ', mes1 , mes2 , mes3 , mes4 , mes5)
 
 
sinasc1 = pd.read_csv('./input/SINASC_RO_2019_'+mes1+'.csv')
sinasc2 = pd.read_csv('./input/SINASC_RO_2019_'+mes2+'.csv')
sinasc3 = pd.read_csv('./input/SINASC_RO_2019_'+mes3+'.csv')
sinasc4 = pd.read_csv('./input/SINASC_RO_2019_'+mes4+'.csv')
sinasc5 = pd.read_csv('./input/SINASC_RO_2019_'+mes5+'.csv')

   
    
max_data1 = sinasc1.DTNASC.max()[:7]

os.makedirs('./output/figs/'+max_data1, exist_ok = True)

plota_pivot_table(sinasc1, 'IDADEMAE', 'DTNASC', 'mean', 'média idade mãe', 'data de nascimento')
plt.savefig('./output/figs/'+max_data1+'/media idade mae.png')

plota_pivot_table(sinasc1, 'IDADEMAE', 'DTNASC', 'count', 'quabtidade de nascimento', 'data de nascimento')
plt.savefig('./output/figs/'+max_data1+'/quantidade bebês ao longo do tempo')

plota_pivot_table(sinasc1, 'IDADEMAE', ['DTNASC', 'SEXO'], 'count',
                  'idade Mãe', 'data de nascimento', 'unstack')
plt.savefig('./output/figs/'+max_data1+'/media idade mae por sexo')

plota_pivot_table(sinasc1, 'PESO', ['DTNASC', 'SEXO'], 'count',
                  'média peso bebê', 'data de nascimento', 'unstack')
plt.savefig('./output/figs/'+max_data1+'/media peso do bebê por sexo')

plota_pivot_table(sinasc1, 'PESO', ['ESCMAE'], 'mean',
                  'peso bebê', 'escolalidade da Mãe', 'sort')
plt.savefig('./output/figs/'+max_data1+'/peso x escolaridade mãe')

plota_pivot_table(sinasc1, 'APGAR1', ['GESTACAO'], 'mean',
                  'apgar 1 médio', 'gestação', 'sort')
plt.savefig('./output/figs/'+max_data1+'/gestação x apgar1')

plota_pivot_table(sinasc1, 'APGAR5', ['GESTACAO'], 'mean',
                  'apgar 5 médio', 'gestação', 'sort')
plt.savefig('./output/figs/'+max_data1+'/gestação x apgar5')



max_data2 = sinasc2.DTNASC.max()[:7]

os.makedirs('./output/figs/'+max_data2, exist_ok = True)

plota_pivot_table(sinasc2, 'IDADEMAE', 'DTNASC', 'mean', 'média idade mãe', 'data de nascimento')
plt.savefig('./output/figs/'+max_data2+'/media idade mae.png')

plota_pivot_table(sinasc2, 'IDADEMAE', 'DTNASC', 'count', 'quabtidade de nascimento', 'data de nascimento')
plt.savefig('./output/figs/'+max_data2+'/quantidade bebês ao longo do tempo')

plota_pivot_table(sinasc2, 'IDADEMAE', ['DTNASC', 'SEXO'], 'count',
                  'idade Mãe', 'data de nascimento', 'unstack')
plt.savefig('./output/figs/'+max_data2+'/media idade mae por sexo')

plota_pivot_table(sinasc2, 'PESO', ['DTNASC', 'SEXO'], 'count',
                  'média peso bebê', 'data de nascimento', 'unstack')
plt.savefig('./output/figs/'+max_data2+'/media peso do bebê por sexo')

plota_pivot_table(sinasc2, 'PESO', ['ESCMAE'], 'mean',
                  'peso bebê', 'escolalidade da Mãe', 'sort')
plt.savefig('./output/figs/'+max_data2+'/peso x escolaridade mãe')

plota_pivot_table(sinasc2, 'APGAR1', ['GESTACAO'], 'mean',
                  'apgar 1 médio', 'gestação', 'sort')
plt.savefig('./output/figs/'+max_data2+'/gestação x apgar1')

plota_pivot_table(sinasc2, 'APGAR5', ['GESTACAO'], 'mean',
                  'apgar 5 médio', 'gestação', 'sort')
plt.savefig('./output/figs/'+max_data2+'/gestação x apgar5')



max_data3 = sinasc3.DTNASC.max()[:7]

os.makedirs('./output/figs/'+max_data3, exist_ok = True)

plota_pivot_table(sinasc3, 'IDADEMAE', 'DTNASC', 'mean', 'média idade mãe', 'data de nascimento')
plt.savefig('./output/figs/'+max_data3+'/media idade mae.png')

plota_pivot_table(sinasc3, 'IDADEMAE', 'DTNASC', 'count', 'quabtidade de nascimento', 'data de nascimento')
plt.savefig('./output/figs/'+max_data3+'/quantidade bebês ao longo do tempo')

plota_pivot_table(sinasc3, 'IDADEMAE', ['DTNASC', 'SEXO'], 'count',
                  'idade Mãe', 'data de nascimento', 'unstack')
plt.savefig('./output/figs/'+max_data3+'/media idade mae por sexo')

plota_pivot_table(sinasc3, 'PESO', ['DTNASC', 'SEXO'], 'count',
                  'média peso bebê', 'data de nascimento', 'unstack')
plt.savefig('./output/figs/'+max_data3+'/media peso do bebê por sexo')

plota_pivot_table(sinasc3, 'PESO', ['ESCMAE'], 'mean',
                  'peso bebê', 'escolalidade da Mãe', 'sort')
plt.savefig('./output/figs/'+max_data3+'/peso x escolaridade mãe')

plota_pivot_table(sinasc3, 'APGAR1', ['GESTACAO'], 'mean',
                  'apgar 1 médio', 'gestação', 'sort')
plt.savefig('./output/figs/'+max_data3+'/gestação x apgar1')

plota_pivot_table(sinasc3, 'APGAR5', ['GESTACAO'], 'mean',
                  'apgar 5 médio', 'gestação', 'sort')
plt.savefig('./output/figs/'+max_data3+'/gestação x apgar5')



max_data4 = sinasc4.DTNASC.max()[:7]

os.makedirs('./output/figs/'+max_data4, exist_ok = True)

plota_pivot_table(sinasc4, 'IDADEMAE', 'DTNASC', 'mean', 'média idade mãe', 'data de nascimento')
plt.savefig('./output/figs/'+max_data4+'/media idade mae.png')

plota_pivot_table(sinasc4, 'IDADEMAE', 'DTNASC', 'count', 'quabtidade de nascimento', 'data de nascimento')
plt.savefig('./output/figs/'+max_data4+'/quantidade bebês ao longo do tempo')

plota_pivot_table(sinasc4, 'IDADEMAE', ['DTNASC', 'SEXO'], 'count',
                  'idade Mãe', 'data de nascimento', 'unstack')
plt.savefig('./output/figs/'+max_data4+'/media idade mae por sexo')

plota_pivot_table(sinasc4, 'PESO', ['DTNASC', 'SEXO'], 'count',
                  'média peso bebê', 'data de nascimento', 'unstack')
plt.savefig('./output/figs/'+max_data4+'/media peso do bebê por sexo')

plota_pivot_table(sinasc4, 'PESO', ['ESCMAE'], 'mean',
                  'peso bebê', 'escolalidade da Mãe', 'sort')
plt.savefig('./output/figs/'+max_data4+'/peso x escolaridade mãe')

plota_pivot_table(sinasc4, 'APGAR1', ['GESTACAO'], 'mean',
                  'apgar 1 médio', 'gestação', 'sort')
plt.savefig('./output/figs/'+max_data4+'/gestação x apgar1')

plota_pivot_table(sinasc4, 'APGAR5', ['GESTACAO'], 'mean',
                  'apgar 5 médio', 'gestação', 'sort')
plt.savefig('./output/figs/'+max_data4+'/gestação x apgar5')



max_data5 = sinasc5.DTNASC.max()[:7]

os.makedirs('./output/figs/'+max_data5, exist_ok = True)

plota_pivot_table(sinasc5, 'IDADEMAE', 'DTNASC', 'mean', 'média idade mãe', 'data de nascimento')
plt.savefig('./output/figs/'+max_data5+'/media idade mae.png')

plota_pivot_table(sinasc5, 'IDADEMAE', 'DTNASC', 'count', 'quabtidade de nascimento', 'data de nascimento')
plt.savefig('./output/figs/'+max_data5+'/quantidade bebês ao longo do tempo')

plota_pivot_table(sinasc5, 'IDADEMAE', ['DTNASC', 'SEXO'], 'count',
                  'idade Mãe', 'data de nascimento', 'unstack')
plt.savefig('./output/figs/'+max_data5+'/media idade mae por sexo')

plota_pivot_table(sinasc5, 'PESO', ['DTNASC', 'SEXO'], 'count',
                  'média peso bebê', 'data de nascimento', 'unstack')
plt.savefig('./output/figs/'+max_data5+'/media peso do bebê por sexo')

plota_pivot_table(sinasc5, 'PESO', ['ESCMAE'], 'mean',
                  'peso bebê', 'escolalidade da Mãe', 'sort')
plt.savefig('./output/figs/'+max_data5+'/peso x escolaridade mãe')

plota_pivot_table(sinasc5, 'APGAR1', ['GESTACAO'], 'mean',
                  'apgar 1 médio', 'gestação', 'sort')
plt.savefig('./output/figs/'+max_data5+'/gestação x apgar1')

plota_pivot_table(sinasc5, 'APGAR5', ['GESTACAO'], 'mean',
                  'apgar 5 médio', 'gestação', 'sort')
plt.savefig('./output/figs/'+max_data5+'/gestação x apgar5')




