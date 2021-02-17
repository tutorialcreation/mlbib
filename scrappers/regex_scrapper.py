import re
url = 'http://example.webscraping.com/view/UnitedKingdom-239'
html = download(url)
re.findall('<td class="w2p_fw">(.*?)</td>', html)

# to avoid failure
re.findall('<tr id="places_area__row"><td class="w2p_fl"><label for="places_area" id="places_area__label">Area: </label></td><td class="w2p_fw">(.*?)</td>', html)

re.findall('<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?) </td>', html)
