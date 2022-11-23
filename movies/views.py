from django.shortcuts import render
import requests
# Create your views here.
# {'Title': 'Lucy', 
# 'Year': '2014', 
# 'imdbID': 'tt2872732',
#  'Type': 'movie', 
# 'Poster': 'https://m.media-amazon.com/images/M/MV5BODcxMzY3ODY1NF5BMl5BanBnXkFtZTgwNzg1NDY4MTE@._V1_SX300.jpg'}
session = requests.Session()
def home(request):
    # ?s=lucy&page=1&apikey=e1683ba0
    params = {
        "s" : "marvel",
        "page" : 1,
        "apikey" : "e1683ba0"
    }
    req_data = session.get(url="https://www.omdbapi.com/", params=params).json()
    # for data in req_data.json()['Search']:
    #     print(data['Title'])
    context = {
        "req_data" : req_data['Search']
        # "data" : req_data.json()
    }
    return render(request, 'movies/homescreen.html', context)




