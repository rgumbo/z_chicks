from django.db import models

# Create your models here.
from django.db import models
from django.db import models
    # from django import django.template.defaultfilters
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
#from slugify import slugify
from django.template.defaultfilters import slugify

# Creating models start here


class Country(models.Model):
    co_code		=	models.CharField(primary_key=True,verbose_name='Country',max_length=10, help_text='User supplied code for a country. Also the primary key for the table')
    co_name		=	models.CharField(max_length=50, verbose_name='Country' , blank=True, null=True, help_text='The name of the Country')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['co_name']
        verbose_name = 'Country'

    def __str__(self):
        return self.co_name

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.co_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class Region(models.Model):
    rg_code		=	models.CharField(primary_key=True,verbose_name='Region',max_length=10, help_text='User supplied code for a region. Also the primary key for the table')
    rg_name		=	models.CharField(max_length=50, verbose_name='Region' , blank=True, null=True, help_text='The name of the region')
    rg_co_code	=	models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country', help_text='Country in which this region falls under')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['rg_name']
        verbose_name = 'Region'

    def __str__(self):
        return self.rg_name

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.rg_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class Town(models.Model):
    to_code		=	models.CharField(primary_key=True,verbose_name='Town',max_length=10, help_text='User supplied code for a town. Also the primary key for the table')
    to_name		=	models.CharField(max_length=50, verbose_name='Town' , blank=True, null=True, help_text='The name of the town')
    to_rg_code	=	models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region', help_text='Town in which this district falls under')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['to_name']
        verbose_name = 'Town'

    def __str__(self):
        return self.to_name

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.to_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class District(models.Model):
    dt_code		=	models.CharField(primary_key=True,verbose_name='District',max_length=10, help_text='User supplied code for a village. Also the primary key for the table')
    dt_to_code	=	models.ForeignKey(Town, on_delete=models.CASCADE, verbose_name='Town', help_text='Town in which this district falls under')
    dt_co_code	=	models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Country', help_text='Country in which this district falls under')
    dt_rg_code	=	models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region', help_text='Region in which this district falls under')
    dt_name		=	models.CharField(max_length=50, verbose_name='District' , blank=True, null=True, help_text='The name of the district')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['dt_name']
        verbose_name = 'District'

    def __str__(self):
        return self.dt_name

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.dt_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class Ward(models.Model):
    wd_code		=	models.CharField(primary_key=True,verbose_name='Ward',max_length=10, help_text='User supplied code for a ward. Also the primary key for the table')
    wd_dt_code	=	models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='District', help_text='District in which this ward falls under')
    wd_to_code	=	models.ForeignKey(Town, on_delete=models.CASCADE, verbose_name='Town', help_text='Town in which this ward falls under')
    wd_rg_code	=	models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region', help_text='Region in which this ward falls under')
    wd_name		=	models.CharField(max_length=50, verbose_name='Ward' , blank=True, null=True, help_text='The name of the ward')
    wd_chief	=	models.CharField(max_length=50, verbose_name='Chief' , blank=True, null=True, help_text='The name of the chief under which the ward falls')
    wd_mobile	=	models.IntegerField(verbose_name='Phone' , blank=True, null=True, help_text='The contact phone')
    wd_email	=	models.EmailField(max_length=50, verbose_name='Email' , blank=True, null=True, help_text='The email address')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['wd_name']
        verbose_name = 'Ward'

    def __str__(self):
        return self.wd_name

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.wd_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class Village(models.Model):
    vg_code		=	models.CharField(primary_key=True,verbose_name='Village', max_length=10, help_text='User supplied code for a village. Also the primary key for the table')
    vg_wd_code	=	models.ForeignKey(Ward, on_delete=models.CASCADE, verbose_name='Ward', help_text='Ward in which this village falls under')
    vg_dt_code	=	models.ForeignKey(District, on_delete=models.CASCADE, verbose_name='District', help_text='District in which this village falls under')
    vg_to_code	=	models.ForeignKey(Town, on_delete=models.CASCADE, verbose_name='Town', help_text='Town in which this village falls under')
    vg_rg_code	=	models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region', help_text='Region in which this village falls under')
    vg_name		=	models.CharField(max_length=50, verbose_name='Name' , blank=True, null=True, help_text='The name of the village')
    vg_mobile	=	models.IntegerField(verbose_name='Phone' , blank=True, null=True, help_text='The contact phone')
    vg_email	=	models.EmailField(max_length=50, verbose_name='Email' , blank=True, null=True, help_text='The email address')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['vg_name']
        verbose_name = 'Village'

    def __str__(self):
        return self.vg_name

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.vg_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class ContractType(models.Model):
    ct_code	=	models.CharField(primary_key=True,verbose_name='Contract Type',max_length=10, help_text='User supplied code for a contract type. Also the primary key for the table')
    ct_desc	=	models.CharField(max_length=50, verbose_name='Description' , blank=True, null=True, help_text='The name of the contract type')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['ct_code']
        verbose_name = 'Contract Type'

    def __str__(self):
        return self.ct_desc

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.ct_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class Qualification(models.Model):
    ql_code	=	models.CharField(primary_key=True,verbose_name='Qualification',max_length=10, help_text='User supplied code for a qualification. Also the primary key for the table')
    ql_desc	=	models.CharField(max_length=100, verbose_name='Description' , blank=True, null=True, help_text='The name of the qualification')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['ql_code']
        verbose_name = 'Qualification'

    def __str__(self):
        return self.ql_desc

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.ql_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class Grade(models.Model):
    gd_code		=	models.CharField(primary_key=True,verbose_name='grade',max_length=10, help_text='User supplied code for a grade. Also the primary key for the table')
    gd_name		=	models.CharField(max_length=50, verbose_name='Description' , blank=True, null=True, help_text='The name of the grade')
    gd_min_sal	=	models.DecimalField(verbose_name='Min Salary',max_digits=15, decimal_places=2, default=0, help_text='Minimum salary for grade', null=True, blank=True)
    gd_max_sal	=	models.DecimalField(verbose_name='Max Salary',max_digits=15, decimal_places=2, default=0, help_text='Max salary for grade', null=True, blank=True)
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['gd_code']
        verbose_name = 'grade'

    def __str__(self):
        return self.gd_name

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.gd_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class Member(models.Model):
    mm_num		=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying the member')
    mm_code		=	models.CharField(verbose_name='Assigned Number',blank=True, null=True, max_length=100, help_text='A number/code by whhich member is identified by')
    mm_trade_name	=	models.CharField(verbose_name='Trade Name', max_length=200, help_text='The member s trade name')
    mm_name		=	models.CharField(verbose_name='Name', max_length=200, help_text='The member s  name')
    mm_comm_date	=	models.DateTimeField(verbose_name='Commencement Date',blank=True, null=True, help_text='Date member commenced operations')
    mm_phone	=	models.IntegerField(verbose_name='Phone',blank=True, null=True, help_text='member s phone number')
    mm_mobile	=	models.IntegerField(verbose_name='Mobile Phone',blank=True, null=True, help_text='member s mobile phone number')
    mm_email	=	models.EmailField(verbose_name='Email', max_length=100,blank=True, null=True, help_text='member s email address')
    mm_wsite	=	models.CharField(verbose_name='Website', max_length=200,blank=True, null=True, help_text='member s website')
    mm_contact	=	models.CharField(verbose_name='Contact Person1',blank=True, null=True,max_length=100, help_text='First contact person')
    mm_phone1	=	models.IntegerField(verbose_name='Phone',blank=True, null=True, help_text='First contact person phone number')
    mm_paddress1	=	models.CharField(verbose_name='Physical Address',blank=True, null=True, max_length=200, help_text='The member s Physical Address line 1')
    mm_paddress2	=	models.CharField(verbose_name='Physical Address',blank=True, null=True, max_length=200, help_text='The member s Physical Address line 2')
    mm_reg_date	=	models.DateTimeField(verbose_name='Date of Registration',blank=True, null=True, help_text='Date member was registered with institution')
    mm_vg_code	=	models.ForeignKey(Village, on_delete=models.CASCADE,blank=True, null=True,verbose_name='Village', help_text='Village to which the member belongs')
    mm_wd_code	=	models.ForeignKey(Ward, on_delete=models.CASCADE,blank=True, null=True, verbose_name='Ward', help_text='Ward to which the member belongs')
    mm_to_code	=	models.ForeignKey(Town, on_delete=models.CASCADE,blank=True, null=True,verbose_name='Town', help_text='Town to which the member belongs')
    mm_dt_code	=	models.ForeignKey(District, on_delete=models.CASCADE,blank=True, null=True, verbose_name='District', help_text='District to which the member belongs')
    mm_rg_code	=	models.ForeignKey(Region, on_delete=models.CASCADE,blank=True, null=True, verbose_name='Region', help_text='Region to which the member belongs')
    mm_co_code	=	models.ForeignKey(Country, on_delete=models.CASCADE,blank=True, null=True, verbose_name='Country', help_text='Country	to which the member belongs')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['mm_num']
        verbose_name = 'Member'

    def __str__(self):
        return self.mm_name

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.mm_num)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class Employee(models.Model):
    gender_choice	=	(('M','Male'),('F', 'Female'))
    recordstatus_choice	=	(('1','On'),('0', 'Off'))
    salute_choice	=	(('1', 'Miss'),('2' , 'Mrs'),('3' , 'Ms'),('4' , 'Mr'),('5' , 'Dr'),('6' , 'Prof'),('7' , 'Hon'))
    ee_num		=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying an employee')
    ee_mm_num	=	models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='Member', help_text='Member')
    ee_fname	=	models.CharField(verbose_name='First Name', max_length=50, help_text='First Name')
    ee_onames	=	models.CharField(verbose_name='Other Names', max_length=30, blank=True, null=True, help_text='Other names')
    ee_initials	=	models.CharField(verbose_name='Initials', max_length=10, help_text='Initials')
    ee_sname	=	models.CharField(verbose_name='Surname', max_length=50, help_text='Surname')
    ee_nid		=	models.CharField(verbose_name='National ID', max_length=20, blank=True, null=True, help_text='National identification')
    ee_pp_num	=	models.CharField(verbose_name='Passport Number', max_length=30, blank=True, null=True, help_text='Pasport number')
    ee_dl_num	=	models.CharField(verbose_name='Driver licence', max_length=30, blank=True, null=True, help_text='Driver s licence number')
    ee_ss_num	=	models.CharField(verbose_name='Social Security', max_length=30, blank=True, null=True, help_text='Social security number')
    ee_dob		=	models.DateTimeField(verbose_name='Date Of Birth',  help_text='Date of birth')
    ee_date_joined	=	models.DateTimeField(verbose_name='Date Joined', help_text='Date of joining')
    ee_gender	=	models.CharField(verbose_name='Gender', max_length=1,choices=gender_choice, blank=True, null=True, help_text='The gender')
    ee_salute	=	models.CharField(verbose_name='Salutation', max_length=1,choices=salute_choice, blank=True, null=True, help_text='The salutation')
    ee_gd_code	=	models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name='Grade', help_text='Current grade')
    ee_ql_code	=	models.ForeignKey(Qualification, on_delete=models.CASCADE, verbose_name='Qualification', help_text='Highest Qualification')
    ee_ct_code	=	models.ForeignKey(ContractType, on_delete=models.CASCADE, verbose_name='Contract Type', help_text='The type of contract held')
    ee_status	=	models.CharField(verbose_name='Record Status', choices=recordstatus_choice, max_length=30, blank=True, null=True, help_text='The general status')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['ee_num']
        verbose_name = 'Employee'

    def __str__(self):
        return self.ee_sname + '' + self.ee_initials

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.ee_num)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class Holding(models.Model):

    type_choice		=	(('1','Owned'),('2', 'Leased'))
    status_choice	=	(('1', 'On'),('2' , 'Off'))
    hd_num  	=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying a holding')
    hd_code	=	models.CharField(verbose_name='Code', max_length=100, help_text='User assigned code for the holding')
    hd_size	=	models.DecimalField(verbose_name='Hactares',max_digits=15, decimal_places=2, default=0,  help_text='Total Hactares - put 0.1 for smallholdings')
    hd_trans_date	=	models.DateTimeField(verbose_name='Commencement Date', help_text='Date Commenced')
    hd_name	=	models.CharField(verbose_name='Name', max_length=200, help_text='The name of the holding')
    hd_mm_num	=	models.ForeignKey(Member,on_delete=models.CASCADE,default=1,verbose_name='Member', help_text='Foreign key to holder/owner/employee')
    hd_vg_code	=	models.ForeignKey(Village,on_delete=models.CASCADE,verbose_name='Village', help_text='Village where the holding is found')
    hd_wd_code	=	models.ForeignKey(Ward,on_delete=models.CASCADE,default=0,verbose_name='Ward', help_text='Ward where the holding is found')
    hd_dt_code	=	models.ForeignKey(District,on_delete=models.CASCADE,verbose_name='District', help_text='District where the holding is found')
    hd_to_code	=	models.ForeignKey(Town, blank=True, null=True,on_delete=models.CASCADE,verbose_name='Town', help_text='Town where the holding is found')
    hd_rg_code	=	models.ForeignKey(Region,on_delete=models.CASCADE,verbose_name='Region', help_text='Region where the holding is found')
    hd_type	=	models.CharField(verbose_name='Type',max_length=1,choices=type_choice, help_text='Type of the holding')
    hd_desc	=	models.CharField(verbose_name='Desc', max_length=200, help_text='A description of the holding')
    hd_status	=	models.CharField(verbose_name='Status', max_length=1,choices=status_choice, help_text='Status')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['hd_num']
        verbose_name = 'Holding'

    def __str__(self):
        return self.hd_code

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.hd_num)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class HoldingInstance(models.Model):
    type_choice		=	(('1','Animal'),('2', 'Cropping'),('2', 'Other'))
    status_choice	=	(('1', 'On'),('2' , 'Off'))

    hi_num	=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying a holding')
    hi_code	=	models.CharField(verbose_name='Code', max_length=100, help_text='User assigned code for the holding instance')
    hi_hd_num	=	models.ForeignKey(Holding,on_delete=models.CASCADE,verbose_name='Holding Instance', help_text='Foreign key to holding')
    hi_days	=	models.IntegerField(verbose_name='Number Of Days', default=0, help_text='Instance days')
    hi_trans_date	=	models.DateTimeField(verbose_name='Trans Date', blank=True, null=True, help_text='Transaction date of the instance')
    hi_start_date	=	models.DateTimeField(verbose_name='Start Date',default=date.today,help_text='Start date of the instance')
    hi_end_date	=	models.DateTimeField(verbose_name='End Date', default=date.today,help_text='End date of the instance')
    hi_use_type	=	models.CharField(verbose_name='Type', max_length=1,choices=type_choice, help_text='Type of the holding instance')
    hi_desc	=	models.CharField(verbose_name='Description', max_length=200, help_text='The description of the holding instance')
    hi_size	=	models.DecimalField(verbose_name='Size',max_digits=10, decimal_places=2, default=0, help_text='Size of instance', null=True, blank=True)
    hi_pprice	=	models.DecimalField(verbose_name='Planned Price',max_digits=10, decimal_places=2, default=0, help_text='Planned Price of instance', null=True,blank=True)
    hi_aprice	=	models.DecimalField(verbose_name='Actual Price',max_digits=10, decimal_places=2, default=0, help_text='Actual Price of instance', null=True, blank=True)
    hi_psize	=	models.DecimalField(verbose_name='Planned Size',max_digits=10, decimal_places=2, default=0, help_text='Planned Size of instance', null=True, blank=True)
    hi_asize	=	models.DecimalField(verbose_name='Actual Size',max_digits=10, decimal_places=2, default=0, help_text='Actual Size of instance', null=True, blank=True)
    hi_tqty	=	models.DecimalField(verbose_name='Target Output',max_digits=10, decimal_places=2, default=0, help_text='Target Output of instance', null=True, blank=True)
    hi_aqty	=	models.DecimalField(verbose_name='Actual Output',max_digits=10, decimal_places=2, default=0, help_text='Actual Output of instance', null=True, blank=True)
    hi_status	=	models.CharField(verbose_name='Status', max_length=1,choices=status_choice,default='1', help_text='Status')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['hi_num']
        verbose_name = 'Holding Instance'

    def __str__(self):
        return self.hi_code

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.hi_num)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class Activity(models.Model):
    type_choice		=	(('1','Clearing'),('2', 'Preparation'),('3', 'Planting'),
                             ('4', 'Production'),('5', 'Packaging'),('6', 'Storage'),
                             ('7', 'Starting'),('8', 'Growing'),('9', 'Finishing'))
    status_choice	=	(('1', 'On'),('2' , 'Off'))
    ac_num	=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying an activity')
    ac_hi_num	=	models.ForeignKey(HoldingInstance,on_delete=models.CASCADE,verbose_name='Holding Instance', help_text='Foreign key to holding instance')
    ac_type	=	models.CharField(verbose_name='Type', max_length=1,choices=type_choice, help_text='Type of the activity')
    ac_day	=	models.IntegerField(verbose_name='Day Number', default=0, help_text='Day Count', null=True, blank=True)
    ac_date	=	models.DateTimeField(verbose_name='Date Start', null=True, blank=True, help_text='Planned start date of activity')
    ac_o_qty	=	models.DecimalField(verbose_name='Open Qty',max_digits=10, decimal_places=2, default=0, help_text='Opening Quantity', null=True, blank=True)
    ac_c_qty	=	models.DecimalField(verbose_name='Closing Qty',max_digits=10, decimal_places=2, default=0, help_text='Closing Quantity', null=True, blank=True)
    ac_t_wqt	=	models.DecimalField(verbose_name='Target Weight',max_digits=10, decimal_places=2, default=0, help_text='Target Weight', null=True, blank=True)
    ac_a_wqt	=	models.DecimalField(verbose_name='Actual Weight',max_digits=10, decimal_places=2, default=0, help_text='Target Weight', null=True, blank=True)
    ac_morlity	=	models.DecimalField(verbose_name='Mortality',max_digits=10, decimal_places=2, default=0, help_text='Day s Motality', null=True, blank=True)
    ac_e_cost	=	models.DecimalField(verbose_name='Est Cost',max_digits=10, decimal_places=2, default=0, help_text='Est Cost', null=True, blank=True)
    ac_desc	=	models.CharField(verbose_name='Description', max_length=200, null=True, blank=True, help_text='The description of the activity')
    ac_pstart_date	=	models.DateTimeField(verbose_name='Planned Start', null=True, blank=True, help_text='Planned start date of activity')
    ac_pend_date	=	models.DateTimeField(verbose_name='Planned End', null=True, blank=True, help_text='Planned end date of activity')
    ac_astart_date	=	models.DateTimeField(verbose_name='Actual Start', null=True, blank=True, help_text='Actual start date of activity')
    ac_aend_date	=	models.DateTimeField(verbose_name='Actual End', null=True, blank=True, help_text='Actual end date of activity')
    ac_status	=	models.CharField(verbose_name='Status', max_length=1,choices=type_choice, help_text='Status of the activity')
    ac_remark	=	models.CharField(verbose_name='Remarks', max_length=200, null=True, blank=True, help_text='The remarks about the activity')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')


    class Meta:
        ordering = ['ac_num']
        verbose_name = 'Activity'

    def __str__(self):
        return self.ac_type

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.ac_num)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class Note(models.Model):

    type_choice		=	(('1','Noting'),('2', 'Instructive'))
    status_choice	=	(('1', 'On'),('2' , 'Off'))
    nt_num	=	models.AutoField(verbose_name='Note Number', primary_key=True,help_text='System generated number uniquely identifying a note')
    nt_ac_num	=	models.ForeignKey(Activity,on_delete=models.CASCADE,verbose_name='Activity', help_text='Foreign key to Activity')
    nt_comment	=	models.CharField(verbose_name='Comment', max_length=200, help_text='The comment on the activity')
    nt_remark	=	models.CharField(verbose_name='Remark', max_length=200, help_text='The Remark on the activity')
    nt_trans_date	=	models.DateTimeField(verbose_name='Trans Start', help_text='Date of notes')
    nt_type	=	models.CharField(verbose_name='Type', max_length=1,choices=type_choice, help_text='Type of the notes')
    nt_status	=	models.CharField(verbose_name='Status', max_length=1,choices=status_choice, help_text='Status of the notes')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['nt_num']
        verbose_name = 'Note'

    def __str__(self):
        return self.nt_status

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.nt_num)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class Resource(models.Model):

    type_choice		=	(('1','Yes'),('2', 'No'))
    status_choice	=	(('1', 'On'),('2' , 'Off'))
    rs_num	=	models.AutoField(verbose_name='Resource Number', primary_key=True,help_text='System generated number uniquely identifying a resourse')
    rs_ac_num	=	models.ForeignKey(Activity,on_delete=models.CASCADE,verbose_name='Activity', help_text='Foreign key to Activity')
    rs_unit	=	models.CharField(verbose_name='Unit', max_length=20, help_text='The unit of measure')
    rs_desc	=	models.CharField(verbose_name='Resource Description', max_length=200, help_text='The description of the activity')
    rs_required	=	models.DecimalField(verbose_name='Required',max_digits=10, decimal_places=2, default=0, help_text='Resources required', null=True, 						blank=True)
    rs_provided	=	models.DecimalField(verbose_name='Provided',max_digits=10, decimal_places=2, default=0, help_text='Actual Price of instance', null=True, 					blank=True)
    rs_date_provided	=	models.DateTimeField(verbose_name='Date Provided', help_text='Date resources were provided')
    rs_req_date	=	models.DateTimeField(verbose_name='Date requested', help_text='Date Resources were requested')
    rs_approved	=	models.CharField(verbose_name='Approved', max_length=1,choices=type_choice, help_text='Status of the notes')
    rs_status	=	models.CharField(verbose_name='Status', max_length=1,choices=status_choice, default='1', help_text='Status of the notes')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['rs_num']
        verbose_name = 'Resource'

    def __str__(self):
        return self.rs_unit

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.rs_num)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class OutPut(models.Model):

    type_choice		=	(('1','Yes'),('2', 'No'))
    status_choice	=	(('1', 'On'),('2' , 'Off'))
    op_num	=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying an output')
    op_hi_num	=	models.ForeignKey(HoldingInstance,on_delete=models.CASCADE,verbose_name='Holding Instance', help_text='Foreign key to Holding Instance')
    op_qty	=	models.DecimalField(verbose_name='Quantity',max_digits=10, decimal_places=2, default=0, help_text='Quantity of output', null=True, 						blank=True)
    op_unit	=	models.CharField(verbose_name='Unit', max_length=20, help_text='The unit of measure')
    op_grade	=	models.CharField(verbose_name='Grade', max_length=100, help_text='The grade of the output')
    op_description	=	models.CharField(verbose_name='Description', max_length=200, help_text='The description of the output')
    op_trans_date	=	models.DateTimeField(verbose_name='Trans requested', help_text='Date output waa acquired')
    op_status_date	=	models.DateTimeField(verbose_name='Date requested', help_text='Status date of output')
    ot_status	=	models.CharField(verbose_name='Status', max_length=1,choices=status_choice, default='1', help_text='Status of the notes')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['op_num']
        verbose_name = 'Output'

    def __str__(self):
        return self.op_unit

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.op_num)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class CustOrders(models.Model):

    pay_choice		=	(('1', 'Outstanding'), ('2','Paid'))
    status_choice	=	(('1', 'Pending'),('2' , 'Confirmed'))
    item_choice		=	(('C', 'Chickens'),('P' , 'Pork'),('O' , 'Other'))
    od_num	=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying an output')
    od_hi_num	=	models.ForeignKey(HoldingInstance,on_delete=models.CASCADE,verbose_name='Holding Instance', help_text='Foreign key to holding instance')
    od_Custname	=	models.CharField(max_length=50, verbose_name='Customer' , blank=True, null=True, help_text='Customer s name')
    od_phone	=	models.CharField(max_length=50, verbose_name='Contact Phone' , blank=True, null=True, help_text='Customer s contact phone')
    od_item	=	models.CharField(max_length=50, verbose_name='Item' ,choices=item_choice, blank=True, null=True, help_text='Order Item')
    od_qty	=	models.DecimalField(verbose_name='Quantity',max_digits=10, decimal_places=2, default=0, help_text='Quantity ordered', null=True,blank=True)
    od_unit_p	=	models.DecimalField(verbose_name='Unit Price',max_digits=10, decimal_places=2, default=0, help_text='Price for each unit', null=True)
    od_unit	=	models.CharField(verbose_name='Unit', max_length=20, help_text='The unit of measure')
    od_grade	=	models.CharField(verbose_name='Grade Ordered', max_length=100, help_text='The grade ordered')
    od_notes	=	models.CharField(verbose_name='Order Notes', max_length=200, help_text='Notes/Instructions on the order')
    od_trans_date	=	models.DateTimeField(verbose_name='Transaction Date', help_text='Transaction date')
    od_status_date	=	models.DateTimeField(verbose_name='Status Date', help_text='Status date of order')
    ot_status	=	models.CharField(verbose_name='Status', max_length=1,choices=status_choice,  default='1',help_text='Status of the order')
    ot_paid	=	models.CharField(verbose_name='Payment Status', max_length=1,choices=pay_choice, default='1', help_text='Payment status of the order')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['od_num']
        verbose_name = 'CustOrders'

    def __str__(self):
        return self.od_unit

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.od_num)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#Beginning of Store mgt Models

