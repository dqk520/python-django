# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class 11(models.Model):
    q = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '11'


class 20164(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    field_field = models.CharField(db_column='\u5907\u6ce8', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_0 = models.CharField(db_column='\u90e8\u95e8', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_1 = models.FloatField(db_column='\u5458\u5de5\u7f16\u53f7', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_2 = models.CharField(db_column='\u5de5\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_3 = models.CharField(db_column='\u59d3\u540d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_4 = models.FloatField(db_column='\u4eba\u6570', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_5 = models.CharField(db_column='\u5c97\u4f4d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_6 = models.CharField(db_column='\u85aa\u8d44\u5e8f\u5217', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_7 = models.FloatField(db_column='\u85aa\u8d44\u6807\u51c6', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_8 = models.CharField(db_column='\u52a0\u73ed\u8d39\u57fa\u6570', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_9 = models.FloatField(db_column='\u57fa\u672c\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_10 = models.FloatField(db_column='\u5c97\u4f4d\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1 = models.FloatField(db_column='\u7ee9\u6548\u5de5\u8d441', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_field_11 = models.FloatField(db_column='\u6708\u5ea6\u8003\u6838', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_12 = models.FloatField(db_column='\u5168\u5458\u7ee9\u6548\u6d6e\u52a8', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_13 = models.FloatField(db_column='\u8003\u6838\u589e\u51cf', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_14 = models.FloatField(db_column='\u9a7b\u5c9b\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_15 = models.FloatField(db_column='\u5de5\u9f84\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_16 = models.FloatField(db_column='\u8282\u65e5\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_17 = models.FloatField(db_column='\u901a\u8baf\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_18 = models.FloatField(db_column='\u5c97\u4f4d\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_19 = models.FloatField(db_column='\u7279\u6280\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_20 = models.FloatField(db_column='\u804c\u79f0\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_21 = models.FloatField(db_column='\u5b66\u5386\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_22 = models.FloatField(db_column='\u7efc\u5408\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_23 = models.FloatField(db_column='\u591c\u9910\u6d25\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_24 = models.FloatField(db_column='\u4e2d\u73ed\u5929\u6570', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_25 = models.FloatField(db_column='\u591c\u73ed\u5929\u6570', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_26 = models.FloatField(db_column='\u4e2d\u591c\u8fde\u73ed', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_27 = models.FloatField(db_column='\u65e5\u5e38\u52a0\u70b9', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_28 = models.FloatField(db_column='\u5468\u672b\u52a0\u73ed', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_29 = models.FloatField(db_column='\u65e5\u5e38\u52a0\u73ed', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_30 = models.FloatField(db_column='\u8282\u65e5\u52a0\u73ed', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_31 = models.FloatField(db_column='\u51fa\u52e4', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_3_field = models.FloatField(db_column='\u5de5\u4f243\u4e2a\u6708\u4ee5\u4e0a', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_32 = models.FloatField(db_column='\u63a2\u4eb2\u5a5a\u4e27\u966a\u54fa', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_3_field_0 = models.FloatField(db_column='\u75c5\u50473\u4e2a\u6708\u4ee5\u5185', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    number_3_field = models.FloatField(db_column='3\u4e2a\u6708\u4ee5\u4e0a\u75c5\u5047', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    field_field_33 = models.FloatField(db_column='\u4e8b\u5047\u65f7\u5de5', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_34 = models.FloatField(db_column='\u4ea7\u5047', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_35 = models.FloatField(db_column='\u4ea7\u5047\u6263\u53d1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_36 = models.FloatField(db_column='\u8bf7\u5047\u6263\u53d1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1_0 = models.FloatField(db_column='\u7efc\u5408\u680f1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_field_37 = models.FloatField(db_column='\u5e94\u53d1\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_38 = models.FloatField(db_column='\u5b9e\u53d1\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_39 = models.FloatField(db_column='\u517b\u8001\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_40 = models.FloatField(db_column='\u533b\u7597', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_41 = models.FloatField(db_column='\u5931\u4fdd', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_42 = models.FloatField(db_column='\u516c\u79ef\u91d1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_43 = models.FloatField(db_column='\u5b9e\u9645\u6263\u7a0e', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_44 = models.FloatField(db_column='\u4f01\u4e1a\u5e74\u91d1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_45 = models.FloatField(db_column='\u6c34\u7535\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_46 = models.FloatField(db_column='\u7269\u4e1a\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_47 = models.FloatField(db_column='\u5176\u5b83', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2 = models.FloatField(db_column='\u7ee9\u6548\u5de5\u8d442', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_field_48 = models.FloatField(db_column='\u804c\u52a1\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_49 = models.FloatField(db_column='\u56fa\u5b9a\u6d25\u8d34\uff08\u996d\u8d34\u3001\u804c\u79f0\u7b49\uff09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_50 = models.FloatField(db_column='\u4e34\u65f6\u6d25\u8d34\uff08\u6807\u5175\u3001\u5e08\u5e26\u5f92\u7b49\uff09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_51 = models.FloatField(db_column='\u6d25\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_52 = models.FloatField(db_column='\u81ea\u52a8\u5339\u914d\u6570\u636e', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_53 = models.FloatField(db_column='\u624b\u5de5\u8c03\u6574', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2_0 = models.FloatField(db_column='\u7efc\u5408\u680f2', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_2_1 = models.FloatField(db_column='\u5b9e\u53d1\u5de5\u8d442', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_field_54 = models.CharField(db_column='\u996d\u8d34\u6807\u51c6', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_55 = models.CharField(db_column='\u53d1\u653e\u91d1\u989d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_56 = models.CharField(db_column='\u8eab\u4efd\u8bc1\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_57 = models.CharField(db_column='\u94f6\u884c\u5361\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = '2016年4月'


class 20165(models.Model):
    field_field = models.CharField(db_column='\u5907\u6ce8', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_0 = models.CharField(db_column='\u90e8\u95e8', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_1 = models.CharField(db_column='\u5458\u5de5\u7f16\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_2 = models.CharField(db_column='\u5de5\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_3 = models.CharField(db_column='\u59d3\u540d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_4 = models.CharField(db_column='\u4eba\u6570', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_5 = models.CharField(db_column='\u5c97\u4f4d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_6 = models.CharField(db_column='\u85aa\u8d44\u5e8f\u5217', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_7 = models.CharField(db_column='\u85aa\u8d44\u6807\u51c6', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_8 = models.CharField(db_column='\u804c\u52a1\u8865\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_9 = models.CharField(db_column='\u52a0\u73ed\u8d39\u57fa\u6570', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_10 = models.CharField(db_column='\u57fa\u672c\u5de5\u8d44', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_11 = models.CharField(db_column='\u5c97\u4f4d\u5de5\u8d44', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1 = models.CharField(db_column='\u7ee9\u6548\u5de5\u8d441', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_field_12 = models.CharField(db_column='\u6708\u5ea6\u8003\u6838', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_13 = models.CharField(db_column='\u5168\u5458\u7ee9\u6548\u6d6e\u52a8', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_14 = models.CharField(db_column='\u8003\u6838\u589e\u51cf', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_15 = models.CharField(db_column='\u9a7b\u5c9b\u8865\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_16 = models.CharField(db_column='\u5de5\u9f84\u5de5\u8d44', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_17 = models.CharField(db_column='\u8282\u65e5\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_18 = models.CharField(db_column='\u901a\u8baf\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_19 = models.CharField(db_column='\u5c97\u4f4d\u8865\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_20 = models.CharField(db_column='\u7279\u6280\u8865\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_21 = models.CharField(db_column='\u804c\u79f0\u8865\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_22 = models.CharField(db_column='\u5b66\u5386\u8865\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_23 = models.CharField(db_column='\u7efc\u5408\u8865\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_24 = models.CharField(db_column='\u591c\u9910\u6d25\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_25 = models.CharField(db_column='\u4e2d\u73ed\u5929\u6570', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_26 = models.CharField(db_column='\u591c\u73ed\u5929\u6570', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_27 = models.CharField(db_column='\u4e2d\u591c\u8fde\u73ed', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_28 = models.CharField(db_column='\u65e5\u5e38\u52a0\u70b9', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_29 = models.CharField(db_column='\u5468\u672b\u52a0\u73ed', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_30 = models.CharField(db_column='\u8282\u65e5\u52a0\u73ed', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_31 = models.CharField(db_column='\u65e5\u5e38\u52a0\u73ed', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1_0 = models.CharField(db_column='\u8282\u65e5\u52a0\u73ed1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_field_32 = models.CharField(db_column='\u51fa\u52e4', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_3_field = models.CharField(db_column='\u5de5\u4f243\u4e2a\u6708\u4ee5\u4e0a', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_33 = models.CharField(db_column='\u63a2\u4eb2\u5a5a\u4e27\u966a\u54fa', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_3_field_0 = models.CharField(db_column='\u75c5\u50473\u4e2a\u6708\u4ee5\u5185', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    number_3_field = models.CharField(db_column='3\u4e2a\u6708\u4ee5\u4e0a\u75c5\u5047', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    field_field_34 = models.CharField(db_column='\u4e8b\u5047\u65f7\u5de5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_35 = models.CharField(db_column='\u4ea7\u5047', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_36 = models.CharField(db_column='\u4ea7\u5047\u6263\u53d1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_37 = models.CharField(db_column='\u8bf7\u5047\u6263\u53d1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_38 = models.CharField(db_column='\u81ea\u52a8\u5339\u914d\u6570\u636e', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_39 = models.CharField(db_column='\u624b\u5de5\u8c03\u6574', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1_1 = models.CharField(db_column='\u7efc\u5408\u680f1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_field_40 = models.CharField(db_column='\u5e94\u53d1\u5de5\u8d44', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_41 = models.CharField(db_column='\u5b9e\u53d1\u5de5\u8d44', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_42 = models.CharField(db_column='\u517b\u8001\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_43 = models.CharField(db_column='\u533b\u7597', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_44 = models.CharField(db_column='\u5931\u4fdd', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_45 = models.CharField(db_column='\u516c\u79ef\u91d1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_46 = models.CharField(db_column='\u5b9e\u9645\u6263\u7a0e', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_47 = models.CharField(db_column='\u4f01\u4e1a\u5e74\u91d1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_48 = models.CharField(db_column='\u6c34\u7535\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_49 = models.CharField(db_column='\u7269\u4e1a\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_50 = models.CharField(db_column='\u5176\u5b83', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2 = models.CharField(db_column='\u7ee9\u6548\u5de5\u8d442', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_1_2 = models.CharField(db_column='\u804c\u52a1\u8865\u8d341', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_field_51 = models.CharField(db_column='\u56fa\u5b9a\u6d25\u8d34\uff08\u996d\u8d34\u3001\u804c\u79f0\u7b49\uff09', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_52 = models.CharField(db_column='\u4e34\u65f6\u6d25\u8d34\uff08\u6807\u5175\u3001\u5e08\u5e26\u5f92\u7b49\uff09', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_53 = models.CharField(db_column='\u6d25\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1_3 = models.CharField(db_column='\u81ea\u52a8\u5339\u914d\u6570\u636e1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_1_4 = models.CharField(db_column='\u624b\u5de5\u8c03\u65741', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_2_0 = models.CharField(db_column='\u7efc\u5408\u680f2', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_1_5 = models.CharField(db_column='\u51fa\u52e41', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_field_54 = models.CharField(db_column='\u996d\u8d34\u6807\u51c6', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_55 = models.CharField(db_column='\u53d1\u653e\u91d1\u989d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_56 = models.CharField(db_column='\u8eab\u4efd\u8bc1\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_57 = models.CharField(db_column='\u94f6\u884c\u5361\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = '2016年5月'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BookbAuthor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'bookb_author'


class BookbBook(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    publisher = models.ForeignKey('BookbPublisher')

    class Meta:
        managed = False
        db_table = 'bookb_book'


class BookbBookAuthors(models.Model):
    book = models.ForeignKey(BookbBook)
    author = models.ForeignKey(BookbAuthor)

    class Meta:
        managed = False
        db_table = 'bookb_book_authors'
        unique_together = (('book', 'author'),)


class BookbPublisher(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'bookb_publisher'


class BooksAuthor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'books_author'


class BooksBook(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    publisher = models.ForeignKey('BooksPublisher')

    class Meta:
        managed = False
        db_table = 'books_book'


class BooksBookAuthors(models.Model):
    book = models.ForeignKey(BooksBook)
    author = models.ForeignKey(BooksAuthor)

    class Meta:
        managed = False
        db_table = 'books_book_authors'
        unique_together = (('book', 'author'),)


class BooksPublisher(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'books_publisher'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Gzzb1(models.Model):
    field_field = models.FloatField(db_column='\u65f6\u95f4', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_0 = models.FloatField(db_column='\u4ee3\u6263\u7a0e', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_1 = models.FloatField(db_column='\u5b9e\u9645\u6263\u7a0e', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_2 = models.FloatField(db_column='\u5b9e\u53d1\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2 = models.FloatField(db_column='\u5b9e\u53d1\u5de5\u8d442', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_field_3 = models.FloatField(db_column='\u5e94\u53d1\u5de5\u8d44\u603b', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_4 = models.FloatField(db_column='\u5b9e\u53d1\u5de5\u8d44\u603b', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_5 = models.CharField(db_column='\u8eab\u4efd\u8bc1\u53f7\u7801', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_6 = models.FloatField(db_column='\u5458\u5de5\u7f16\u53f7', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_7 = models.CharField(db_column='\u94f6\u884c\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_8 = models.CharField(db_column='\u4e0a\u6d77\u7f34\u7eb3\u4e2a\u7a0e', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2_field = models.FloatField(db_column='\u88682\u7ee9\u6548', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_1_field = models.FloatField(db_column='\u88681\u7ee9\u6548', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_9 = models.FloatField(db_column='\u666e\u901a\u52a0\u73ed\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    number_2_field = models.FloatField(db_column='2\u500d\u52a0\u73ed\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    field_field_10 = models.FloatField(db_column='\u6cd5\u5b9a\u52a0\u73ed\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_11 = models.FloatField(db_column='\u793e\u4fdd', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1_field_0 = models.FloatField(db_column='\u88681\u75c5\u5047\u6263', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2_field_0 = models.FloatField(db_column='\u88682\u75c5\u5047\u6263', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1_field_1 = models.FloatField(db_column='\u88681\u4e8b\u5047\u6263', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2_field_1 = models.FloatField(db_column='\u88682\u4e8b\u5047\u6263', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1_field_2 = models.FloatField(db_column='\u88681\u8f6e\u4f11\u6263', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2_field_2 = models.FloatField(db_column='\u88682\u8f6e\u4f11\u6263', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_12 = models.FloatField(db_column='\u5176\u4ed6\u6263', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2_field_3 = models.FloatField(db_column='\u88682\u6263', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_13 = models.FloatField(db_column='\u7ee9\u6548\u589e\u51cf', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_14 = models.FloatField(db_column='\u8d77\u5f81\u70b9', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2_field_4 = models.FloatField(db_column='\u6cd5\u5b9a\u548c2\u500d\u52a0\u73ed\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_15 = models.FloatField(db_column='\u8f6e\u4f11\u548c\u5176\u4ed6\u6263', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_16 = models.FloatField(db_column='\u75c5\u4e8b\u5047\u6263', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_17 = models.FloatField(db_column='\u5e94\u53d1\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_18 = models.FloatField(db_column='\u7eb3\u7a0e\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_19 = models.CharField(db_column='\u57fa\u5730', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_20 = models.CharField(db_column='\u5355\u4f4d\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_21 = models.FloatField(db_column='\u52a0\u73ed\u57fa\u6570', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_22 = models.CharField(db_column='\u5355\u4f4d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_23 = models.CharField(db_column='\u5de5\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_24 = models.CharField(db_column='\u59d3\u540d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_25 = models.FloatField(db_column='\u7f3a\u52e4', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_26 = models.FloatField(db_column='\u52a0\u73ed\u65e5', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_27 = models.FloatField(db_column='\u4e8c\u500d\u65e5', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_28 = models.FloatField(db_column='\u51fa\u52e4', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_29 = models.FloatField(db_column='\u6cd5\u5b9a\u65e5', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_30 = models.FloatField(db_column='\u75c5\u5047\u65e5', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_3_field = models.CharField(db_column='\u75c5\u50473\u6708', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_31 = models.FloatField(db_column='\u5176\u4ed6\u65e5', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_32 = models.FloatField(db_column='\u8f6e\u4f11\u65e5', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_33 = models.FloatField(db_column='\u5de5\u8d44\u6807\u51c6', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_34 = models.FloatField(db_column='\u5c97\u4f4d\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_35 = models.FloatField(db_column='\u7ee9\u6548\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1 = models.FloatField(db_column='\u7ee9\u6548\u589e\u51cf1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_2_0 = models.FloatField(db_column='\u7ee9\u6548\u589e\u51cf2', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_field_36 = models.FloatField(db_column='\u804c\u52a1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_37 = models.FloatField(db_column='\u9a7b\u5c9b', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_38 = models.FloatField(db_column='\u5de5\u9f84', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_39 = models.FloatField(db_column='\u4f19\u98df\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_40 = models.FloatField(db_column='\u4e2d\u591c\u73ed\u6d25\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_41 = models.FloatField(db_column='\u8282\u65e5\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1_0 = models.FloatField(db_column='\u7efc\u5408\u680f1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_2_1 = models.FloatField(db_column='\u7efc\u5408\u680f2', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_field_42 = models.FloatField(db_column='\u6c34\u7535\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_43 = models.FloatField(db_column='\u517b\u8001\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_44 = models.FloatField(db_column='\u533b\u7597', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_45 = models.FloatField(db_column='\u5931\u4fdd', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_46 = models.FloatField(db_column='\u516c\u79ef\u91d1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_47 = models.FloatField(db_column='\u6263\u53d1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_48 = models.FloatField(db_column='\u996d\u8d34\u57fa\u6570', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_49 = models.CharField(db_column='\u5206\u7c7b', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_50 = models.FloatField(db_column='\u901a\u8baf\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_51 = models.CharField(db_column='\u5c97\u4f4d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_52 = models.CharField(db_column='\u5b66\u5386', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_53 = models.CharField(db_column='\u5165\u53f8\u65f6\u95f4', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_54 = models.CharField(db_column='\u5bb6\u5ead\u4f4f\u5740', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_55 = models.CharField(db_column='\u8f6c\u6b63\u65e5\u671f', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_56 = models.FloatField(db_column='\u6027\u522b', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_57 = models.CharField(db_column='\u5e8f\u5217\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_58 = models.CharField(db_column='\u793e\u4fdd\u7f16\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_59 = models.CharField(db_column='\u516c\u79ef\u91d1\u7f16\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_60 = models.FloatField(db_column='\u5b66\u5386\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_61 = models.FloatField(db_column='\u804c\u79f0\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_62 = models.FloatField(db_column='\u7279\u6280\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_63 = models.FloatField(db_column='\u5c97\u4f4d\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_64 = models.FloatField(db_column='\u6d25\u8d34\u5408\u8ba1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_65 = models.CharField(db_column='\u5de5\u8d44\u5236', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'gzzb1'


class Gzzb3(models.Model):
    field_field = models.CharField(db_column='\u65f6\u95f4', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_0 = models.CharField(db_column='\u4ee3\u6263\u7a0e', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_1 = models.CharField(db_column='\u5b9e\u9645\u6263\u7a0e', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_2 = models.CharField(db_column='\u5b9e\u53d1\u5de5\u8d44', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2 = models.CharField(db_column='\u5b9e\u53d1\u5de5\u8d442', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_field_3 = models.FloatField(db_column='\u5e94\u53d1\u5de5\u8d44\u603b', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_4 = models.FloatField(db_column='\u5b9e\u53d1\u5de5\u8d44\u603b', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_5 = models.CharField(db_column='\u8eab\u4efd\u8bc1\u53f7\u7801', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_6 = models.CharField(db_column='\u5458\u5de5\u7f16\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_7 = models.CharField(db_column='\u94f6\u884c\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_8 = models.CharField(db_column='\u4e0a\u6d77\u7f34\u7eb3\u4e2a\u7a0e', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2_field = models.CharField(db_column='\u88682\u7ee9\u6548', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_1_field = models.CharField(db_column='\u88681\u7ee9\u6548', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_9 = models.CharField(db_column='\u666e\u901a\u52a0\u73ed\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    number_2_field = models.CharField(db_column='2\u500d\u52a0\u73ed\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    field_field_10 = models.CharField(db_column='\u6cd5\u5b9a\u52a0\u73ed\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_11 = models.CharField(db_column='\u793e\u4fdd', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1_field_0 = models.CharField(db_column='\u88681\u75c5\u5047\u6263', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2_field_0 = models.CharField(db_column='\u88682\u75c5\u5047\u6263', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1_field_1 = models.CharField(db_column='\u88681\u4e8b\u5047\u6263', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2_field_1 = models.CharField(db_column='\u88682\u4e8b\u5047\u6263', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1_field_2 = models.CharField(db_column='\u88681\u8f6e\u4f11\u6263', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2_field_2 = models.CharField(db_column='\u88682\u8f6e\u4f11\u6263', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_12 = models.CharField(db_column='\u5176\u4ed6\u6263', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2_field_3 = models.CharField(db_column='\u88682\u6263', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_13 = models.CharField(db_column='\u7ee9\u6548\u589e\u51cf', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_14 = models.CharField(db_column='\u8d77\u5f81\u70b9', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2_field_4 = models.CharField(db_column='\u6cd5\u5b9a\u548c2\u500d\u52a0\u73ed\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_15 = models.CharField(db_column='\u8f6e\u4f11\u548c\u5176\u4ed6\u6263', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_16 = models.CharField(db_column='\u75c5\u4e8b\u5047\u6263', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_17 = models.CharField(db_column='\u5e94\u53d1\u5de5\u8d44', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_18 = models.CharField(db_column='\u7eb3\u7a0e\u5de5\u8d44', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_19 = models.CharField(db_column='\u57fa\u5730', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_20 = models.CharField(db_column='\u5355\u4f4d\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_21 = models.CharField(db_column='\u52a0\u73ed\u57fa\u6570', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_22 = models.CharField(db_column='\u5355\u4f4d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_23 = models.CharField(db_column='\u5de5\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_24 = models.CharField(db_column='\u59d3\u540d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_25 = models.CharField(db_column='\u7f3a\u52e4', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_26 = models.CharField(db_column='\u52a0\u73ed\u65e5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_27 = models.CharField(db_column='\u4e8c\u500d\u65e5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_28 = models.CharField(db_column='\u51fa\u52e4', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_29 = models.CharField(db_column='\u6cd5\u5b9a\u65e5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_30 = models.CharField(db_column='\u75c5\u5047\u65e5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_3_field = models.CharField(db_column='\u75c5\u50473\u6708', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_31 = models.CharField(db_column='\u5176\u4ed6\u65e5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_32 = models.CharField(db_column='\u8f6e\u4f11\u65e5', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_33 = models.CharField(db_column='\u5de5\u8d44\u6807\u51c6', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_34 = models.CharField(db_column='\u5c97\u4f4d\u5de5\u8d44', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_35 = models.CharField(db_column='\u7ee9\u6548\u5de5\u8d44', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1 = models.CharField(db_column='\u7ee9\u6548\u589e\u51cf1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_2_0 = models.CharField(db_column='\u7ee9\u6548\u589e\u51cf2', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_field_36 = models.CharField(db_column='\u804c\u52a1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_37 = models.CharField(db_column='\u9a7b\u5c9b', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_38 = models.CharField(db_column='\u5de5\u9f84', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_39 = models.CharField(db_column='\u4f19\u98df\u8865\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_40 = models.CharField(db_column='\u4e2d\u591c\u73ed\u6d25\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_41 = models.CharField(db_column='\u8282\u65e5\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1_0 = models.CharField(db_column='\u7efc\u5408\u680f1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_2_1 = models.CharField(db_column='\u7efc\u5408\u680f2', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_field_42 = models.CharField(db_column='\u6c34\u7535\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_43 = models.CharField(db_column='\u517b\u8001\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_44 = models.CharField(db_column='\u533b\u7597', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_45 = models.CharField(db_column='\u5931\u4fdd', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_46 = models.CharField(db_column='\u516c\u79ef\u91d1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_47 = models.CharField(db_column='\u6263\u53d1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_48 = models.CharField(db_column='\u996d\u8d34\u57fa\u6570', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_49 = models.CharField(db_column='\u5206\u7c7b', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_50 = models.CharField(db_column='\u901a\u8baf\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_51 = models.CharField(db_column='\u5c97\u4f4d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_52 = models.CharField(db_column='\u5b66\u5386', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_53 = models.CharField(db_column='\u5165\u53f8\u65f6\u95f4', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_54 = models.CharField(db_column='\u5bb6\u5ead\u4f4f\u5740', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_55 = models.CharField(db_column='\u8f6c\u6b63\u65e5\u671f', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_56 = models.CharField(db_column='\u6027\u522b', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_57 = models.CharField(db_column='\u5e8f\u5217\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_58 = models.CharField(db_column='\u793e\u4fdd\u7f16\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_59 = models.CharField(db_column='\u516c\u79ef\u91d1\u7f16\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_60 = models.CharField(db_column='\u5b66\u5386\u8865\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_61 = models.CharField(db_column='\u804c\u79f0\u8865\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_62 = models.CharField(db_column='\u7279\u6280\u8865\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_63 = models.CharField(db_column='\u5c97\u4f4d\u8865\u8d34', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_64 = models.CharField(db_column='\u6d25\u8d34\u5408\u8ba1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_65 = models.CharField(db_column='\u5de5\u8d44\u5236', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'gzzb3'


class Gzzb4(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    field_field = models.CharField(db_column='\u5907\u6ce8', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_0 = models.CharField(db_column='\u90e8\u95e8', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_1 = models.FloatField(db_column='\u5458\u5de5\u7f16\u53f7', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_2 = models.CharField(db_column='\u5de5\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_3 = models.CharField(db_column='\u59d3\u540d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_4 = models.FloatField(db_column='\u4eba\u6570', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_5 = models.CharField(db_column='\u5c97\u4f4d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_6 = models.CharField(db_column='\u85aa\u8d44\u5e8f\u5217', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_7 = models.FloatField(db_column='\u85aa\u8d44\u6807\u51c6', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_8 = models.FloatField(db_column='\u804c\u52a1\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_9 = models.CharField(db_column='\u52a0\u73ed\u8d39\u57fa\u6570', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_10 = models.FloatField(db_column='\u57fa\u672c\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_11 = models.FloatField(db_column='\u5c97\u4f4d\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1 = models.FloatField(db_column='\u7ee9\u6548\u5de5\u8d441', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_field_12 = models.CharField(db_column='\u6708\u5ea6\u8003\u6838', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_13 = models.CharField(db_column='\u5168\u5458\u7ee9\u6548\u6d6e\u52a8', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_14 = models.FloatField(db_column='\u8003\u6838\u589e\u51cf', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_15 = models.FloatField(db_column='\u9a7b\u5c9b\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_16 = models.FloatField(db_column='\u5de5\u9f84\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_17 = models.CharField(db_column='\u8282\u65e5\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_18 = models.FloatField(db_column='\u901a\u8baf\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_19 = models.FloatField(db_column='\u5c97\u4f4d\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_20 = models.FloatField(db_column='\u7279\u6280\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_21 = models.FloatField(db_column='\u804c\u79f0\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_22 = models.FloatField(db_column='\u5b66\u5386\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_23 = models.FloatField(db_column='\u7efc\u5408\u8865\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_24 = models.FloatField(db_column='\u591c\u9910\u6d25\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_25 = models.CharField(db_column='\u4e2d\u73ed\u5929\u6570', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_26 = models.CharField(db_column='\u591c\u73ed\u5929\u6570', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_27 = models.CharField(db_column='\u4e2d\u591c\u8fde\u73ed', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_28 = models.CharField(db_column='\u65e5\u5e38\u52a0\u70b9', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_29 = models.FloatField(db_column='\u5468\u672b\u52a0\u73ed', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_30 = models.FloatField(db_column='\u8282\u65e5\u52a0\u73ed', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_31 = models.FloatField(db_column='\u65e5\u5e38\u52a0\u73ed', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_32 = models.FloatField(db_column='\u8282\u65e5\u52a0\u73ed\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_33 = models.FloatField(db_column='\u51fa\u52e4', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_3_field = models.FloatField(db_column='\u5de5\u4f243\u4e2a\u6708\u4ee5\u4e0a', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_34 = models.FloatField(db_column='\u63a2\u4eb2\u5a5a\u4e27\u966a\u54fa', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_3_field_0 = models.FloatField(db_column='\u75c5\u50473\u4e2a\u6708\u4ee5\u5185', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    number_3_field = models.FloatField(db_column='3\u4e2a\u6708\u4ee5\u4e0a\u75c5\u5047', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    field_field_35 = models.FloatField(db_column='\u4e8b\u5047\u65f7\u5de5', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_36 = models.FloatField(db_column='\u4ea7\u5047', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_37 = models.CharField(db_column='\u4ea7\u5047\u6263\u53d1', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_38 = models.FloatField(db_column='\u8bf7\u5047\u6263\u53d1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_39 = models.CharField(db_column='\u81ea\u52a8\u5339\u914d\u6570\u636e', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_40 = models.CharField(db_column='\u624b\u5de5\u8c03\u6574', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_1_0 = models.FloatField(db_column='\u7efc\u5408\u680f1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_field_41 = models.FloatField(db_column='\u5e94\u53d1\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_42 = models.FloatField(db_column='\u5b9e\u53d1\u5de5\u8d44', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_43 = models.FloatField(db_column='\u517b\u8001\u8d39', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_44 = models.FloatField(db_column='\u533b\u7597', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_45 = models.FloatField(db_column='\u5931\u4fdd', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_46 = models.FloatField(db_column='\u516c\u79ef\u91d1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_47 = models.FloatField(db_column='\u5b9e\u9645\u6263\u7a0e', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_48 = models.FloatField(db_column='\u4f01\u4e1a\u5e74\u91d1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_49 = models.CharField(db_column='\u6c34\u7535\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_50 = models.CharField(db_column='\u7269\u4e1a\u8d39', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_51 = models.FloatField(db_column='\u5176\u5b83', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2 = models.FloatField(db_column='\u7ee9\u6548\u5de5\u8d442', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_2_0 = models.FloatField(db_column='\u804c\u52a1\u8865\u8d342', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_field_52 = models.FloatField(db_column='\u56fa\u5b9a\u6d25\u8d34\uff08\u996d\u8d34\u3001\u804c\u79f0\u7b49\uff09', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_53 = models.CharField(db_column='\u4e34\u65f6\u6d25\u8d34\uff08\u6807\u5175\u3001\u5e08\u5e26\u5f92\u7b49\uff09', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_54 = models.FloatField(db_column='\u6d25\u8d34', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_2_1 = models.CharField(db_column='\u81ea\u52a8\u5339\u914d2', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_2_2 = models.CharField(db_column='\u624b\u5de5\u8c03\u65742', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_2_3 = models.FloatField(db_column='\u7efc\u5408\u680f2', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_2_4 = models.FloatField(db_column='\u5b9e\u53d1\u5de5\u8d442', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_2_5 = models.CharField(db_column='\u51fa\u52e42', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because of name conflict.
    field_field_55 = models.CharField(db_column='\u996d\u8d34\u6807\u51c6', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_56 = models.CharField(db_column='\u53d1\u653e\u91d1\u989d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_57 = models.CharField(db_column='\u8eab\u4efd\u8bc1\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_58 = models.CharField(db_column='\u94f6\u884c\u5361\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_59 = models.IntegerField(db_column='\u65f6\u95f4', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'gzzb4'


class Mima(models.Model):
    field_field = models.CharField(db_column='\u5458\u5de5\u7f16\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_field_0 = models.CharField(db_column='\u5de5\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_1 = models.CharField(db_column='\u59d3\u540d', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_2 = models.CharField(db_column='\u8eab\u4efd\u8bc1\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_3 = models.CharField(db_column='\u94f6\u884c\u5361\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_field_4 = models.CharField(db_column='\u5bc6\u7801', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'mima'


class Sheet1(models.Model):
    field_field = models.CharField(db_column='\u5de5\u53f7', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'sheet1'
