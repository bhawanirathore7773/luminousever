"""
Phase 5: real Service/ServiceCategory/Industry views replace the Phase 3
"coming soon" placeholders. URL names are unchanged (index, industries) so
nothing that links via {% url %} needed to change; two new named routes
(detail, industry_detail) are added for the individual pages.
"""

from django.urls import path

from .views import IndustryDetailView, IndustryIndexView, SAPConsultingView, ServiceDetailView, ServiceIndexView

app_name = "services"

urlpatterns = [
    path("sap-consulting/", SAPConsultingView.as_view(), name="sap_consulting"),
    path("services/", ServiceIndexView.as_view(), name="index"),
    path("services/<slug:slug>/", ServiceDetailView.as_view(), name="detail"),
    path("industries/", IndustryIndexView.as_view(), name="industries"),
    path("industries/<slug:slug>/", IndustryDetailView.as_view(), name="industry_detail"),
]
