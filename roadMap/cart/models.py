from django.db import models

from user.models import Profile
from courses.models import Course

class Cart(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, through="CartItem")
    is_paid = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    @property
    def get_cart_price(self):
        result = 0
        if self.is_paid:
            for elm in self.cartitem_set.all():
                result += elm.price_paid
        else:
            for elm in self.cartitem_set.all():
                result += elm.course.price * elm.during_time
        return result

    class Meta:
        ordering = ["-created_date"]

    def __str__(self) -> str:
        return self.user.username

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    during_time = models.IntegerField()
    price_paid = models.IntegerField(null=True, blank=True)