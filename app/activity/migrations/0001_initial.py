# Generated by Django 2.1.7 on 2019-03-05 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_name', models.CharField(max_length=255, verbose_name='折扣券名称')),
                ('coupon_type', models.CharField(choices=[('percent', '折扣百分比'), ('decrease', '减免数额')], max_length=255, verbose_name='折扣券类型')),
                ('coupon_value', models.FloatField(verbose_name='折扣券面额')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='领取日期')),
                ('validity_time', models.DateTimeField(verbose_name='有效期')),
                ('useless', models.BooleanField(default=False, verbose_name='是否失效')),
            ],
            options={
                'verbose_name': '折扣券活动',
                'verbose_name_plural': '折扣券活动',
                'db_table': 'code_activity_discount',
                'ordering': ['-id'],
            },
        ),
    ]
