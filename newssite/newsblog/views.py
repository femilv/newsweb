from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Category

from .models import News
# Create your views here.

#handles the index page
def index(request):
    news = News.objects.all()

    singlenews = Category.objects.get(name='News')
    sing_news = News.objects.filter(category= singlenews)[10:11]

    enternews = Category.objects.get(name='News')
    ent_news = News.objects.filter(category= enternews)[14:15]

    busnews = Category.objects.get(name='Business')
    bus_news = News.objects.filter(category= busnews)[17:18]

    polinews = Category.objects.get(name='Politics')
    pol_news = News.objects.filter(category= polinews)[12:13]

    news_category = Category.objects.get(name ='News')
    news_news = News.objects.filter(category= news_category)

    sport_category = Category.objects.get(name ='Sports')
    sport_news = News.objects.filter(category=sport_category)
    sport_cont= News.objects.filter(category=sport_category)[:4]

    politics_category = Category.objects.get(name ='Politics')
    politics_news = News.objects.filter(category=politics_category)
    poli_cont= News.objects.filter(category=politics_category)[:5]
    poli_cont2= News.objects.filter(category=politics_category)[3:8]

    entertainment_category = Category.objects.get(name ='Entertainment')
    entertainment_news = News.objects.filter(category=entertainment_category)
    ent_cont= News.objects.filter(category=entertainment_category)[:5]
    ent_cont2= News.objects.filter(category=entertainment_category)[3:8]
    
    technews_category = Category.objects.get(name ='TechNews')
    technews_news = News.objects.filter(category=technews_category)
    
    business_category = Category.objects.get(name ='Business')
    business_news = News.objects.filter(category=business_category)
    bus_cont= News.objects.filter(category=business_category)[:5]
    bus_cont2= News.objects.filter(category=business_category)[3:8]
    
    podcast_category = Category.objects.get(name ='Podcast')
    podcast_news = News.objects.filter(category=podcast_category)

    latest_news = News.objects.order_by('created_at')[:5]
    top_news = News.objects.order_by('created_at')[4:9]

    return render(request, "index.html", {'news':news, 'news_news': news_news, 'sport_news':sport_news, 'politics_news': politics_news, 'entertainment_news':entertainment_news, 'technews_news': technews_news, 'business_news': business_news, 'podcast_news': podcast_news, 'sing_news':sing_news, 'latest_news': latest_news, 'top_news': top_news, 'ent_news':ent_news, 'bus_news': bus_news, 'pol_news': pol_news, 'ent_cont': ent_cont, 'ent_cont2': ent_cont2, 'sport_cont': sport_cont, 'poli_cont': poli_cont, 'poli_cont2': poli_cont2, 'bus_cont': bus_cont, 'bus_cont2': bus_cont2})


# handles the viewing page
def news_details(request, new_id):
    new = get_object_or_404(News, pk = new_id)
    return render (request, 'viewing.html', {'new': new})


# handles the category
def category_news(request, category_id=None):
    category = get_object_or_404(Category, pk=category_id)
    news = News.objects.filter(category=category)
    news_list = News.objects.filter(category=category)



    newscenter = get_object_or_404(Category, pk=category_id)
    cent_news = News.objects.filter(category= newscenter)[:1]
    category_right = News.objects.filter(category= newscenter)[:5]
    category_left = News.objects.filter(category= newscenter)[1:6]
    news_group = News.objects.filter(category= newscenter)[:5]
    news_group_next = News.objects.filter(category= newscenter)[5:11]

    paginator = Paginator(news_list, 5)  # 5 news per page
    page_number = request.GET.get('page', 1)  # Get page number from URL, default to 1
    page_obj = paginator.get_page(page_number) 

    return render(request, 'category.html', {"category": category, "news": news, 'cent_news': cent_news, 'category_right': category_right, 'category_left': category_left, 'news_group':news_group, 'news_group_next': news_group_next,"page_obj": page_obj,})
