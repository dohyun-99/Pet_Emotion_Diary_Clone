from django.db import models

from account.models import User


# Create your models here.
class Pet(models.Model):
    GENDER_CHOICES = [
        ("W", "암컷"),
        ("M", "수컷"),
    ]
    KIND_CHOICES = [
        ("Cat", "고양이"),
        ("Dog", "강아지"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_pet")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    owner_name = models.CharField(max_length=15)
    birth_day = models.DateField()
    meet_day = models.DateField()
    name = models.CharField(max_length=15)
    kind = models.CharField(max_length=3, choices=KIND_CHOICES)
    image = models.ImageField(upload_to="pet_images/", null=True, blank=True)
    is_neutered = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Personality(models.Model):
    ACTIVITY_CHOICES = [
        ("A", "모험-A"),
        ("L", "안주-L"),
    ]
    RELATIONSHIP_CHOICES = [
        ("E", "외향-E"),
        ("I", "내향-I"),
    ]
    PROTO_DOG_CHOICES = [
        ("C", "교감-C"),
        ("W", "본능-W"),
    ]
    DEPENDENCE_CHOICES = [
        ("T", "신뢰-T"),
        ("N", "필요-N"),
    ]
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    activity = models.CharField(max_length=1, choices=ACTIVITY_CHOICES)
    relationship = models.CharField(max_length=1, choices=RELATIONSHIP_CHOICES)
    proto_dog = models.CharField(max_length=1, choices=PROTO_DOG_CHOICES)
    dependence = models.CharField(max_length=1, choices=DEPENDENCE_CHOICES)

    def __str__(self):
        return self.pet.name