#PackType Class - class representing the Package type e.g each, cartoon,case,litres, kgs
class PackType(models.Model):
	pt_status_choices = (('1', 'Active'), ('0', 'Inactive'))

	pt_code = models.AutoField(verbose_name='Code',primary_key=True, help_text='Code uniquely identify a Package Type')
	pt_name = models.CharField(verbose_name='Package Type',max_length=100, help_text='Package Type')
	pt_desc = models.CharField(verbose_name='description',max_length=100, help_text='Description of the Package Type')
	pt_status = models.CharField(verbose_name='Status',max_length=1, choices=pt_status_choices, help_text='Status of the Pack Type', default='1')
	ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['pt_code']
		verbose_name = 'Packaging Type'

	def __str__(self):
		return self.pt_name

	def get_absolute_url(self):
		return reverse('Index', args=[str(self.pt_code)])

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

#Currency Class - class representing the Package type e.g each, cartoon,case,litres, kgs
class Currency(models.Model):
	cu_status_choices = (('1', 'Active'), ('0', 'Inactive'))
	cu_base_choices = (('Y', 'Home Currency'), ('1', 'Currency 1'), ('2', 'Currency 1'))

	cu_num = models.AutoField(verbose_name='Currecny ID',primary_key=True, help_text='Code uniquely identify a Currecny')
	cu_code = models.CharField(verbose_name='Code',max_length=3, help_text='The currency Code')
	cu_name = models.CharField(verbose_name='Currency Name',max_length=100, help_text='Currency Name')
	cu_base = models.CharField(verbose_name='Base Currency ?',max_length=1,choices=cu_base_choices, default='N', help_text='Indicates whether the currency is the base currency')
	cu_rate = models.DecimalField(verbose_name='Rate to base',max_digits=15, decimal_places=2, help_text='Rate to base',default=0)
	cu_valid_from = models.DateTimeField(verbose_name='Valid From',help_text='Date date from which rate is valid')
	cu_status = models.CharField(verbose_name='Status',max_length=1, choices=cu_status_choices, help_text='Status of the currency', default='1')
	ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['cu_code']
		verbose_name = 'Currency'

	def __str__(self):
		return self.cu_name

	def get_absolute_url(self):
		return reverse('Index', args=[str(self.cu_code)])

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

