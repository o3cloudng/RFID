# Generated by Django 4.1.5 on 2023-02-24 14:44

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("member", "0002_alter_member_address_alter_member_email_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="member",
            old_name="parent_guardian",
            new_name="parent_guardian_name",
        ),
        migrations.RemoveField(
            model_name="member",
            name="address",
        ),
        migrations.RemoveField(
            model_name="member",
            name="email",
        ),
        migrations.RemoveField(
            model_name="member",
            name="phone_number",
        ),
        migrations.AddField(
            model_name="member",
            name="day_boarder",
            field=models.CharField(
                choices=[("DAY", "Day"), ("BOARDER", "Boarder")],
                default="BOARDER",
                max_length=20,
                verbose_name="Last name",
            ),
        ),
        migrations.AddField(
            model_name="member",
            name="parent_guardian_address",
            field=models.TextField(
                default="My Parents", verbose_name="Parent or Guardian Address"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="member",
            name="parent_guardian_email",
            field=models.CharField(
                default="parent@example.com",
                max_length=255,
                verbose_name="Parent or Guardian Email Address",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="member",
            name="parent_guardian_phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                default="+2348060617791",
                max_length=128,
                region=None,
                verbose_name="Parent or Guardian Phone number",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="member",
            name="student_age",
            field=models.IntegerField(default=16, verbose_name="Age"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="member",
            name="student_sex",
            field=models.CharField(
                choices=[("MALE", "Male"), ("FEMALE", "Female")],
                default="FEMALE",
                max_length=20,
                verbose_name="Sex / Gender",
            ),
        ),
    ]
