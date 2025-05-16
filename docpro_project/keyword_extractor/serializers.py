# keyword_extractor/serializers.py
from rest_framework import serializers

class KeywordRequestSerializer(serializers.Serializer):
    text = serializers.CharField()
    num_keywords = serializers.IntegerField(default=10, required=False)
