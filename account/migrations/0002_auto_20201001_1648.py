# Generated by Django 3.1.1 on 2020-10-01 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userfollowing',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='userfollowing',
            name='kogo_follow',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userfollowing',
            name='kto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='following', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userfollowing',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='userfollowing',
            unique_together={('kto', 'kogo_follow')},
        ),
        migrations.RemoveField(
            model_name='userfollowing',
            name='following_user_id',
        ),
        migrations.RemoveField(
            model_name='userfollowing',
            name='user_id',
        ),
    ]
