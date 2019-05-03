from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import post
from django.utils import timezone
from .forms import post_fo
from django.db.models import Q

def index(request):

    posts_list = post.objects.all().order_by('-date')
    site = request.GET.get('site')
    search_text = request.GET.get('search')

    if search_text != None:
        posts_list = posts_list.filter(Q(title__contains=search_text) | Q(contry__contains=search_text))
    
    if site != 'None' and site != None:
        posts_list = posts_list.filter(site=request.GET.get('site'))
        

    if request.GET.get('rate') == 'true':
        posts_list = posts_list.order_by('-rate')
    
    paginator = Paginator(posts_list, 15)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    ratelist = [1,2,3,4,5]
    sitelist = ['All', 'Netfilx', 'Watcha', 'Tving', 'Qoop', 'Etc']

    return render(request, 'index.html',{'posts':posts, 'site':site, 'sitelist':sitelist, 'ratelist':ratelist})



def detail(request, post_id):

    po = get_object_or_404(post, pk = post_id)
    ratelist = [1,2,3,4,5]

    return render(request, 'detail.html', {'post':po, 'ratelist':ratelist})


def delet(request, post_id):

    po = get_object_or_404(post, pk = post_id)
    po.delete()

    return redirect(index)


def new(request):
    if request.method == 'POST':
        form = post_fo(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.date = timezone.now()
            post.save()
            return redirect(detail, post.id)
    else:
        form = post_fo()
        return render(request, 'new.html', {'form':form})

def update(request, post_id):

    po = get_object_or_404(post, pk = post_id)
    if request.method == 'POST':
        
            po.site = request.POST.get("site")
            po.contry = request.POST.get("contry")
            po.genre = request.POST.get("genre")
            po.rate = request.POST.get("rate")
            po.title = request.POST.get("title")
            po.review = request.POST.get("review")
            po.date = timezone.now()
            
            po.save()
            return redirect(detail, po.id)
    else:      
        return render(request, 'update.html', {'post_id':post_id, 'po':po})


