import  requests

print(requests.get('http://catalog.api.2gis.ru/geo/search',params={'version':'1.3','key':'123456789','city': 'Moscow'}).text)