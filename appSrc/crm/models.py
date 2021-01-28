from django.db import models
""" from projects.models import Project """
from django.contrib.auth.models import User

class Relation(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    relation = models.CharField(max_length=50, default="Other", unique=True)
    
    class Meta:
        ordering = ["relation"]

    def __str__(self):
        return self.relation

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


# Create your models here.
class Property(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    street_1 = models.CharField(verbose_name="Street 1", max_length=50)
    street_2 = models.CharField(
        verbose_name="Street 2", max_length=50, blank=True)
    city = models.CharField(verbose_name="City", max_length=50)
    state = models.CharField(verbose_name="State", max_length=50)
    zip_code = models.CharField(verbose_name="Zip Code", max_length=50)
    fullAdd = "{} {} {}, {} {} ".format(str(street_1), str(street_2), city, state, str(zip_code))
    

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
        ordering = ["street_1"]

    def __str__(self):
        return self.street_1 + ' ' + self.city + ' ' + self.state

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Person(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    label = [('Agent','Agent'), ('Client','Client'), ('Vendor','Vendor'), ('Family','Family'), ('Friend','Friend'), ('Coworker','Coworker'), ('Other','Other')]
    levels = [('Platinum','Platinum'), ('Gold','Gold'), ('Silver',"Silver"), ('Bronze',"Bronze")]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    relations = models.ManyToManyField(Relation, blank=True)
    level = models.CharField(choices=levels, max_length=50, default="Bronze")
    properties = models.ManyToManyField(Property, blank=True)
    twitter_url = models.CharField(
        verbose_name="Twitter Url", max_length=200, blank=True)
    facebook_url = models.CharField(
        verbose_name="Facebook Url", max_length=200, blank=True)
    instagram_url = models.CharField(verbose_name="Instagram Url", max_length=200, blank=True)

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Active(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status_choices = [("Active", 'Active'), ('Pending','Pending'), ('Under Contract', 'Under Contract'), ('Dropped', 'Dropped'), ('Closed','Closed')]
    title = models.CharField("Title", max_length=50)
    people = models.ManyToManyField(Person, verbose_name="Clients")
    Property = models.ForeignKey(Property, verbose_name="Property", on_delete=models.DO_NOTHING)
    status = models.CharField(choices=status_choices, max_length=50)
    """ projects = models.ForeignKey(Project, verbose_name="Projects", on_delete=models.CASCADE, blank=True) """

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


