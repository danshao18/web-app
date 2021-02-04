from django.shortcuts import render
from bs4 import BeautifulSoup
from home.models import Home
from home.models import Comment
from .forms import CommentForm
import re
import requests
from django.forms.models import model_to_dict


# Create your views here.
def home(request):
    session = requests.session()
    req = session.get("https://www.basketball-reference.com/boxscores/")
    doc = BeautifulSoup(req.content, 'html.parser')
    winners = re.sub("\\<.*?\\> ?", "", str(doc.findAll('tr', {"class": "winner"})))
    winners = re.sub("OT", "", re.sub("\n", " ", re.sub("Final", "", winners)))
    winners = winners.replace('[','').replace(']','')
    wpts = [int(x) for x in winners.split() if x.isdigit()]
    winners = [x.strip() for x in ''.join([i for i in winners if not i.isdigit()]).split(',') if not x.isdigit()]
    losers = re.sub("\\<.*?\\> ?", "", str(doc.findAll('tr', {"class": "loser"})))
    losers = re.sub("OT", "", re.sub("\n", " ", re.sub("Final", "", losers)))
    losers = losers.replace('[','').replace(']','')
    lpts = [int(x) for x in losers.split() if x.isdigit()]
    losers = [x.strip() for x in ''.join([i for i in losers if not i.isdigit()]).split(',') if not x.isdigit()]
    for i in range(len(winners)):
        if (i == 0) & (Home.objects.exists()):
            obj = model_to_dict(Home.objects.all()[0])
            if ((winners[i] == obj['winner']) & (losers[i] == obj['loser']) & (wpts[i] == obj['wpts']) & (lpts[i] == obj['lpts'])):
                break
            else:
                Home.objects.all().delete()
        entry = Home(winner=winners[i], wpts=wpts[i], loser=losers[i], lpts=lpts[i])
        if not Home.objects.filter(winner=winners[i], wpts=wpts[i], loser=losers[i], lpts=lpts[i]).exists():
            entry.save()
    home = Home.objects.all()
    context = {
        'home': home
    }
    return render(request, 'home.html', context)
    
    

def home_detail(request, pk):
    home = Home.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                game=home
            )
            comment.save()
    comments = Comment.objects.filter(game=home)
    context = {
        'home': home,
        'comments': comments,
        'form': form,
    }
    return render(request, 'home_detail.html', context)
