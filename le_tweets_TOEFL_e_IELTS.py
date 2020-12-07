## Autores: Grupo #GetPubli
## Objetivo 1: Upload dos CSVs TOEFL_tweets.csv e IELTS_tweets.csv
## Objetivo 2: Criação da coluna Sentimento com a avaliação de Positivo, Neutro ou Negativo
## Objetivo 3: Criação da coluna Subjetividade com a avalição de Subjetivo, Neutro ou Objetivo
## Objetivo 3: Contagem de Sentimentos   Positivos, Neutros   e Negativos em cada .csv
## Objetivo 4: Contagem de Subjetividade Subjetivda, Objetiva e Neutra em cada .csv
## Objetivo 4: Classificação de qual é o melhor falado no twitter diante das análises
## Objetivo 5: Apresentação dos resultados em tela ao usuário pelo comando PRINT
##------------------------------------------------------------------------

## Informações importantes da biblíoteca TextBlob que será explorada ao longo do código
##<<<<<<<<<<<<<<<<<<<<<<<Polaridade>>>>>>>>>>>>>>>>>>>>>>>>>>>>
##Segundo a documentação: "The polarity score is a float within the range [-1.0, 1.0]"
##       polaridade negativa     = Negativo
##       polaridade igual a zero = Neutro
##       polaridade positiva     = Positivo
##<<<<<<<<<<<<<<<<<<<<<<<Polaridade>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          
##<<<<<<<<<<<<<<<<<<<<<<<Subjetividade>>>>>>>>>>>>>>>>>>>>>>>>>>>>
##Segundo a documentação: "The subjectivity is a float within the range [0.0, 1.0] where 
##0.0 is very objective and 1.0 is very subjective."
##       subjetividade < 0.5        = Objetivo
##       subjetividade igual a zero = Neutro
##       subjetividade > 0.5        = Subjetivo
##<<<<<<<<<<<<<<<<<<<<<<<Subjetividade>>>>>>>>>>>>>>>>>>>>>>>>>>>>

##<<<<<<<<<<<<<<<<<<<<<<<<<Começo do código>>>>>>>>>>>>>>>>>>>>>>>>>
##<<<<<<<<<<<<<<<<<<<<<<<<<Começo do código>>>>>>>>>>>>>>>>>>>>>>>>>
##<<<<<<<<<<<<<<<<<<<<<<<<<Começo do código>>>>>>>>>>>>>>>>>>>>>>>>>

# Bibliotecas utilizadas
import numpy                       as np
import pandas                      as pd
from   textblob.classifiers    import NaiveBayesClassifier
from   sklearn.model_selection import train_test_split
from   sklearn.tree            import DecisionTreeClassifier
from   sklearn.linear_model    import LogisticRegression
from   sklearn.linear_model    import LinearRegression
from   sklearn.naive_bayes     import MultinomialNB
from   sklearn                 import metrics
from   textblob                import TextBlob


## Carregando os dados dos arquivos gerados TOEFL_tweets.csv e IELTS_tweets.csv
##Arquivo TOEFL_tweets.csv
dataset_TOEFL = pd.read_csv('TOEFL_tweets.csv')

##Arquivo IELTS_tweets.csv
dataset_IELTS = pd.read_csv('IELTS_tweets.csv')



##Declarações de variáveis para classificações de TOEFL e IELTS
##Variáveis TOEFL
positive_TOEFL          = 0
negative_TOEFL          = 0
neutral_TOEFL           = 0
sub_neutral_TOEFL       = 0
sub_objective_TOEFL     = 0
sub_subjectivity_TOEFL  = 0 


##Variáveis IELTS
positive_IELTS          = 0
negative_IELTS          = 0
neutral_IELTS           = 0
sub_neutral_IELTS       = 0
sub_objective_IELTS     = 0
sub_subjectivity_IELTS  = 0


## Insere a coluna Sentimento e coloca como resultado Não Classificado nos arquivos.
##Coluna sentimento no dataset_TOEFL
dataset_TOEFL['Sentimento']    = 'Não classificado'

