from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(User_details)
class User_ContactAdmin(admin.ModelAdmin):
    list_display = ['id','user','subject','qualification','designation','contact','date_of_joining','gender','profile_picture']
    
@admin.register(General_Register)
class General_RegisterAdmin(admin.ModelAdmin):
    list_display = ['lang','gr_number','student_name','religion','birth_place','dob','dob_in_words','previous_school_std','school_joining','admission_std','fees','date_leaving','leaving_std','leaving_reason','progress','behaviour','date_taking_lc','note']

@admin.register(Keyword_Defination)
class Keyword_DefinationAdmin(admin.ModelAdmin):
    list_display = ['term','text','lang']
    
@admin.register(Grant_Register)
class Grant_RegisterAdmin(admin.ModelAdmin):
    list_display = ['entry_no','account','grant_details','amount','order_no','bank_deposite_date','remarks']
    
@admin.register(Cash_Book)
class Cash_BookAdmin(admin.ModelAdmin):
    list_display = ['entry_no','ledger','date','name_and_particulars','reciept','voucher_no','total_amount','debit_or_credit']
    
@admin.register(General_Ledger)
class Geeral_LedgerAdmin(admin.ModelAdmin):
    list_display = ['entry_no','account','date','particulars','credit','debit','credit_bal','debit_bal']    

@admin.register(Cheque_Register)
class Cheque_RegisterAdmin(admin.ModelAdmin):
    list_display = ['entry_no','account','date','agency_name','purchase_detail','bill_no','cheque_no','cheque_date','amount','paying_amount']      

@admin.register(Bill_Book)
class Bill_BookAdmin(admin.ModelAdmin):
    list_display = ['entry_no','account','bill_from','date','bill_voucher','bill_amount','payable_amount']      

@admin.register(Student_Data)
class Student_DataAdmin(admin.ModelAdmin):
    list_display = ['student_name','standard','gender','cast','division','udise']      
  
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['date','attendance','student']      
  
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['term','qoute']      
    
@admin.register(Useful_Links)
class Useful_LinksAdmin(admin.ModelAdmin):
    list_display = ['term','link','category']      
  
@admin.register(Noticeboard)
class NoticeboardAdmin(admin.ModelAdmin):
    list_display = ['title','body']      
  
@admin.register(Gal_Category)
class Gal_CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category']  
   
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id','image','desc','category']

@admin.register(Briliant_Students)
class Briliant_StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name','standard','division','achievement','date']
    
@admin.register(school_speciality)
class school_specialityAdmin(admin.ModelAdmin):
    list_display = ['id','body']
    
@admin.register(Account_Model)
class Account_ModelAdmin(admin.ModelAdmin):
    list_display = ['id','account_name']