import requests

response_obj = requests.get('https://in.nba.com/?gr=www')

# print(response_obj.text)
# print(response_obj.ok)

payload = {'abc': 'ow', 'abcd': 45}
# response_obj = requests.get('https://httpbin.org/get', params=payload)

# print(response_obj.text)
#
# response_obj = requests.post('https://httpbin.org/post', data=payload)
#
# response_dict = response_obj.json()
#
# print(response_dict[form])
#
# print(response_obj.json())

# response_obj = requests.get('http://httpbin.org/basic-auth/sukruth/ananth', auth =('sukruth1','ananth'),timeout=3)

response_obj = requests.get('https://in.nba.com/?gr=www', params=payload)


# response_obj = requests.get('http://httpbin.org/delay/1', timeout=3)

# print(response_obj.url)


# from bs4 import BeautifulSoup
#
# with open('simple.html') as f:
#     soup = BeautifulSoup(f,'lxml')
#
# # print(soup.title.text)
#
# # print(soup.find('div', class_='ot-sdk-show-settings'))
#
#
# #use findall
#
#
# for articles in soup.findAll('span', class_='choose-edition'):
#     headline = articles.text
#     print(headline)


import xml.etree.cElementTree as ET
import csv

file_xml = ET.parse('books.xml')

file_root = file_xml.getroot()
#
# # print(file_root[0])
# f = open('catalog.csv', 'w')
# books_writer = csv.writer(f)

# books_writer.writerow(['BOOK ID', 'AUTHOR', 'TITLE', 'GENRE', 'PRICE', 'PUBLISH_DATE','DESCRIPTION'])
# print(help(file_root.iter()))
# book_list = []
# for n in file_root.iter():
#     book_list.append(n.text)
#     print(book_list)

# print(file_root[0].get('id'))

# for book in file_root:
#     book_list.append(book.get('id'))
#     for n in range(len(book)):
#         item = book[n].text
#         book_list.append(item)
#         # print(book_list)
#     books_writer.writerow(book_list)
#     book_list = []
#
#
# f.close()

# print((file_root.))
# print(help(file_xml))

'''f = open('menu.csv','w')
writer = csv.writer(f)
writer.writerow(["ITEM NAME","ITEM PRICE", "ITEM DESCRIPTION", "ITEM CALORIES"])
#
row_list = []
for food in file_root:
    for n in range(len(food)):
        item = food[n].text
        row_list.append(item)
    writer.writerow(row_list)
    row_list = []


f.close()

# print(file_xml.getroot()[0][2].text)

'''
#
# url = 'https://tech.hindustantimes.com/rss'
#
# response_obj = requests.get(url)
#
# print(response_obj.content)
#
# # with open('newrss.xml','wb') as f:
# #      f.write(response_obj.content)
#
#
# parse_rss = ET.fromstring(response_obj.content)
#
# print(parse_rss.tag)


import pynput

from pynput.keyboard import Key, Listener

keys = []
