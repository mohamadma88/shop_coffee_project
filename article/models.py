from django.db import models
from account.models import User
from product.models import Category
from django_jalali.db import models as jmodels


class Article(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article',verbose_name='نویسنده')
    title = models.CharField(max_length=200,verbose_name='عنوان')
    Category = models.ManyToManyField(Category, related_name='article',verbose_name='دسته بندی')
    image = models.ImageField(verbose_name='عکس')
    Introduction = models.TextField(verbose_name='مقدمه')
    text = models.TextField(verbose_name='بدنه مقاله')
    ingredient = models.TextField(blank=True,null=True,verbose_name='مواد لازم')
    recipe = models.TextField(verbose_name='رسپی' , blank=True,null=True)
    pub = models.BooleanField(verbose_name='منتشر شود؟')
    created_at = jmodels.jDateTimeField(auto_now_add=True,verbose_name='تاریخ انتشار')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
