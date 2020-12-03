from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Organizer(models.Model):
  """ Организаторы """
  name = models.CharField("Организаторы", max_length=150)
  email = models.CharField("E-mail", max_length=60)
  password = models.CharField("Пароль", max_length=60)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Организатор"
    verbose_name_plural = "Организаторы"


class Teachers(models.Model):
  """ Преподаватели """
  name = models.CharField("Имя", max_length=150)
  email = models.CharField("E-mail", max_length=60)
  password = models.CharField("Пароль", max_length=60)
  organizer = models.ForeignKey(Organizer, verbose_name="Организатор", on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Преподаватель"
    verbose_name_plural = "Преподаватели"


class Groups(models.Model):
  """ Группы """
  name = models.CharField("Название", max_length=150)
  organizer = models.ForeignKey(Organizer, verbose_name="Организатор", on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Группа"
    verbose_name_plural = "Группы"


class Students(models.Model):
  """ Студенты """
  name = models.CharField("Имя", max_length=150)
  password = models.CharField("Пароль", max_length=60)
  group = models.ForeignKey(Groups, verbose_name="Группа", on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Студент"
    verbose_name_plural = "Студенты"


class Subjects(models.Model):
  """ Предметы """
  name = models.CharField("Предмет", max_length=150)
  teacher = models.ForeignKey(Teachers, verbose_name="Преподаватель", on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Предмет"
    verbose_name_plural = "Предметы"


class Lessons(models.Model):
  """ Занятия """
  title = models.CharField("Тема занятия", max_length=300, default="Theme")
  date = models.DateField("Дата", default=date.today)
  teacher = models.ForeignKey(Teachers, verbose_name="Имя", on_delete=models.CASCADE)
  group = models.ForeignKey(Groups, verbose_name="Группа", on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = "Занятие"
    verbose_name_plural = "Занятия"


class Reviews(models.Model):
  """ Отзывы """
  name = models.CharField("Название", max_length=150, default="review")
  date = models.DateField("Дата", default=date.today)
  lesson = models.ForeignKey(Lessons, verbose_name="Занятие", on_delete=models.CASCADE)
  student = models.ForeignKey(Students, verbose_name="Студент", on_delete=models.CASCADE)
  text = models.TextField("Отзыв")
  rating = models.PositiveIntegerField("Значение", default=0)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Отзыв"
    verbose_name_plural = "Отзывы"


