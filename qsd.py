from urllib import response
import requests,json

word=str(input())

api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+word

response=requests.get(api_url)

word_details = response.json()

def get_meaning(wd):
    meanings = []
    for i in range(len(wd[0]["meanings"])):
        definition = wd[0]["meanings"][i]["definitions"][0]["definition"]
        synonym = wd[0]["meanings"][i]["definitions"][0]["synonyms"]
        antonym = wd[0]["meanings"][i]["definitions"][0]["antonyms"]
        meanings.append([definition, synonym, antonym])
    return meanings

def print_definitions():
    definitions = get_meaning(word_details)
    for k in range(len(definitions)):
        print(f"{k}. \nMeaning : {definitions[k][0]} \nSynonyms : {definitions[k][1]} \nAntonyms : {definitions[k][2]}\n\n")

print_definitions()