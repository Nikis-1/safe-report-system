from django.db import models
from django.conf import settings
from cryptography.fernet import Fernet

# Your fixed Fernet key (make sure it's correct!)
FERNET_KEY = b'DarFNESBHHcqrifpTM1b55pT3XW_kEr6zvpZfI2oAO8='
fernet = Fernet(FERNET_KEY)

class Report(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    encrypted_description = models.BinaryField()
    location = models.CharField(max_length=255, default='Unknown')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('In Progress', 'In Progress'),
            ('Resolved', 'Resolved')
        ],
        default='Pending'
    )

    # ✅ NEW: store sentiment score
    sentiment_score = models.FloatField(null=True, blank=True)

    def set_description(self, raw_text):
        self.encrypted_description = fernet.encrypt(raw_text.encode())

    def get_description(self):
        return fernet.decrypt(self.encrypted_description).decode()

    def __str__(self):
        return f"{self.title} by {self.user.username}"