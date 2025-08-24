from django.db import models
from django.views.debug import default_urlconf

from account.models import User
from django_jalali.db import models as jmodels


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='category',
                               verbose_name='دسته بندی های دیگر')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    image = models.ImageField(verbose_name='عکس')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = "دسته بندی ها"


class AmountCaffeine(models.Model):
    title = models.CharField(max_length=100, verbose_name='میزان کافئین')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "میزان کافئین"


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان محصول')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی')
    image1 = models.ImageField(verbose_name='عکس اول')
    image2 = models.ImageField(null=True, verbose_name='عکس دوم')
    image3 = models.ImageField(null=True, verbose_name='عکس سوم')
    image4 = models.ImageField(null=True, verbose_name='عکس چهارم')
    amountcaffeine = models.ManyToManyField(AmountCaffeine, verbose_name='میزان کافئین')
    price = models.IntegerField(null=True, blank=True, verbose_name='قیمت')
    discount = models.SmallIntegerField(verbose_name='تخفیف')
    origin = models.CharField(max_length=100, null=True, blank=True, verbose_name='خاستگاه')
    ingredient = models.CharField(max_length=200, null=True, blank=True, verbose_name='ماده تشکیل دهنده')
    introduction = models.TextField(verbose_name='مقدمه')
    stock = models.IntegerField(default=0, verbose_name='تعداد موجودی')
    best_selling = models.BooleanField(default=False, verbose_name='بهترین فروش')
    amazing = models.BooleanField(default=False, verbose_name='محصولات شگفت انگیز')
    create = jmodels.jDateTimeField(auto_now=True, verbose_name='تاریخ ثبت محصول')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = "محصولات"


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    title = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    create = jmodels.jDateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'کامنت محصول'
        verbose_name_plural = "کامنت محصولات"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='like')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.phone


class RatingProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'product',)
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.phone} rated {self.product.title} with {self.score}'

