from django.db import models

# Create your models here.
class Realisator(models.Model):
    name = models.CharField(max_length=350)

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(verbose_name="Titre", max_length=200)
    release_date = models.DateTimeField(verbose_name="Date de Sortie")
    # vote = models.IntegerField()
    # score = models.IntegerField(default=0)
    realisator = models.ForeignKey(Realisator, on_delete=models.CASCADE, verbose_name="Réalisateur")

    def __str__(self):
        return self.title

    # @property
    # def get_score(self):
    #     return self.vote
