# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Entities(models.Model):
    hashtags = models.ForeignKey('Hashtag', models.DO_NOTHING, blank=True, null=True)
    urls = models.ForeignKey('Url', models.DO_NOTHING, blank=True, null=True)
    user_mentions_id_str = models.ForeignKey('UserMentions', models.DO_NOTHING, db_column='user_mentions_id_str', blank=True, null=True)
    symbols = models.ForeignKey('Symbol', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Entities'


class Hashtag(models.Model):
    indices = models.TextField()
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Hashtag'


class Place(models.Model):
    id_str = models.CharField(primary_key=True, max_length=900)
    url = models.TextField(blank=True, null=True)
    place_type = models.TextField()
    name = models.TextField()
    full_name = models.TextField()
    country_code = models.TextField()
    country = models.TextField()

    class Meta:
        managed = False
        db_table = 'Place'


class Symbol(models.Model):
    indices = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Symbol'


class Tweet(models.Model):
    id_str = models.CharField(primary_key=True, max_length=900)
    created_at = models.TextField()
    text = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    truncated = models.BooleanField()
    in_reply_to_status_id_str = models.TextField(blank=True, null=True)
    in_reply_to_user_id_str = models.TextField(blank=True, null=True)
    in_reply_to_screen_name = models.TextField(blank=True, null=True)
    user_id_str = models.ForeignKey('User', models.DO_NOTHING, db_column='user_id_str')
    coordinates = models.TextField(blank=True, null=True)
    place = models.ForeignKey(Place, models.DO_NOTHING, blank=True, null=True)
    is_quote_status = models.BooleanField()
    retweet_count = models.IntegerField()
    favorite_count = models.IntegerField(blank=True, null=True)
    entities = models.ForeignKey(Entities, models.DO_NOTHING, blank=True, null=True)
    favorited = models.BooleanField(blank=True, null=True)
    retweeted = models.BooleanField(blank=True, null=True)
    possibly_sensitive = models.BooleanField(blank=True, null=True)
    lang = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tweet'


class Url(models.Model):
    display_url = models.TextField()
    expanded_url = models.TextField()
    indices = models.TextField(blank=True, null=True)
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'Url'


class User(models.Model):
    id_str = models.CharField(primary_key=True, max_length=900)
    name = models.TextField(blank=True, null=True)
    screen_name = models.TextField()
    location = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    protected = models.BooleanField()
    verified = models.BooleanField()
    followers_count = models.IntegerField()
    friends_count = models.IntegerField()
    listed_count = models.IntegerField()
    favourites_count = models.IntegerField(blank=True, null=True)
    created_at = models.TextField()
    profile_banner_url = models.TextField(blank=True, null=True)
    profile_image_url_https = models.TextField(blank=True, null=True)
    default_profile = models.BooleanField(blank=True, null=True)
    default_profile_image = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


class UserMentions(models.Model):
    id_str = models.CharField(primary_key=True, max_length=900)
    indices = models.TextField()
    name = models.TextField(blank=True, null=True)
    screen_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User_Mentions'
