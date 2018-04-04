# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 17:38:30 2018

@author: felipe
"""
"""
Crie uma lista com 10 endereços de sites distintos, para cada um destes sites crie uma
requisição http utilizando o urllib e exiba as meta-informações retornadas por cada site.
Explique com suas palavras o significado de pelo menos uma das meta-informações
retornada por cada endereço."""

import urllib.request
import urllib.parse

sites = ("http://wikipedia.org",   #1
         "http://google.com",  #2
         "http://facebook.com",#3
         "https://superanimes.site",#4
         "http://youtube.com", #5
         "http://yahoo.com",   #6
         "http://gmail.com",   #7
         "http://si3.ufc.br",  #8
         "http://caixa.gov.br",#9
         "http://netflix.com") #10


         
for link in sites:
    try:
        x = urllib.request.urlopen(link)
        print (x.info())
    except urllib.error.HTTPError as e:
        print (link)
        print('Error code:', e.code)
        print('Error code:', e.reason)## Diz o razão do erro de http
    except urllib.error.URLError as e:
        print(link)
        print('Error code:', e.reason)

"""
O cache control é um cabeçalho que nos diz especificamente os mecanismos de cache tanto requests como
em responses, as diretivas do Cache-Control sao unidirecionais, ou seja, uma diretiva que ocorre em 
um request não será necessariamente o mesmo quando ocorre uma response.
Os erros apresentados nessa lista de sites, foi:

https://superanimes.site
Error code: 403
Error code: Forbidden

http://caixa.gov.br
Error code: 302
Error code: The HTTP server returned a redirect error that would lead to an infinite loop.

O 403 é quando pedido é reconhecido pelo servidor mas este recusa-se a executá-lo.
O 302 exigiu que o cliente fizesse um redirecionamento temporário, porém a mensagem diz que esse
redirecionamento levaria a um loop infinito.

"""