#StoreName Class - the class repersenting the store
class StoreName(models.Model):
	sn_status_choices = (('1', 'Active'), ('0', 'Inactive'))

	sn_code = models.CharField(verbose_name='Code',primary_key=True, max_length=10,help_text='Code uniquely identify a store')
	sn_name = models.CharField(verbose_name='Name',max_length=50, help_text='The name of the store')
	sn_remark = models.CharField(verbose_name='Remark',max_length=50, help_text='Enter prime scale factor')
	sn_resp = models.CharField(verbose_name='Responsible',max_length=50, help_text='Responsible authority', null=True, blank=True)
	sn_to_code = models.ForeignKey(Town, on_delete=models.CASCADE, related_name='stown',verbose_name='Town', help_text='Town', null=True, blank=True)
	sn_rg_code = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='region',verbose_name='Region', help_text='Region', null=True, blank=True)
	sn_phone = models.CharField(verbose_name='Contact Phone',max_length=50, help_text='Contact phone', null=True, blank=True)
	sn_email = models.CharField(verbose_name='Email Address',max_length=50, help_text='Email Address', null=True, blank=True)
	sn_paddress = models.CharField(verbose_name='Physical Address',max_length=100, help_text='The Email Address', null=True, blank=True)
	sn_status = models.CharField(verbose_name='Status',max_length=1, choices=sn_status_choices, help_text='Status of the Store', default='1')
	ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['sn_name']
		verbose_name = 'Trading Store'

	def __str__(self):
		return self.sn_name

	def get_absolute_url(self):
		return reverse('Index', args=[str(self.sn_code)])

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

