from django.db import models

from account.infrastructure.orm.models import CustomUser

class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=100)
    phone = models.IntegerField()
    default = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.address}, {self.city}, {self.country}"
    

    class Meta:
        ordering = ['country', 'city']
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def save(self, *args, **kwargs):
        if self.default:
            Address.objects.filter(user=self.user, default=True).update(default=False)
        super().save(*args, **kwargs)