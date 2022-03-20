# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 22:56:21 2018

@author: eduardo salmoria fantin
"""

import pyansys

import numpy as np

import os.path

print('insira o caminho para o .rst')
arquivo = input()

print('insira o quais modos que você quer(separado por espços 0 2 3 4)')
str_posi_modos=input().split(' ')
posi_modos=[int(num) for num in str_posi_modos]

print('insira o numero de modos que você quer (separado por espços 0.1 0.2 0.3 0.4)')
str_modal_damp=input().split(' ')
modal_damp=[float(num2) for num2 in str_modal_damp]

print('insira a direcao que você quer o arquivo 0=x 1=y 2=z 3=xy 4=yz 5=xz (Por algum motivo 5 é o maior valor para a viga sanduiche')
str_direcao = input()
direcao=[int(num3) for num3 in str_direcao]

print('insira caminho para salvar o arquivo')
savepath=input()

print('insira o nome do projeto')
projectname=input()

result = pyansys.ResultReader(arquivo)

nodes=result.geometry.get('nodes')

freqs= result.GetTimeValues()

modes = result.GetNodalResult(0, True)

if posi_modos[0]==12345:
    for i in range(0,len(freqs)):
        posi_modos[i]=i
else:
    posi_modos=posi_modos

    
if modal_damp[0]==12345:
    for j in range(0,len(freqs)):
        modal_damp[j]=0.001
else:
    modal_damp=modal_damp

"""
for i in range(0, len(nodes)):
    for j in range(0,3):
        nodes3D[i,j]=nodes[i,j]

    

np.savetxt('example.txt', np.c_[nodes3D],
               header='Filexy\nnodes3D', fmt='%.10e',
               delimiter='\t')
"""

filename=os.path.join(savepath,projectname+".eig")
file=open(filename,"w")
a=[1, 3, 5, 9, 11]


for k in range(0,len(posi_modos)):  
  file.write(' ')
  file.write(str(freqs[posi_modos[k]]))  

file.write("\n")
file.write("\n")
for p1 in range(0,len(posi_modos)):
    file.write(' ')
    file.write(str(modal_damp[p1]))
    
    
for p2 in range(0,len(posi_modos)):
    modes = result.GetNodalResult(posi_modos[p2],True)
    file.write("\n")
    file.write("\n")
    for p3 in range(0,len(modes[1])):
        file.write(' ')
        file.write(str(float(modes[1][p3][direcao])))
    
file.close()

filenamedat=os.path.join(savepath,projectname+".dat")
filedat=open(filenamedat,"w")
filedat.write("nblock,3")
filedat.write("\n")
for p4 in range(0, len(nodes)):
    filedat.write(' ')
    filedat.write(str(p4))
    for p5 in range(0, 3):
        filedat.write(' ')
        filedat.write(str(nodes[p4,p5]))
    filedat.write("\n")    

filedat.write("\n")
filedat.write("/wb")
filedat.close()