##Coluna sentimento no dataset_IELTS
dataset_IELTS['Sentimento']    = 'Não classificado'

##Coluna subjetividade no dataset_TOEFL
dataset_TOEFL['Subjetividade'] = 'Não classificado'

##Coluna subjetividade no dataset_IELTS
dataset_IELTS['Subjetividade'] = 'Não classificado'


## Lógica para avaliar o sentimento como Positivo, Neutro ou Negativo no arquivo TOEFL_tweets
for index, row in dataset_TOEFL.iterrows():
    analysis        =  TextBlob(row['Tweet'])
    #Classificação de Polaridade -> TOEFL 
    if (analysis.sentiment.polarity == 0):
        dataset_TOEFL.loc[index, 'Sentimento'] = 'Neutro'
        neutral_TOEFL = neutral_TOEFL + 1
    elif (analysis.sentiment.polarity < 0):
        dataset_TOEFL.loc[index, 'Sentimento'] = 'Negativo'
        negative_TOEFL = negative_TOEFL + 1
    elif (analysis.sentiment.polarity > 0):
        dataset_TOEFL.loc[index, 'Sentimento'] = 'Positivo'
        positive_TOEFL = positive_TOEFL + 1
    
    ## Lógica para avaliar a subjetividade como Neutro, Objetivo ou Subjetivo no arquivo TOEFL_tweets
    #Classificação de Subjetividade -> TOEFL 
    if     (analysis.sentiment.subjectivity == 0.5):
        dataset_TOEFL.loc[index, 'Subjetividade'] = 'Neutro'
        sub_neutral_TOEFL = sub_neutral_TOEFL + 1
    elif   (analysis.sentiment.subjectivity < 0.5):
        dataset_TOEFL.loc[index, 'Subjetividade'] = 'Objetivo'
        sub_objective_TOEFL = sub_objective_TOEFL + 1
    elif (analysis.sentiment.subjectivity > 0.5):
        dataset_TOEFL.loc[index, 'Subjetividade'] = 'Subjetivo'
        sub_subjectivity_TOEFL = sub_subjectivity_TOEFL + 1


## Lógica para avaliar o sentimento como Positivo, Neutro ou Negativo no arquivo IELTS_tweets
for index, row in dataset_IELTS.iterrows():
    analysis        =  TextBlob(row['Tweet'])
    #Classificação de Polaridade -> IELTS
    if (analysis.sentiment.polarity == 0):
        dataset_IELTS.loc[index, 'Sentimento'] = 'Neutro'
        neutral_IELTS = neutral_IELTS + 1
    elif (analysis.sentiment.polarity < 0):
        dataset_IELTS.loc[index, 'Sentimento'] = 'Negativo'
        negative_IELTS = negative_IELTS + 1
    elif (analysis.sentiment.polarity > 0):
        dataset_IELTS.loc[index, 'Sentimento'] = 'Positivo'
        positive_IELTS = positive_IELTS + 1
    
    ## Lógica para avaliar a subjetividade como Neutro, Objetivo ou Subjetivo no arquivo IELTS_tweets
    #Classificação de Subjetividade -> IELTS
    if     (analysis.sentiment.subjectivity == 0.5):
        dataset_IELTS.loc[index, 'Subjetividade'] = 'Neutro'
        sub_neutral_IELTS = sub_neutral_IELTS + 1
    elif   (analysis.sentiment.subjectivity < 0.5):
        dataset_IELTS.loc[index, 'Subjetividade'] = 'Objetivo'
        sub_objective_IELTS = sub_objective_IELTS + 1
    elif (analysis.sentiment.subjectivity > 0.5):
        dataset_IELTS.loc[index, 'Subjetividade'] = 'Subjetivo'
        sub_subjectivity_IELTS = sub_subjectivity_IELTS + 1


##Lógica para comparação da melhor opção
if (positive_IELTS == positive_TOEFL) and (negative_IELTS < negative_TOEFL):
    melhor_opcao = 'IELTS'

