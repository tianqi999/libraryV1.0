# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Readertype(models.Model):
    rtid = models.AutoField(primary_key=True)
    typename = models.CharField(unique=True, max_length=50, blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    cprice = models.IntegerField(blank=True, null=True)
    validity = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'readertype'

class Readerinfo(models.Model):
    rid = models.AutoField(primary_key=True)
    rname = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=4, blank=True, null=True)
    barcode = models.CharField(db_column='BARCODE', unique=True, max_length=30, blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateField(blank=True, null=True)
    papertype = models.CharField(db_column='paperType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    paperno = models.CharField(db_column='PAPERNO', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=100, blank=True, null=True)
    createdate = models.DateField(db_column='createDate', blank=True, null=True,auto_now_add=True)  # Field name made lowercase.
    address = models.CharField(max_length=100, blank=True, null=True)
    isdelete = models.IntegerField(blank=True, null=True,default=0)
    rtid = models.ForeignKey(Readertype,db_column='rtid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'readerinfo'
class Booktype(models.Model):
    btid = models.AutoField(primary_key=True)
    typename = models.CharField(unique=True, max_length=30, blank=True, null=True)
    btime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'booktype'
class Bookcase(models.Model):
    bcid = models.AutoField(primary_key=True)
    bcname = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookcase'

class Bookinfo(models.Model):
    bid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=70, blank=True, null=True)
    btid = models.ForeignKey(Booktype,db_column='btid', blank=True, null=True ,on_delete=models.SET_NULL)
    author = models.CharField(max_length=30, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(blank=True, null=True)
    bcid = models.ForeignKey(Bookcase,db_column='bcid', blank=True, null=True)
    pubilshing = models.CharField(max_length=70, blank=True, null=True)
    isdelete = models.IntegerField(blank=True, null=True,default=0)
    addtime = models.DateField(blank=True, null=True,auto_now_add=True)
    bookcode = models.CharField( unique=True, max_length=30, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bookinfo'
class Bookback(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rid = models.ForeignKey(Readerinfo,db_column='rid', blank=True, null=True)
    bid = models.ForeignKey(Bookinfo,db_column='bid', blank=True, null=True)
    backtime = models.DateTimeField(blank=True, null=True)
    operator = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookback'


class Borrow(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rid = models.ForeignKey(Readerinfo, models.DO_NOTHING, db_column='rid', blank=True, null=True)
    bid = models.ForeignKey(Bookinfo, models.DO_NOTHING, db_column='bid', blank=True, null=True)
    borrowtime = models.DateTimeField(blank=True, null=True)
    backtime = models.DateTimeField(blank=True, null=True)
    ifback = models.IntegerField(blank=True, null=True,default=0)

    class Meta:
        managed = False
        db_table = 'borrow'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Library(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    libraryname = models.CharField(max_length=50, blank=True, null=True)
    curator = models.CharField(max_length=10, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(blank=True, null=True)
    introduce = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library'


class Manager(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user = models.CharField(unique=True, max_length=30, blank=True, null=True)
    pwd = models.CharField(max_length=30, blank=True, null=True)
    sysset = models.IntegerField(blank=True, null=True)
    readerset = models.IntegerField(blank=True, null=True)
    bookset = models.IntegerField(blank=True, null=True)
    borrowset = models.IntegerField(blank=True, null=True)
    sysquery = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager'
