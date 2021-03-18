# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tweet(models.Model):
    id_str = models.CharField(max_length=899)
    text = models.TextField()
    hashtags = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    user_id = models.TextField()
    geo = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    possibly_sensitive = models.BooleanField(blank=True, null=True)
    lang = models.CharField(max_length=3, blank=True, null=True)
    created_at = models.TextField()

    class Meta:
        managed = False
        db_table = 'Tweet'


class User(models.Model):
    id_str = models.CharField(primary_key=True, max_length=899)
    name = models.TextField()
    screen_name = models.TextField()
    location = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    followers_count = models.IntegerField(blank=True, null=True)
    friends_count = models.IntegerField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    verified = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'
