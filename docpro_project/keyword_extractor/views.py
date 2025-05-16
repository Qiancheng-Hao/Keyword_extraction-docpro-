# keyword_extractor/views.py

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .keyword_utils import extract_keywords

class ExtractKeywordsView(APIView):
    def post(self, request):
        try:
            data = request.data
            text = data.get('text', '')
            num_keywords = int(data.get('num_keywords', 10))
            keywords = extract_keywords(text, num_keywords)
            return Response({'keywords': keywords}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)

def index(request):
    return render(request, "index.html")