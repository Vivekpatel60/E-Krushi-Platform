from django.db import models
from django.contrib.auth.models import User

class FarmerData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    farmer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    village = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    farm_id = models.CharField(max_length=50, unique=True)
    owner = models.CharField(max_length=100)
    water_source = models.CharField(max_length=20, choices=[('Canal', 'Canal'), ('Borewell', 'Borewell'), ('Rain-fed', 'Rain-fed'), ('Drip farming', 'Drip farming')])
    irrigation_type = models.CharField(max_length=50)
    organic_type = models.CharField(max_length=15, choices=[('Organic', 'Organic'), ('Non-organic', 'Non-organic')])
    aadhaar_number = models.CharField(max_length=12, unique=True, null=True, blank=True)
    aadhaar_image = models.ImageField(upload_to='aadhaar_images/', null=True, blank=True)
    crop_type = models.CharField(max_length=100)
    land_area = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.farmer_name} - {self.crop_type}"

    class Meta:
        ordering = ['-created_at']