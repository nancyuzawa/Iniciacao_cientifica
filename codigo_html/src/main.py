import re, urllib.request, random, time
from bs4 import BeautifulSoup
from openpyxl import Workbook
from Sheet import Sheet
from Score import Score
from Enhance import Enhance

list_urls      = open('../scripts/urls/general-urls.txt')
list_keywords  = open('../scripts/keywords/keywords.txt', encoding='UTF-8').read().splitlines()
forbidden_file = open('../src/forbidden-urls.txt', 'a')
iterator       = 0
url_number     = 0
max_scrape     = 0
occurrences    = 0
row            = 2

obj_en    = Enhance()
obj_sc    = Score()
obj_sheet = Workbook()
sheet     = obj_sheet.active
ns        = Sheet('Planilha de Ocorrencias', 'planilha', obj_sheet, sheet)
ns.set_header1()
ns.save_sheet()

for url in list_urls:

    # if iterator >= max_scrape:
    #     break

    if obj_en.set_delay(url):
        delay = random.randint(0, 13)
        print('Delay: ' + str(delay))
        time.sleep(delay)

    print('Sheet: {} | N: {} | URL: {}'.format(iterator + 1, url_number + 1, url))
    boolean = False

    try:
        answer      = urllib.request.urlopen(url, timeout=5)
        http_info   = answer.info()
        contenttype = http_info.get_content_type()

        if contenttype == 'text/html':
            html = answer.read()
            soup = obj_en.enhance_html(url, html)
            string = soup.get_text(" ")
            occurrences = 0
            boolean = True
            obj_sc.clear_elements()
            aux_placeholder = re.findall('placeholder', str(soup), re.I)

            for word in list_keywords:
                lista = re.findall(r'\W' + word + r'\W', string, re.IGNORECASE)
                list_placeholder = []

                if len(aux_placeholder) > 0:
                    list_placeholder = re.findall(r'placeholder="[a-zA-Z0-9 -áàâãéèêíóôõúç]*' + r'\W' + word + r'\W', str(soup), re.I)
                
                if len(lista) > 0 or len(list_placeholder) > 0:
                    occurrences = len(lista) + len(list_placeholder)
                    obj_sc.set_dictionary(word, occurrences)

            multiply = obj_sc.calculate_score_list() * obj_sc.calculate_score_dictionary()            

            ns.readable_page1(row, url, contenttype, obj_sc.keywords_string_curtailed(), obj_sc.calculate_score_list(), obj_sc.calculate_score_dictionary(), multiply, obj_sc.calculate_by_severity(), obj_sc.calculate_weighted_avg(), obj_sc.calculate_by_simultaneity())

            ns.save_sheet()
    except urllib.error.URLError as e:
        forbidden_file.write(str(e) + ' | ' + url)
    except urllib.error.HTTPError as e:    
        forbidden_file.write(str(e) + ' | ' + url)
    except Exception as e:        
        forbidden_file.write(str(e) + ' | ' + url)
    
    if boolean:
        iterator += 1
        row      += 1
    
    url_number += 1

list_urls.close()
forbidden_file.close()