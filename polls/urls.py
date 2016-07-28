from django.conf.urls import url
from .views import ProductList, IndoorProductList, OutdoorProductList, ProductDetailView, CaseStudieList, CaseStudieDetailView, AutomotiveCaseStudieList, InstitutionalCaseStudieList, InsdustrialCaseStudieList, AboutView

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

]
