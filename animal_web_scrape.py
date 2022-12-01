import requests
from bs4 import BeautifulSoup

url = "https://a-z-animals.com/animals/"

# that url has urls of animals that have the actual data
# found in common: all href links are children of elements with a class of "list-item col-md-4 col-sm-6"
#ex. link: https://a-z-animals.com/animals/yellow-aphids/

res = requests.get(url)

text = res.text
soup = BeautifulSoup(text, features="html.parser")

parentList = soup.find("li",class_="list-item col-md-4 col-sm-6")

animalUrl = parentList.contents[0].get('href')

animalPage = requests.get(animalUrl)

animalText = animalPage.text
animalSoup = BeautifulSoup(animalText, features="html.parser")

animalClass = {
    "name": "",
    "classifications": {
        "kingdom": "",
        "phylum": "",
        "class": "",
        "order": "",
        "family": "",
        "genus": "",
        "scientific_name": ""
    },
    "general_facts": {
        "prey": "",
        "name_of_young": "",
        "group_behavior": "",
        "fun_fact": "",
        "estimated_pop_size": "",
        "biggest_threat": "",
        "distinct_feat": "",
        "other_names": "",
        "habitat": "",
        "diet": "",
        "avg_litter_size": "",
        "lifestyle": "",
        "common_name": "",
        "num_of_species": "",
        "location": ""
    },
    "top_speed": "",
    "lifespan": "",
    "weight": "",
    "length": "",
    "photo": {
        "credit": "",
        "image": ""
    } 
}

classData = animalSoup.find_all('dd', class_="col-sm-9")
animalName = animalSoup.find('article', class_="type-animals").get('aria-label')
photoCredit = animalSoup.find('cite').contents[0]
photoUrl = animalSoup.find('cite').contents[1].get('href')
animalFacts = animalSoup.find('dl', class_="row", attrs={"title": f'{animalName} Facts'}).find_all('div', class_="row")
animalChar = animalSoup.find('dl', class_="row", attrs={"title": f'{animalName} Physical Characteristics'}).find_all('dd')

animalClass["name"] = animalName
animalClass["photo"]["credit"] = photoCredit
animalClass["photo"]["image"] = photoUrl

animalClassification = animalClass["classifications"]
for i, data in enumerate(classData):
    if i == 0:
        animalClassification["kingdom"] = classData[i].string
    elif i == 1:
        animalClassification["phylum"] = classData[i].string
    elif i == 2:
        animalClassification["class"] = classData[i].string
    elif i == 3:        
        animalClassification["order"] = classData[i].string
    elif i == 4:
        animalClassification["family"] = classData[i].string
    elif i == 5:
        animalClassification["genus"] = classData[i].string
    elif i == 6:
        animalClassification["scientific_name"] = classData[i].string

animalGenFacts = animalClass["general_facts"]
factsOne = animalFacts[0].find_all('dd');
for i, data in enumerate(factsOne):

    if i == 0:
        animalGenFacts["prey"] = factsOne[i].string
    elif i == 1:
        animalGenFacts["name_of_young"] = factsOne[i].string
    elif i == 2:
        animalGenFacts["group_behavior"] = factsOne[i].string
    elif i == 3:        
        animalGenFacts["fun_fact"] = factsOne[i].string
    elif i == 4:
        animalGenFacts["estimated_pop_size"] = factsOne[i].string
    elif i == 5:
        animalGenFacts["biggest_threat"] = factsOne[i].string
    elif i == 6:
        animalGenFacts["distinct_feat"] = factsOne[i].string
    elif i == 7:
        animalGenFacts["other_names"] = factsOne[i].string

factsTwo = animalFacts[1].find_all('dd');
for i, data in enumerate(factsTwo):
    if i == 0:
        animalGenFacts["habitat"] = factsTwo[i].string
    elif i == 1:
        animalGenFacts["diet"] = factsTwo[i].string
    elif i == 2:
        animalGenFacts["avg_litter_size"] = factsTwo[i].string
    elif i == 3:        
        animalGenFacts["lifestyle"] = factsTwo[i].string
    elif i == 4:
        animalGenFacts["common_name"] = factsTwo[i].string
    elif i == 5:
        animalGenFacts["num_of_species"] = factsTwo[i].string
    elif i == 6:
        animalGenFacts["location"] = factsTwo[i].string

for i, data in enumerate(animalChar):
    if i == 2:
        animalClass["top_speed"] = animalChar[i].string
    elif i == 3:
        animalClass["lifespan"] = animalChar[i].string
    elif i == 4:
        animalClass["weight"] = animalChar[i].string
    elif i == 5:        
        animalClass["length"] = animalChar[i].string

print(animalClass)
