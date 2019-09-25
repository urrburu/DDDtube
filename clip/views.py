from django.shortcuts import render
from django.template.context_processors import request
from django.contrib import messages
from .models import clip, Tag
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect
from django.db.models import Count
from .forms import ClipPostForm
from django.core.paginator import Paginator,EmptyPage
from .upload_fuc import get_data, urlCut
import pyperclip

def copyurl(request,clip):
    url = clip.url
    if request.is_ajax() or request.method == 'GET':
        if form.is_valid():
            return HttpResponse("url")
        else:
            return HttpResponse("Fail")

def clip_list(request, tag=None):
    tag_all = Tag.objects.annotate(num_post=Count('clip'))

    q = request.GET.get('q','')
    if q:
        tag=q
    if tag:
        clips = clip.objects.filter(tag_set__name__iexact=tag).prefetch_related('tag_set')
    else:
        clips = clip.objects.prefetch_related('tag_set').all()

    if request.method == 'POST':
        tag = request.POST.get('tag')
        tag_clean = ''.join(e for e in tag if e.isalnum())  # 특수문자 삭제
        return redirect('clip:clip_search', tag_clean)
    paginator = Paginator(clips,5)
    page = request.GET.get('page')
    clips = paginator.get_page(page)
    return render(request,'clip/list.html', {'clips':clips, 'tag':tag, tag_all:tag_all, })


def clip_gallary(request, tag=None):
    tag_all = Tag.objects.annotate(num_post=Count('clip'))

    if tag:
        clips = clip.objects.filter(tag_set__name__iexact=tag).prefetch_related('tag_set')
    else:
        clips = clip.objects.prefetch_related('tag_set').all()

    if request.method == 'POST':
        tag = request.POST.get('tag')
        tag_clean = ''.join(e for e in tag if e.isalnum())  # 특수문자 삭제
        return redirect('clip:clip_search', tag_clean)

    return render(request,'clip/gallary.html', {'clips':clips, 'tag':tag, tag_all:tag_all, })

def clip_new(request):
    if request.method == 'POST':
        form = ClipPostForm(request.POST)
        if form.is_valid():
            clip = form.save(commit=False)
            clip.clipID = urlCut(clip.clipID)
            clip.author_id = request.user.id
            clip.title = get_data(str(clip.clipID))['title']
            clip.streamer = get_data(str(clip.clipID))['broadcaster']['display_name']
            clip.url = get_data(str(clip.clipID))['url']
            clip.embed_url = get_data(str(clip.clipID))['embed_html']
            clip.save()
            clip.tag_save()

            return redirect('clip:clip_list')
    else:
        form = ClipPostForm()
    return render(request, 'clip/upload.html', {'form': form})


#class ClipUploadView(CreateView):
#    model = clip
#    fields = ['clipID','contents']
#    template_name = 'clip/upload.html'
#    def form_valid(self, form):
#        form.instance.author_id = self.request.user.id
#        if form.is_valid():
#            form.save(commit = False)
#            return redirect('/')
#        else:
#            return self.render_to_response({'form':form})


#class ClipDeleteView(DeleteView):
#    model = clip
#    success_url = '/'
#    template_name = 'clip/delete.html'


class ClipUpdateView(UpdateView):
    model = clip
    fields = ['clipID','text']
    template_name = 'clip/update.html'




#ClientId = "gsu4z8hkdn2xlqgbyye6rzogo3t5o5"

