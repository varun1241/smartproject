# Generated by Django 3.1.5 on 2021-01-29 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.PositiveIntegerField(null=True)),
                ('department', models.CharField(max_length=100)),
                ('email', models.EmailField(default='name@default.com', max_length=100)),
                ('picture', models.ImageField(upload_to='images/')),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
