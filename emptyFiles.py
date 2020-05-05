# -*- coding: utf-8 -*-
import os

basicText1 = '''*Flores a Maria*
Pe. Martinho A. Pereira da Silva, 1907

## '''

basicText2 = ''' de  maio -- 

## Primeiro ponto -- ;



## Segundo ponto -- ;



## Terceiro ponto -- .



## Oração



## Lição -- .

## Máxima espiritual

"_._" Sto. .
'''
inicial = 7
final = 31
for dia in range(inicial,final+1):
    with open("{:02d}.md".format(dia),"w", encoding="utf-8") as arquivo:
        arquivo.write(basicText1)
        arquivo.write("{:d}".format(dia))
        arquivo.write(basicText2)
        arquivo.close()