from Word import Word

class Score:

    def __init__(self):
        self.keywords_dic = {}
        self.keywords     = []
        self.list_aux     = []

    def clear_elements(self):
        self.keywords_dic.clear()
        self.keywords.clear()
        self.list_aux.clear()

    def get_list(self):
        return self.keywords

    def set_list(self, kw):
        self.keywords.append(kw)    

    def get_dictionary(self):
        return self.keywords_dic

    def set_dictionary(self, kw, occurrences):
        self.keywords_dic[kw] = occurrences

    def return_list(self):
        return self.list_aux

    def curtail_dictionary(self):        
        aux_dic = {}
        dic     = self.get_dictionary()
        wd      = Word()

        for key in dic:
            word = wd.word_validation(key)
            occu = dic[key]

            if word in aux_dic:
                aux_dic[word] += occu
            else:
                aux_dic[word] = occu
        
        return aux_dic

    def curtail_list(self):
        aux_list = []
        dic      = self.curtail_dictionary()

        for key in dic:
            aux_list.append(key)

        return aux_list

    def keywords_string_curtailed(self):
        dictionary = self.curtail_dictionary()
        string = ''    

        for key, occu in dictionary.items():
            string += key + ' (' + str(occu) + ') | '

        return string

    def calculate_score_list(self):         #Pontuação baseada no nº de keywords
        return len(self.curtail_list())

    def calculate_score_dictionary(self):   #Pontuação baseada no nº de ocorrências de todas as KWS!
        counter = 0

        for value in self.keywords_dic.values():
            counter += value

        return counter

    def calculate_weighted_avg(self):       #Calculo da média ponderada
        dic      = self.get_dictionary()
        wd       = Word()
        dividend = 0
        divisor  = 0
        avg      = 0

        if len(dic) > 0:
            for key, occurrences in dic.items():
                validated  = wd.word_validation(key)
                weight     = wd.categorize_word(validated)

                dividend += weight * occurrences
                divisor  += occurrences
            
            avg = dividend / divisor
                
        return avg

    def calculate_by_severity(self):        #Pontuação baseada na "severidade" de cada palavra
        dic     = self.curtail_dictionary()        
        counter = 0
        weight  = 0
        wd      = Word()

        for key, occurrences in dic.items():
            validated  = wd.word_validation(key)
            weight     = wd.categorize_word(validated)
            counter   += occurrences * weight

        return counter

    def calculate_by_simultaneity(self):    #Pontuação baseada na simultaneidade de palavras
        keywords = self.curtail_list()
        parameter = ['documento', 'cpf', 'rg', 'cnh', 'nome', 'endereço', 'email', 'telefone', 'celular', 'pessoa jurídica', 'endereço', 'cep', 'cidade']
        counter = 0
        
        for kw in keywords:
            for p in parameter:
                if kw == p:
                    counter += 1
        
        if counter >= 8:
            return 'Max'
        elif counter >= 4:
            return 'Med'
        elif counter >= 1:
            return 'Min'
        else:
            return 'Useless'