# EXPRESSÕES ARITMETICAS TEM PRECEDENCIAS SOBRE AS LOGICAS

print(5==5)
 #
print(2+1 >= 3)
 # PRIMEIRO A EXPRESSÃO ARITMETICA É RESOLVIDA E O RESULTADO É COMPARADO COM O VALOR 3
print(13 % 10 != 3)
 #  A PERGUNTA É: O RESTO DA DIVISAO ENTRE 13 E 10 É DIFERENTE DE 3?
print(1>3 or 1+3>2)
 # OU: SE UMA DAS PROPOSIÇÕES FOR TRUE, A EXPRESSÃO RESULTA NUM TRUE
print(1>2 and 1+3>2)
 # E: A EXPRESSAO SO RESULTA TRUE QUANDO TODAS AS PROPOSIÇÕES SAO VERDADEIRAS
print(not 1>3 and 1+3>2)
 # NÃO: O NOT EM FRENTE A QUALQUER NUMERO OU EXPRESSÃO CONVERTE O VALOR DAQUILO Q ELE PRECEDE NO CONTRARIO