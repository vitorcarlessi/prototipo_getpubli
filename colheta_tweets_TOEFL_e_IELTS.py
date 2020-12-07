## Autores: Grupo #GetPubli
## Objetivo 1: Autenticação com a API do twitter
## Objetivo 2: Busca de 450 tweets com a #TOEFL no twitter e posteriormente criação do arquivo TOEFL_tweets.csv com os usuários que postaram e seu tweet
## Objetivo 3: Busca de 450 tweets com a #IELTS no twitter e posteriormente criação do arquivo IELTS_tweets.csv com os usuários que postaram e seu tweet
## Objetivo 4: PRINT alertando que os arquivos foram gerado com sucesso, próximas etapas em colheta_tweets_TOEFL_e_IELTS.py
##------------------------------------------------------------------------

##<<<<<<<<<<<<<<<<<<<<<<<<<Começo do código>>>>>>>>>>>>>>>>>>>>>>>>>
##<<<<<<<<<<<<<<<<<<<<<<<<<Começo do código>>>>>>>>>>>>>>>>>>>>>>>>>
##<<<<<<<<<<<<<<<<<<<<<<<<<Começo do código>>>>>>>>>>>>>>>>>>>>>>>>>

# Bibliotecas utilizadas
import sys
import csv
import tweepy
import pandas
import json


#Keys para autenticação na API do twitter
consumerKey        = "wJsWaCxR2ismW20UpDQ8YObqV"
consumerSecret     = "8qRJTzCBqHhh5ZXBnWbODCRBLaArwzCRlZqx2Lce2N9CvYfG3c"
accessToken        = "1106181670821154817-VigfLv5XYLS3ZTR9WSFbmiwFwQBD9Q"
accessTokenSecret  = "dhdkuYTBPiE1aM6bVz7qpoRiHmhNFSAjxGYWsUtjHlqgL"

#Autenticação na API do Twitter
auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#Termo de busca será no twitter: #TOEFL
searchTerm = "#TOEFL" + "-fielter:retweets" ##Filtrando os reetwets -> não pegar o mesmo reeetweet mais de uma vez

#Tweepy.cursor irá buscar no twitter os últimos 450 twittes com a palavra #TOEFL
tweets = tweepy.Cursor(api.search, q=searchTerm, show_user = True, lang='en').items(450) 

#Criação da lista de tweets
listTweets = []

#appendando a primeira linha que saíra no .CSV, com a coluna Usuário e Tweet
row_list = [["Usuario","Tweet"]]

#percorrendo todos os tweets encontrados
for tweet in tweets:
    #appendando o nome do usuário e o tweet feito pelo mesmo na lista
    listTweets.append(list((tweet.user.screen_name, tweet.text)))

for x in listTweets:
    row_list.append(x)

#Codificações para escrever a saida no arquivo .CSV resultados.csv    
csv.register_dialect('myDialect',
                     delimiter=',',
                     quoting=csv.QUOTE_ALL)
with open('TOEFL_tweets.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerows(row_list)


#Termo de busca será no twitter será #IELTS
searchTerm = "#IELTS" + "-fielter:retweets" ##Filtrando os reetwets -> não pegar o mesmo reeetweet mais de uma vez

#Tweepy.cursor irá buscar no twitter os últimos 450 twittes com a palavra #IELTS
tweets = tweepy.Cursor(api.search, q=searchTerm, show_user = True, lang='en').items(450) 

#Criação da lista de tweets
listTweets = []

#appendando a primeira linha que saíra no .CSV, com a coluna Usuário e Tweet
row_list = [["Usuario","Tweet"]]

#percorrendo todos os tweets encontrados
for tweet in tweets:
    #appendando o nome do usuário e o tweet feito pelo mesmo na lista
    listTweets.append(list((tweet.user.screen_name, tweet.text)))

for x in listTweets:
    row_list.append(x)

#Codificações para escrever a saida no arquivo .CSV IELTS_tweets.csv    
csv.register_dialect('myDialect',
                     delimiter=',',
                     quoting=csv.QUOTE_ALL)
with open('IELTS_tweets.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerows(row_list)

#Alerta que os arquivos foram gerados com sucesso
print('Arquivos gerados com sucesso!!!')
