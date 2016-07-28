from django.conf.urls import url
from .views import ProductList, IndoorProductList, OutdoorProductList, ProductDetailView, CaseStudieList, CaseStudieDetailView, AutomotiveCaseStudieList, InstitutionalCaseStudieList, InsdustrialCaseStudieList, AboutView, ContactView, WhyAmerlightView, WhyLedView, AdvantageView, SignLightView, EstimateView, SalesSearchView, StartView

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^products/$', ProductList.as_view(), name='products'),
    url(r'^products/indoor/$', IndoorProductList.as_view(), name='indoor_products'),
    url(r'^products/outdoor/$', OutdoorProductList.as_view(), name='outdoor_products'),
    url(r'^proudcts/(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='product_detail'),

    url(r'^case_studies/$', CaseStudieList.as_view(), name='case_studies'),
    url(r'^case_studies/automotive/$', AutomotiveCaseStudieList.as_view(), name='automotive_projects'),
    url(r'^case_studies/institutional/$', InstitutionalCaseStudieList.as_view(), name='institutional_projects'),
    url(r'^case_studies/industrial/$', InsdustrialCaseStudieList.as_view(), name='industrial_projects'),
    url(r'^case_studies/(?P<slug>[\w-]+)/$', CaseStudieDetailView.as_view(), name='case_detail'),

    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^why_amerlight/$', WhyAmerlightView.as_view(), name='why_amerlight'),
    url(r'^why_led/$', WhyLedView.as_view(), name='why_led'),
    url(r'^advantage/$', AdvantageView.as_view(), name='advantage'),
    url(r'^sign_light/$', SignLightView.as_view(), name='sign_light'),
    url(r'^estimate/$', EstimateView.as_view(), name='estimate'),
    url(r'^sales_search/$', SalesSearchView.as_view(), name='sales_search'),
    url(r'^start/$', StartView.as_view(), name='start'),

]
