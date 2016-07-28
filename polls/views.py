from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import ListView
from django.views.generic import DetailView


from .models import Choice, Question, Product, CaseStudie

from itertools import chain
def concat():
    all_case_studies = CaseStudie.objects.all()
    all_products = Product.objects.all()
    result_list = list(chain(all_case_studies, all_products))
    return result_list


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'home_list'
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()

        # And so on for more models
        return context


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class ProductList(ListView):
    model = Product
    template_name = 'polls/product.html'
    context_object_name = 'all_products'


class AboutView(generic.ListView):
    template_name = 'polls/about.html'
    context_object_name = 'about'
    all_case_studies = CaseStudie.objects.all()
    all_products = Product.objects.all()
    queryset = list(chain(all_products, all_case_studies))

class ProductDetailView(DetailView):
    context_object_name = 'product'
    queryset = Product.objects.all()
    template_name = 'polls/product_detail.html'
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context




class IndoorProductList(ListView):
    context_object_name = 'indoor_product_list'
    queryset = Product.objects.filter(isIndoor='True')
    template_name = 'polls/product.html'

class OutdoorProductList(ListView):
    context_object_name = 'outdoor_product_list'
    queryset = Product.objects.filter(isOutdoor='True')
    template_name = 'polls/product.html'


class CaseStudieList(ListView):
    context_object_name = 'all_case_studies'
    model = CaseStudie
    template_name = 'polls/case.html'

class CaseStudieDetailView(DetailView):
    context_object_name = 'casestudie'
    queryset = CaseStudie.objects.all()
    template_name = 'polls/case_detail.html'

class AutomotiveCaseStudieList(ListView):
    context_object_name = 'automotive_project_list'
    queryset = CaseStudie.objects.filter(isAutomotive='True')
    template_name = 'polls/case.html'

class InstitutionalCaseStudieList(ListView):
    context_object_name = 'institutional_project_list'
    queryset = CaseStudie.objects.filter(isInstitutional='True')
    template_name = 'polls/case.html'

class InsdustrialCaseStudieList(ListView):
    context_object_name = 'industrial_project_list'
    queryset = CaseStudie.objects.filter(isIndustrial='True')
    template_name = 'polls/case.html'
