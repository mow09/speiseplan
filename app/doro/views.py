from django.views.generic import TemplateView


class AuthorView(TemplateView):
    template_name = "doro/author.html"


class CreateView(TemplateView):
    template_name = "doro/create.html"


class DetailsView(TemplateView):
    template_name = "doro/details.html"


class ExploreView(TemplateView):
    template_name = "doro/explore.html"


class IndexView(TemplateView):
    template_name = "doro/index.html"