#StockLoc Class - class representing where stock items- types are located in the store
class StockLoc(models.Model):
	sl_status_choices = (('1', 'Active'), ('0', 'Inactive'))

	sl_code = models.CharField(verbose_name='Code',primary_key=True, max_length=10,help_text='Code uniquely identify a stock location')
	sl_name = models.CharField(verbose_name='Name',max_length=100, help_text='The name of the stock location')
	sl_sn_code = models.ForeignKey(StoreName, on_delete=models.CASCADE, related_name='sl_store',verbose_name='Store', help_text='The Store', null=True, blank=True)
	sl_desc = models.CharField(verbose_name='Description',max_length=100, help_text='A more detailed description to help locate it')
	sl_resp = models.CharField(verbose_name='Responsible',max_length=50, help_text='Responsible authority', null=True, blank=True)
	sl_phone = models.CharField(verbose_name='Contact phone',max_length=50, help_text='Contact phone', null=True, blank=True)
	sl_status = models.CharField(verbose_name='Status',max_length=1, choices=sl_status_choices, help_text='Status of the Location', default='1')
	ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['sl_code']
		verbose_name = 'Stock Location'

	def __str__(self):
		return self.sl_name

	def get_absolute_url(self):
		return reverse('Index', args=[str(self.sl_code)])

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

