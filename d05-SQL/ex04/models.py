from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True)
    episode_nb = models.PositiveIntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()

    class Meta:
        db_table = 'ex04_movies'

    def __str__(self):
        return self.title