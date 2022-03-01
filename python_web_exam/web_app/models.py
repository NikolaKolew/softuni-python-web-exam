from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    USER_NAME_MAX_CHARS = 15
    USER_NAME_MIN_CHARS = 2
    MIN_AGE = 0

    user_name = models.CharField(
        max_length=USER_NAME_MAX_CHARS,
        validators=(
            MinLengthValidator(USER_NAME_MIN_CHARS),
        )
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MIN_AGE),
        )
    )


class Album(models.Model):
    ALBUM_NAME_MAX_CHARS = 30
    ARTIST_NAME_MAX_CHARS = 30
    GENRE_MAX_CHARS = 30
    MIN_PRICE = 0.0

    POPMUSIC = 'Pop Music'
    JAZZMUSIC = 'Jazz Music'
    RBMUSIC = 'R&B Music'
    ROCKMUSIC = 'Rock Music'
    COUNTRYMUSIC = 'Country Music'
    DANCEMUSIC = 'Dance Music'
    HIPHOPMUSIC = 'Hip Hop Music'
    OTHER = 'Other'

    GENRE_CHOICES = [
        (POPMUSIC, 'Pop Music'),
        (JAZZMUSIC, 'Jazz Music'),
        (RBMUSIC, 'R&B Music'),
        (ROCKMUSIC, 'Rock Music'),
        (COUNTRYMUSIC, 'Country Music'),
        (DANCEMUSIC, 'Dance Music'),
        (HIPHOPMUSIC, 'Hip Hop Music'),
        (OTHER, 'Other'),
    ]

    name = models.CharField(
        max_length=ALBUM_NAME_MAX_CHARS,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_NAME_MAX_CHARS,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_CHARS,
        choices=GENRE_CHOICES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE),
        )
    )
