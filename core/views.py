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
        'section': section,
        'links': links,
        'linktypes': linktypes
    }
    return render(request, "link_list.html", context) # shortcuts


def link_detail(request, havola_idisi):
    link = get_object_or_404(Link, id=havola_idisi) # shortcut

    return render(request, 'link_detail.html', {'link': link}) # 200 HTTP


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
