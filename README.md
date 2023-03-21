# Bem-vindo ao Projeto TING!

Este é um projeto da [Trybe](https://www.betrybe.com/) que foi desenvolvido no módulo de Ciência da Computação.

Trata-se da implementação de um programa que simula um algoritmo de indexação de documentos similar ao do Google. Este programa é capaz de identificar ocorrências de termos em arquivos TXT. Retornando uma lista de objetos com o nome do arquivo, linhas onde o termo buscado aparece e, caso deseje, o conteúdo desta linha.

## Tecnologias utilizadas

Em seu desenvolvimento foi utilizada linguagem ***Python*** para escrever os códigos, e o framework ***pytest***, para testar uma classe que já havia sido implementada pela Trybe.

## Habilidades que foram trabalhadas:

  - Manipulação de filas (Queue); 

## Como rodar o projeto na sua máquina:

1. Navegue até o local onde deseja clonar o repositório e utilize o **git clone**:
```
git clone git@github.com:LucasOAssuncao/Project_Ting.git
```

2. Acesse o diretório do projeto **project-ting**:
```
cd project-ting
```

3. Crie e ative um ambiente virtual para o projeto:
```
python3 -m venv .venv && source .venv/bin/activate
```

4. Instale as dependências:
```
python3 -m pip install -r dev-requirements.txt
```

5. Para rodar o teste é utilizado o seguinte comando:
```
python3 -m pytest
```
