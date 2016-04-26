from django.db import models
from django.utils import timezone


class Employee(models.Model):
    
    TITLE_LIST = (
    ('MR','Mr'),
    ('MIS','Miss'),
    ('MRS', 'Mrs'),
    ('MS', 'Ms'),
    )
    
    title = models.CharField(max_length=3,choices=TITLE_LIST)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    address = models.CharField(max_length=100)
    post_code = models.CharField(max_length=8)
    
    email = models.EmailField(primary_key=True)
    telephone = models.IntegerField()
    
    DEPARTMENT_LIST = (
    ('PRD', 'Production'),
    ('DEV', 'Development'),
    ('PR', 'Public Relations'),
    ('HR', 'Human Resources'),
    ('FIN', 'Finance'),
    )
    
    department = models.CharField(max_length=3, choices=DEPARTMENT_LIST)
    is_manager = models.BooleanField(default=False)
    	
    created_by = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(blank=True, null=True)

    def update(self):
        self.last_updated = timezone.now()
        self.save()

    def __str__(self):
        return self.email
