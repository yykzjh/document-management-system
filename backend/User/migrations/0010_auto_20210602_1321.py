# Generated by Django 3.2.1 on 2021-06-02 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_emailverificationcode_is_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('_id', models.AutoField(db_column='id', primary_key=True, serialize=False, verbose_name='部门编号')),
                ('name', models.CharField(max_length=255, verbose_name='部门名称')),
            ],
            options={
                'db_table': 'dms_departments',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name='电子邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='User.department'),
        ),
    ]
