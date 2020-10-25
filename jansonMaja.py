'''zad 42
Skopiuj listę pracowników z zadania 41 i wklej ją do pliku. Wczytaj plik i oblicz średnią pensję dla
pracowników w ﬁrmie.
Dołącz wyliczoną pensję do obiektu (do każdej ﬁrmy) i zapisz tak zmienione dane jako JSON w
innym pliku.'''

import json
from pprint import pprint
from statistics import mean

# with open("file.json", encoding='utf-8') as json_file:
#     data = json.load(json_file)  # dict
# data is now a Python object and can be modified
# pprint(data)
# pprint(type(data))

with open("file.json", encoding='utf-8') as json_file:
    data = json.load(json_file)

avg_salaries = {}
for shop, employees in data.items():
    salaries = []
    for employee in employees:
        salaries.append(employee['salary'])
        avg_salary = round(mean(salaries))
        avg_salaries[shop] = avg_salary
print(avg_salaries)

with open("save.json", "w", encoding='utf-8') as json_file:
    json.dump(avg_salaries, json_file, ensure_ascii=False)

# for shop,epmpoyees in data.items():
#    average_salaty=mean(employee['salary'] for employee in employees)
#    for employee in epmpoyees:
#        employee['average_salary']=average_salaty
#     # salary = []
#     for employee in epmpoyees:



'''for shop,epmpoyees in data.items():
    pensja = []
    print(shop,epmpoyees)
    for dane in epmpoyees:
        print(dane)
        
        for zmienna,wartosc in dane.items():
            # print(zmienna)
            # print(wartosc)

            if zmienna=="salary":
                # print(wartosc)
                pensja.append(wartosc)
                print(pensja)
'''



# print(data['Biedronka'])
# for employ in data['Biedronka']:
#     print(employ['salary'])

data = str(data)
# print(data)

with open("save.json", "w", encoding='utf-8') as json_file:  # wsadzanie dopliku save.json
    json.dump(data, json_file, ensure_ascii=False)  #(ensure_ascii=False)=można zapisać polskie znaki

    # data_json=json.dumps(data)
    # json.dumps(data_json,json_file)
