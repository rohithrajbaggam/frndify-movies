from django.shortcuts import render, redirect
import requests
from .models import SaveAPITokenModel, userSearchHistoryModel, userMovieSaveModel
from django.http import HttpResponse
from .utils import get_home_page_content 
from django.contrib.auth.decorators import login_required

# Create your views here.
# {'Title': 'Lucy', 
# 'Year': '2014', 
# 'imdbID': 'tt2872732',
#  'Type': 'movie', 
# 'Poster': 'https://m.media-amazon.com/images/M/MV5BODcxMzY3ODY1NF5BMl5BanBnXkFtZTgwNzg1NDY4MTE@._V1_SX300.jpg'}
session = requests.Session()

@login_required(login_url='login')
def home(request):
    try:
        # ?s=lucy&page=1&apikey=e1683ba0
        # user_save_post_list = user_save_post.values_list('post', flat=True)
        api_key = SaveAPITokenModel.objects.filter(is_active=True).last()
        params = {
            "s" : "batman",
            # "s" : get_home_page_content(),
            "page" : 1,
            "apikey" : api_key.api_key,
            
        }
        req_data = session.get(url="https://www.omdbapi.com/", params=params).json()
        # for data in req_data.json()['Search']:
        #     print(data['Title'])
        context = {
            "req_data" : req_data['Search']
            # "data" : req_data.json()
        }
        return render(request, 'movies/homescreen.html', context)
    except:
        return HttpResponse("Internal Server Error")
@login_required(login_url='login')
def userMovieSaveView(request, link, imdbid):
    try:
        if userMovieSaveModel.objects.filter(imdbid=imdbid, user=request.user).exists():
            query = userMovieSaveModel.objects.get(imdbid=imdbid, user=request.user)
            query.is_saved = True 
            query.save()
        else:
            query = userMovieSaveModel.objects.create(
                user = request.user,
                imdbid = imdbid,
                link = link,
                is_saved = True     
            )
        
        return redirect("home")
    except:
        return redirect("home")

@login_required(login_url='login')
def userMovieUnSaveView(request, imdbid):
    try:
        query = userMovieSaveModel.objects.get(
        user = request.user,
        imdbid = imdbid 
        )
        query.is_saved = False 
        query.save()
        return redirect("home")
    except:
        return redirect("home")

@login_required(login_url='login')
def suggestionsView(request, name):
    # ?s=lucy&page=1&apikey=e1683ba0
    try:
        api_key = SaveAPITokenModel.objects.filter(is_active=True).last()
        params = {
            "s" : name,
            "page" : 1,
            "apikey" : api_key.api_key
        }
        search_url = "https://www.omdbapi.com/"
        req_data = session.get(url=search_url, params=params).json()
        user_search_history = userSearchHistoryModel.objects.create(
                user = request.user,
                url = f"{search_url}?s={name}&apikey={api_key}",
                api_key = api_key.api_key,
                search_keyword = name 
                    )
        # for data in req_data.json()['Search']:
        #     print(data['Title'])
        context = {
            "req_data" : req_data['Search']
            # "data" : req_data.json()
        }
        return render(request, 'movies/homescreen.html', context)
    except:
        return HttpResponse("Internal Server Error")



@login_required(login_url='login')
def search(request):
    try:
        keyword = ''
        if request.GET["keyword"] in ["", [], None]:
            return redirect('home')
        result = False 
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            
            api_key = SaveAPITokenModel.objects.filter(is_active=True).last()
            if not api_key:
                return HttpResponse("API Not Found")
            params1 = {
            "s" : keyword,
            "page" : 1,
            "apikey" : api_key.api_key,
            # "apikey" : "e1683ba0"
            }
            search_url = "https://www.omdbapi.com/"
            req_data1 = session.get(url=search_url, params=params1)
            
            if  "Search" in req_data1.json():
                req_data1 = req_data1.json()["Search"]
                result = True 
                # params2 = {
                # "s" : keyword,
                # "page" : 2,
                # "apikey" : api_key.api_key,
                # # "apikey" : "e1683ba0"
                # }
                # req_data2 = session.get(url=search_url, params=params2).json()['Search']
                # print('req_data', req_data)
                user_search_history = userSearchHistoryModel.objects.create(
                    user = request.user,
                    url = f"{search_url}?s={keyword}&apikey={api_key}",
                    api_key = api_key.api_key,
                    search_keyword = keyword 
                )
                context = {
                    'keyword' : keyword, 
                    'result' : result,
                    'req_data' : req_data1
                }
                return render(request, 'movies/search.html', context)
            else:
                context = {
                    'keyword' : keyword, 
                    'result' : result,
                    'req_data' : req_data1
                }
                return render(request, 'movies/search.html', context)
                # return HttpResponse(req_data1.json()['Error'])
    except:
        context = {
                    'keyword' : None, 
                    'result' : False,
                    'req_data' : None
                }
        return render(request, 'movies/search.html', context)

@login_required(login_url='login')
def userBrowsingHistory(request):
    user_history = userSearchHistoryModel.objects.filter(user=request.user).order_by("-timestamp")
    context = {
        'req_data' : user_history
    }
    return render(request, "movies/history.html", context)