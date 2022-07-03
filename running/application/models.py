from django.db import models
from django.contrib.auth.models import User



class Runner(models.Model):
    FOR_WHAT = (
        ('Maraphone', 'Пробігти марафон'),
        ('Tonuse', 'Для тонусу'),
        ('Don*t live', 'Не можеш жити без бігу')
    )
    SEX = (
        ('M', 'чоловік'),
        ('W', 'жінка'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    runer_name = models.CharField(max_length=255, verbose_name='поганялово', default=False)
    age = models.IntegerField(default=0, 
                                    verbose_name='твій вік/вікова категорія')
    why_u_run = models.CharField(max_length=255, choices=FOR_WHAT, 
                                        verbose_name='для чого ти бігаєш?')
    running_experience = models.CharField(default=0, max_length=255,
                                        verbose_name='біговий стаж (км/рік)')
    weight = models.DecimalField(default=0, 
                                    max_digits=5, decimal_places=1,
                                            verbose_name='вага')
    sex = models.CharField(max_length=255, choices=SEX, null=True,
                                                verbose_name='стать')
    max_duration = models.DecimalField(max_digits=5, decimal_places=2, default=0,
                                verbose_name="максимальна подолана відстань")


    def __str__(self):
        return f'id {self.id}: {self.user}'


