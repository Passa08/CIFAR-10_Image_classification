from django.db import models

class ImagePrediction(models.Model):
    image = models.ImageField(upload_to='images/')
    prediction = models.CharField(max_length=100, blank=True)
    confidence = models.FloatField(default=0.0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prediction} ({self.confidence:.2f}%)"

    class Meta:
        app_label = 'classifier'