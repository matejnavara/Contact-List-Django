from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class Employee(models.Model):
    """
    Model for employees.
    
    #title: Choice of options from TITLE_LIST
    #first_name: Entry field for first name validated for only text input, limited to 30 chars.
    #last_name: Entry field for last name validated for only text input, limited to 30 chars.
    #address: Entry field for address, limited to 100 chars.
    #post_code: Entry field for post code, limited to 8 chars. //Could use more validation
    #email: Entry for email using EmailValidator.
    #telephone: Entry for telephone number validated for 9-15 digits and beginning with a +
    #department: Choice of Department objects available, established by admin
    #manager: Choice of Employee objects defined as managers
    #is_manager: Defines Employee object as a manager. Default false.
    #is_active: Defines Employee object as active. Default true.
    
    """
    TITLE_LIST = (
    ('MR','Mr'),
    ('MIS','Miss'),
    ('MRS', 'Mrs'),
    ('MS', 'Ms'),
    )
    
    title = models.CharField(max_length=3,choices=TITLE_LIST)
    
    text_regex = RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')
    first_name = models.CharField(validators=[text_regex], max_length=30)
    last_name = models.CharField(validators=[text_regex], max_length=30)
    
    address = models.CharField(max_length=100)
    post_code = models.CharField(max_length=8)
    
    email = models.EmailField(primary_key=True)

    phone_regex = RegexValidator(r'^\+?1?\d{9,15}$', message="Enter in the format: '+0123456789'. Up to 15 digits allowed.")
    telephone = models.CharField(validators=[phone_regex], max_length=15)
    
    department = models.ForeignKey("Department")
    
    manager = models.ForeignKey('self', blank=True, null = True, limit_choices_to={'is_manager':True})
    is_manager = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
        	
    created_by = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(default=timezone.now)

    def update(self):
        self.save()

    def __str__(self):
        return '{0} {1} ({2})'.format(self.first_name,self.last_name,self.department)
    

class Department(models.Model):
    """
    Model for Departments.
    
    #name: Name of department, defined by admin
    """   
    name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name

    
    
