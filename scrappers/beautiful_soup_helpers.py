from bs4 import BeautifulSoup
url = 'http://example.webscraping.com/places/view/United-Kingdom-239'
html = download(url)

broken_html = '<ul class=country><li>Area<li>Population</ul>'
soup = BeautifulSoup(broken_html, 'html.parser')
fixed_html = soup.prettify()
print(fixed_html)

ul = soup.find('ul', attrs={'class':'country'})
ul.find('li')
ul.find_all('li')


soup = BeautifulSoup(html)
tr = soup.find(attrs={'id':'places_area__row'})
td = tr.find(attrs={'class':'w2p_fw'})
area = td.text
print(area)
