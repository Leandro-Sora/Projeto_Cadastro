#!/bin/bash
#Código do Sora :P
clear

echo "Cadastro";
nome(){
read -p  "Informe seu Nome por favor: " NAME
echo $NAME| grep -E '[0-9,.;:/?!@#$%"&*()_+=]'
        if [ $? == 1 ]; then
        echo "nome válido" && email
        else
        echo "nome inválido tente novamente" && nome
        fi
}
email(){
read -p "Informe seu E-mail por favor: " EMAIL
echo $EMAIL| grep -E  '^([a-zA-Z0-9_-.])+@[0-9a-zA-Z.-]+\.[a-z]{2,3}$' \
&& echo -e "e-mail válido" && telefone || echo -e \
"e-mail inválido tente novamente" && email
}

telefone(){
echo "telefone no formato (xx)xxxx-xxxx"
read -p "Informe seu Telefone por favor: " TEL
echo $TEL | grep -E '^[(][0-9]{2}[)][0-9]{4}+-[0-9]{4}$' && \
echo -e "telefone válido" && rg || echo -e \
 "telefone inválido tente novamente" && telefone
}

rg(){
echo "RG no formato xx.xxx.xxx-x"
read -p "Informe seu RG por favor: " RG
echo $RG | grep -E '^[0-9]{2}\.[0-9]{3}\.[0-9]{3}-[0-9]|[xX]{1}' &&
echo -e "RG válido" && cpf || echo -e "RG inválido" && rg
}
cpf(){
echo "CPF no formato xxx.xxx.xxx-xx"
read -p "Informe seu CPF por favor: " CPF
echo $CPF | grep -E '^[0-9]{3}\.[0-9]{3}\.[0-9]{3}[-]{0,1}[0-9]{2}' &&
echo -e "CPF válido" && data || echo -e "CPF inválido" && cpf
}

data(){
echo "Data no formato xx/xx/xxxx"
read -p "Informe sua Data de nascimento por favor: " DATA
echo $DATA | grep -E '^[0-3]{1}[0-9]{1}[/][0-1]{1}[0-9]{1}[/][0-9]{4}$' &&
echo -e "Data de nascimento válida" && ip || echo -e \
"Data de nascimento inválida" && data
}

ip(){
read -p "Informe seu IP por favor: " IP
echo $IP | grep -E '^(((([2]([5][0-5]|[0-4][0-9])|[0-9][0-9])|[0-9])\.)|(1[0-9][0-9]\.)){3}((([2]([5][0-5]|[0-4][0-9])|[0-9][0-9])|[0-9])|[1][0-9][0-9])$'
        if (( $? == 0 )); then
        echo "IP válido" && mascara
        else
        echo "IP inválido" && ip
        fi
}
mascara(){
read -p "Informe sua Mascara por favor: " MASK
echo $IP | grep -E '^(((([2]([5][0-5]|[0-4][0-9])|[0-9][0-9])|[0-9])\.)|(1[0-9][0-9]\.)){3}((([2]([5][0-5]|[0-4][0-9])|[0-9][0-9])|[0-9])|[1][0-9][0-9])$'
        if (( $? == 0 )); then
        echo "Mascara válida" && end
        else
        echo "Mascara inválida" && mascara
        fi
}

end(){
echo "você completou o cadastro com sucesso, parabéns !!!"

sleep 2 && exit

}
nome
