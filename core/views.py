from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from core.models import GeneralLink, Section


def link_list(request, slug):
    section = get_object_or_404(Section, slug=slug) # slug=areas -> Section=Sohalar
    # links = GeneralLink.objects.filter(section=section)
    links = section.generallink_set.all()
    linktypes = section.linktype_set.all()
    context = {
        'links': links,
        'linktypes': linktypes
    }
    return render(request, "link_list.html", context) # shortcuts


# def link_detail(request, havola_idisi):
#     try:
#         link = Link.objects.get(id=havola_idisi)  # get(name="birinchi havola")
#     except Exception as e:
#         print(e)
#         raise Http404('Afsuski siz izlagan link topilmadi!')
#         # return HttpResponse("Afsuski siz izlagan link topilmadi!") # 200 HTTP 
    

#     return render(request, 'link_detail.html', {'link': link}) # 200 HTTP


def link_detail(request, havola_idisi):
    link = get_object_or_404(Link, id=havola_idisi) # shortcut

    return render(request, 'link_detail.html', {'link': link}) # 200 HTTP


# def link_create(request):
#     errors = {}
#     data = {}
#     print(f"==========={request.method}===============")
#     if request.method == 'GET':
#         print('bu GET so\'rovi edi. Bunday zaproslar kelganda biror logika boyicha response qaytarish mumkin')
#         print('request.GET=', request.GET) # request.GET  - QueryDict: {} (QueryDictionary)

#     if request.method == 'POST':
#         print(request.POST)
#         link_name = request.POST.get('name')
#         link_description = request.POST.get('description')
#         link_url = request.POST.get('url')
#         data['name'] = link_name
#         data['description'] = link_description
#         data['url'] = link_url
#         # new_link = Link(name=link_name)
#         # new_link.url = link_url
#         # new_link.description = link_description
#         # new_link.image = 'asd'
#         # new_link.save()
#         if link_name and link_url:
#             old_link = Link.objects.filter(name=link_name) # QuerySet [<Link 1>, <Link 2>]
#             if old_link: # old_link.exists()
#                 errors['other'] = 'Bunday nom bilan havola qoshilgan. Iltimos boshqa nom tanlang'
            
#             new_link = Link.objects.create(
#                 name=link_name,
#                 description=link_description,
#                 url=link_url
#             )
#             return redirect('/havolalar/') # domain.nomie/havolalar/
#         else:
#             if not link_name:
#                 errors['name'] = 'Please input link name'
            
#             if not link_url:
#                 errors['url'] = 'Please input link url'

#     return render(request, 'link_create.html', {'errors': errors, 'data': data}) # 200 HTTP

def link_create(request):
    form = LinkForm()

    if request.method == 'POST':
        # request.POST['name']
        form = LinkForm(request.POST) # is_bounded
        # form.is_valid()
        if form.is_valid(): # False
            form.save() # model from
            return redirect('/havolalar/')

    return render(request, 'link_create.html', {'form': form}) # 200 HTTP


def link_update(request, link_id):
    link = get_object_or_404(Link, id=link_id)
    form = LinkForm(instance=link) #
    
    if request.method == 'POST':
        form = LinkForm(instance=link, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/havolalar/') # domain.nomie/havolalar/

    return render(request, 'link_update.html', {'form': form})
