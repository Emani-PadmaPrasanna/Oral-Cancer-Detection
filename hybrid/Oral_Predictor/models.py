from django.db import models

# Create your models here.

class OralPrediction(models.Model):
    tumor_size=models.FloatField()
    tobacco_use=models.IntegerField()
    alcohol_consumption=models.IntegerField()
    reverse_smoking=models.IntegerField()
    restricted_mouth_opening=models.IntegerField()
    gender=models.IntegerField()
    age_group=models.IntegerField()
    classification=models.IntegerField()

    def _int_(self):
        return self.age_group