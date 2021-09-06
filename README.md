# Fullstack Convert CurrencyMoney 
Esse projeto foi um desafio técnico da empresa Data Stone, e faz conversão monetária.

## Forex-Python
Blibioteca utilizada para fazer as conversões foi o [forex-python](https://pythonrepo.com/repo/MicroPyramid-forex-python-python-e-commerce-and-payments).

### Fonte da Biblioteca:
[ratesapi](https://ratesapi.io) é uma API gratuita para as taxas de câmbio atuais e históricas publicadas pelo Banco Central Europeu. As taxas são atualizadas diariamente às 3PM CET.

Preços do Bitcoin calculados a cada minuto. Para obter mais informações, visite [CoinDesk API](http://www.coindesk.com/api/).

## Recursos
- Backend Python REST com FastAPI
- Frontend VueJS
- Docker Compose

## Executar Projeto com Docker

### Configurar
1. Clone este repositório
2. Faça cd na raiz do projeto e execute:
```bash
docker-compose up --build -d
```

### Aplicativo WEB - Frontend
http://localhost:8080/

### Docs API FastAPI - Backend
http://localhost:5000/docs


## Executar Projeto sem Docker
1. Clone este repositório

### Executar API sem Docker - Backend
1.1. Acessar o diretorio (/backend)
1.2. Criar um ambiente virtual com o comando abaixo
```bash
virtualenv .venv
```
1.3. Ainda no diretorio (/backend) rode o comando abaixo para ativar o ambiente virtual
```bash
 .\.venv\Scripts\activate
```
1.4. Rode o comando abaixo para instalar as dependencias
```bash
 pip install -r requirements.txt
```
1.5. Rode o comando abaixo para rodar a API FastAPI
```bash
uvicorn app:app --reload  
```

### Executar Web sem Docker - Frontend
1.1. Acessar o diretorio (/frontend)
1.2. Configuração do projeto
```
npm install
```
1.3. Executa Projeto
```
npm run serve
```



