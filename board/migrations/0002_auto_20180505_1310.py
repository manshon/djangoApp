# Generated by Django 2.0.4 on 2018-05-05 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='内容')),
                ('created_ad', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='投稿日時'),
        ),
        migrations.AlterField(
            model_name='board',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='変更日時'),
        ),
        migrations.AddField(
            model_name='board',
            name='comment',
            field=models.ManyToManyField(to='board.Comment', verbose_name='コメント'),
        ),
    ]
