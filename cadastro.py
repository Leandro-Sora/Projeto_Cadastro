#!/bin/usr/python
# -*- coding: utf8 -*-

import os, re

def nome():
         Nome = raw_input("Digite o seu nome: ")
         match = re.match ('^[a-zA-Z]', Nome)
         if match:
                 print 'Nome Válido!'

         else:
                 print 'Nome Inválido!'

                 print 'Digite Novamente: '
                 nome()
nome()

def email():
        Email = raw_input("Digite seu e-mail: ")
        match = re.match ('^[a-z]+([._-][0-9a-z]+|[0-9])*@[a-z]+([._-][0-9a-z]+|[0-9])*(\.com|\.br|.\com\.br)$' , Email)
        if match:
                print 'E-mail Válido!'

        else:
                print 'E-mail Inválido!'

                print 'Digite novamente: '
                email()
email()

def telefone():
        print 'Formato do número de telefone: (DDD) xxxx-xxxx'
        Telefone = raw_input("Digite o número de telefone: ")
        match = re.match ('^[(][0-9]{2}[)][ ][0-9]{4}-[0-9]{4}$' , Telefone)
        if match:
                print 'Número de Telefone válido!'
        else:
                print 'Número de Telefone inválido!'

                print 'Digite novamente: '
                telefone()
telefone()

def rg():
        print 'RG no formato xx.xxx.xxx-x'
        RG = raw_input("Digite o número do seu RG: ")
        match = re.match ('^[0-9]{2}\.[0-9]{3}\.[0-9]{3}-([0-9]|[xX]{1})$', RG)
        if match:
                print 'Número do RG válido!'

        else:
                print 'Número do RG inválido!'

                print 'Digite novamente: '
                rg()
rg()
def cpf():
          print 'CPF no formato xxx.xxx.xxx-xx'
          CPF = raw_input("Digite o número do seu CPF: ")
          match = re.match ('^[0-9]{3}\.[0-9]{3}\.[0-9]{3}[-]{0,1}[0-9]{2}$' , CPF)
          if match:
              print 'Número de CPF válido!'

          else:
              print 'Número de CPF inválido!'

              print 'Digite novamente: '
              cpf()
cpf()

def data():
        print 'Formato da data: dd/mm/aaaa'
        DATA = raw_input("Digite a sua data de nascimento: ")
        match = re.match ('^[0-3]{1}[0-9]{1}[/][0-1]{1}[0-9]{1}[/][0-9]{4}$' , DATA)
        if match:
                print  'Data de Nascimeto válida!'
        else:
                print 'Data de Nascimento inválida!'

                print 'Digite novamente: '
                data()
data()

def ip():
        IP = raw_input("Digite o seu IP: ")
        match = re.match ('^(((([2]([5][0-5]|[0-4][0-9])|[0-9][0-9])|[0-9])\.)|(1[0-9][0-9]\.)){3}((([2]([5][0-5]|[0-4][0-9])|[0-9][0-9])|[0-9])|[1][0-9][0-9])$', IP)
        if match:
                print 'Ip válido!'

        else:
                print 'IP inválido!'

                print 'Digite Novamente: '
                ip()
ip()
def mascara():
           Mascara = raw_input("Digite sua Mascara: ")
           match = re.search('^(((([2]([5][0-5]|[0-4][0-9])|[0-9][0-9])|[0-9])\.)|(1[0-9][0-9]\.)){3}((([2]([5][0-5]|[0-4][0-9])|[0-9][0-9])|[0-9])|[1][0-9][0-9])$',  Mascara)
           if match:
                   print 'Mascara válida'

           else:
                   print 'Mascara inválida'

                   print 'Digite novamente: '
                   mascara()
mascara()

print 'Você completou o cadastro com sucesso!!!!'
