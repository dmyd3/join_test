from django.db import models


# Relacionamentos 1-1
class Modelo1(models.Model):
    name = models.CharField(max_length=100)


class Modelo2(models.Model):
    name = models.CharField(max_length=100)
    model1 = models.OneToOneField(
        Modelo1,
        on_delete=models.CASCADE,
        related_name='model2'
    )


# Relacionamento 1-N
class Modelo3(models.Model):
    name = models.CharField(max_length=100)


class Modelo4(models.Model):
    name = models.CharField(max_length=100)
    model3 = models.ForeignKey(
        Modelo3,
        on_delete=models.CASCADE,
        related_name='model4'
    )


# Relacionamento N-N
class Modelo5(models.Model):
    name = models.CharField(max_length=100)


class Modelo6(models.Model):
    name = models.CharField(max_length=100)
    model5 = models.ManyToManyField(
        to=Modelo5,
        related_name='model6'
    )