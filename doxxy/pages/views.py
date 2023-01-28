from django.shortcuts import render
from pages.forms import CommentForm
from news.models import Comments, News


# Create your views here.
def main(requests):
    request_url = requests.build_absolute_uri().split('//')
    language = request_url[1].split(".")[0]
    print("request for language:::", language)
    context = dict()
    if requests.method == 'POST':
        comment_form = CommentForm(requests.POST)
        if comment_form.is_valid():
            comment, slug = requests.POST.get('comment'), \
                requests.POST.get('slug')
            try:
                news = News.objects.get(slug=slug)
                created = Comments.objects.create(news_slug=news, comment=comment, language=language)
                print("created comment:", created)
            except Exception as e:
                print(e)
                context['error'] = " ⚠️Oops,something wasn't right"
        else:
            context['error'] = " ⚠️Oops,something wasn't right"
    context['language'] = language
    return render(requests, 'main.html', context)
