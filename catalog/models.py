from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Film(models.Model):
    # Keep exact assignment field names for identical forms/output
    MovieID = models.PositiveIntegerField(primary_key=True)
    MovieTitle = models.CharField(max_length=200)
    Actor1Name = models.CharField(max_length=120)
    Actor2Name = models.CharField(max_length=120)
    DirectorName = models.CharField(max_length=120)

    # Use choices here (a slight internal difference from the other sample)
    GENRES = [
        ('Comedy', 'Comedy'),
        ('Romance', 'Romance'),
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Other', 'Other'),
    ]
    MovieGenre = models.CharField(max_length=20, choices=GENRES)

    ReleaseYear = models.PositiveIntegerField(
        validators=[MinValueValidator(1888), MaxValueValidator(2100)]
    )

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"