from pathlib import Path

from bs4 import BeautifulSoup

flag = 0
while flag == 0:
    pars_file_name = input("Укажите путь к файлу с расширением .html: ")
    if not Path(pars_file_name).exists():
        print("\nПуть Не существует\n")
    else:
        flag += 1

with open(pars_file_name, encoding="utf8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

coordinates_links = soup.find_all(
    class_="search-snippet-view__body _type_business")


def creating_coordinates_list():
    coordinates_list = []
    for link in coordinates_links:
        coordinates_list.append(link.get("data-coordinates"))

    return coordinates_list


adress_links = soup.find_all(
    "div", class_="search-business-snippet-view__address")


def creating_adresses_list():
    adresses_list = []
    for item in adress_links:
        adresses_list.append(item.text)

    adresses_list_mod = []
    for item in adresses_list:
        adress = item.rsplit()
        adresses_list_mod.append(' '.join(adress))

    return adresses_list_mod
