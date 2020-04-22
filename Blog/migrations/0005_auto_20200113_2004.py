# Generated by Django 3.0.1 on 2020-01-13 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0004_likecomment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('post_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.Post')),
                ('usr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_detail',
            name='usr',
        ),
        migrations.DeleteModel(
            name='LikeComment',
        ),
        migrations.DeleteModel(
            name='User_detail',
        ),
    ]