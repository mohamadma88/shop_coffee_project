from django.db import models


class Contact(models.Model):
    phone = models.CharField(max_length=100, null=True, blank=True,verbose_name='شماره تلفن')
    sub = models.CharField(max_length=100,null=True,blank=True,verbose_name='عنوان')
    text = models.CharField(max_length=1000,null=True,blank=True,verbose_name='متن دیدگاه')

    def __str__(self):
        return self.sub
    class Meta:
        verbose_name = 'ارتباط با ما'
        verbose_name_plural = 'ارتباط با ما'
