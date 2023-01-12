# Generated by Django 3.2.16 on 2023-01-12 21:06

import catalog.common.utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("journal", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="cover",
            field=models.ImageField(
                blank=True,
                default="item/default.svg",
                upload_to=catalog.common.utils.piece_cover_path,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="rating",
            unique_together={("owner", "item")},
        ),
        migrations.AlterUniqueTogether(
            name="shelfmember",
            unique_together={("parent", "item")},
        ),
        migrations.AlterUniqueTogether(
            name="tagmember",
            unique_together={("parent", "item")},
        ),
    ]
