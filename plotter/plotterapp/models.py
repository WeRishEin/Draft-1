from django.db import models

class Gene(models.Model):
    symbol = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    direct_evidence = models.CharField(max_length=255)
    inference_gene_symbol = models.CharField(max_length=255)
    inference_score = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Genes'

    def __str__(self):
        return self.symbol
