from django.urls import path
from keyword_extractor.views import ExtractKeywordsView, index

urlpatterns = [
    path("api/extract_keywords/", ExtractKeywordsView.as_view(), name='extract_keywords'),
    path("", index, name="home"),
]
