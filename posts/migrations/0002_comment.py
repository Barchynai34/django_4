# Generated by Django 4.2.3 on 2023-08-03 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Имя комьентатора')),
                ('text', models.CharField(max_length=300, verbose_name='Текст коментария')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='posts.post', verbose_name='Запись')),
            ],
        ),
    ]
