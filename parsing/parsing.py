import requests
from prettytable import PrettyTable
from bs4 import BeautifulSoup

def parse(url):
    data = []

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find("tbody")

    names = table.find_all("p", class_="sc-1eb5slv-0 iworPT")
    marketCaps = table.find_all("span", class_="sc-1ow4cwt-1 ieFnWP")
    prices = table.find_all("div", class_="sc-131di3y-0 cLgOOr")

    for i in range(len(names)):
        item = {
            "name": names[i].text,
            "marketCap": marketCaps[i].text,
            "price": prices[i].text
        }

        data.append(item)

    return data

def printData(data):

    if len(data) == 0:
        print("\nInvalid name")
        return

    table = PrettyTable()

    table.field_names = ["Name", "Market Cap", "Price"]

    for element in data:
        table.add_row([element["name"], element["marketCap"], element["price"]])

    print(table)

def search(data, key):
    findItems = []

    for item in data:
        if item.get("name").lower().startswith(key.lower()):
            findItems.append(item)

    return findItems

if __name__ == "__main__":
    url = "https://coinmarketcap.com/"
    data = parse(url)
    printData(data)

    while(1):
        print("\nSearch cryptocurrency by name:")
        inputValue = input()
        printData(search(data, inputValue))