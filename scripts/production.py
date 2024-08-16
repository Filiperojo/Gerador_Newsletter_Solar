
import scrape

def main():
    flag = 9
    titulo_novo, texto_novo, url = scrape.coleta_resumo(flag)


    #  - - - - - - - - - -- - - - - - -- - - - - - -  PRIMEIRO CAMPO - - -- - - -- --- - -- - -- -- -- -#
    with open('HTML/index.html', 'r',encoding='utf-8') as file:
        html_content = file.read()
        html_content = html_content.replace('titulo1', titulo_novo)
        html_content = html_content.replace('texto1', texto_novo)
        html_content = html_content.replace('link1', url)
    

   
    #  - - - - - - - - - -- - - - - - -- - - - - - -  PRIMEIRO CAMPO - - -- - - -- --- - -- - -- -- -- -#


    #  - - - - - - - - - -- - - - - - -- - - - - - -  SEGUNDO CAMPO - - -- - - -- --- - -- - -- -- -- -#
    
    titulo_novo, texto_novo, url = scrape.coleta_resumo(flag + 2)

    html_content = html_content.replace('titulo2', titulo_novo)
    html_content = html_content.replace('texto2', texto_novo)
    html_content = html_content.replace('link2', url)
    

    
      #  - - - - - - - - - -- - - - - - -- - - - - - -  SEGUNDO CAMPO - - -- - - -- --- - -- - -- -- -- -#


      #  - - - - - - - - - -- - - - - - -- - - - - - -  TERCEIRO CAMPO - - -- - - -- --- - -- - -- -- -- -#
    titulo_novo, texto_novo, url = scrape.coleta_resumo(flag + 4)
 
    html_content = html_content.replace('titulo3', titulo_novo)
    html_content = html_content.replace('texto3', texto_novo)
    html_content = html_content.replace('link3', url)
      #  - - - - - - - - - -- - - - - - -- - - - - - -  TERCEIRO CAMPO - - -- - - -- --- - -- - -- -- -- -#

      #  - - - - - - - - - -- - - - - - -- - - - - - -  QUARTO CAMPO - - -- - - -- --- - -- - -- -- -- -#
    titulo_novo, texto_novo, url = scrape.coleta_resumo(flag + 6)

    html_content = html_content.replace('titulo4', titulo_novo)
    html_content = html_content.replace('texto4', texto_novo)
    html_content = html_content.replace('link4', url)

    with open('HTML/exemplo.html', 'w',encoding='utf-8') as file:
        file.write(html_content)
      #  - - - - - - - - - -- - - - - - -- - - - - - -  QUARTO CAMPO - - -- - - -- --- - -- - -- -- -- -#
    return()
