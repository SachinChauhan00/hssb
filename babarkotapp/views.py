
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, logout, login as my_login
from django.shortcuts import render, redirect
from django.utils import (dateformat, formats)
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
from babarkotsite.settings import BASE_DIR
from .models import *
import xlsxwriter
import os
import dateutil.parser
from datetime import date
from django.http.response import HttpResponse,FileResponse


# creating the date object of today's date
todays_date = date.today()

# Create your views here.

def index(request):
    request.session['color'] = '#009EFF' 
    quote = Quote.objects.get(pk='1')   
    return render(request, "index.html", {'home': 'active','quote':quote})



def login(request):
    if 'lang' in request.session:
        lang = request.session['lang']
        print(lang)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            my_login(request, user)
            nex = User.objects.get(username=username)
            request.session['first_name'] = nex.first_name
            return redirect('index')
        else:
            messages.error(request, "Login Error! Try Again")
    return render(request, "login.html")
# def register(request):
#     return render(request, "register.html",{'reg':'active'})


def teacher_signup(request):
    role = "Teacher"

    if request.method == "POST":
        profile_picture = request.FILES['pp']
        username = request.POST.get('uname')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        qualification = request.POST.get('qualification')
        subject = request.POST.get('subject')
        password = request.POST.get('pass')
        designation = request.POST.get('designation')
        contact = request.POST.get('contact')
        DOJ = request.POST.get('date')
        teacher_code = request.POST.get('tcode')
        gender = request.POST.get('gender')

        # fetch and filter
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username Already Used Try Different One!")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "This Email Is Already Used!")
        elif User_details.objects.filter(contact=contact).exists():
            messages.error(request, "This Contact Is Already Used!")
        elif User_details.objects.filter(teacher_code=teacher_code).exists():
            messages.error(request, "Teacher Code Already Registered")
        else:
            user = User.objects.create_user(
                username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            contact_sv = User_details.objects.create(user=user, profile_picture=profile_picture, qualification=qualification, subject=subject,
                                                     designation=designation, contact=contact, date_of_joining=DOJ, teacher_code=teacher_code, gender=gender)
            user.save()
            contact_sv.save()
    return render(request, "teacher_signup.html", {'nav': 'active'})

def edit_profile(request,id):
    # Male = ""
    # Female = ""
    # user = User.objects.get(pk=id)
    # user_details = User_details.objects.get(user=user)
    # if user_details.gender == "Male" :
    #     Male = "checked"
    # else:
    #     Female = "checked"
    # if request.method == "POST":
    #     # profile_picture = request.FILES['pp']
    #     username = request.POST.get('uname')
    #     first_name = request.POST.get('fname')
    #     last_name = request.POST.get('lname')
    #     email = request.POST.get('email')
    #     qualification = request.POST.get('qualification')
    #     subject = request.POST.get('subject')
    #     password = request.POST.get('pass')
    #     designation = request.POST.get('designation')
    #     contact = request.POST.get('contact')
    #     DOJ = request.POST.get('date')
    #     teacher_code = request.POST.get('tcode')
    #     gender = request.POST.get('gender')
        
    #         # user_details.profile_picture.delete(False)
    #     try:
    #         if profile_picture != "":
    #             print('got profile')
    #         else:
    #             pass
    #         # user_details.profile_picture.delete(False)
    #         userlog = User.objects.filter(pk=id).update(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
    #         userdet = User_details.objects.filter(user=userlog).update(user=userlog, profile_picture=profile_picture, qualification=qualification, subject=subject,designation=designation, contact=contact, date_of_joining=DOJ, teacher_code=teacher_code, gender=gender)
    #         return redirect('account_list')
    #     except:
    #         messages.error(request,"Something Went Wrong!")
    #     # except:
        #     messages.error(request,"Something Went Wrong!")
    return render(request,"edit_user.html",{'user':user,'user_details':user_details,'male':Male,'female':Female})
   

def General_register(request):
  
    gr = General_Register.objects.filter(lang='en')
    cl1 = "GR No."
    cl2 = "Student Full Name"
    cl3 = "Mother Name"
    cl4 = "Religion And Race"
    cl5 = "Place Of Birth"
    cl6 = "Date Of Birth"
    cl7 = "Date Of Birth In Words"
    cl8 = "Previous School And Standard"
    cl9 = "Date Of School Joining"
    cl10 = "Admission Standard"
    cl11 = "Fees Or Waiver"
    cl12 = "Date Of Leaving School"
    cl13 = "Standard When Leaving School"
    cl14 = "Reason Of Leaving School"
    cl15 = "Progress"
    cl16 = "Behaviour"
    cl17 = "Date Of Taking LC"
    cl18 = "Note"
    cl19 = "Edit"
    cl20 = "Delete"
    # elif request.session['lang'] == 'gu':
    #     gr = General_Register.objects.filter(lang='gu')
    #     cl1 = "સામાન્ય વય પત્રક નંબર"
    #     cl2 = "વિધ્યાર્થીનું પૂરેપુરું નામ અને માતાનું નામ"
    #     cl3 = "ધર્મ અને જાતિ"
    #     cl4 = "જન્મ સ્થળ"
    #     cl5 = "ખ્રિસ્તી વર્ષ અનુસાર જન્મની તારીખ, મહિનો, સાલ"
    #     cl6 = "જન્મ તારીખ શબ્દોમાં"
    #     cl7 = "પૂર્વ શાળા અને ધોરણ"
    #     cl8 = "નિશાળમાં દાખલ થયાની તારીખ કે ખાતા મંજૂરી હોય તો તેની નોંધ"
    #     cl9 = "પ્રવેશ આપવા માં આવેલ ધોરણ અને વર્ગ"
    #     cl10 = "ફી ભરીને કે માફી"
    #     cl11 = "શાળા છોડયાની તારીખ"
    #     cl12 = "શાળા છોડતી વખતે ધોરણ અને વર્ગ"
    #     cl13 = "શાળા છોડવાનું કારણ"
    #     cl14 = "પ્રગતિ"
    #     cl15 = "વર્તણૂક"
    #     cl16 = "લીવીંગ સર્ટિ. આપ્યાની તારીખ"
    #     cl17 = "નોંધ (બાકી ફી, ડુપ્લિકેટ સર્ટિ વિગેરે.)"
    #     cl18 = "ફેરફાર કરો"
    #     cl19 = "કાઢી નાખો"
    if request.method == "POST":
        name = "General Register ("+str(todays_date.year)+").xlxs"
        if 'download' in request.POST:
            if request.session['lang'] == 'en':    
            
                workbook = xlsxwriter.Workbook(BASE_DIR/'General Register'/name)
                worksheet = workbook.add_worksheet()
                worksheet.write(0, 0, "GR No.")
                worksheet.write(0, 1, "Student Full Name")
                worksheet.write(0, 2, "Religion And Race")
                worksheet.write(0, 3, "Place Of Birth")
                worksheet.write(0, 4, "Date Of Birth")
                worksheet.write(0, 5, "Date Of Birth In Words")
                worksheet.write(0, 6, "Previous School And Standard")
                worksheet.write(0, 7, "Date Of School Joining")
                worksheet.write(0, 8, "Admission Standard")
                worksheet.write(0, 9, "Fees Or Waiver")
                worksheet.write(0, 10, "Date Of Leaving School")
                worksheet.write(0, 11, "Standard When Leaving School")
                worksheet.write(0, 12, "Reason Of Leaving School")
                worksheet.write(0, 13, "Progress")
                worksheet.write(0, 14, "Behaviour")
                worksheet.write(0, 15, "Date Of Taking LC")
                worksheet.write(0, 16, "Note")

                row = 1
                col = 0

                for record in gr:
                    worksheet.write(row, col, record.gr_number)
                    worksheet.write(row, col + 1, record.student_name)
                    worksheet.write(row, col + 2, record.religion)
                    worksheet.write(row, col + 3, record.birth_place)
                    worksheet.write(row, col + 4, record.dob)
                    worksheet.write(row, col + 5, record.dob_in_words)
                    worksheet.write(row, col + 6, record.previous_school_std)
                    worksheet.write(row, col + 7, record.school_joining)
                    worksheet.write(row, col + 8, record.admission_std)
                    worksheet.write(row, col + 9, record.fees)
                    worksheet.write(row, col + 10, record.date_leaving)
                    worksheet.write(row, col + 11, record.leaving_std)
                    worksheet.write(row, col + 12, record.leaving_reason)
                    worksheet.write(row, col + 13, record.progress)
                    worksheet.write(row, col + 14, record.behaviour)
                    worksheet.write(row, col + 15, record.date_taking_lc)
                    worksheet.write(row, col + 16, record.note)
                    row += 1

                workbook.close()
            elif request.session['lang'] == 'gu':    
                workbook = xlsxwriter.Workbook(BASE_DIR/'General Register'/name)
                worksheet = workbook.add_worksheet()
                worksheet.write(0, 0, "સામાન્ય વય પત્રક નંબર")
                worksheet.write(0, 1, "વિધ્યાર્થીનું પૂરેપુરું નામ અને માતાનું નામ")
                worksheet.write(0, 2, "ધર્મ અને જાતિ")
                worksheet.write(0, 3, "જન્મ સ્થળ")
                worksheet.write(0, 4, "ખ્રિસ્તી વર્ષ અનુસાર જન્મની તારીખ, મહિનો, સાલ")
                worksheet.write(0, 5, "જન્મ તારીખ શબ્દોમાં")
                worksheet.write(0, 6, "પૂર્વ શાળા અને ધોરણ")
                worksheet.write(0, 7, "નિશાળમાં દાખલ થયાની તારીખ કે ખાતા મંજૂરી હોય તો તેની નોંધ")
                worksheet.write(0, 8, "પ્રવેશ આપવા માં આવેલ ધોરણ અને વર્ગ")
                worksheet.write(0, 9, "ફી ભરીને કે માફી")
                worksheet.write(0, 10, "શાળા છોડયાની તારીખ")
                worksheet.write(0, 11, "શાળા છોડતી વખતે ધોરણ અને વર્ગ")
                worksheet.write(0, 12, "શાળા છોડવાનું કારણ")
                worksheet.write(0, 13, "પ્રગતિ")
                worksheet.write(0, 14, "વર્તણૂક")
                worksheet.write(0, 15, "લીવીંગ સર્ટિ. આપ્યાની તારીખ")
                worksheet.write(0, 16, "નોંધ (બાકી ફી, ડુપ્લિકેટ સર્ટિ વિગેરે.)")

                row = 1
                col = 0

                for record in gr:
                    worksheet.write(row, col, record.gr_number)
                    worksheet.write(row, col + 1, record.student_name)
                    worksheet.write(row, col + 2, record.religion)
                    worksheet.write(row, col + 3, record.birth_place)
                    worksheet.write(row, col + 4, record.dob)
                    worksheet.write(row, col + 5, record.dob_in_words)
                    worksheet.write(row, col + 6, record.previous_school_std)
                    worksheet.write(row, col + 7, record.school_joining)
                    worksheet.write(row, col + 8, record.admission_std)
                    worksheet.write(row, col + 9, record.fees)
                    worksheet.write(row, col + 10, record.date_leaving)
                    worksheet.write(row, col + 11, record.leaving_std)
                    worksheet.write(row, col + 12, record.leaving_reason)
                    worksheet.write(row, col + 13, record.progress)
                    worksheet.write(row, col + 14, record.behaviour)
                    worksheet.write(row, col + 15, record.date_taking_lc)
                    worksheet.write(row, col + 16, record.note)
                    row += 1

                workbook.close()
            
            path_to_file = os.path.join(BASE_DIR,'General Register',name)
            return FileResponse(open(path_to_file, 'rb'), as_attachment=True)
        elif 'add' in request.POST:
            return redirect('add_gr')
    return render(request,"general_register.html",{'gr':gr,'cl1':cl1,'cl2':cl2,'cl3':cl3,'cl4':cl4,'cl5':cl5,'cl6':cl6,'cl7':cl7,'cl8':cl8,'cl9':cl9,'cl10':cl10,'cl11':cl11,'cl12':cl12,'cl13':cl13,'cl14':cl14,'cl15':cl15,'cl16':cl16,'cl17':cl17,'cl18':cl18,'cl19':cl19,'cl20':cl20,'nav':'active'})

def add_gr(request):
    if request.method == "POST":
        try:
            gr_no = request.POST.get('gr_num')
            stud_name = request.POST.get('full_name')
            moth_name = request.POST.get('moth_name')
            religion = request.POST.get('religion')
            birth_place = request.POST.get('birth_place')
            dob = request.POST.get('dob')
            dob_in_words = request.POST.get('dob_in_words')
            previos_school_std = request.POST.get('previos_school_std')
            dosj = request.POST.get('dosj')
            admission_std = request.POST.get('admission_std')
            fees = request.POST.get('fees')
            dols = request.POST.get('dols')
            stdleaving = request.POST.get('stdleaving')
            leaving_reason = request.POST.get('leaving_reason')
            progress = request.POST.get('progress')
            behaviour = request.POST.get('behaviour')
            dotl = request.POST.get('dotl')
            note = request.POST.get('note')
            lang = 'en'
            # guj
            gr_no_guj = request.POST.get('gr_num_gu')
            stud_name_guj = request.POST.get('full_name_gu')
            moth_name_guj = request.POST.get('moth_name_gu')
            religion_guj = request.POST.get('religion_gu')
            birth_place_guj = request.POST.get('birth_place_gu')
            dob_guj = request.POST.get('dob_gu')
            dob_in_words_guj = request.POST.get('dob_in_words_gu')
            previos_school_std_guj = request.POST.get('previos_school_std_gu')
            dosj_guj = request.POST.get('dosj_gu')
            admission_std_guj = request.POST.get('admission_std_gu')
            fees_guj = request.POST.get('fees_gu')
            dols_guj = request.POST.get('dols_gu')
            stdleaving_guj = request.POST.get('stdleaving_gu')
            leaving_reason_guj = request.POST.get('leaving_reason_gu')
            progress_guj = request.POST.get('progress_gu')
            behaviour_guj = request.POST.get('behaviour_gu')
            dotl_guj = request.POST.get('dotl_gu')
            note_guj = request.POST.get('note_gu')
            lang_guj = 'gu'
            add_gr = General_Register.objects.create(gr_number=gr_no,student_name=stud_name,mother_name=moth_name,religion=religion,birth_place=birth_place,dob=dob,dob_in_words=dob_in_words,previous_school_std=previos_school_std,school_joining=dosj,admission_std=admission_std,fees=fees,date_leaving=dols,leaving_std=stdleaving,leaving_reason=leaving_reason,progress=progress,behaviour=behaviour,date_taking_lc=dotl,note=note,lang=lang)
            add_gr_guj = General_Register.objects.create(gr_number=gr_no_guj,student_name=stud_name_guj,mother_name=moth_name_guj,religion=religion_guj,birth_place=birth_place_guj,dob=dob_guj,dob_in_words=dob_in_words_guj,previous_school_std=previos_school_std_guj,school_joining=dosj_guj,admission_std=admission_std_guj,fees=fees_guj,date_leaving=dols_guj,leaving_std=stdleaving_guj,leaving_reason=leaving_reason_guj,progress=progress_guj,behaviour=behaviour_guj,date_taking_lc=dotl_guj,note=note_guj,lang=lang_guj)
            add_gr_guj.save()
            add_gr.save()
            messages.success(request,"Entry Succesfully Inserted!")
            return redirect('gr_view')
        except:
            messages.error(request,"Something Went Wrong!")
    return render(request,"add_gr.html",{'nav':'active'})

def add_keywords(request):
    if request.method == "POST":
        term = request.POST.get('term')
        txt = request.POST.get('txt')
        lang = request.POST.get('lang')
        term_add = Keyword_Defination.objects.create(term=term,text=txt,lang=lang)
        term_add.save()
    return render(request,"define_keyword.html",{'key':'active'})

def trail_cert(request):
    trial_student_list = General_Register.objects.filter(lang='en')
    return render(request, "trial_certificate.html",{'list':trial_student_list,'nav':'active'})



def gen_trial(request,id):
    if not General_Register.objects.filter(id=id).exists():
        return redirect('nota')
    else:
        detail = General_Register.objects.get(id=id)
        
        if request.method == "POST":
            crno = request.POST.get('crno')
            exm = request.POST.get('exm')
            attempt = request.POST.get('attempt')
            subjects = request.POST.get('sub')
            date = str(todays_date.day)+'/'+str(todays_date.month)+'/'+str(todays_date.year)
            yourdate = dateutil.parser.parse(detail.school_joining)
            todate = dateutil.parser.parse(detail.date_leaving)
            to_date = str(todate.year)
            from_date = str(yourdate.year)
            from PIL import Image, ImageDraw, ImageFont
            import pandas as pd
            font = ImageFont.truetype('arial.ttf',50)
            img = Image.open(os.path.join(BASE_DIR,"Trial Certificate",'main','trial-cert.jpg'))
            draw = ImageDraw.Draw(img)
            draw.text(xy=(650,1030 ),text='{}'.format(crno),fill=(0,0,0),font=font)
            draw.text(xy=(1850,1030 ),text='{}'.format(date),fill=(0,0,0),font=font)
            draw.text(xy=(400,1430 ),text='{}'.format(detail.student_name),fill=(0,0,0),font=font)
            draw.text(xy=(1550,1505 ),text='{}'.format(from_date),fill=(0,0,0),font=font)
            draw.text(xy=(600,1570 ),text='{}'.format(to_date),fill=(0,0,0),font=font)
            draw.text(xy=(1350,1765 ),text='{}'.format(exm),fill=(0,0,0),font=font)
            draw.text(xy=(650,1825 ),text='{}'.format(subjects),fill=(0,0,0),font=font)
            draw.text(xy=(600,2025 ),text='{}'.format(attempt),fill=(0,0,0),font=font)
            draw.text(xy=(500,2890 ),text='{}'.format('Babarkot'),fill=(0,0,0),font=font)
            img.save(BASE_DIR/'Trial Certificate/{}.jpg'.format(detail.student_name))
            file_name = str(detail.student_name + '.jpg')
            path_to_file = os.path.join(BASE_DIR,'Trial Certificate',file_name)
            return FileResponse(open(path_to_file, 'rb'), as_attachment=True)
    return render(request,"gen_trial.html",{'detail':detail,'nav':'active'})

def bonafide(request):
    bonafide_student_list = General_Register.objects.filter(lang='en')
    return render(request,"bonafide.html",{'list':bonafide_student_list,'nav':'active'})

def gen_bonafide(request,id):
    if not General_Register.objects.filter(id=id).exists():
        return redirect('nota')
    else:
        detail = General_Register.objects.get(id=id)
        if request.method == "POST":
            std = request.POST.get('std')
            year = request.POST.get('year')
            date = str(todays_date.day)+'/'+str(todays_date.month)+'/'+str(todays_date.year)
            from PIL import Image, ImageDraw, ImageFont
            import pandas as pd
            font = ImageFont.truetype('arial.ttf',50)
            img = Image.open(os.path.join(BASE_DIR,"Bonafide Certificate",'main','bonafide-certi.jpg'))
            draw = ImageDraw.Draw(img)
            draw.text(xy=(700,1350 ),text='{}'.format(detail.student_name),fill=(0,0,0),font=font)
            draw.text(xy=(2000,1420 ),text='{}'.format(std),fill=(0,0,0),font=font)
            draw.text(xy=(770,1485 ),text='{}'.format(year),fill=(0,0,0),font=font)
            draw.text(xy=(470,2605 ),text='{}'.format('Babarkot'),fill=(0,0,0),font=font)
            draw.text(xy=(450,2670 ),text='{}'.format(date),fill=(0,0,0),font=font)
            img.save(BASE_DIR/'Bonafide Certificate/{}.jpg'.format(detail.student_name))
            file_name = str(detail.student_name + '.jpg')
            path_to_file = os.path.join(BASE_DIR,'Bonafide Certificate',file_name)
            return FileResponse(open(path_to_file, 'rb'), as_attachment=True)
    return render(request,"gen_bona.html",{'detail':detail,'nav':'active'})

def birth(request):
    birth_student_list = General_Register.objects.filter(lang='en')
    return render(request,"birth.html",{'list':birth_student_list,'nav':'active'})

def gen_birth(request,id):
    if not General_Register.objects.filter(id=id).exists():
        return redirect('nota')
    else:
        detail = General_Register.objects.get(id=id)
        if request.method == "POST":
            std = request.POST.get('std')
            year = request.POST.get('year')
            date = str(todays_date.day)+'/'+str(todays_date.month)+'/'+str(todays_date.year)
            from PIL import Image, ImageDraw, ImageFont
            import pandas as pd
            font = ImageFont.truetype('arial.ttf',50)
            img = Image.open(os.path.join(BASE_DIR,"Birth Certificate",'main','birth-cert.jpg'))
            draw = ImageDraw.Draw(img)
            draw.text(xy=(700,1410 ),text='{}'.format(detail.student_name),fill=(0,0,0),font=font)
            draw.text(xy=(1110,1485 ),text='{}'.format(std),fill=(0,0,0),font=font)
            draw.text(xy=(1850,1485 ),text='{}'.format(year),fill=(0,0,0),font=font)
            draw.text(xy=(1700,1680 ),text='{}'.format(detail.dob),fill=(0,0,0),font=font)
            draw.text(xy=(600,1740 ),text='{}'.format(detail.dob_in_words),fill=(0,0,0),font=font)
            draw.text(xy=(950,1810 ),text='{}'.format(detail.gr_number),fill=(0,0,0),font=font)
            draw.text(xy=(460,2735 ),text='{}'.format("Babarkot"),fill=(0,0,0),font=font)
            draw.text(xy=(450,2800 ),text='{}'.format(date),fill=(0,0,0),font=font)
            img.save(BASE_DIR/'Birth Certificate/{}.jpg'.format(detail.student_name))
            file_name = str(detail.student_name + '.jpg')
            path_to_file = os.path.join(BASE_DIR,'Birth Certificate',file_name)
            return FileResponse(open(path_to_file, 'rb'), as_attachment=True)
    return render(request,"gen_birth.html",{'detail':detail,'nav':'active'})

@login_required
def profile(request):
    user = request.user
    user_i = user.id
    profile = User.objects.get(username=str(user))
    profdet = User_details.objects.get(user=user) 
    return render(request,"profile.html",{'profile':profile,'profdet':profdet,'prol':'active'})

def grant_reg(request):
    grant = Grant_Register.objects.all()
    name = "Grant Register ("+str(todays_date.year)+").xlxs"
    if request.method == "POST":
        if 'add-grant' in request.POST:
            return redirect('add_grant')
        elif 'export' in request.POST:
            workbook = xlsxwriter.Workbook(BASE_DIR/'Grant Register'/name)
            worksheet = workbook.add_worksheet()
            worksheet.write(0, 0, "Entry No.")
            worksheet.write(0, 1, "Grant Details")
            worksheet.write(0, 2, "Amount")
            worksheet.write(0, 3, "Order No./Deposite No.")
            worksheet.write(0, 4, "Bank Deposite Date")
            worksheet.write(0, 5, "Remarks")  

            row = 1
            col = 0

            for record in grant:
                worksheet.write(row, col, record.entry_no)
                worksheet.write(row, col + 1, record.grant_details)
                worksheet.write(row, col + 2, record.amount)
                worksheet.write(row, col + 3, record.order_no)
                worksheet.write(row, col + 4, record.bank_deposite_date)
                worksheet.write(row, col + 5, record.remarks)
                row += 1
            workbook.close()
            path_to_file = os.path.join(BASE_DIR,'Grant Register',name)
            return FileResponse(open(path_to_file, 'rb'), as_attachment=True)
        elif 'edit' in request.POST:
            pass
        elif 'delete' in request.POST:
            del_id = request.POST.get('delete')
            delete_grant = Grant_Register.objects.filter(pk = del_id).delete()
    return render(request,"grant_reg.html",{'grant':grant})

def add_grant(request):
    if request.method == "POST":
        entry_no = request.POST.get('enno')
        grant_det = request.POST.get('grantdet')
        amount = request.POST.get('amount')
        order_no = request.POST.get('odno')
        deposite_date = request.POST.get('deposite_date')
        remarks = request.POST.get('remarks')
        grant_entry = Grant_Register.objects.create(entry_no=entry_no,grant_details=grant_det,amount=amount,order_no=order_no,bank_deposite_date=deposite_date,remarks=remarks)
        grant_entry.save()
        return redirect('grant')
    return render(request,"add_grant.html")

def account_list(request):
    users = User.objects.filter(is_superuser=0)
    if request.method == "POST":
        if 'del_user' in request.POST:
            ids = request.POST.get('del_user')
            delete_user = User.objects.filter(pk=ids).delete()
        if 'edit' in request.POST:
            teacher_id = request.POST.get('edit')
            return redirect('editprof',id=teacher_id)
    return render(request,"account_list.html",{'users':users,'nav':'active'})

def pagenotfound(request):
    return render(request,"404.html")
    
def general_ledger(request):
    gledger = General_Ledger.objects.all()
    name = "General-Ledger.xlxs"
    if request.method == "POST":
        if 'add-entry' in request.POST:
            return redirect('ledger_entry')
        elif 'export' in request.POST:
            workbook = xlsxwriter.Workbook(BASE_DIR/'General Ledger'/name)
            worksheet = workbook.add_worksheet()
            worksheet.write(0, 0, "એન્ટ્રી નં.")
            worksheet.write(0, 1, "તારીખ")
            worksheet.write(0, 2, "વિગત")
            worksheet.write(0, 3, "રોજમેળ સંદર્ભ")
            worksheet.write(0, 4, "જમા રુપિયા/પૈસા")
            worksheet.write(0, 5, "ઉધાર રુપિયા/પૈસા")  
            worksheet.write(0, 6, "જમા બાકી રુપિયા/પૈસા")  
            worksheet.write(0, 7, "ઉધાર બાકી રુપિયા/પૈસા")  
            worksheet.write(0, 8, "ખાતાનું નામ")              

            row = 1
            col = 0

            for record in gledger:
                worksheet.write(row, col, record.entry_no)
                worksheet.write(row, col + 1, record.date)
                worksheet.write(row, col + 2, record.particulars)
                worksheet.write(row, col + 3, record.c_b_r_no.entry_no)
                worksheet.write(row, col + 4, record.credit)
                worksheet.write(row, col + 5, record.debit)
                worksheet.write(row, col + 6, record.credit_bal)
                worksheet.write(row, col + 7, record.debit_bal)
                worksheet.write(row, col + 8, record.name_of_account)
                row += 1
            workbook.close()
            path_to_file = os.path.join(BASE_DIR,'General Ledger',name)
            return FileResponse(open(path_to_file, 'rb'), as_attachment=True)
    return render(request,"general_ledger.html",{'ledgerdet':gledger})

def ledger_entry(request):
    if request.method =="POST":
        ccentry = request.POST.get('ccentry')
        ccdate = request.POST.get('ccdate')
        ccnameandperticulars = request.POST.get('ccnameandperticulars')
        ccreciept = request.POST.get('ccreciept')
        cctotal = request.POST.get('cctotal')
        cc = "જમા"
        
        cdentry = request.POST.get('cdentry')
        cddate = request.POST.get('cddate')
        cdnameandperticulars = request.POST.get('cdnameandperticulars')
        cdvoucher = request.POST.get('cdvoucher')
        cdtotal = request.POST.get('cdtotal')
        cd = "ઉધાર"
        
        glentry = request.POST.get('glentry')
        gldate = request.POST.get('gldate')
        glperticular = request.POST.get('glperticulars')
        gldeposite = request.POST.get('gldeposite')
        glcredit = request.POST.get('glcredit')
        glleftdeposite = request.POST.get('glleftdeposite')
        glleftcredit = request.POST.get('glleftcredit')
        glaccount = request.POST.get('glaccount')
        
        cashc = Cash_Book.objects.create(entry_no=ccentry,date=ccdate,name_and_particulars=ccnameandperticulars,reciept=ccreciept,total_amount=cctotal,debit_or_credit=cc)
        cashc.save()
        cashd = Cash_Book.objects.create(entry_no=cdentry,date=cddate,name_and_particulars=cdnameandperticulars,voucher_no=cdvoucher,total_amount=cdtotal,debit_or_credit=cd)
        cashd.save()
        gledger = General_Ledger.objects.create(entry_no=glentry,date=gldate,particulars=glperticular,c_b_r_no=cashc,credit=glcredit,debit=gldeposite,credit_bal=glleftcredit,debit_bal=glleftdeposite,name_of_account=glaccount)
        gledger.save()
        
    return render(request,"ledger_cash_book_entry.html")

def cashbook(request):
    cashbook = Cash_Book.objects.all()
    name = "Cash-Book.xlxs"
    if request.method == "POST":
        if 'add-entry' in request.POST:
            return redirect('ledger_entry')
        if 'export' in request.POST:
            workbook = xlsxwriter.Workbook(BASE_DIR/'Cash Book'/name)
            worksheet = workbook.add_worksheet()
            worksheet.write(0, 0, "એન્ટ્રી નં.")
            worksheet.write(0, 1, "તારીખ")
            worksheet.write(0, 2, "ખાતાનું નામ અને વિગત")
            worksheet.write(0, 3, "રસીદ નંબર")
            worksheet.write(0, 4, "વાઉચર નંબર")
            worksheet.write(0, 5, "કુલ રકમ")
            worksheet.write(0, 6, "જમા/ઉધાર")     

            row = 1
            col = 0

            for record in cashbook:
                worksheet.write(row, col, record.entry_no)
                worksheet.write(row, col + 1, dateformat.format(record.date, formats.get_format('dd-mm-yyyy')))
                worksheet.write(row, col + 2, record.name_and_particulars)
                worksheet.write(row, col + 3, record.reciept)
                worksheet.write(row, col + 4, record.voucher_no)
                worksheet.write(row, col + 5, record.total_amount)
                worksheet.write(row, col + 6, record.debit_or_credit)
                row += 1
            workbook.close()
            path_to_file = os.path.join(BASE_DIR,'Cash Book',name)
            return FileResponse(open(path_to_file, 'rb'), as_attachment=True)
    return render(request,"cashbook.html",{'cashbook':cashbook})
    
def cashbook_filter(request,id):
    filtered = Cash_Book.objects.filter(entry_no=id)
    return render(request,"cashbook_filter.html",{'cashbook':filtered})

def cheque_register(request):
    details = Cheque_Register.objects.all()
    name = "Cheque-Register.xlxs"
    if request.method == "POST":
        if 'add-cheque' in request.POST:
            return redirect('cheque_reg_add')
        if 'export' in request.POST:
            workbook = xlsxwriter.Workbook(BASE_DIR/'Cheque Register'/name)
            worksheet = workbook.add_worksheet()
            worksheet.write(0, 0, "એન્ટ્રી નં.")
            worksheet.write(0, 1, "તારીખ")
            worksheet.write(0, 2, "ખર્ચ સદર એજન્સીનું નામ")
            worksheet.write(0, 3, "ખર્ચની વિગત")
            worksheet.write(0, 4, "બિલ નંબર")
            worksheet.write(0, 5, "ચેક નંબર")
            worksheet.write(0, 6, "ચેકની તારીખ") 
            worksheet.write(0, 7, "રકમ/રૂપિયા")     
            worksheet.write(0, 8, "ચુકવવાની ચોખ્ખી રકમ")     
            worksheet.write(0, 9, "આચાર્યની સહી")     
            worksheet.write(0, 9, "રિમાર્ક્સ")     

            row = 1
            col = 0

            for record in details:
                worksheet.write(row, col, record.entry_no)
                worksheet.write(row, col + 1, str(record.date.day)+'/'+str(record.date.month)+'/'+str(record.date.year))
                worksheet.write(row, col + 2, record.agency_name)
                worksheet.write(row, col + 3, record.purchase_detail)
                worksheet.write(row, col + 4, record.bill_no)
                worksheet.write(row, col + 5, record.cheque_no)
                worksheet.write(row, col + 6, record.cheque_date)
                worksheet.write(row, col + 7, record.amount)
                worksheet.write(row, col + 8, record.paying_amount)
                
                row += 1
            workbook.close()
            path_to_file = os.path.join(BASE_DIR,'Cheque Register',name)
            return FileResponse(open(path_to_file, 'rb'), as_attachment=True)
    return render(request,"cheque_reg.html",{'cheque_reg':details})
    
def cheque_register_add(request):
    if request.method == "POST":
        entryno = request.POST.get('enno')
        date = request.POST.get('date')
        agency_name = request.POST.get('agname')
        purchase_det = request.POST.get('purchase_detail')
        billno = request.POST.get('billno')
        chequeno = request.POST.get('chequeno')
        chequedate = request.POST.get('chequedate')
        amount = request.POST.get('amount')
        payableamount = request.POST.get('payableamount')
        newentry = Cheque_Register.objects.create(entry_no=entryno,date=date,agency_name=agency_name,purchase_detail=purchase_det,bill_no=billno,cheque_no=chequeno,cheque_date=chequedate,amount=amount,paying_amount=payableamount)
        newentry.save()
        return redirect('cheque_reg')
    return render(request,"cheque_reg_add.html")

def bill_book(request):
    bill_book = Bill_Book.objects.all()
    name = "Bill-Book.xlxs"
    if request.method == "POST":
        if 'add-bill' in request.POST:
            return redirect("billbookadd")
        if 'export' in request.POST:
            workbook = xlsxwriter.Workbook(BASE_DIR/'Bill Book'/name)
            worksheet = workbook.add_worksheet()
            worksheet.write(0, 0, "એન્ટ્રી નં.")
            worksheet.write(0, 1, "બિલ આપનારનું નામ")
            worksheet.write(0, 2, "તારીખ")
            worksheet.write(0, 3, "બિલ/વાઉચર નંબર")
            worksheet.write(0, 4, "બિલની રકમ રૂપિયામાં")
            worksheet.write(0, 5, "ચૂકવવાની ચોક્કસ રકમ")
            worksheet.write(0, 6, "મંજૂર કરનારની સહી") 
               

            row = 1
            col = 0

            for record in bill_book:
                worksheet.write(row, col, record.entry_no)
                worksheet.write(row, col + 1, record.bill_from)
                worksheet.write(row, col + 2, str(record.date.day)+'/'+str(record.date.month)+'/'+str(record.date.year))
                worksheet.write(row, col + 3, record.bill_voucher)
                worksheet.write(row, col + 4, record.bill_amount)
                worksheet.write(row, col + 5, record.payable_amount)
                
                row += 1
            workbook.close()
            path_to_file = os.path.join(BASE_DIR,'Bill Book',name)
            return FileResponse(open(path_to_file, 'rb'), as_attachment=True)
    return render(request,"bill_book.html",{'bill_book':bill_book})

def bill_book_add(request):
    if request.method == "POST":
        entryno = request.POST.get('enno')
        bill_from = request.POST.get('bill_from')
        date = request.POST.get('date')
        bill_voucher = request.POST.get('bill')
        amount = request.POST.get('amount')
        payable = request.POST.get('payable')
        bill_add = Bill_Book.objects.create(entry_no=entryno,bill_from=bill_from,date=date,bill_voucher=bill_voucher,bill_amount=amount,payable_amount=payable)
        bill_add.save()
        return redirect('billbook')
    return render(request,'bill_book_add.html')

def std_attence(request):
    return render(request,"std_attence.html",{'nav':'active','teach':'active'})

def add_remove_student(request):
    student_list = Student_Data.objects.all()
    if request.method == "POST":
        if 'addstud' in request.POST:
            name = request.POST.get('student_name')
            std = request.POST.get('std')
            gender = request.POST.get('gender')
            cast = request.POST.get('cast')
            division = request.POST.get('division')
            udise = request.POST.get('UDISE')
            student_data = Student_Data.objects.create(student_name=name,standard=std,gender=gender,cast=cast,division=division,udise=udise)
            student_data.save()
        elif 'delete' in request.POST:
            ids = request.POST.get('delete')
            delo = Student_Data.objects.filter(pk=ids).delete()
        elif 'udisebtn' in request.POST:
            udisefil = request.POST.get('udisefilter')
            student_list = Student_Data.objects.filter(udise=udisefil)
        elif 'namebtn' in request.POST:
            namefil = request.POST.get('namefilter')
            student_list = Student_Data.objects.filter(student_name__icontains=namefil)
        elif 'stdbtn' in request.POST:
            stdfil = request.POST.get('stdfilter')
            student_list = Student_Data.objects.filter(standard=stdfil)
        elif 'divbtn' in request.POST:
            divfil = request.POST.get('divfilter')
            student_list = Student_Data.objects.filter(division=divfil)
        elif 'castbtn' in request.POST:
            castfil = request.POST.get('castfilter')
            student_list = Student_Data.objects.filter(cast=castfil)
        elif 'genbtn' in request.POST:
            genfil = request.POST.get('genderfilter')
            student_list = Student_Data.objects.filter(gender=genfil)
        elif 'filter' in request.POST:
            genfil = request.POST.get('genderfilter')
            castfil = request.POST.get('castfilter')
            divfil = request.POST.get('divfilter')
            stdfil = request.POST.get('stdfilter')
            student_list = Student_Data.objects.filter(gender=genfil,cast=castfil,division=divfil,standard=stdfil)
            
    return render(request,"add_remove_student.html",{'nav':'active','studlist':student_list,'teach':'active'})

def edit_student(request,id):
    student = Student_Data.objects.get(pk=id)
    if request.method == "POST":
        name = request.POST.get('student_name')
        std = request.POST.get('std')
        gender = request.POST.get('gender')
        cast = request.POST.get('cast')
        division = request.POST.get('division')
        udise = request.POST.get('UDISE')
        savedata = Student_Data.objects.filter(pk=id).update(student_name=name,standard=std,gender=gender,cast=cast,division=division,udise=udise)
        return redirect('add_remove_st')
        
    return render(request,"edit_student_data.html",{'student' : student,'nav' : 'active'})

def tenth_attendance(request):
    div = "A"
    students = Student_Data.objects.filter(standard="STD 10",division=div)
    count = Attendance.objects.filter(date=todays_date,attendance='present',student__standard='STD 10',student__division=div)
    count = count.count()
    # count = students.count()
    # print(count)
    broken = ""
    today = str(todays_date.day)+"/"+str(todays_date.month)+"/"+str(todays_date.year)
    if request.method == "POST":
        if 'filter' in request.POST:
            div = request.POST.get('division')
            students = Student_Data.objects.filter(standard="STD 10",division=div)
            count = Attendance.objects.filter(date=todays_date,attendance='present',student__standard='STD 10',student__division=div)
            count = count.count()
        elif 'next' in request.POST:
            for x in students:
                attendance = request.POST.get(x.student_name)
                student = Student_Data.objects.get(pk=x.id)
                if Attendance.objects.filter(student=student,date=todays_date).exists():
                    broken = "True"
                    break
                elif attendance is None:
                    present_or_not = 'absent'
                    attend = Attendance.objects.create(student=student, attendance=present_or_not,date=todays_date)
                    attend.save()
                else:
                    present_or_not = 'present'
                    attend = Attendance.objects.create(student=student, attendance=present_or_not,date=todays_date)
                    attend.save()
    if broken == "True":
        messages.error(request, "Todays Attendence Already Taken!")
        
    return render(request,"tenth_attendance.html",{'student':students,'today':today,'count':count,'nav':'active'})
    
def nineth_attendance(request):
    students = Student_Data.objects.filter(standard="STD 9")
    # count = students.count()
    # print(count)
    broken = ""
    today = str(todays_date.day)+"/"+str(todays_date.month)+"/"+str(todays_date.year)
    if request.method == "POST":
        for x in students:
            attendance = request.POST.get(x.student_name)
            student = Student_Data.objects.get(pk=x.id)
            if Attendance.objects.filter(student=student,date=todays_date).exists():
                broken = "True"
                break
            elif attendance is None:
                present_or_not = 'absent'
                attend = Attendance.objects.create(student=student, attendance=present_or_not,date=todays_date)
                attend.save()
            else:
                present_or_not = 'present'
                attend = Attendance.objects.create(student=student, attendance=present_or_not,date=todays_date)
                attend.save()
    if broken == "True":
        messages.error(request, "Todays Attendence Already Taken!")
    count = Attendance.objects.filter(date=todays_date,attendance='present',student__standard='STD 9')
    count = count.count()
        
    return render(request,"ninethattendance.html",{'student':students,'today':today,'count':count,'nav':'active'})

def view_attendance(request):
    attendance = Attendance.objects.filter(date=todays_date)
    if request.method == "POST":
        if 'filter' in request.POST:
            std = request.POST.get('std')
            gender = request.POST.get('gender')
            cast = request.POST.get('cast')
            date = request.POST.get('date')
            if date == "":
                pass
            elif std or gender or cast == "All":
                pass
            print("Standard: "+std+" Gender: "+gender+" Cast: "+cast+" Date: "+date)
    return render(request,"view_attendance.html",{'attend':attendance,'nav':'active','teach':'active'})

def vision(request):
    return render(request,"vision.html",{'about':'active'})

def staff(request):
    teacher = User_details.objects.all()
    return render(request,"staff.html",{'teacher':teacher,'staff':'active'})

def admission(request):
    return render(request,"admission.html",{'stu':'active'})

def qoute(request):
    if request.method == "POST":
        term = request.POST.get('term')
        body = request.POST.get('body')
        quote = Quote.objects.filter(pk='1').update(term=term,qoute=body)
        messages.success(request,"Successfully Updated Today's Quote!")
    return render(request,"todays_qoute.html")

def useful_links_stud(request):
    link = Useful_Links.objects.filter(category='student')
    if request.method == "POST":
        fil = request.POST.get('filter')
        link = Useful_Links.objects.filter(term__icontains=fil)
    return render(request,"useful_links_stud.html",{'stu':'active','link':link})

def useful_links_teach(request):
    link = Useful_Links.objects.filter(category='teacher')
    if request.method == "POST":
        fil = request.POST.get('filter')
        link = Useful_Links.objects.filter(term__icontains=fil)
    return render(request,"useful_link_teach.html",{'link':link})


def addlink(request):
    if request.method == "POST":
        term = request.POST.get('term')
        link = request.POST.get('link')
        category = request.POST.get('category')
        try:
            addlink = Useful_Links.objects.create(term=term,link=link,category=category)
            addlink.save()
            messages.success(request,"Link Added Succefully!")
        except:
            messages.error(request,"Something Went Wrong!")
        
    return render(request,"add_links.html")

def noticeboard(request):
    text = Noticeboard.objects.all()
    return render(request,"noticeboard.html",{'stu':'active','text':text})

def add_notice(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        try:
            nat = Noticeboard.objects.create(title=title,body=body)
            messages.success(request,"Notice Added Successfully!")
        except:
            messages.error(request,"Something Went Wrong!")
    return render(request,"add_notice.html")

def gallery(request):
    category = Gal_Category.objects.all()
    gallery = Gallery.objects.all()
    return render(request,"gallery.html",{'gallery':'active','gallery':category,'image':gallery})

def view_gallery(request,id):
    images = Gallery.objects.filter(category__id=id)
    cat = Gal_Category.objects.get(pk=id)
    return render(request,"view_gallery.html",{'images':images,'category':cat})

def logout(request):
    auth.logout(request)
    return redirect('/')

# def student_signup(request):
#     role = "Student"
#     if request.method == "POST":
#         profile_picture = request.FILES['pp']
#         username = request.POST.get('uname')
#         first_name = request.POST.get('fname')
#         last_name = request.POST.get('lname')
#         father_name = request.POST.get('fthname')
#         contact = request.POST.get('contact')
#         password = request.POST.get('pass')
#         udise = request.POST.get('udise')
#         std = request.POST.get('std')
#         category = request.POST.get('category')
#         pline = request.POST.get('pline')
#         gender = request.POST.get('gender')
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username Already Used Try Different One!")
#         elif User_details.objects.filter(udise_code=udise).exists():
#             messages.error(request, "UDISE CODE Already Registered!")
#         else:
#             user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
#             contact_sv = User_details.objects.create(user=user,profile_picture=profile_picture,father_name=father_name,contact=contact,udise_code=udise,std=std,category=category,poority_line=pline,gender=gender,Role=role)
#             user.save()
#             contact_sv.save()
#     return render(request, "student_signup.html",{'reg':'active'})
