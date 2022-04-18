
from ast import Try
from distutils import text_file
from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from httpx import request
from numpy import char




# Create your models here.
class User_details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # Role = models.CharField(null=False,max_length=50)
    subject = models.CharField(null=True, max_length=50)
    qualification = models.CharField(null=True, max_length=50)
    designation = models.CharField(null=True, max_length=50)
    contact = models.BigIntegerField(null=False)
    date_of_joining = models.DateField(null=True)
    teacher_code = models.BigIntegerField(null=True)
    gender = models.CharField(null=False, max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pics',blank=True,null=True)
    
class General_Register(models.Model):
    lang = models.CharField(null=False, max_length=50)
    gr_number = models.IntegerField(null=False)
    student_name = models.CharField(null=False, max_length=255)
    mother_name = models.CharField(null=True, max_length=50)
    religion = models.CharField(null=False, max_length=100)
    birth_place = models.CharField(null=False, max_length=50)
    dob = models.CharField(null=False, max_length=50)
    dob_in_words = models.CharField(null=False, max_length=50)
    previous_school_std = models.TextField(null=False)
    school_joining = models.CharField(null=False, max_length=50)
    admission_std = models.CharField(null=False, max_length=50)
    fees = models.CharField(null=True,max_length=50)
    date_leaving = models.CharField(null=False, max_length=50)
    leaving_std = models.CharField(null=False, max_length=50)
    leaving_reason = models.TextField(null=False)
    progress = models.CharField(null=False, max_length=50)    
    behaviour = models.CharField(null=False, max_length=50)
    date_taking_lc = models.CharField(null=False, max_length=50)
    note = models.TextField(null=False)
        

class Keyword_Defination(models.Model):
    term = models.CharField(null=False, max_length=255)
    text = models.TextField(null=False)
    lang = models.CharField(null=False, max_length=50)
    
class Grant_Register(models.Model):
    entry_no = models.IntegerField(null=False,unique=True)
    grant_details = models.TextField(null=False)
    amount = models.CharField(null=False, max_length=50)
    order_no = models.CharField(null=False, max_length=100)
    bank_deposite_date = models.DateField(null=False, auto_now=False, auto_now_add=False)
    remarks = models.TextField(null=False)
    
class Cash_Book(models.Model):
    entry_no = models.IntegerField(null=False)
    date = models.DateField(null=False, auto_now=False, auto_now_add=False)
    name_and_particulars = models.TextField(null=False)
    reciept = models.CharField(null=True, blank=True, max_length=50)
    voucher_no = models.CharField(null=True,blank=True, max_length=50)
    total_amount = models.CharField(null=False,max_length=50)
    debit_or_credit = models.CharField(null=False, max_length=50)
    
class General_Ledger(models.Model):
    entry_no = models.IntegerField(null=False)
    date = models.DateField(null=False, auto_now=False, auto_now_add=False)
    particulars = models.TextField(null=False)
    c_b_r_no = models.ForeignKey(Cash_Book, on_delete=models.CASCADE)
    credit = models.CharField(null=False, max_length=50)
    debit = models.CharField(null=False, max_length=50)
    credit_bal = models.CharField(null=False, max_length=50)
    debit_bal = models.CharField(null=True, max_length=50)
    name_of_account = models.CharField(null=False, max_length=50)
    
    
class Cheque_Register(models.Model):
    entry_no = models.IntegerField(null=False,unique=True)
    date = models.DateField(null=False, auto_now=False, auto_now_add=False)
    agency_name = models.CharField(null=False, max_length=255)
    purchase_detail = models.CharField(null=False, max_length=255)
    bill_no = models.CharField(null=False, max_length=50)
    cheque_no = models.CharField(null=False, max_length=100)
    cheque_date = models.DateField(null=False, auto_now=False, auto_now_add=False)
    amount = models.CharField(null=False, max_length=50)
    paying_amount = models.CharField(null=False, max_length=50)
    
class Bill_Book(models.Model):
    entry_no = models.IntegerField(null=False)
    bill_from = models.CharField(null=False, max_length=100)
    date = models.DateField(null=False, auto_now=False, auto_now_add=False)
    bill_voucher = models.CharField(null=False, max_length=200)
    bill_amount = models.CharField(null=False, max_length=255)
    payable_amount = models.CharField(null=False, max_length=50)
    
class Student_Data(models.Model):
    student_name = models.CharField(null=False, max_length=255) 
    standard = models.CharField(null=False, max_length=50)
    gender = models.CharField(null=False, max_length=50)
    cast = models.CharField(null=False, max_length=50)
    division = models.CharField(null=False,max_length=50)
    udise = models.CharField(null=False, max_length=155)
    
class Attendance(models.Model):
    date = models.DateField(null=False, auto_now=False, auto_now_add=False)
    attendance=models.CharField(null=False, max_length=50)
    student = models.ForeignKey(Student_Data,on_delete=models.CASCADE)
    
class Quote(models.Model):
    term = models.CharField(null=False, max_length=50)
    qoute = models.TextField(null=False)
    
class Useful_Links(models.Model):
    term = models.CharField(null=False, max_length=255)
    link = models.CharField(null=False, max_length=255)
    category = models.CharField(null=False, max_length=50)
    
class Noticeboard(models.Model):
    title = models.CharField(null=False, max_length=50)
    body = models.TextField(null=False)
 
class Gal_Category(models.Model):
    category = models.CharField(null=False, max_length=100)
    
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    desc = models.CharField(null=True, max_length=255)
    category = models.ForeignKey(Gal_Category,on_delete=models.CASCADE)
    
