# Generated by Django 5.1.3 on 2024-11-23 18:36

from django.db import migrations


def add_contributor_tag(apps, schema_editor):
    # Get the models dynamically to avoid dependency issues
    User = apps.get_model("auth", "User")
    UserProfile = apps.get_model("website", "UserProfile")
    Tag = apps.get_model("website", "Tag")

    # Get or create the "contributor" tag
    contributor_tag, _ = Tag.objects.get_or_create(name="BLT-Contributors", slug="BLT-Contributors")

    # Add the tag to specific users
    usernames = [
        "jajodiaraghav",
        "CodeWithBishal",
        "amrit",
        "mohit",
        "souravbadami",
        "goyal-sidd",
        "neethu",
        "donnie",
        "ankit2001",
        "mrigank",
        "Kej-r03",
        "bhawna",
        "shubham",
        "Tarachris",
        "Jisan",
        "radac",
        "akankshsinha",
        "justary27",
    ]

    for username in usernames:
        try:
            user = User.objects.get(username=username)
            user_profile = UserProfile.objects.get(user=user)
            user_profile.tags.add(contributor_tag)
        except User.DoesNotExist:
            print(f"User '{username}' does not exist.")
        except UserProfile.DoesNotExist:
            print(f"UserProfile for '{username}' does not exist.")


class Migration(migrations.Migration):
    dependencies = [
        (
            "website",
            "0153_delete_contributorstats",
        ),  # Update with the correct last migration in your app
    ]

    operations = [
        migrations.RunPython(add_contributor_tag),
    ]
