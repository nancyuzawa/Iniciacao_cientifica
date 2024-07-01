# Essa classe ategoriza palavras e valida palavras específicas.
class Word:

    # Método:  Classifica uma palavra como pessoal ou sensível com base em listas de palavras-chave carregadas de arquivos.
    def categorize_word(self, word):
        # Transforma o arquivo .txt que está um embaixo do outro em uma lista
        personal_keywords = open('scripts/keywords/personal-keywords.txt', encoding='UTF-8').read().splitlines() # splitlines() -> dividir uma string em uma lista de linhas.
        sensible_keywords = open('scripts/keywords/sensible-keywords.txt', encoding='UTF-8').read().splitlines()        
        weight = 0 #  atribui um peso à palavra, dependendo de qual lista ela pertence.

        for element in personal_keywords: # iterando sobre cada palavra em personal_keywords
            if element == word.lower(): # compara com a word convertida para minúsculas
                weight = 1
                return weight
        
        for element in sensible_keywords:
            if element == word.lower():
                weight = 3
                return weight

    # Método: Valida e categoriza uma palavra com base em várias listas de palavras-chave específicas para diferentes tipos de documentos ou termos.
    def word_validation(self, word):
        listRG = ['r\.g\.', 'registro geral', 'número do r\.g\.', 'numero do r\.g\.']
        listID = ['carteira de identidade', 'número de identidade', 'numero de identidade', 'documento de identidade']
        listCPF = ['c\.p\.f\.', 'cadastro de pessoa fisica', 'cadastro de pessoa física', 'número do c\.p\.f\.']
        listCNH = ['c\.n\.h\.', 'habilitação', 'habilitacao', 'carteira nacional de habilitação', 'carteira nacional de habilitacao', 'carteira de motorista']
        listCTPS = ['c\.t\.p\.s\.', 'carteira de trabalho', 'número da carteira de trabalho', 'numero da carteira de trabalho', 'carteira profissional']
        listAgencia = ['agencia', 'agência bancária', 'agencia bancaria', 'número da agência', 'numero da agencia']
        listEmail = ['e-mail', 'endereço eletrônico', 'endereco eletronico', 'endereço de e-mail']
        listPCD = ['p\.c\.d\.', 'pessoa com deficiência', 'pessoa com deficiencia']
        listCID = ['c\.i\.d\.', 'classificação internacional de doenças', 'classificacao internacional de doencas']
        validated_word = '' # armazenar a categoria da palavra, se ela corresponder a uma das listas acima


        # Verifica se algum valor da lista listaRG é igual a uma palavra que entrou
        # está verificando desse jeito pois há uma lista de maneiras que pode ter sido escrito
        for value in listRG:
            if word.lower() == value:
                validated_word = 'rg'
                return validated_word

        for value in listID:
            if word.lower() == value:
                validated_word = 'identidade'
                return validated_word

        for value in listCPF:
            if word.lower() == value:
                validated_word = 'cpf'
                return validated_word

        for value in listCNH:
            if word.lower() == value:
                validated_word = 'cnh'
                return validated_word            

        for value in listCTPS:
            if word.lower() == value:
                validated_word = 'ctps'
                return validated_word           

        for value in listAgencia:
            if word.lower() == value:
                validated_word = 'agência'
                return validated_word

        for value in listEmail:
            if word.lower() == value:
                validated_word = 'email'
                return validated_word

        for value in listPCD:
            if word.lower() == value:
                validated_word = 'pcd'
                return validated_word

        for value in listCID:
            if word.lower() == value:
                validated_word = 'cid'
                return validated_word

        # Verifica word contra vários outros termos específicos e define validated_word para valores apropriados
        if word.lower() == 'número do documento' or word.lower() == 'numero do documento':
            validated_word = 'documento'
        elif word.lower() == 'titulo de eleitor' or word.lower() == 'número do título de eleitor' or word.lower() == 'numero do título de eleitor':
            validated_word = 'título de eleitor'
        elif word.lower() == 'passport' or word.lower() == 'número do passaporte' or word.lower() == 'numero do passaporte':
            validated_word = 'passaporte'
        elif word.lower() == 'p\.i\.s\.' or word.lower() == 'número do pis' or word.lower() == 'numero do pis':
            validated_word = 'pis'
        elif word.lower() == 'responsavel legal' or word.lower() == 'nome do responsável legal':
            validated_word = 'responsável legal'
        elif word.lower() == 'inscricao municipal':
            validated_word = 'inscrição municipal'
        elif word.lower() == 'inscricao estadual':
            validated_word = 'inscrição estadual'
        elif word.lower() == 'viuvo':
            validated_word = 'viúvo'
        elif word.lower() == 'uniao estavel':
            validated_word = 'união estável'
        elif word.lower() == 'genero':
            validated_word = 'gênero'
        elif word.lower() == 'conjuge' or word.lower() == 'nome do cônjuge' or word.lower() == 'nome do conjuge':
            validated_word = 'cônjuge'
        elif word.lower() == 'nome do companheiro':
            validated_word = 'companheiro'
        elif word.lower() == 'nome do pai':
            validated_word = 'pai'
        elif word.lower() == 'mae' or word.lower() == 'nome da mãe' or word.lower() == 'nome da mae':
            validated_word = 'mãe'
        elif word.lower() == 'nome dos filhos':
            validated_word = 'filhos'
        elif word.lower() == 'poupanca':
            validated_word = 'poupança'
        elif word.lower() == 'conta corrente':
            validated_word = 'conta-corrente'
        elif word.lower() == 'conta salario':
            validated_word = 'conta salário'
        elif word.lower() == 'conta universitario':
            validated_word = 'conta universitário'
        elif word.lower() == 'f\.g\.t\.s\.' or word.lower() == 'número do fgts' or word.lower() == 'numero do fgts':
            validated_word = 'fgts'
        elif word.lower() == 'remuneracao':
            validated_word = 'remuneração'
        elif word.lower() == 'salario':
            validated_word = 'salário'
        elif word.lower() == 'salario-minimo':
            validated_word = 'salário-mínimo'
        elif word.lower() == 'bonus':
            validated_word = 'bônus'
        elif word.lower() == 'beneficios':
            validated_word = 'benefícios'
        elif word.lower() == 'auxilio':
            validated_word = 'auxílio'
        elif word.lower() == 'carga horaria':
            validated_word = 'carga horária'
        elif word.lower() == 'horario de trabalho':
            validated_word = 'horário de trabalho'
        elif word.lower() == 'profissao':
            validated_word = 'profissão'
        elif word.lower() == 'ocupacao':
            validated_word = 'ocupação'
        elif word.lower() == 'número de telefone' or word.lower() == 'numero de telefone':
            validated_word = 'telefone'
        elif word.lower() == 'número de celular' or word.lower() == 'numero de celular':
            validated_word = 'celular'
        elif word.lower() == 'domicilio':
            validated_word = 'domicílio'
        elif word.lower() == 'residencia':
            validated_word = 'residência'
        elif word.lower() == 'proprio':
            validated_word = 'próprio'
        elif word.lower() == 'endereco':
            validated_word = 'endereço'
        elif word.lower() == 'u\.f\.' or word.lower() == 'unidade federativa':
            validated_word = 'uf'
        elif word.lower() == 'formacao':
            validated_word = 'formação'
        elif word.lower() == 'ensino medio':
            validated_word = 'ensino médio'
        elif word.lower() == 'graduacao':
            validated_word = 'graduação'
        elif word.lower() == 'pos-graduacao':
            validated_word = 'pós-graduação'
        elif word.lower() == 'estagio':
            validated_word = 'estágio'
        elif word.lower() == 'c\.l\.t\.' or word.lower() == 'celetista':
            validated_word = 'clt'
        elif word.lower() == 'estatuario':
            validated_word = 'estatuário'
        elif word.lower() == 'temporario':
            validated_word = 'temporário'
        elif word.lower() == 'estagiario':
            validated_word = 'estagiário'
        elif word.lower() == 'pessoa juridica':
            validated_word = 'pessoa jurídica'
        elif word.lower() == 'autonomo':
            validated_word = 'autônomo'
        elif word.lower() == 'localizacao':
            validated_word = 'localização'
        elif word.lower() == 'raca':
            validated_word = 'raça'
        elif word.lower() == 'indigena':
            validated_word = 'indígena'
        elif word.lower() == 'orientacao sexual':
            validated_word = 'orientação sexual'
        elif word.lower() == 'religiao':
            validated_word = 'religião'
        elif word.lower() == 'fe':
            validated_word = 'fé'
        elif word.lower() == 'catolica':
            validated_word = 'católica'
        elif word.lower() == 'evangelica':
            validated_word = 'evangélica'
        elif word.lower() == 'candomble':
            validated_word = 'candomblé'
        elif word.lower() == 'espirita':
            validated_word = 'espírita'
        elif word.lower() == 'hinduismo':
            validated_word = 'hinduísmo'
        elif word.lower() == 'muculmana':
            validated_word = 'muçulmana'
        elif word.lower() == 'judaismo':
            validated_word = 'judaísmo'
        elif word.lower() == 'igreja messianica mundial':
            validated_word = 'igreja messiânica mundial'
        elif word.lower() == 'religioes orientais':
            validated_word = 'religiões orientais'
        elif word.lower() == 'testemunhas de jeova':
            validated_word = 'testemunhas de jeová'
        elif word.lower() == 'tradicoes esotericas':
            validated_word = 'tradições esotéricas'
        elif word.lower() == 'tradicoes indigenas':
            validated_word = 'tradições indígenas'
        elif word.lower() == 'religiao afrobrasileira':
            validated_word = 'religião afrobrasileira'
        elif word.lower() == 'cristas':
            validated_word = 'cristãs'
        elif word.lower() == 'partido politico':
            validated_word = 'partido político'
        elif word.lower() == 'conviccao politica':
            validated_word = 'convicção política'
        elif word.lower() == 'posicionamento politico':
            validated_word = 'posicionamento político'
        elif word.lower() == 'filiacao politica':
            validated_word = 'filiação política'
        elif word.lower() == 'filiacao partidaria':
            validated_word = 'filiação partidária'
        elif word.lower() == 'movimento democrático brasileiro' or word.lower() == '\(mdb\)':
            validated_word = '(mdb)'
        elif word.lower() == 'partido dos trabalhadores' or word.lower() == '\(pt\)':
            validated_word = '(pt)'
        elif word.lower() == 'partido da social democracia brasileira' or word.lower() == '\(pdsb\)':
            validated_word = '(psdb)'
        elif word.lower() == 'progressistas' or word.lower() == '\(pp\)':
            validated_word = '(pp)'
        elif word.lower() == 'partido democrático trabalhista' or word.lower() == '\(pdt\)':
            validated_word = '(pdt)'
        elif word.lower() == 'partido trabalhista brasileiro' or word.lower() == '\(ptb\)':
            validated_word = '(ptb)'
        elif word.lower() == 'democratas' or word.lower() == '\(dem\)':
            validated_word = '(dem)'
        elif word.lower() == 'partido liberal' or word.lower() == '\(pl\)':
            validated_word = '(pl)'
        elif word.lower() == 'partido socialista brasileiro' or word.lower() == '\(psb\)':
            validated_word = '(psb)'
        elif word.lower() == 'partido social liberal' or word.lower() == '\(psl\)':
            validated_word = '(psl)'
        elif word.lower() == 'partido social cristão' or word.lower() == '\(psc\)':
            validated_word = '(psc)'
        elif word.lower() == '\(republicanos\)':
            validated_word = '(republicanos)'
        elif word.lower() == '\(cidadania\)':
            validated_word = '(cidadania)'
        elif word.lower() == 'partido comunista do brasil' or word.lower() == 'pc do b' or word.lower() == '\(pcdob\)':
            validated_word = '(pcdob)'
        elif word.lower() == 'podemos' or word.lower() == '\(pode\)':
            validated_word = '(pode)'
        elif word.lower() == 'partido social democrático' or word.lower() == '\(psd\)':
            validated_word = '(psd)'
        elif word.lower() == 'partido verde' or word.lower() == '\(pv\)':
            validated_word = '(pv)'
        elif word.lower() == '\(patriota\)':
            validated_word = '(patriota)'
        elif word.lower() == '\(solidariedade\)' or word.lower() == '\(sd\)':
            validated_word = '(sd)'
        elif word.lower() == 'partido da mobilização nacional' or word.lower() == '\(pmn\)':
            validated_word = '(pmn)'
        elif word.lower() == '\(avante\)':
            validated_word = '(avante)'
        elif word.lower() == 'partido trabalhista cristão' or word.lower() == '\(ptc\)':
            validated_word = '(ptc)'
        elif word.lower() == 'partido socialismo e liberdade' or word.lower() == '\(psol\)':
            validated_word = '(psol)'
        elif word.lower() == 'democracia cristã' or word.lower() == '\(psdc\)' or word.lower() == '\(dc\)':
            validated_word = '(dc)'
        elif word.lower() == 'partido renovador trabalhista brasileiro' or word.lower() == '\(prtb\)':
            validated_word = '(prtb)'
        elif word.lower() == 'partido republicano da ordem social' or word.lower() == '\(pros\)':
            validated_word = '(pros)'
        elif word.lower() == 'partido da mulher brasileira' or word.lower() == '\(pmb\)':
            validated_word = '(pmb)'
        elif word.lower() == 'partido novo' or word.lower() == '\(novo\)':
            validated_word = '(novo)'
        elif word.lower() == 'rede sustentabilidade' or word.lower() == '\(rede\)':
            validated_word = '(rede)'
        elif word.lower() == 'partido socialista dos trabalhadores unificado' or word.lower() == '\(pstu\)':
            validated_word = '(pstu)'
        elif word.lower() == 'partido comunista brasileiro' or word.lower() == '\(pcb\)':
            validated_word = '(pcb)'
        elif word.lower() == 'partido da causa operária' or word.lower() == '\(pco\)':
            validated_word = '(pco)'
        elif word.lower() == 'unidade popular' or word.lower() == '\(up\)':
            validated_word = '(up)'
        elif word.lower() == 'partido republicano progressista' or word.lower() == '\(prp\)':
            validated_word = '(prp)'
        elif word.lower() == 'partido ecológico nacional' or word.lower() == '\(pen\)':
            validated_word = '(pen)'
        elif word.lower() == 'partido republicano brasileiro' or word.lower() == '\(prb\)':
            validated_word = '(prb)'
        elif word.lower() == 'partido pátria livre' or word.lower() == '\(ppl\)':
            validated_word = '(ppl)'
        elif word.lower() == 'partido humanista da solidariedade' or word.lower() == '\(phs\)':
            validated_word = '(phs)'
        elif word.lower() == 'partido trabalhista do brasil' or word.lower() == 'pt do b' or word.lower() == '\(pt do b\)':
            validated_word = '(ptdob)'
        elif word.lower() == 'partido de reedificação da ordem nacional' or word.lower() == '\(prona\)':
            validated_word = '(prona)'
        elif word.lower() == 'partido dos aposentados da nação' or word.lower() == '\(pan\)':
            validated_word = '(pan)'
        elif word.lower() == 'partido progressista brasileiro' or word.lower() == '\(ppb\)':
            validated_word = '(ppb)'
        elif word.lower() == 'partido da reconstrução nacional' or word.lower() == '\(prn\)':
            validated_word = '(prn)'
        elif word.lower() == 'partido da frente liberal' or word.lower() == '\(pfl\)':
            validated_word = '(pfl)'
        elif word.lower() == 'partido geral dos trabalhadores' or word.lower() == '\(pgt\)':
            validated_word = '(pgt)'
        elif word.lower() == 'partido municipalista brasileiro' or word.lower() == '\(pmr\)':
            validated_word = '(pmr)'
        elif word.lower() == 'partido social trabalhista' or word.lower() == '\(pst\)':
            validated_word = '(pst)'
        elif word.lower() == 'posicionamento filosofico':
            validated_word = 'posicionamento filosófico'
        elif word.lower() == 'conviccao filosofica':
            validated_word = 'convicção filosófica'
        elif word.lower() == 'tipo sanguineo':
            validated_word = 'tipo sanguíneo'
        elif word.lower() == 'genetica':
            validated_word = 'genética'
        elif word.lower() == 'cadastro biometrico':
            validated_word = 'cadastro biométrico'
        elif word.lower() == 'licenca':
            validated_word = 'licença'
        elif word.lower() == 'filiacao sindical':
            validated_word = 'filiação sindical'

        # Se validated_word ainda for uma string vazia (ou seja, não houve correspondência),
        # define validated_word como a word original.
        if validated_word == '':
            validated_word = word

        # Retorna o valor de validated_word, que será a palavra categorizada ou validada.
        return validated_word
