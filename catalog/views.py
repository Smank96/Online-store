from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from catalog.models import Contacts, Product, Category, Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator


class ProductListView(ListView):
    model = Product
    paginate_by = 6


class ContactsListView(ListView):
    model = Contacts


class ContactCreateView(CreateView):
    model = Contacts
    success_url = reverse_lazy('catalog:home')


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = ("product_name", "product_description", "product_picture", "category", "price")
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("product_name", "product_description", "product_picture", "category", "price")
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class ArticleListView(ListView):
    model = Article


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ("title", "body", "preview", "is_published")
    success_url = reverse_lazy('catalog:article_detail')

    def get_success_url(self):
        return reverse('catalog:article_detail', args=[self.object.slug])

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article

    fields = ("title", "slug", "body", "preview", "is_published")
    success_url = reverse_lazy('catalog:article_list')


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('catalog:article_list')
