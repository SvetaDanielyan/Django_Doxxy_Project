from django.shortcuts import render
from .models import News, Comments


def news(requests):
    context = {}
    context['news'] = News.objects.all()

    return render(requests, 'news.html', context)


# Create your views here.
def single_news(requests, news_number_slug):
    request_url = requests.build_absolute_uri().split('//')
    language = request_url[1].split(".")[0]

    news_number_slug = news_number_slug.lower()
    context = {}
    single_news_obj = News.objects.get(slug=news_number_slug)
    context['title'] = single_news_obj.title
    context['description'] = single_news_obj.description
    comments = Comments.objects.filter(news_slug_id=single_news_obj.id, language=language)
    context["comments"] = []
    for comment in comments:
        context["comments"].append(comment.comment)
    return render(requests, 'single_news.html', context)

