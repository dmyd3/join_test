from django.db import models
from django.db.models.fields import DateField
import datetime

# Create your models here.
# class UsedMovie (models.Model):
#     '''
#         Used movies by this system users,
#         only basic information
#     '''
#     release_year = models.PositiveIntegerField(
#         verbose_name=_('Release Year'),
#         validators=[MinValueValidator(1800)],
#     )

#     tmdb_id = models.CharField(
#         verbose_name=_('TMDB ID'),
#         max_length=30,
#         help_text=_('ID in The Movie DataBase'),
#         unique=True,
#         blank=False, null=False
#     )

#     def __str__(self):
#         return self.original_title +" - "+ str(self.release_year)

#     class Meta:
#         verbose_name = _('Used Movie')
#         verbose_name_plural = _('Used Movies')


class Cargo(models.Model):

    nome_cargo = models.CharField(
        verbose_name='Cargo',
        max_length=200,
        unique=True,
        blank=False, null=False
    )

    def __str__(self):
        return self.nome_cargo

class Pessoa(models.Model):

    nome = models.CharField(
        verbose_name='Nome',
        max_length=200,
        blank=False, null=False
    )

    id_cargo = models.ForeignKey(
        Cargo,
        on_delete=models.CASCADE,
        related_name='pessoa',
    )

    admissao = models.DateField(
        verbose_name='Data de Admissao',
        default=datetime.date.today,
    )

    def __str__(self):
        return self.nome +'::'+ self.id_cargo.nome_cargo

