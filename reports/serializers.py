from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    description = serializers.CharField(write_only=True)
    decrypted_description = serializers.CharField(read_only=True, source='get_description')
    location = serializers.CharField()

    class Meta:
        model = Report
        fields = [
            'id',
            'title',
            'description',
            'decrypted_description',
            'created_at',
            'sentiment_score'
        ]

    def create(self, validated_data):
        # Pop out the virtual field so it doesn’t get passed to Report()
        raw_description = validated_data.pop('description')
        # Pull user and score from context or kwargs if needed
        user = self.context['request'].user
        sentiment_score = validated_data.pop('sentiment_score', None)

        # Create the object WITHOUT description yet
        report = Report(
            user=user,
            title=validated_data['title'],
            sentiment_score=sentiment_score
        )

        # Encrypt and save
        report.set_description(raw_description)
        report.save()

        return report
