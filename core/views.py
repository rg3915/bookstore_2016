from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from django.views.generic import TemplateView, ListView, DetailView

from braces.views import GroupRequiredMixin
from .models import Customer, Book, Store


def home(request):
    return render(request, 'index.html')


def logged(request):
    return HttpResponse('Você está logado como {{ user.first_name }}')


def message(request):
    return HttpResponse('Acesso negado')


def customer_list(request):
    customers_all = Customer.objects.all()
    count = customers_all.count()

    paginator = Paginator(customers_all, 8)  # mostra 8 itens por pagina
    page = request.GET.get('page')
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        customers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        customers = paginator.page(paginator.num_pages)
    ctx = {'customers': customers, 'count': count, 'name_plural': 'clientes'}
    return render(request, 'core/customer_list.html', ctx)


class CounterMixin(object):

    def get_context_data(self, **kwargs):
        ''' counter registers '''
        context = super(CounterMixin, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class BookList(CounterMixin, ListView):
    template_name = 'core/book_list.html'
    model = Book
    context_object_name = 'books'
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        context['name_plural'] = 'livros'
        return context

    def get_queryset(self):
        ''' use prefetch_related for m2m performance '''
        b = Book.objects.prefetch_related('authors').all()
        return b


class StoreList(CounterMixin, ListView):
    template_name = 'core/store_list.html'
    model = Store
    context_object_name = 'stores'

    def get_context_data(self, **kwargs):
        context = super(StoreList, self).get_context_data(**kwargs)
        context['name_plural'] = 'lojas'
        return context

    def get_queryset(self):
        ''' use prefetch_related for m2m performance '''
        s = Store.objects.prefetch_related('books').all()
        return s


class StoreDetail(DetailView):
    template_name = 'core/store_detail.html'
    model = Store


class SomeProtectedView(GroupRequiredMixin, TemplateView):
    template_name = 'core/logged.html'
    group_required = u'Diretor'
