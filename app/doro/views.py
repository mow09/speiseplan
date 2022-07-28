from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist

from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Q

from collections import namedtuple

from doro.forms import ContactForm
from content.models import Info, Opening, OwlImage, Intro, Place
from food.models import Meal, Category
from users.models import Contact


def layer3_context():
    return Opening.objects.all()


class BaseTemplateView(TemplateView):
    """A base-view for all sites needed context."""
    title = None
    urls_stuff = [
        # WARNING make sure you have them all in doro.urls contained!!
        {
            'url': '/',
            'name': 'Home',
        },
        # {
        #     'url': '/author/',
        #     'name': 'Author-',
        # },
        # {
        #     'url': '/create/',
        #     'name': 'Create-',
        # },
        # {
        #     'url': '/details/',
        #     'name': 'Details-',
        # },
        # {
        #     'url': '/explore/',
        #     'name': 'Explore',
        # },
        # IS right TODO
        {
            'url': '/produktpalette/',
            # 'name': 'Produkte',
            'name': 'Produktpalette',
        },
        # {
        #     'url': '#',
        #     'name': 'Freibackhaus-Sortiment',
        # },
        # {
        #     'url': '#',
        #     'name': 'Korngesundes Handwerk ,
        # },
        {
            'url': None,
            # 'name': 'Gut',
            'name': 'Gut-zu-wissen',
            'sub': [
                {
                    'url': '#',
                    'name': 'Lebensmittelhinweise',
                    # 'name': 'Allergene und Zusatzstoffeverordnung',
                },
                {
                    'url': '#',
                    'name': 'Hygienefakten',
                    # 'name': 'Aktuelles zur pandemische Lage/ Hygiene Hinweise',
                },
            ]},
        {
            'url': None,
            'name': 'Über uns',
            'sub': [
                {
                    'url': '#',
                    'name': 'Schlözers',
                },
                {
                    'url': '#',
                    'name': 'Schübi',
                },
            ]},
        {
            'url': None,
            'name': 'Weiteres',
            'sub': [
                {
                    'url': '#',
                    'name': 'Lageplan',
                },
                {
                    'url': '/kontakt/',
                    # 'name': 'Kontakt',
                    'name': 'Kontaktformular',
                },
            ]},
    ]

    class Meta:
        abstract = True

    def mark_active_page(self, current_url):
        # TODO test this !
        # TODO run a test that just checks that all doro.urls ar in that BaseV
        for i, each in enumerate(self.urls_stuff):
            if each['url'] == current_url:
                self.urls_stuff[i]['active'] = True
            else:
                self.urls_stuff[i]['active'] = False
        return self.urls_stuff

    def get_current_url(self):
        return self.request.get_full_path()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        host = self.request.get_host()
        current_url = self.get_current_url()
        context['title'] = self.title
        context['urls_stuff'] = self.mark_active_page(current_url)
        return context


class SubBaseTemplateView(BaseTemplateView):

    class Meta:
        abstract = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_url = self.get_current_url()
        try:
            context['intro'] = Intro.get_intro(current_url)
        except ObjectDoesNotExist as e:
            context['intro'] = ''
        return context


class IndexView(BaseTemplateView):
    template_name = "doro/index.html"
    title = 'Index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = Info.get_index_info()
        context['owl_images'] = OwlImage.objects.all()
        # ['logo/bistro.jpg', 'logo/cafe.jpg', 'images/banner-02.png', ]
        context['openings'] = layer3_context()
        return context


class AuthorView(SubBaseTemplateView):
    template_name = "doro/author.html"


class CreateView(SubBaseTemplateView):
    template_name = "doro/create.html"


# class DetailsView(DetailView):
class DetailsView(DetailView, SubBaseTemplateView):
    template_name = "doro/details.html"
    model = Meal
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        self.object = self.model.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context['openings'] = layer3_context()
        return context


class ExploreView(SubBaseTemplateView):
    template_name = "doro/explore.html"


class PlaceView(SubBaseTemplateView, DetailView):
    template_name = "doro/place.html"
    model = Place
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        slug = self.kwargs['slug']
        self.object = self.model.objects.get(slug=slug)
        self.title = self.object.name
        context = super().get_context_data(**kwargs)
        context['openings'] = layer3_context()
        context['meal_count'] = self.object.meals.all().count()
        context['vegan_count'] = self.object.meals.filter(
            Q(vegan=True) | Q(vegetarian=True)).count()
        return context


class ContactView(CreateView, FormView):
    # class ContactView(SubBaseTemplateView, CreateView):
    template_name = "doro/contact.html"
    model = Contact

    form_class = ContactForm
    # success_url = reverse_lazy("user:overview")
    success_url = reverse_lazy("doro:contact_post")
    success_message = "Nachricht wurde übermittelt."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm
        return context

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class ProductsView(SubBaseTemplateView):
    template_name = "doro/products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Meal.objects.filter(show=True)
        context['categories'] = Category.objects.filter()
        return context


class SuccessView(SubBaseTemplateView):
    template_name = "doro/contact_success.html"
