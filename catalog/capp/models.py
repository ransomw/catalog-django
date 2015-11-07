from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)


def lots_of_items():
    """ populate database with sample data """
    categorySoccer = Category(name="Soccer")
    categoryBasketball = Category(name="Basketball")
    categoryBaseball = Category(name="Baseball")
    categoryFrisbee = Category(name="Frisbee")
    categorySnowboarding = Category(name="Snowboarding")
    categoryRockClimbing = Category(name="Rock Climbing")
    categoryFoosball = Category(name="Foosball")
    categorySkating = Category(name="Skating")
    categoryHockey = Category(name="Hockey")


    categorySoccer.save()
    categoryBasketball.save()
    categoryBaseball.save()
    categoryFrisbee.save()
    categorySnowboarding.save()
    categoryRockClimbing.save()
    categoryFoosball.save()
    categorySkating.save()
    categoryHockey.save()

    item = Item(
        title="Stick",
        description="A hockey stick",
        category=categoryHockey)
    item.save()

    item = Item(
        title="Goggles",
        description="Keep the snow out of your eyes",
        category=categorySnowboarding)
    item.save()

    item = Item(
        title="Snowboard",
        description="Type-A vintage",
        category=categorySnowboarding)
    item.save()

    item = Item(
        title="Two shinguards",
        description="Prevent injuries resulting from kicks to the shin",
        category=categorySoccer)
    item.save()

    item = Item(
        title="Shinguards",
        description="Prevent injuries resulting from kicks to the shin",
        category=categorySoccer)
    item.save()

    item = Item(
        title="Frisbee",
        description="A flying disc",
        category=categoryFrisbee)
    item.save()

    item = Item(
        title="Bat",
        description="Louisville slugger",
        category=categoryBaseball)
    item.save()

    item = Item(
        title="Jersey",
        description="World Cup 2014 commemorative jersy",
        category=categorySoccer)
    item.save()

    item = Item(
        title="Soccer Cleats",
        description="Nike cleats",
        category=categorySoccer)
    item.save()
