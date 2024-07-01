OBS: em general_urls.txt é necessário que eu já tenha os links dos sites

# Resumo dos arquivo
## main.py0
O script lê URLs de um arquivo, faz requisições HTTP para cada URL, verifica se o conteúdo é HTML, busca por palavras-chave no conteúdo HTML, calcula várias pontuações com base nas palavras-chave encontradas, e armazena os resultados em uma planilha Excel. Em caso de erros durante a requisição, registra as URLs problemáticas em um arquivo separado. Também inclui um atraso aleatório entre as requisições para evitar ser bloqueado por fazer muitas requisições em um curto período de tempo.
## sheet.py
Este código define uma classe Sheet que facilita a manipulação de planilhas Excel usando o módulo openpyxl. A classe fornece métodos para configurar cabeçalhos, preencher linhas com dados específicos e salvar a planilha em um arquivo.
## score.py
Esses métodos fornecem várias formas de manipular, analisar e calcular pontuações para palavras-chave, tornando a classe Score útil para análise de texto ou dados baseados em palavras-chave.
## word.py
A classe Word é projetada para validar e categorizar palavras fornecidas:

**Validação**: word_validation compara a palavra com várias listas de termos conhecidos e padroniza a forma como essas palavras são representadas (e.g., várias maneiras de escrever 'RG' são todas mapeadas para 'rg').</br>
**Categorização**: categorize_word atribui um peso a uma palavra com base em sua presença em listas de palavras-chave pessoais ou sensíveis, facilitando a análise de severidade ou importância das palavras no contexto.
Esses métodos são úteis para garantir a consistência na análise de texto e facilitar a avaliação de palavras-chave em termos de sua importância ou sensibilidade.
## enhance.py
enhance_html: Limpa o HTML removendo elementos específicos com base em padrões na URL e no conteúdo HTML.</br>
set_delay: Determina se deve haver um atraso antes de processar a URL com base na presença de 'arq-camp' na URL.
