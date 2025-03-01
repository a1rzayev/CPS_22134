import urllib.request
import requests

# создаем объект, который будет раскрывать сайты
opener = urllib.request.build_opener()

response = opener.open("https://httpbin.org/get")
print(response.read())

print("\n\n") # Ответы будут разные

response = requests.get("https://httpbin.org/get")
print(response.content)

# создаем объект, который будет раскрывать сайты

# создание post запроса с данными и c header 
response = requests.post("https://httpbin.org/post",
                            data="IsmailIsmail",
                            headers={"h1": "Ismaaaiiil!"})
print("text - ", response.text)


"""Парсинг сайтов"""

response = requests.get("https://coinmarketcap.com")

print(response.text, "\n\n")

res_parse_list = []

response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem1 in response_parse:
    if ( parse_elem1.startswith("$")):
        for parse_elem2 in parse_elem1.split("</span>"):
            if (parse_elem2.startswith("$") and parse_elem2[1].isdigit()):
                res_parse_list.append(parse_elem2)

bitcoin_exchange_rate = res_parse_list[0]
print(res_parse_list, "\n\n")
print(bitcoin_exchange_rate)
        
