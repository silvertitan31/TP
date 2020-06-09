from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.


class Quiz(models.Model):
    """Model definition for Quiz App - needed for API."""

    question = models.CharField( max_length=300, blank=False, null=True)
    choice1 = models.CharField( max_length=300, blank=False, null=True)
    choice2 = models.CharField( max_length=300, blank=False, null=True)
    choice3 = models.CharField( max_length=300, blank=False, null=True)
    choice4 = models.CharField( max_length=300, blank=False, null=True)
    answer = models.PositiveIntegerField(default=0, blank=False, null=True, validators=[MinValueValidator(1), MaxValueValidator(4)])
    
    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural  = 'Quizes'

