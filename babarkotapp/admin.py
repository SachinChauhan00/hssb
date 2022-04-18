from django.contrib import admin

from babarkotapp.views import cashbook
from .models import *

# Register your models here.

@admin.register(User_details)
class User_ContactAdmin(admin.ModelAdmin):
    list_display = ['id','user','subject','qualification','designation','contact','date_of_joining','teacher_code','gender','profile_picture']
    
@admin.register(General_Register)
class General_RegisterAdmin(admin.ModelAdmin):
    list_display = ['lang','gr_number','student_name','religion','birth_place','dob','dob_in_words','previous_school_std','school_joining','admission_std','fees','date_leaving','leaving_std','leaving_reason','progress','behaviour','date_taking_lc','note']

@admin.register(Keyword_Defination)
class Keyword_DefinationAdmin(admin.ModelAdmin):
    list_display = ['term','text','lang']
    
@admin.register(Grant_Register)
class Grant_RegisterAdmin(admin.ModelAdmin):
    list_display = ['entry_no','grant_details','amount','order_no','bank_deposite_date','remarks']
  
@admin.register(Gal_Category)
class Gal_CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']  
   
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['image','desc','category']

@admin.register(Cash_Book)
class Cash_BookAdmin(admin.ModelAdmin):
    list_display = ['entry_no','date','name_and_particulars','reciept','voucher_no','total_amount','debit_or_credit']
    
@admin.register(General_Ledger)
class Geeral_LedgerAdmin(admin.ModelAdmin):
    list_display = ['entry_no','date','particulars','c_b_r_no','credit','debit','credit_bal','debit_bal','name_of_account']