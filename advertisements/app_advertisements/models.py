from django.db import models

class Advetisement(models.Model):
    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=3)
    auction = models.BooleanField(verbose_name='Торг', help_text='Укажите если возможен торг')
    date_creat = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    id = models.CharField(verbose_name="id", max_length=64, primary_key=True)