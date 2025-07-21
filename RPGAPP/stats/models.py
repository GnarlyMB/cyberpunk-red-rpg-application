from django.db import models

class NpcStatistics(models.Model):
    name_text = models.CharField(max_length=200)
    class_text = models.CharField(max_length=200)
    health_int = models.IntegerField()
    weapons_text = models.CharField()
    cyberware_text = models.CharField()
    cooldowns_bool = models.BooleanField()



