import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.utils.text import slugify
from users.models import BookmarkedLink
from core.models import Company, GeneralLink, Like, Section, LinkType
from .forms import GeneralLinkForm


def link_list(request, slug, type_slug=None):
    section = get_object_or_404(Section, slug=slug) # slug=areas -> Section=Sohalar
    # links = GeneralLink.objects.filter(section=section)
    links = section.generallink_set.all()
    linktypes = section.linktype_set.all()
    filter_options = GeneralLink.objects.filter(
        Q(section__slug='areas') | Q(section__slug='tools')
    )
    if type_slug:
        type = get_object_or_404(LinkType, slug=type_slug)
        links = links.filter(type=type)

    choosen_filter = request.GET.get('filter') # request.GET['filter']
    if choosen_filter:
        link = GeneralLink.objects.filter(slug=choosen_filter).first()
        if link:
            links = links.filter(tools__in=[link])
    q = request.GET.get('q')
    if q:
        links = links.filter(
            Q(name__icontains=q) |
            Q(short_description__icontains=q) |
            Q(description__icontains=q) |
            Q(company__name__icontains=q)
        )
    sort = request.GET.get('sort')
    if sort in ('name', '-name', '-created_time', '-rating'):
        links = links.order_by(sort)
        
    page = int(request.GET.get('page', 1)) # har bir page da 10tadan link chiqsin
    format = request.GET.get('format', 'html')
    links = links[(page-1)*3:page*3]  # page=1 -> links[0:10] | page=2  -> links[10:20]
    # filter_options = GeneralLink.objects.filter(section__slug='tools')
    context = {
        'section': section,
        'links': links,
        'linktypes': linktypes,
        'filter_options': filter_options,
        'slug': slug,
        'type_slug': type_slug
    }

    if format == 'json':
        print('returned json')
        return JsonResponse(data={
            'links': [{
                'id': link.id,
                'photo_url': link.photo.url,
                'name': link.name,
                'slug': link.slug,
                'type': link.type.name,
                'short_description': link.short_description,
                'tools': [{
                    'name': tool.name,
                    'slug': tool.slug,
                    'photo_url': tool.photo.url
                } for tool in link.tools.all()],
                'status': link.status(request.user), # L, K, W, ''
                'likes_count': link.likes_count(),
                'is_liked': True if link.is_liked(request.user) == 'like' else False,
                'is_disliked': True if link.is_liked(request.user) == 'dislike' else False
                # ...
            } for link in links],   # [{....} for link in links]
            'page': page
        })
        # {'links': [], 'page': 1}
    return render(request, "link_list.html", context) # shortcuts


def link_detail(request, link_slug):
    link = get_object_or_404(GeneralLink, slug=link_slug) # shortcut
    link.views_count += 1
    link.save()
    return render(request, 'link_detail.html', {'link': link}) # 200 HTTP


def link_create(request):
    form = GeneralLinkForm(data=request.POST or None, files=request.FILES or None) # 
    context = {
        'sections': Section.objects.all(),
        'types': LinkType.objects.all(),
        'tools': GeneralLink.objects.filter(
                    Q(section__slug='areas') | Q(section__slug='tools')
                ),
        'companies': Company.objects.all(),
        'form': form
    }

    if request.method == 'POST':
        print(request.POST)
        if form.is_valid(): # False
            new_link = form.save(commit=False) # model from
            new_link.author = request.user
            new_link.slug = slugify(new_link.name)
            new_link.save()
            return redirect('/')
        print(form.errors)

    return render(request, 'link_create.html', context) # 200 HTTP


# def link_update(request, link_id):
#     link = get_object_or_404(Link, id=link_id)
#     form = LinkForm(instance=link) #
    
#     if request.method == 'POST':
#         form = LinkForm(instance=link, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/havolalar/') # domain.nomie/havolalar/

#     return render(request, 'link_update.html', {'form': form})


@csrf_exempt
def like(request):
    if not request.user.is_authenticated:
        return HttpResponse(status=401)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)   # json.loads: str or bytes --> dict 
            obj_type = data['obj_type']
            obj_id = int(data['id'])
            value = data['value']
            # request.user # AnonymousUser if user not logged in
            if obj_type == 'link':
                old_like = Like.objects.filter(author=request.user, link=obj_id).first()
                if old_like:
                    if old_like.type == value:
                        old_like.delete()
                    else:
                        old_like.type = value
                        old_like.save()
                else:
                    Like.objects.create(
                        author=request.user,
                        link_id=obj_id,
                        type=value
                    )
            return HttpResponse(status=200)
        except Exception as e:
            print(e)
            return HttpResponse(status=400)
    return HttpResponse(status=403)


@csrf_exempt
def bookmarking(request, link_id):
    if not request.user.is_authenticated:
        return HttpResponse(status=401)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)   # json.loads: str or bytes --> dict 
            status = data['status']
            obj_id = link_id
            bookmark, created = BookmarkedLink.objects.get_or_create(user=request.user, link_id=obj_id) # -> (bookmark obj, True/False)
            bookmark.status = status
            bookmark.save()
            return HttpResponse(status=200)
        except Exception as e:
            print(e)
            return HttpResponse(status=400)
    return HttpResponse(status=403)
