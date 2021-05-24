# Instalar ambiente virtual 
- sudo pip install virtualenv

## Criar diretorio virtual
###          nome do diretorio 
- virtualenv env

## Ativar diretório virtual
###     nome diretorio
env\Scripts\activate

## Desligar diretorio virtual
env\Scripts\deactivate

### requirements.txt -> arquivo com toda configuração a ser instalada para rodar o projeto 

# rodar na pasta do projeto se usar diretório virtual
- pip install -r requirements.txt 

# rodar na pasta do projeto direto na maquina local
pip install --user -r requirements.txt
