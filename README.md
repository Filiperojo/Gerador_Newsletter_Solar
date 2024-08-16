# Gerador de Newsletter Solar21

Este projeto automatiza a geração de newsletters para a Solar21. Ele utiliza a automação do Selenium para coletar resumos de artigos do site Canal Solar e, em seguida, formata esses resumos em um template HTML para envio via e-mail.

## Funcionalidades

- Coleta automática de resumos e títulos de artigos usando o Selenium e BeautifulSoup.
- Geração dinâmica de um template HTML para a newsletter.
- Envio de e-mails em massa usando a API do SendGrid.
- Integração com a API da OpenAI para gerar resumos e títulos concisos.

## Requisitos

Antes de executar o projeto, certifique-se de ter as seguintes dependências instaladas:

- Python 3.8+
- `selenium`
- `requests`
- `beautifulsoup4`
- `openai`
- `sendgrid`
- `webdriver-manager`
- `fitz`

Você pode instalar todas as dependências com o seguinte comando:
```bash
pip install -r requirements.txt
```

## Instalação
Clone o repositório:

```bash
git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio
```

## Instale as dependências:

```bash
pip install -r requirements.txt
```

Adicione suas chaves de API ao código:

No arquivo scrape.py, substitua o valor de OpenAI.api_key e SendGridAPIClient pela sua chave da API do OpenAI e do SendGrid, respectivamente.

## Uso
Configure o template HTML da newsletter:

O arquivo HTML/index.html é utilizado como template. O script substituirá os placeholders (titulo1, texto1, link1, etc.) pelos conteúdos coletados.

Execute o script sending.py para rodar o código e gerar a newsletter:

```bash
python scripts/sending.py
```
O sistema irá gerar uma prévia da newsletter e solicitará a sua confirmação antes de enviar os e-mails para os franqueados.

## Estrutura do Projeto

```bash
/newsletter-generator
├── /HTML
│   ├── index.html          # Template da newsletter
│   └── exemplo.html        # Arquivo HTML gerado pela execução
├── /scripts
│   ├── production.py       # Script principal para a geração do HTML da newsletter
│   ├── scrape.py           # Script para coleta de resumos e títulos de artigos
│   └── sending.py          # Script responsável por enviar os e-mails
├── README.md               # Documentação do projeto
├── requirements.txt        # Lista de dependências
└── .gitignore              # Arquivos a serem ignorados no Git
```
