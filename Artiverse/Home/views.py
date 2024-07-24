from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from Artworks.models import Artwork
from User. models import Visitor
from Authentication.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import F

# Create your views here.
def index(request):
    latest_arts = Artwork.objects.order_by('-year_created')[:6]
    user = request.user

    profile = None
    if user.is_authenticated:
        try:
            profile = Visitor.objects.get(user=user)
        except Visitor.DoesNotExist:
            pass

    context = {
        'arts': latest_arts,
        'profile': profile
    }

    return render(request, 'Home/index.html', context)

@login_required
def explore(request):
    query = request.GET.get('query', '')
    medium = request.GET.get('medium', '')
    style = request.GET.get('style', '')
    price_range_min = request.GET.get('price_range_min', '')
    price_range_max = request.GET.get('price_range_max', '')
    genre = request.GET.get('genre', '')
    user = request.user
    profile = None
    try:
        profile = Visitor.objects.get(user=user)
    except Visitor.DoesNotExist:
       
        pass

    arts = Artwork.objects.all()
    if query:
        arts = arts.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    if medium:
        arts = arts.filter(medium=medium)

    if style:
        arts = arts.filter(style=style)

    if genre:
        arts = arts.filter(genre=genre)

    if price_range_min and price_range_max:
        arts = arts.filter(price__range=(price_range_min, price_range_max))
    elif price_range_min:
        arts = arts.filter(price__gte=price_range_min)
    elif price_range_max:
        arts = arts.filter(price__lte=price_range_max)

    paginator = Paginator(arts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
  

    context = {
        'arts': page_obj,
        'profile':profile
    }

    return render(request, 'Home/explore.html', context)


@login_required
def search(request):
    query = request.GET.get('query', '')
    medium = request.GET.get('medium', '')
    style = request.GET.get('style', '')
    price_range_min = request.GET.get('price_range_min', '')
    price_range_max = request.GET.get('price_range_max', '')
    genre = request.GET.get('genre', '')
    print(f"Query: {query}, Medium: {medium}, Style: {style}, Genre: {genre}, Price Range: {price_range_min}-{price_range_max}")
    result = Artwork.objects.all()
    user = request.user
    profile = None
    try:
        profile = Visitor.objects.get(user=user)
    except Visitor.DoesNotExist:
        
        pass

    if query:
        result = result.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    if medium:
        result = result.filter(medium=medium)

    if style:
        result = result.filter(style=style)

    if genre:
        result = result.filter(genre=genre)

    if price_range_min and price_range_max:
        result = result.filter(price__range=(price_range_min, price_range_max))
    elif price_range_min:
        result = result.filter(price__gte=price_range_min)
    elif price_range_max:
        result = result.filter(price__lte=price_range_max)

    paginator = Paginator(result, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'result':result,
        'arts': page_obj,
        'query': query,
        'medium':medium,
        'style':style,
        'genre':genre,
        'price_range_min':price_range_min,
        'price_range_max':price_range_max,
        'profile':profile
    }
    return render(request, 'Home/search.html', context)

@login_required
def artist_list(request):
    artists = User.objects.filter(is_artist=True)
    return render(request, 'artist_app/artist_list.html', {'artists': artists})
