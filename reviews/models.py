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


class Groups(models.Model):
  """ Группы """
  name = models.CharField("Название", max_length=150)
  organizer = models.ForeignKey(Organizer, verbose_name="Организатор", on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Группа"
    verbose_name_plural = "Группы"

class Subjects(models.Model):
  """ Предметы """
  name = models.CharField("Предмет", max_length=150)
  organizer = models.ForeignKey(Organizer, verbose_name="Организатор", on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Предмет"
    verbose_name_plural = "Предметы"


class Teachers(models.Model): 
  """ Преподаватели """
  name = models.CharField("Имя", max_length=150)
  email = models.CharField("E-mail", max_length=60)
  password = models.CharField("Пароль", max_length=60)
  organizer = models.ForeignKey(Organizer, verbose_name="Организатор", on_delete=models.SET_NULL, null=True)
  groups = models.ManyToManyField(Groups, verbose_name="Группы", related_name="teacher_groups")
  subjects = models.ManyToManyField(Subjects, verbose_name="Предметы", related_name="teacher_subjects")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Преподаватель"
    verbose_name_plural = "Преподаватели"


class Students(models.Model):
  """ Студенты """
  name = models.CharField("Имя", max_length=150)
  email = models.CharField("E-mail", max_length=60, null=True)
  password = models.CharField("Пароль", max_length=60)
  group = models.ForeignKey(Groups, verbose_name="Группа", on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Студент"
    verbose_name_plural = "Студенты"


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


class Сriterions(models.Model):
  """ Критерии """
  name = models.CharField("Название", max_length=300, default="Сriterions")
  # review = models.ForeignKey(Reviews, verbose_name="Отзыв", on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Критерий"
    verbose_name_plural = "Критерии"


class СriterionAnswers(models.Model):
  """ Критерии ответа """
  criterion = models.ForeignKey(Сriterions, verbose_name="Критерий", on_delete=models.CASCADE)
  rating = models.PositiveSmallIntegerField(verbose_name="Оценка", default="0")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Критерий ответ"
    verbose_name_plural = "Критерии ответ"


class Reviews(models.Model):
  """ Отзывы """
  name = models.CharField("Название", max_length=150, default="review")
  group = models.ForeignKey(Groups, verbose_name="Группа", on_delete=models.SET_NULL, null=True)
  teacher = models.ForeignKey(Teachers, verbose_name="Преподаватель", on_delete=models.SET_NULL, null=True)
  subject = models.ForeignKey(Subjects, verbose_name="Предмет", on_delete=models.SET_NULL, null=True)
  dateStart = models.DateField("Дата начала", default=date.today)
  dateEnd = models.DateField("Дата конца", default=date.today)
  # сriterions = models.ManyToManyField(Сriterions, verbose_name="Критерии", related_name="сriterions")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "Отзыв"
    verbose_name_plural = "Отзывы"

class Answers(models.Model):
  """ Ответы """
  date = models.DateField("Дата", default=date.today)
  review = models.ForeignKey(Reviews, verbose_name="Отзыв", on_delete=models.SET_NULL, null=True)
  availability = models.PositiveIntegerField("Доступность и понятность изложения материала", default=0)
  fascination = models.PositiveIntegerField("Увлекательность изложения материала", default=0)
  сomplexity = models.PositiveIntegerField("Сложность изученного материала", default=0)
  novelty = models.PositiveIntegerField("Новизна изученного материала", default=0)
  interest = models.PositiveIntegerField("Заинтересованность предметом", default=0)
  text = models.TextField("Текст")
  rating = models.PositiveIntegerField("Рейтинг", default=0)
  student = models.ForeignKey(Students, verbose_name="Студент", on_delete=models.SET_NULL, null=True)

  class Meta:
    verbose_name = "Ответ"
    verbose_name_plural = "Ответы"

 