#StockType Class - class representing stock types/groups (product groups) sold in the store
class StockType(models.Model):
	st_status_choices = (('1', 'Active'), ('0', 'Inactive'))

	st_code = models.CharField(verbose_name='Code',primary_key=True, max_length=10,help_text='Code uniquely identify a stock type')
	st_name = models.CharField(verbose_name='Stock Type',max_length=100, help_text='The name of the stock type')
	st_sl_code = models.ForeignKey(StockLoc, on_delete=models.CASCADE,verbose_name='Location', help_text='Location Stock')
	st_sn_code = models.ForeignKey(StoreName, on_delete=models.CASCADE, related_name='st_store',verbose_name='Store', help_text='The Store', null=True, blank=True)
	st_desc = models.CharField(verbose_name='description',max_length=100, help_text='Description of StockType')
	st_status = models.CharField(verbose_name='Status',max_length=1, choices=st_status_choices, help_text='Status of the Stock Type', default='1')
	ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['st_code']
		verbose_name = 'Stock Type'

	def __str__(self):
		return self.st_name

	def get_absolute_url(self):
		return reverse('Index', args=[str(self.st_code)])

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

#StockItem Class - class representing the stock itemns sold in the store
class StockItem(models.Model):
	si_status_choices = (('1', 'Active'), ('0', 'Inactive'))

	si_code = models.CharField(verbose_name='Code',primary_key=True, max_length=20,help_text='Code uniquely identify a stock item')
	si_name = models.CharField(verbose_name='Stock Item',max_length=100, help_text='The name of the stock item')
	si_st_code = models.ForeignKey(StockType, on_delete=models.CASCADE,verbose_name='Stock Type', help_text='StockType')
	si_pt_code = models.ForeignKey(PackType, related_name='packagetype',on_delete=models.CASCADE,verbose_name='Package Type', help_text='Package Type')
	si_sn_code = models.ForeignKey(StoreName, on_delete=models.CASCADE, related_name='si_store',verbose_name='Store', help_text='The Store', null=True, blank=True)
	si_desc = models.CharField(verbose_name='description',max_length=100, help_text='Description of StockType')
	si_qty = models.DecimalField(verbose_name='Quantity',max_digits=15, decimal_places=2, help_text='Quantity',default=0)
	si_reord_qty = models.DecimalField(verbose_name='Re-Order',max_digits=15, decimal_places=2, help_text='The re-order quantity',default=0)
	si_std_cost = models.DecimalField(verbose_name='Std Cost',max_digits=15, decimal_places=2, help_text='Standard Cost',default=0)
	si_avg_cost = models.DecimalField(verbose_name='Avg Cost',max_digits=15, decimal_places=2, help_text='Average Cost',default=0)
	si_price_b = models.DecimalField(verbose_name='Base Price',max_digits=15, decimal_places=2, help_text='Price at base currency', default=0)
	si_price_1 = models.DecimalField(verbose_name='Price 1',max_digits=15, decimal_places=2, help_text='Price at currency 1', default=0)
	si_price_2 = models.DecimalField(verbose_name='Price 2',max_digits=15, decimal_places=2,  help_text='Price at currency 2', default=0)
	si_cu_id_b = models.ForeignKey(Currency, on_delete=models.CASCADE,related_name='base_curr',verbose_name='Base Currency', help_text='Base Currency')
	si_cu_id_1 = models.ForeignKey(Currency, on_delete=models.CASCADE,related_name='first_curr',verbose_name='Currency 1', help_text='Currency 1', null=True, blank=True)
	si_cu_id_2 = models.ForeignKey(Currency, on_delete=models.CASCADE,related_name='sec_curr',verbose_name='Currency 2', help_text='Currency 2', null=True, blank=True)
	si_tax = models.DecimalField(verbose_name='Tax Rate', help_text='Exch. Rate', blank=True, null=True, max_digits=15, decimal_places=2, default=0)
	si_disc = models.DecimalField(verbose_name='Discount', help_text='Discount', blank=True, null=True, max_digits=15,decimal_places=2, default=0)
	si_status = models.CharField(verbose_name='Status',max_length=1, choices=si_status_choices, help_text='Status of the Stock Item', default='1')
	ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['si_code']
		verbose_name = 'Stock Item'

	def __str__(self):
		return self.si_name

	def get_absolute_url(self):
		return reverse('Index', args=[str(self.si_code)])

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

