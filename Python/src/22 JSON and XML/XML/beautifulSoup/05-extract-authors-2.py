from ReadFile import readFile
from bs4 import BeautifulSoup

doc = readFile("xml/book.xml")
soup =  BeautifulSoup(doc, 'lxml')

subtree = soup.book.author
subtree.extract()   # extract first author

print(soup.prettify())

# extract all authors
tags = soup.findAll("author")
for tag in tags:
    tag.extract()
    
print(soup.prettify())


1
    


