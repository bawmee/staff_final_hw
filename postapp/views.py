from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import post
from django.utils import timezone
from .forms import post_fo

def index(request):

    posts_list = post.objects.all()
    site = request.GET.get('site')
    
    if site != None:
        posts_list = posts_list.filter(site=request.GET.get('site'))

    if request.GET.get('rate') == 'true':
        posts_list = posts_list.order_by('-rate')
    
    paginator = Paginator(posts_list, 10)
    page = request.GET.get('page')
    print(page)
    posts = paginator.get_page(page)

    return render(request, 'index.html',{'posts':posts, 'site':site})



def detail(request, post_id):

    po = get_object_or_404(post, pk = post_id)

    return render(request, 'detail.html', {'post':po})


def delet(request, post_id):

    po = get_object_or_404(post, pk = post_id)
    po.delete()

    return redirect('/')


def new(request):
    if request.method == 'POST':
        form = post_fo(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.date = timezone.now()
            post.save()
            return redirect('/'+str(post.id))
    else:
        form = post_fo()
        return render(request, 'new.html', {'form':form})

def update(request, post_id):
    if request.method == 'POST':
        
            po = get_object_or_404(post, pk = post_id)
            po.site = request.POST.get("site")
            po.contry = request.POST.get("contry")
            po.genre = request.POST.get("genre")
            po.rate = request.POST.get("rate")
            po.title = request.POST.get("title")
            po.review = request.POST.get("review")
            po.date = timezone.now()
            
            po.save()
            return redirect('/'+str(po.id))
    else:
        form = post_fo()
        post_id = post_id
        po = get_object_or_404(post, pk = post_id)
        return render(request, 'update.html', {'form':form,'post_id':post_id, 'po':po})


