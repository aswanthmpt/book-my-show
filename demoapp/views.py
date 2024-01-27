from django.shortcuts import render,redirect
from .models import Movie
from .forms import MovieForm
# Create your views here.
def home(req):
    movies=Movie.objects.all()
    return render(req,'index.html',{'movies':movies})


def register(req):
    if req.method=='POST':
        name=req.POST.get('name','')
        rating=req.POST.get('rating','')
        type=req.POST.get('type','')
        language=req.POST.get('language','')
        certificate=req.POST.get('certificate','')
        category=req.POST.get('category','')
        duration=req.POST.get('duration','')
        date=req.POST.get('date','')
        poster=req.FILES['poster']
        banner=req.FILES['banner']
        movie=Movie(name=name,rating=rating,type=type,language=language,certificate=certificate,category=category,duration=duration,date=date,poster=poster,banner=banner)
        movie.save()
        
        return redirect('home')
    return render(req,'register.html')
def details(req,id):
    
    movie=Movie.objects.get(id=id)
    
    return render(req,'details.html',{'movie':movie})

def update(req,id):
    movie=Movie.objects.get(id=id)
    if req.method=='POST':
        name=req.POST.get('name','')
        rating=req.POST.get('rating','')
        type=req.POST.get('type','')
        language=req.POST.get('language','')
        certificate=req.POST.get('certificate','')
        category=req.POST.get('category','')
        duration=req.POST.get('duration','')
        date=req.POST.get('date','')
        poster=req.FILES['poster']
        banner=req.FILES['banner']
        print(name,rating,type,language,certificate,category,duration,date,poster,banner)
      
        postername=str(poster)
        bannername=str(banner)
        movie.poster.save(postername,poster,save=True)
        movie.banner.save(bannername,banner,save=True)
        Movie.objects.filter(id=id).update(name=name,rating=rating,type=type,language=language,certificate=certificate,category=category,duration=duration,date=date)
        return redirect("home")
    # f=MovieForm(req.POST,req.FILES or None,instance=movie)
    # if f.is_valid():
        
    #     f.save()
        # return redirect("home")
    
    return render(req,'update.html',{"movie":movie})
def delete(req,id):
    tasks=Movie.objects.get(id=id)
    if req.method=="POST":
                                              
        
        Movie.objects.filter(id=id).delete()
        return redirect("home")
    return render(req,'delete.html',{"task":tasks})