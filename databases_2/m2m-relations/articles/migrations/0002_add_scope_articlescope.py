# Generated by Django 3.1.2 on 2021-05-17 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField(unique=True, verbose_name='Название раздела')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(unique=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=256, unique=True, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='ArticleScope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основной раздел')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.scope')),
            ],
            options={
                'ordering': ['-is_main'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='articles', through='articles.ArticleScope', to='articles.Scope', verbose_name='Разделы'),
        ),
    ]
