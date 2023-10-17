# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PlyMeta(models.Model):
    ply_id = models.IntegerField(primary_key=True)
    ply_title = models.CharField(max_length=500, blank=True, null=True)
    ply_tag_lst = models.TextField(blank=True, null=True)
    ply_like_cnt = models.IntegerField(blank=True, null=True)
    ply_updt = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ply_meta'


class PlyTitleEmbedding(models.Model):
    emd_id = models.AutoField(primary_key=True)
    ply = models.ForeignKey(PlyMeta, models.DO_NOTHING, related_name='plytoemd')
    ply_title_emd = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ply_title_embedding'


class SongInPly(models.Model):
    songinply_id = models.AutoField(primary_key=True)
    ply = models.ForeignKey(PlyMeta, models.DO_NOTHING, blank=True, null=True, related_name='plyto')
    song = models.ForeignKey('SongMeta', models.DO_NOTHING, blank=True, null=True, related_name='songto')

    class Meta:
        managed = False
        db_table = 'song_in_ply'


class SongMeta(models.Model):
    song_id = models.IntegerField(primary_key=True)
    song_name = models.CharField(max_length=500, blank=True, null=True)
    artist_name_lst = models.TextField(blank=True, null=True)
    song_gnr_lst = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'song_meta'

class UserLog(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_title = models.CharField(max_length=500, blank=True, null=True)
    user_title_embedding = models.TextField(blank=True, null=True)
    user_song_id_lst = models.TextField(blank=True, null=True)
    user_tag_lst = models.TextField(blank=True, null=True)
    user_updt = models.CharField(max_length=100, blank=True, null=True)
    user_like_cnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_log'