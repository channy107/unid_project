from django.db import models

# 상속
# SQL create table Person (name varchar(10), )
# ORM - Object Relational Mapper

class Person(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField
    c_date = models.DateTimeField
