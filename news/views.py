
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView, FormView
from django.urls import reverse, reverse_lazy

from accounts.models import Profile
from .models import News, Category,Comentary
from .form import ContactForm,ComentaryForm
from config.custom_permissions import OnlyLoggedsuperUser
from hitcount.views import HitCountDetailView

def news_list(request):
    news_list = News.objects.all()
    context = {'news_list':news_list}
    return render(request,"news/news_list.html",context)

# def news_detail(request,news):
#     news = get_object_or_404(News, slug=news,status=News.Status.Published)
#     context = {'news':news}
#     return render(request,'news/news_detail.html',context)

def home_View(request):
    categories = Category.objects.all()
    news_list = News.objects.all().order_by('-publish_time')[:5]
    one_uzb_new = News.objects.all().filter(category__name = "O'zbekiston").order_by('-publish_time')[:1]
    uzb_news = News.objects.all().filter(category__name = "O'zbekiston").order_by('-publish_time')[1:6]
    context = {
        'categories':categories,
        'news_list':news_list,
        'one_uzb_new':one_uzb_new,
        'uzb_news':uzb_news,
    }
    return render(request, 'news/home.html', context)
class HomeView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] =self.model.objects.all().order_by('-publish_time')[:15]
        context['uzb_news'] = self.model.objects.all().filter(category__name = "O'zbekiston").order_by('-publish_time')[:5]
        context['jahon_news'] = self.model.objects.all().filter(category__name = "Jahon").order_by('-publish_time')[:5]
        context['iqtisod_news'] = self.model.objects.all().filter(category__name = "Iqtisodiyot").order_by('-publish_time')[:5]
        context['sport_news'] = self.model.objects.all().filter(category__name = "Sport").order_by('-publish_time')[:5]
        return context


# funksiya orqali qilingan contactview

# def contact_View(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse("<h2> Biz bilan bog'langaniz uchun raxmat !")
#     context = {'form':form}
#     return render(request, 'news/contact.html', context)

# funskiyadagi viewni classga aylantirilgan varianti chat.deepseek.com yordamida (test qib ko'rmadim hali)

# class ContactPageView(FormView):
#     template_name = 'news/contact.html'  # Shablon faylning manzili
#     form_class = ContactForm  # Foydalaniladigan forma
#     success_url = '/'  # Forma muvaffaqiyatli to'ldirilgandan so'ng yo'naltiriladigan URL
#
#     def form_valid(self, form):
#         # Forma to'g'ri to'ldirilgan bo'lsa, uni saqlaymiz
#         form.save()
#         # Foydalanuvchiga xabar qaytaramiz
#         return HttpResponse("<h2> Biz bilan bog'langaniz uchun raxmat!</h2>")

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self,request,*args,**kwargs):
        form = ContactForm()
        context = {'form':form}
        return render(request,'news/contact.html',context)
    def post(self,request,*args,**kwargs):
        form = ContactForm(request.POST)
        if form.is_valid() and request.method == 'POST':
            form.save()
            return HttpResponse("<h2>Biz bilan bog'langaningiz uchun tashakkur</h2>")
        context = {'form':form}
        return render(request,'news/contact.html',context)




def single_View(request,title):
    news = get_object_or_404(News, title=title,status=News.Status.Published)
    comments = news.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = ComentaryForm(data = request.POST)
        if comment_form.is_valid():
            # yangi komment obyektini yaratamiz lekin DB ga saqlamaymiz
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.news = news
            new_comment.save()
            comment_form = ComentaryForm()
    else :
        comment_form = ComentaryForm()

    context = {
        'news':news,
        'comments':comments,
        'new_comment':new_comment,
        'comment_form':comment_form,
    }
    return render(request,'news/single_page.html',context)


class SinglePageView(HitCountDetailView):
    model = News
    template_name = 'news/single_page.html'
    count_hit = True
    def get(self,request,title,*args,**kwargs):
        news = get_object_or_404(News, title=title, status=News.Status.Published)
        comments = news.comments.filter(active=True)
        comments_count = comments.count
        comment_form = ComentaryForm()
        context = {
            'news': news,
            'comments': comments,
            'comment_form': comment_form,
            'comments_count': comments_count,
        }
        return render(request, 'news/single_page.html', context)
    def post(self,request,title,*args,**kwargs):
        news = get_object_or_404(News, title=title, status=News.Status.Published)
        comments = news.comments.filter(active=True)
        comments_count = comments.count()
        new_comment = None
        comment_form = ComentaryForm(data=request.POST)
        if comment_form.is_valid():
            # yangi komment obyektini yaratamiz lekin DB ga saqlamaymiz
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.news = news
            new_comment.save()
            return redirect(reverse('single', kwargs={'title': title}))

        context = {
            'news': news,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,
            'comments_count': comments_count,
        }
        return render(request, 'news/single_page.html', context)

def page_404_View(request):
    context = {}
    return render(request, 'news/404.html', context)

class UzbekistonPageView(ListView):
    model = News
    template_name = 'news/uzbekiston.html'
    context_object_name = 'uzb_news'
    def queryset(self):
        news = self.model.objects.all().filter(category__name = "O'zbekiston")
        return news

class JahonPageView(ListView):
    model = News
    template_name = 'news/jahon.html'
    context_object_name = 'jahon_news'
    def queryset(self):
        news = self.model.objects.all().filter(category__name = "Jahon")
        return news

class IqtisodPageView(ListView):
    model = News
    template_name = 'news/iqtisod.html'
    context_object_name = 'iqtisod_news'
    def queryset(self):
        news = self.model.objects.all().filter(category__name = "Iqtisodiyot")
        return news

class SportPageView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'



# views.py
#
# def NewsUptadeView(request,title):
#     news_update = get_object_or_404(News, title=title,status=News.Status.Published)
#     context = {'news_update':news_update}
#     return render(request,'crud/update.html',context)

# class NewsUptadeView(UpdateView):
#     model = News
#     fields = ['title', 'slug', 'body', 'image', 'status']
#     template_name = 'crud/update.html'
#     def queryset(self):
#         news = self.model.objects.all()
#         return news

class NewsUptadeView(OnlyLoggedsuperUser,UpdateView):
    model = News
    fields = ['title', 'body', 'image', 'status']
    template_name = 'crud/update.html'

    def get_object(self, queryset=None):
        # URL orqali kelgan 'title' qiymati asosida obyektni olish
        title = self.kwargs.get('title')
        return self.model.objects.get(title=title)


class NewsCreateView(OnlyLoggedsuperUser,CreateView):
    model = News
    template_name = 'crud/create.html'
    fields = ('title','title_uz','title_en','title_ru','body','body_uz','body_en','body_ru','slug','slug_uz','slug_en','slug_ru', 'image', 'category', 'status')


class NewsDeleteView(OnlyLoggedsuperUser,DeleteView):
    model = News
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('home')
    def get_object(self, queryset=None):
        # URL orqali kelgan 'title' qiymati asosida obyektni olish
        title = self.kwargs.get('title')
        return self.model.objects.get(title=title)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    admin_users = User.objects.filter(is_superuser=True)
    comments = Comentary.objects.filter(active=True)
    context = {
        'admin_users':admin_users,
        'comments':comments,
    }
    return render(request, 'pages/admin_page.html', context)

class SearchResultsView(ListView):
    model = News
    template_name = 'news/search_result.html'
    context_object_name = 'barcha_yangiliklar'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(
            Q(title__icontains=query)|Q(body__icontains=query)
        )

def Disable_comment(request,comment_id):
    comment = get_object_or_404(Comentary, id=comment_id)
    comment.active = False
    comment.save()
    return redirect('admin_page')









