# saude-permuta


# User Guide Python first steps

## Listar os módulos instalados

``` $ pip list ```

## Listar os módulos instalados para arquivo texto

``` $ pip freeze ```

> Obs: nomeie o arquivo como **requirements.txt**

## Instalar dependencias que foram salvas em arquivo texto

``` $ pip install -r requirements.txt ```

## Criar uma nova pasta para o projeto

``` $ mkdir <nome_do_projeto> ```

## Criar um novo ambiente virtual com VENV

``` $ python -m venv <nome_do_ambiente_virtual> ```

> Lembre-se de estar dentro da pasta do projeto para executar esse comando. \
> Sugestão de nome para o ambiente virtual: **<nome_do_projeto>\venv**

## Ativando o ambiente virtual

``` $ <nome_do_ambiente_virtual>/scripts/activate.bat ```

> Obs: O uso das barras [ \ ] ou [ / ] poderá ser invertido dependendo da linha de comando que você estiver executando os comandos.

## Desativando o ambiente virtual

``` $ deactivate ```

> Obs: para desativar o ambiente, é necessário que já esteja em um ambiente virtual.

## Remover o ambiente virtual

``` $ rmdir <nome_do_ambiente_virtual> /s ```

> Obs: O parâmetro /s indica que as subpastas também serão removidas.

## Instalar biblioteca para trabalhar com requisições HTTP

``` $ pip install requests ``` **ou** ``` $ python -m pip install requests ```

## Biblioteca de datetime pytz

``` $ pip install pytz ```

## Criar um APP/modulo dentro do projeto

``` $ django-admin startapp <nome_do_modulo> ``` \
> Ex: ```django-admin startapp pessoa```

---

## Executar as migrações do Django

``` $ python manage.py migration ```

## Criar migrações escritas posteriormente

``` $ python manage.py makemigrations ```

## Executar as migrações criadas

``` $ python manage.py migrate ```

