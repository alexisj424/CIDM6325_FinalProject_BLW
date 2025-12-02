from django.db import models

class Baby(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to="baby_photos/", null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    FRUIT = "fruit"
    VEG = "vegetable"
    PROTEIN = "protein"
    GRAIN = "grain"
    DAIRY = "dairy"
    OTHER = "other"
    CATEGORY_CHOICES = [
        (FRUIT, "Fruit"),
        (VEG, "Vegetable"),
        (PROTEIN, "Protein"),
        (GRAIN, "Grain"),
        (DAIRY, "Dairy"),
        (OTHER, "Other"),
    ]

    name = models.CharField(max_length=120, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=OTHER)
    is_allergen = models.BooleanField(default=False)
    image = models.ImageField(upload_to="food_images/", null=True, blank=True)

    def __str__(self):
        return self.name


class Meal(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="meals")
    date = models.DateField()
    foods = models.ManyToManyField(Food, related_name="meals", blank=True)
    notes = models.TextField(blank=True)
    photo = models.ImageField(upload_to="meal_photos/", null=True, blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.baby} — {self.date}"


class Reaction(models.Model):
    RASH = "rash"
    HIVES = "hives"
    VOMIT = "vomiting"
    DIARRHEA = "diarrhea"
    SWELL = "swelling"
    OTHER = "other"
    REACTION_CHOICES = [
        (RASH, "Rash"),
        (HIVES, "Hives"),
        (VOMIT, "Vomiting"),
        (DIARRHEA, "Diarrhea"),
        (SWELL, "Swelling"),
        (OTHER, "Other"),
    ]

    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="reactions")
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="reactions")
    reaction_type = models.CharField(max_length=20, choices=REACTION_CHOICES, default=OTHER)
    severity = models.PositiveSmallIntegerField(default=1, help_text="1 (mild) – 5 (severe)")
    notes = models.TextField(blank=True)
    date = models.DateField()

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.baby} — {self.food} — {self.reaction_type}"


# Create your models here.
