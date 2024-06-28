from bs4 import BeautifulSoup

## Limpa ou remove elementos específicos do HTML com base na presença de certos padrões na URL e no conteúdo do HTML.
class Enhance:
    soup = BeautifulSoup(html, 'html.parser') if url.find('cpat') != -1 \
        else BeautifulSoup(html, 'lxml')

    def enhance_html(self, url, html): # recebe parâmetros para url (a URL da página) e html (o conteúdo HTML da página).

        soup = BeautifulSoup(html,'html.parser') if url.find('cpat') != -1 else BeautifulSoup(html,'lxml') #Cria um objeto BeautifulSoup para analisar o HTML.
        #Se 'cpat' estiver na URL: Usa html.parser.
        #Se 'cpat' não estiver na URL: Usa lxml.

        #Limpar elementos específicos
        if url.find('cpat') != -1: # Verifica se 'cpat' está na URL
            soup.find('div', id='navigation-primary').clear()
            soup.find('title').clear()
            soup.find('div', id="link2").clear()

        if soup.find('div', 'footer') != None: # Verifica se existe um <div> com a classe 'footer'.
            soup.find('div', 'footer').clear()

        if soup.find('div', id='copyright2') != None:
            soup.find('div', id='copyright2').clear()
            
        if soup.find('div', 'form-item form-item-email') != None:
            soup.find('div', 'form-item form-item-email').clear()

        if soup.find('section', id='alliedMaterialsArea') != None:
            soup.find('section', id='alliedMaterialsArea').clear()

        if soup.find(style="border-bottom:none; margin-bottom:0;") != None: # Verifica se existe um elemento com o estilo inline especificado.
            for element in soup.find_all(style="border-bottom:none; margin-bottom:0;"):
                element.replace_with('') # Substitui o elemento pelo texto vazio, efetivamente removendo-o.

        return soup # Retorna o objeto BeautifulSoup modificado.


    ## Determina se um atraso deve ser configurado com base na presença de um padrão específico na URL.
    def set_delay(self, url):
        string = str(url).lower() # converter a url para letras minusculas

        if string.find('arq-camp') != -1: # Verifica se 'arq-camp' está na URL.
            return True
        else:
            return False