#Customer Class - class representing the Customers
class Customer(models.Model):
	cs_type_choices = (('C', 'Cash'), ('A', 'Account'))
	cs_status_choices = (('1', 'Active'), ('0', 'Inactive'))

	cs_num		=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying the Customer')
	cs_code		=	models.CharField(verbose_name='Assigned Number',blank=True, null=True, max_length=100, help_text='Customer Code')
	cs_sn_code 	= 	models.ForeignKey(StoreName, on_delete=models.CASCADE,verbose_name='Store', help_text='Customer s Store')
	cs_fname	=	models.CharField(verbose_name='Name', max_length=200, blank=True, null=True, help_text='The Customer s first name')
	cs_sname	=	models.CharField(verbose_name='Name', max_length=200, blank=True, null=True, help_text='The Customer s  surname name')
	cs_type		=	models.CharField(verbose_name='Customer Type', max_length=200,choices=cs_type_choices, default='1', help_text='Type of the customer')
	cs_mobile	=	models.IntegerField(verbose_name='Mobile Phone',blank=True, null=True, help_text='Customer s mobile phone number')
	cs_email	=	models.EmailField(verbose_name='Email', max_length=100,blank=True, null=True, help_text='Customer s email address')
	cs_contact	=	models.CharField(verbose_name='Contact Person1',blank=True, null=True,max_length=100, help_text='First contact person')
	cs_paddress	=	models.CharField(verbose_name='Physical Address',blank=True, null=True, max_length=200, help_text='Physical Address line')
	cs_reg_date	=	models.DateTimeField(verbose_name='Reg. Date',blank=True, null=True, help_text='Date of Registration')
	cs_to_code	=	models.ForeignKey(Town, on_delete=models.CASCADE,blank=True, null=True,verbose_name='Town', help_text='Customr s town')
	cs_status 	= 	models.CharField(verbose_name='Status',max_length=1, choices=cs_status_choices, help_text='Status of the Customer', default='1')
	ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['cs_sname']
		verbose_name = 'Customer'

	def __str__(self):
		return self.cs_sname

	def get_absolute_url(self):
		return reverse('Index', args=[str(self.cs_num)])

	def get_post_url(self):
			return reverse('edit', kwargs={'pk': self.pk})

