# Generated by Django 2.0.4 on 2018-04-24 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('body', models.TextField(verbose_name='内容')),
                ('created_at', models.DateTimeField(verbose_name='投稿日時')),
                ('updated_at', models.DateTimeField(verbose_name='変更日時')),
                ('admin_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='タグ名')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='tag',
            field=models.ManyToManyField(to='board.Tag', verbose_name='タグ'),
        ),
    ]
