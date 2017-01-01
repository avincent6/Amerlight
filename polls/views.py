from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import ListView
from django.views.generic import DetailView
from django import forms
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from .models import Choice, Question, Product, CaseStudie, Faq

from itertools import chain
def concat():
    all_case_studies = CaseStudie.objects.all()
    all_products = Product.objects.all()
    result_list = list(chain(all_case_studies, all_products))
    return result_list
def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })

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
    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context


class AboutView(generic.ListView):
    template_name = 'polls/about.html'
    context_object_name = 'about'
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context


class ContactView(generic.ListView):
    template_name = 'polls/contact.html'
    context_object_name = 'contact'
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context

class WhyAmerlightView(generic.ListView):
    template_name = 'polls/why_amerlight.html'
    context_object_name = 'why_amerlight'
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super(WhyAmerlightView, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context

class WhyLedView(generic.ListView):
    template_name = 'polls/why_led.html'
    context_object_name = 'why_led'
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super(WhyLedView, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context

class AdvantageView(generic.ListView):
    template_name = 'polls/advantage.html'
    context_object_name = 'advantage'
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super(AdvantageView, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context

class SignLightView(generic.ListView):
    template_name = 'polls/sign_light.html'
    context_object_name = 'sign_light'
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super(SignLightView, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context

class EstimateView(generic.ListView):
    template_name = 'polls/estimate.html'
    context_object_name = 'estimate'
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super(EstimateView, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context

class SalesSearchView(generic.ListView):
    template_name = 'polls/sales_search.html'
    context_object_name = 'sales_search'
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super(SalesSearchView, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context

class StartView(generic.ListView):
    template_name = 'polls/start.html'
    context_object_name = 'start'
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super(StartView, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context

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
    def get_context_data(self, **kwargs):
        context = super(IndoorProductList, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context

class OutdoorProductList(ListView):
    context_object_name = 'outdoor_product_list'
    queryset = Product.objects.filter(isOutdoor='True')
    template_name = 'polls/product.html'
    def get_context_data(self, **kwargs):
        context = super(OutdoorProductList, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context



class CaseStudieList(ListView):
    context_object_name = 'all_case_studies'
    model = CaseStudie
    template_name = 'polls/case.html'
    def get_context_data(self, **kwargs):
        context = super(CaseStudieList, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context

class CaseStudieDetailView(DetailView):
    context_object_name = 'casestudie'
    queryset = CaseStudie.objects.all()
    template_name = 'polls/case_detail.html'
    def get_context_data(self, **kwargs):
        context = super(CaseStudieDetailView, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context

class AutomotiveCaseStudieList(ListView):
    context_object_name = 'automotive_project_list'
    queryset = CaseStudie.objects.filter(isAutomotive='True')
    template_name = 'polls/case.html'
    def get_context_data(self, **kwargs):
        context = super(AutomotiveCaseStudieList, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context

class InstitutionalCaseStudieList(ListView):
    context_object_name = 'institutional_project_list'
    queryset = CaseStudie.objects.filter(isInstitutional='True')
    template_name = 'polls/case.html'
    def get_context_data(self, **kwargs):
        context = super(InstitutionalCaseStudieList, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context

class InsdustrialCaseStudieList(ListView):
    context_object_name = 'industrial_project_list'
    queryset = CaseStudie.objects.filter(isIndustrial='True')
    template_name = 'polls/case.html'
    def get_context_data(self, **kwargs):
        context = super(InsdustrialCaseStudieList, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context

class FaqView(generic.ListView):
    context_object_name = 'frequently_asked_questions'
    queryset = Faq.objects.all()
    template_name = 'polls/faq.html'
    def get_context_data(self, **kwargs):
        context = super(FaqView, self).get_context_data(**kwargs)
        context['all_case_studies'] = CaseStudie.objects.all()
        context['all_products'] = Product.objects.all()
        # And so on for more models
        return context
