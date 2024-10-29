# from django.db import models

# class Post(models.Model):
#     title = models.CharField(max_length=75)
#     ticketsdtails = models.TextField()
#     comment = models.CharField(max_length=75)
#     datecreated = models.DateTimeField(auto_now_add=True)
#     PRIORITY_CHOICES = [
#         ('low', 'Low'),
#         ('medium', 'Medium'),
#         ('high', 'High'),
#         ('critical', 'Critical'),
#     ]
#     piority = models.CharField(
#         max_length=10,
#         choices=PRIORITY_CHOICES,
#         default='low',
#     )
#     Duedate = models.DateField()

#     def __str__(self):
#         return self.title


from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=75)
    ticketsdtails = models.TextField()
    comment = models.CharField(max_length=75)
    datecreated = models.DateTimeField(auto_now_add=True)
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]
    piority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='low',
    )
    Duedate = models.DateField()

    def __str__(self):
        return self.title

















