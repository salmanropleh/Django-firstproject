from django.db import models

# Create your models here.


class Menuitem(models.Model):  # is going to inherit from models.model
    # define different attributes which will correspond to a column in our database.
    name = models.CharField(max_length=255)
    # another coloumn named price will create a database table with the columns name and prince. to create this table we need to make migrations
    price = models.IntegerField()


class Reservation(models.Model):  # new model wil have different attributes
    # first name attribute with max_length
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)  # last name attribute
    guest_count = models.IntegerField()           # attribute with integer typpe
    # property called auto_now will correct current date
    Reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)


# our models will be stored to db.sqlite3 file when we migrate it (python manage.py makemigrations)-(python manage.py migrate)
# migration is a process which will convert whatever changes we make in the model.py file to our actual databse.
# to make migrations in our application, run the above commands.
