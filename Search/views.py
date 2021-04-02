from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
from .models import SearchModel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from Login.models import UserProfile


class Home(LoginRequiredMixin, ListView):
    model = SearchModel
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = {}
        if self.request.method == 'GET':
                search = self.request.GET.get('search','').lower()
                print(search)
                if search != "":
                    url = 'https://www.ask.com/web?q='+search
                    res = requests.get(url)
                    soup = bs(res.text, 'lxml')
                    b = SearchModel(search_by=self.request.user,keyword=search)
                    b.save()
                    result_listings = soup.find_all('div', {'class': 'PartialSearchResults-item'})
                    print(len(result_listings))
                    

                    final_result = []
                    
                    
                    for result in result_listings:
                        result_title = result.find(class_='PartialSearchResults-item-title').text
                        result_url = result.find('a').get('href')
                        result_desc = result.find(class_='PartialSearchResults-item-abstract').text
                        final_result.append((result_title, result_url, result_desc))

                    context = {
                        'final_result': final_result
                    }
                    
        return context

        
class History(ListView):
    model = SearchModel
    template_name = 'Search/history.html'
    

    def get_context_data(self, **kwargs):
        
        # users = []
        histories = SearchModel.objects.all()
        keywords = SearchModel.objects.order_by().values_list('keyword',flat=True).distinct()
        # keywords = SearchModel.objects.order_by().values('keyword').distinct()
        print(keywords)
        counts = {}
        wanted_items = set()
        for keyword in keywords:
            counts[keyword] = SearchModel.objects.filter(keyword__contains=keyword).count()
            wanted_items.add(keyword+" ["+str(counts[keyword])+" times found]")
        histories_all = []
        print(wanted_items)
        for history in histories:
            keyword = history.keyword
            user = history.search_by
            date = history.search_date
            histories_all.append((keyword,user,date))
        dates = {}
        users = UserProfile.objects.all()
        # keywords = {}
        for history in histories:
            # keywords[history.keyword] = history.keyword
            dates[history.search_date] = history.search_date
        
        context = {
            'histories': histories,
            'users':users,
            # 'keywords': keywords,
            'keywords': wanted_items,
            'dates' : dates,
            'histories_all': histories_all,
            
        }
            
        return context

# def historyByUser(request, user):
#     histories = SearchModel.objects.filter(user=user)
#     context = {
#             'histories': histories,
#             'users':users,
#             'keywords': keywords,
#             'dates' : dates,
#         }
#     return 

