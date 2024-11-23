from django.db import models

class Organization(models.Model):

    name = models.CharField(max_length=255)
    bio_waste = models.IntegerField(default=0)  # количество биоотходов
    glass = models.IntegerField(default=0)     # количество стекла
    plastic = models.IntegerField(default=0)   # количество пластика

    def __str__(self):
        return self.name

class Storage(models.Model):
    name = models.CharField(max_length=255)
    bio_waste_capacity = models.IntegerField()
    glass_capacity = models.IntegerField()
    plastic_capacity = models.IntegerField()
    bio_waste_current = models.IntegerField(default=0)
    glass_current = models.IntegerField(default=0)
    plastic_current = models.IntegerField(default=0)
    latitude = models.FloatField()
    longitude = models.FloatField()
    type = models.CharField(max_length=50, default='general')
    capacity = models.IntegerField(default=0)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    def can_accept(self, waste_type, amount):
        if waste_type == 'bio_waste':
            return self.bio_waste_current + amount <= self.bio_waste_capacity
        elif waste_type == 'glass':
            return self.glass_current + amount <= self.glass_capacity
        elif waste_type == 'plastic':
            return self.plastic_current + amount <= self.plastic_capacity
        return False
