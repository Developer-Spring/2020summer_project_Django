from django.db import models

# Create your models here.

class Document(models.Model):
    INVESTOR_TYPE = [
        ('1', '상장기업'),
        ('2', '비상장기업'),
        ('3', '개인사업자'),
    ]
    InvestorType = models.CharField(max_length=10, choices=INVESTOR_TYPE)
    # investor_type = models.CharField(max_length=1, choices=INVESTOR_TYPE)
    asset = models.TextField()
    debt = models.IntegerField()
    foreignassets = models.IntegerField()
    foreigndebt = models.IntegerField()
    year_export = models.IntegerField()
    year_import = models.IntegerField()
    investment = models.IntegerField()
    #
    # def __str__(self):
    #     return self.InvestorType