from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Report
from .serializers import ReportSerializer

from textblob import TextBlob  # ✅ For sentiment

class ReportCreateView(generics.ListCreateAPIView):
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Each user sees only *their* reports
        return Report.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # 1️⃣ Get raw description from request
        raw_description = self.request.data.get('description')

        # 2️⃣ Run sentiment analysis
        blob = TextBlob(raw_description)
        score = blob.sentiment.polarity  # -1.0 to +1.0

        # 3️⃣ Save Report without description yet
        report = serializer.save(
            user=self.request.user,
            sentiment_score=score
        )

        # 4️⃣ Encrypt the description & save
        report.set_description(raw_description)
        report.save()
