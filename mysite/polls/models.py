from datetime import date

from django.db import models

# Create your models here.

'''
| django_migrations   |

| polls_choice        |
| question_meta

| polls_blog          |
| polls_author        |
| polls_entry         |
| polls_entry_authors |
'''


class Dog(models.Model):
    name = models.CharField(max_length=100)
    data = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100)
    # test_migrate = models.CharField(max_length=100,default='fenglvzi')
    tagline = models.TextField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingback = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class Meta:
        db_table = 'question_meta'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
