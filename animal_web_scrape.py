import requests
from bs4 import BeautifulSoup
import json

url = "https://a-z-animals.com/animals/"

# that url has urls of animals that have the actual data
# found in common: all href links are children of elements with a class of "list-item col-md-4 col-sm-6"
#ex. link: https://a-z-animals.com/animals/yellow-aphids/

res = requests.get(url)

text = res.text
soup = BeautifulSoup(text, features="html.parser")

parentList = soup.find_all("li",class_="list-item col-md-4 col-sm-6")
# print(parentList[1].contents)
for i, data in enumerate(parentList):

    animalUrl = parentList[i].contents[0].get('href')

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
    # photoCredit = animalSoup.find('cite').contents[0]
    # photoUrl = animalSoup.find('cite').contents[1].get('href')
    # animalFacts = animalSoup.find('dl', class_="row", attrs={"title": f'{animalName} Facts'}).find_all('div', class_="row")
    # animalChar = animalSoup.find('dl', class_="row", attrs={"title": f'{animalName} Physical Characteristics'}).find_all('dd')
    animalClass["name"] = animalSoup.find('article', class_="type-animals").get('aria-label')
    # animalGenFacts["diet"] = animalSoup.find('a', string="Diet").parent.next_sibling.string

    def setGenAttr(str, animalAttr):
        animalGenFacts = animalClass["general_facts"]
        try:
            if animalSoup.find('a', string=f'{str}').parent:

                animalGenFacts[f'{animalAttr}'] = animalSoup.find('a', string=f'{str}').parent.next_sibling.string
            else: 
                animalGenFacts[f'{animalAttr}'] = ""

        except(AttributeError):
            animalGenFacts[f'{animalAttr}'] = ""

    # def setPhoto():
    #     animalPhotos = animalClass["photo"]["image"]
        
    #     try:
    #         if animalSoup.find('cite', class_="text-white font-weight-light").parent:
    #             print(animalSoup.find('a', string="text-white font-weight-light").parent)
    #             print("IN PHOTO")
    #             animalPhotos["image"] = animalSoup.find('a', string="text-white font-weight-light").parent.next_sibling.string
    #         else: 
    #             print("IN ELSE PHOTO")
    #             animalPhotos = ""
    #     except(AttributeError):
    #         animalPhotos = ""

    setGenAttr("Biggest Threat","biggest_threat")
    setGenAttr("Common Name","common_name")
    setGenAttr("Biggest Threat","biggest_threat")
    setGenAttr("Average Litter Size","avg_litter_size")
    setGenAttr("Location","location")
    setGenAttr("Estimated Population Size", "estimated_pop_size")
    setGenAttr("Diet", "diet")
    setGenAttr("Fun Fact", "fun_fact")
    setGenAttr("Other Name(s)", "other_names")
    setGenAttr("Most Distinctive Feature", "distinct_feat")
    setGenAttr("Habitat", "habitat")
    setGenAttr("Lifestyle", "lifestyle")
   
    # setPhoto()
      
    # animalClass["photo"]["credit"] = photoCredit
    # animalClass["photo"]["image"] = photoUrl
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


    # pretty = json.dumps(animalClass, indent=3)
    # print(pretty)
