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
