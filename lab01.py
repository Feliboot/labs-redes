# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
#"""
#import socket
#socket.gethostbyname(socket.gethostname())
#questao 1
import json
import requests as req
import os, sys
import socket as sk
host_name=sk.gethostname()##retorna o hotname da maquina

#print('hostname:',host_name)
base = 'https://api.ipify.org'##site que retorna como texto o ip da maquina
ip = req.get(base).text
print("Hostname:{}\nIP:{}".format(host_name,ip))


print('ITEM C')
for port in range(10000):
    try:
        tcp=sk.getservbyport(port,'tcp')
    except OSError:
        tcp=None
    try:
        udp=sk.getservbyport(port,'udp')
    except OSError:
        udp=None
    #Pode ser que existam portas que sejam tanto udp como tcp
    if tcp and udp:
        print('Porta:{}\tProtocolo: TCP e UDP'.format(port))
    elif tcp:
        print('Porta:{}\tProtocolo: TCP'.format(port))
    elif udp:
        print('Porta:{}\tProtocolo: UDP'.format(port))
    #pode acontecer da porta nao usar nenhum dos dois protocolos

print('Fim da execução da primeira questão')

print('2 questão')
base_2q='http://freegeoip.net/json/'
sites = ("globo.com",   #1
         "google.com",  #2
         "facebook.com",#3
         "superanimes.com",#4
         "youtube.com", #5
         "yahoo.com",   #6
         "gmail.com",   #7
         "si3.ufc.br",  #8
         "caixa.gov.br",#9
         "netflix.com") #10
for link in sites:
    req_get = req.get(base_2q+link)
    print(link)
    dados=req_get.json()
    print("IP:",dados['ip'],"  COUNTRY:",dados['country_name'],"REGION:",dados['region_name'],"\n")
    
    
    