if (positive_IELTS == positive_TOEFL) and (negative_TOEFL < negative_IELTS):
    melhor_opcao = 'TOEFL'


if (positive_IELTS > positive_TOEFL):
    melhor_opcao = 'IELTS'
else:
    melhor_opcao = 'TOEFL'



##Exibição dos valores encontrados
##Exame IELTS
print("---------------------Exame IELTS---------------------")
print('Quanto a polaridade: ')
print('O número de tweets positivos  em IELTS_tweets.csv é: ', positive_IELTS)
print('O número de tweets negativos  em IELTS_tweets.csv é: ', negative_IELTS)
print('O número de tweets neutros    em IELTS_tweets.csv é: ', neutral_IELTS)
print('Quanto a subjetividade: ')
print('O número de tweets subjetivos em IELTS_tweets.csv é: ', sub_subjectivity_IELTS)
print('O número de tweets objetivos  em IELTS_tweets.csv é: ', sub_objective_IELTS)
print('O número de tweets neutros    em IELTS_tweets.csv é: ', sub_neutral_IELTS)
print("---------------------Exame IELTS---------------------")

##Exame TOEFL
print("---------------------Exame TOEFL---------------------")
print('Quanto a polaridade: ')
print('O número de tweets positivos  em TOEFL_tweets.csv é: ', positive_TOEFL)
print('O número de tweets negativos  em TOEFL_tweets.csv é: ', negative_TOEFL)
print('O número de tweets neutros    em TOEFL_tweets.csv é: ', neutral_TOEFL)
print('Quanto a subjetividade: ')
print('O número de tweets subjetivos em TOEFL_tweets.csv é: ', sub_subjectivity_TOEFL)
print('O número de tweets objetivos  em TOEFL_tweets.csv é: ', sub_objective_TOEFL)
print('O número de tweets neutros    em TOEFL_tweets.csv é: ', sub_neutral_TOEFL)
print("---------------------Exame TOEFL---------------------")


##Resultado da comparação
print("---------------------Resultado-----------------------")
if   melhor_opcao == 'IELTS':
    print("O Exame IELTS é o melhor conceituado no Twitter!!", 
          "\nTem", positive_IELTS, "tweets positivos,", negative_IELTS, "tweets negativos", "e", neutral_IELTS, "tweets neutros",
          "\nQuanto a subjetividade, tem ", sub_subjectivity_IELTS, "tweets subjetivos,", sub_objective_IELTS, "tweets objetivos", "e", sub_neutral_IELTS, "tweets neutros",
          "\nO segundo colocado é o exame TOEFL",
          "\nTem", positive_TOEFL, "tweets positivos,", negative_TOEFL, "tweets negativos", "e", neutral_TOEFL, "tweets neutros"
          "\nQuanto a subjetividade, tem ", sub_subjectivity_TOEFL, "tweets subjetivos,", sub_objective_TOEFL, "tweets objetivos", "e", sub_neutral_TOEFL, "tweets neutros",
          ),          
elif melhor_opcao == 'TOEFL':
    print("O Exame TOEFL é o melhor conceituado no Twitter!!", 
          "\nTem", positive_TOEFL, "tweets positivos,", negative_TOEFL, "tweets negativos", "e", neutral_TOEFL, "tweets neutros"
          "\nQuanto a subjetividade, tem ", sub_subjectivity_TOEFL, "tweets subjetivos,", sub_objective_TOEFL, "tweets objetivos", "e", sub_neutral_TOEFL, "tweets neutros",
          "\nO segundo colocado é o exame IELTS",
          "\nTem", positive_IELTS, "tweets positivos,", negative_IELTS, "tweets negativos", "e", neutral_IELTS, "tweets neutros"
          "\nQuanto a subjetividade, tem ", sub_subjectivity_IELTS, "tweets subjetivos,", sub_objective_IELTS, "tweets objetivos", "e", sub_neutral_IELTS, "tweets neutros",
          )
print("---------------------Resultado-----------------------")