#StoreOrder Class - class representing the Orders
class StoreOrder(models.Model):
	so_type_choices = (('C', 'Cash Order'), ('O', 'Other'))
	so_pur_sales = (('P', 'Purchase Order'), ('S', 'Sales Order'))
	so_received = (('Y', 'Yes'), ('N', 'No'))
	so_invoiced = (('Y', 'Yes'), ('N', 'No'))
	so_status_choices = (('1', 'Active'), ('0', 'Inactive'))

	so_num		=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying the Order')
	so_code		=	models.CharField(verbose_name='Assigned Number',blank=True, null=True, max_length=100, help_text='Order Code')
	so_cs_num 	= models.ForeignKey(Customer, on_delete=models.CASCADE,verbose_name='Order', help_text='Customer')
	so_sn_code = models.ForeignKey(StoreName, on_delete=models.CASCADE, related_name='o_store',verbose_name='Store', help_text='The Store', null=True, blank=True)
	so_type		=	models.CharField(verbose_name='Order Type', max_length=1,choices=so_type_choices, default='C', help_text='Type of the Order')
	so_p_s		=	models.CharField(verbose_name='Purchase/Sales', max_length=1,choices=so_pur_sales, default='S', help_text='Type of the Order')
	so_mobile	=	models.IntegerField(verbose_name='Mobile Phone',blank=True, null=True, help_text='Order s mobile phone number')
	so_email	=	models.EmailField(verbose_name='Email', max_length=100,blank=True, null=True, help_text='Order s email address')
	so_contact	=	models.CharField(verbose_name='Contact Person1',blank=True, null=True,max_length=100, help_text='First contact person')
	so_paddress	=	models.CharField(verbose_name='Physical Address',blank=True, null=True, max_length=200, help_text='Delivery Address')
	so_ord_date	=	models.DateTimeField(verbose_name='Order Date',blank=True, null=True, help_text='Date of Order')
	so_del_date	=	models.DateTimeField(verbose_name='Req Date',blank=True, null=True, help_text='Date of Order is required')
	so_to_code	=	models.ForeignKey(Town, on_delete=models.CASCADE,blank=True, null=True,verbose_name='Town', help_text='Order town')
	so_trans_amnt	=  	models.DecimalField(verbose_name='Trans. Amnt', help_text='Trans. Amnt', blank=True, null=True,max_digits=15, decimal_places=2,default=0)
	so_base_amnt	=  	models.DecimalField(verbose_name='Base Amnt', help_text='Base Amnt', blank=True, null=True,max_digits=15, decimal_places=2,default=0)
	so_tax_amnt = models.DecimalField(verbose_name='Tax Amount', help_text='Total Tax amount', max_digits=15, decimal_places=2, blank=True, null=True, default=0)
	so_disc_amnt = models.DecimalField(verbose_name='Disc Amnt', help_text='Total Discount amnt', max_digits=15, decimal_places=2, blank=True, null=True, default=0)
	so_tot_amnt = models.DecimalField(verbose_name='Total Amnt', help_text='Total amount due', max_digits=15, decimal_places=2, blank=True, null=True, default=0)
	so_status 	= models.CharField(verbose_name='Status',max_length=1, choices=so_status_choices, help_text='Status of the Order', default='1')
	so_received 	= models.CharField(verbose_name='Status',max_length=1, choices=so_received, help_text='Status of the Order', default='Y')
	so_rec_date	=	models.DateTimeField(verbose_name='Rec. Date',blank=True, null=True, help_text='Date of Goods receipt')
	so_invoiced 	= models.CharField(verbose_name='Status',max_length=1, choices=so_invoiced, help_text='Status of the Order', default='Y')
	so_inv_date	=	models.DateTimeField(verbose_name='Inv. Date',blank=True, null=True, help_text='Date of Invoicing')
	ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['so_type']
		verbose_name = 'Store Order'

	def __str__(self):
		return self.so_code

	def get_absolute_url(self):
		return reverse('Index', args=[str(self.so_num)])

	def get_post_url(self):
			return reverse('edit', kwargs={'pk': self.pk})

#OrderItem Class - class representing the OrderItem
class OrderItem(models.Model):
    oi_status_choices = (('1', 'Active'), ('0', 'Inactive'))
    io_pur_sales = (('P', 'Purchase Order'), ('S', 'Sales Order'))

    oi_num = models.AutoField(verbose_name='Number', primary_key=True, help_text='System generated number uniquely identifying the Order')
    oi_so_num = models.ForeignKey(StoreOrder, on_delete=models.CASCADE, verbose_name='Store Order', blank=True,null=True, help_text='Store Order')
    oi_si_code = models.ForeignKey(StockItem, on_delete=models.CASCADE, verbose_name='Stock Item',help_text='Stock Item')
    oi_so_p_s = models.CharField(verbose_name='Purchase/Sales', max_length=1, choices=io_pur_sales, default='S',help_text='Type of the Order')
    oi_pt_code = models.ForeignKey(PackType, on_delete=models.CASCADE, verbose_name='Pack Type', help_text='Pack Type')
    oi_cu_id = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name='Currency', help_text='Currency')
    oi_ord_qty = models.DecimalField(verbose_name='O Quantity', help_text='Ordered Quantity', max_digits=15, blank=True,null=True, decimal_places=2)
    oi_rec_qty = models.DecimalField(verbose_name='R Quantity', help_text='Recieved Quantity', max_digits=15, blank=True,null=True, decimal_places=2)
    oi_uprice = models.DecimalField(verbose_name='Unit Price', help_text='Unit Price', max_digits=15, blank=True, null=True,decimal_places=2, default=0)
    oi_ucost = models.DecimalField(verbose_name='Avg Cost', help_text='Avg Cost', max_digits=15, blank=True, null=True,decimal_places=2, default=0)
    oi_trans_amnt = models.DecimalField(verbose_name='Trans. Amnt', help_text='Trans. Amnt', blank=True, null=True,max_digits=15, decimal_places=2, default=0)
    oi_base_amnt = models.DecimalField(verbose_name='Base Amnt', help_text='Base Amnt', blank=True, null=True, max_digits=15, decimal_places=2, default=0)
    oi_tax_amnt = models.DecimalField(verbose_name='Tax Amount', help_text='Total Tax amount', max_digits=15,decimal_places=2, blank=True, null=True, default=0)
    oi_disc_amnt = models.DecimalField(verbose_name='Disc Amnt', help_text='Total Discount amnt', max_digits=15,decimal_places=2, blank=True, null=True, default=0)
    oi_tot_amnt = models.DecimalField(verbose_name='Total Amnt', help_text='Total amount due', max_digits=15, decimal_places=2, blank=True, null=True, default=0)
    oi_rate = models.DecimalField(verbose_name='Exch. Rate', help_text='Exch. Rate', blank=True, null=True, max_digits=15,decimal_places=2, default=0)
    oi_tax = models.DecimalField(verbose_name='Tax Rate', help_text='Exch. Rate', blank=True, null=True, max_digits=15, decimal_places=2, default=0)
    oi_disc = models.DecimalField(verbose_name='Discount', help_text='Discount', blank=True, null=True, max_digits=15, decimal_places=2, default=0)
    oi_status = models.CharField(verbose_name='Status', max_length=1, choices=oi_status_choices, help_text='Status of the Order', default='1')
    ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')


    class Meta:
        ordering = ['oi_status']
        verbose_name = 'Order Item'

    def __str__(self):
        return self.oi_status

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.oi_num)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#Start Interation Models

