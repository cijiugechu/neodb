# Generated by Django 3.2.16 on 2023-01-12 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CrossSiteUserInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        max_length=200, verbose_name="username and original site"
                    ),
                ),
                (
                    "local_id",
                    models.PositiveIntegerField(verbose_name="local database id"),
                ),
                (
                    "target_site",
                    models.CharField(
                        max_length=100, verbose_name="target site domain name"
                    ),
                ),
                ("site_id", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="MastodonApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "domain_name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="site domain name"
                    ),
                ),
                (
                    "app_id",
                    models.CharField(max_length=100, verbose_name="in-site app id"),
                ),
                (
                    "client_id",
                    models.CharField(max_length=100, verbose_name="client id"),
                ),
                (
                    "client_secret",
                    models.CharField(max_length=100, verbose_name="client secret"),
                ),
                (
                    "vapid_key",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="vapid key"
                    ),
                ),
                (
                    "star_mode",
                    models.PositiveIntegerField(
                        default=0,
                        verbose_name="0: custom emoji; 1: unicode moon; 2: text",
                    ),
                ),
                (
                    "max_status_len",
                    models.PositiveIntegerField(
                        default=500, verbose_name="max toot len"
                    ),
                ),
                ("is_proxy", models.BooleanField(blank=True, default=False)),
                ("proxy_to", models.CharField(blank=True, default="", max_length=100)),
            ],
        ),
        migrations.AddConstraint(
            model_name="crosssiteuserinfo",
            constraint=models.UniqueConstraint(
                fields=("uid", "target_site"), name="unique_cross_site_user_info"
            ),
        ),
    ]