class PostCategory(models.Model):
	ct_code = models.CharField(verbose_name='Code', max_length=10, primary_key=True,help_text='Enter code uniquely identifying post category')
	ct_desc = models.CharField(max_length=50, blank=True, null=True, help_text='The description of the category')
	ct_seo_title = models.CharField(verbose_name = 'SEO Title',max_length=300, blank=True, null=True, help_text='The SEO title of the blog')
	ct_seo_desc = models.CharField(verbose_name = 'SEO Description',max_length=250, blank=True, null=True, help_text='The SEO description of the blog')
	slug = models.SlugField(max_length=250, unique=True, help_text='The slug field for the blog for user facing title', blank=True)
	ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['ct_desc']
		verbose_name = 'Blog Category'

	def save(self, *arg, **kwargs):
		self.slug = slugify(str(self.ct_desc))
		super(PostCategory, self).save(*arg, **kwargs)

	def __str__(self):
		return self.ct_desc

	def get_absolute_url(self):
		return reverse('IndexView', args=[str(self.ct_desc)])

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

class PostOrigin(models.Model):
	po_num = models.CharField(verbose_name='Code', max_length=10, primary_key=True,help_text='Enter code uniquely identifying originator of the post')
	po_name = models.CharField(max_length=100, blank=True, null=True, help_text='The name of the originator')
	po_position = models.CharField(max_length=50, blank=True, null=True, help_text='The position/title of the originator')
	ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['po_name']
		verbose_name = 'PostOrigin'

	def __str__(self):
		return self.po_name

	def get_absolute_url(self):
		return reverse('IndexView', args=[str(self.po_name)])

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

class BlogPost(models.Model):
	bp_choices = (('D', 'Draft'), ('R', 'Peered'), ('P', 'Publish'))
	bp_num = models.AutoField(verbose_name='Post Number',primary_key=True, help_text='Number uniquely identifying the post')
	bp_ct_code = models.ForeignKey(PostCategory, on_delete=models.CASCADE,verbose_name='Category', help_text='Category into which this post falls')
	bp_po_num = models.ForeignKey(PostOrigin, on_delete=models.CASCADE,verbose_name='Originator', help_text='The originator of the post')
	bp_heading = models.CharField(verbose_name='Heading',max_length=100, help_text='The heading of the post')
	bp_seo_title = models.CharField(verbose_name = 'SEO Title',max_length=300, blank=True, null=True, help_text='The SEO title of the blog')
	bp_seo_desc = models.CharField(verbose_name = 'SEO Description',max_length=250, blank=True, null=True, help_text='The SEO description of the blog')
	slug = models.SlugField(max_length=250, unique=True, help_text='The slug field for the blog for user facing title', blank=True)
	bp_date = models.DateTimeField(auto_now_add=True, help_text='Date on which this post was created')
	bp_body = models.TextField(verbose_name='Message',max_length=350, help_text='The post s message')
	bp_status = models.CharField(verbose_name='Status',max_length=1, choices=bp_choices, default='D', help_text='Enter the status of the post')
	bp_file = models.FileField(upload_to='media/', verbose_name='Attachment File', help_text = 'Choose File to upload',blank=True,null=True)
	bp_image = models.ImageField(upload_to='media/', verbose_name='Image', help_text='Choose image to upload',blank=True,null=True)
	ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['bp_date']
		verbose_name = 'Blog Post'

	def save(self, *arg, **kwargs):
		self.slug = slugify(str(self.bp_heading))
		super(BlogPost, self).save(*arg, **kwargs)

	def __str__(self):
		return self.bp_heading

	def get_absolute_url(self):
		#return reverse('Index', args=[str(self.bp_heading)])
		return reverse('index', kwargs={'pk': self.pk, 'slug': self.slug})

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

class PostContribution(models.Model):
	pc_num = models.AutoField(verbose_name='Contribution Number',primary_key=True, help_text='Number uniquely identifying the contribution')
	pc_bp_num = models.ForeignKey(BlogPost, on_delete=models.CASCADE,verbose_name='BlogPost', db_column='pc_bp_num', related_name='contributions', help_text='The Reference post for this contribution')
	pc_contribution = models.TextField(verbose_name='Contribution',max_length=350, help_text='The contribution to a post')
	pc_email = models.EmailField(verbose_name='Email', blank=True, null=True,help_text='The contributor s email')
	pc_contributor = models.CharField(verbose_name='Contributor',max_length=50, blank=True, null=True, help_text='The name of the contributor')
	pc_active = models.BooleanField(verbose_name='Accepted',default=False , help_text='Indicates whether contribution is accepted or not')
	ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The Creating record')
	ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['ad_date_c']
		verbose_name = 'Contribution'

	def __str__(self):
		return self.pc_contribution

	def get_absolute_url(self):
		return reverse('Index', args=[str(self.pc_num)])

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

	def approve_contributions(self):
		self.pc_active=True
		self.save()
