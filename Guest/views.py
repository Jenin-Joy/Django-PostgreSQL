from django.shortcuts import render,redirect
from DjangoPostgreSQL.settings import conn
from DjangoPostgreSQL import settings
import os
# Create your views here.

cursor = conn.cursor()

def login(request):
    return

def user(request):
    cursor.execute("select * from tbl_district")
    district = cursor.fetchall()
    if request.method == "POST":
        image =  request.FILES.get("txt_photo")
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'User', image.name)
        # print(upload_dir)

        with open(upload_dir, 'wb+') as destination:
            for chunk in image.chunks():
                # print(chunk)
                destination.write(chunk)
        name = request.POST.get("txt_name")
        contact = request.POST.get("txt_contact")
        email = request.POST.get("txt_email")
        address = request.POST.get("txt_address")
        photo = request.FILES.get("txt_photo")
        password = request.POST.get("txt_password")
        place = request.POST.get("sel_place")
        cursor.execute("insert into tbl_user(user_name,user_contact,user_email,user_address,user_photo,user_password,place_id) values('"+ name +"','"+ contact +"','"+ email +"','"+ address +"','"+ photo.name +"','"+ password +"','"+ place +"')")
        conn.commit()
        # print(request.FILES.get("txt_photo"))
                
        return render(request,"Guest/User.html",{"msg":"Registred sucessfully...."})
    else:
        return render(request,"Guest/User.html",{'district':district})

def shop(request):
    cursor.execute("select * from tbl_district")
    district = cursor.fetchall()
    if request.method == "POST":
        image = request.FILES.get("txt_photo")
        proof = request.FILES.get("txt_proof")
        imagedir = os.path.join(settings.MEDIA_ROOT, 'Shop', image.name)
        proofdir = os.path.join(settings.MEDIA_ROOT, 'Shop', proof.name)
        # print(upload_dir)

        with open(imagedir, 'wb+') as imagedestination:
            for chunk in image.chunks():
                # print(chunk)
                imagedestination.write(chunk)

        with open(proofdir, 'wb+') as proofdestination:
            for chunk in proof.chunks():
                # print(chunk)
                proofdestination.write(chunk)

        name = request.POST.get("txt_name")
        contact = request.POST.get("txt_contact")
        email = request.POST.get("txt_email")
        address = request.POST.get("txt_address")
        password = request.POST.get("txt_password")
        place = request.POST.get("sel_place")

        cursor.execute("insert into tbl_shop(shop_name,shop_contact,shop_email,shop_address,shop_photo,shop_proof,shop_password,place_id) values('"+ name +"','"+ contact +"','"+ email +"','"+ address +"','"+ image.name +"','"+ proof.name +"','"+ password +"','"+ place +"')")
        conn.commit()
        # print(request.FILES.get("txt_photo"))
                
        return render(request,"Guest/Shop.html",{"msg":"Registred sucessfully...."})
    else:
        return render(request,"Guest/Shop.html",{'district':district})

def ajaxplace(request):
    cursor.execute("select * from tbl_place where district_id ='"+ request.GET.get("did") +"'")
    place = cursor.fetchall()
    # print(place)
    return render(request,"Guest/AjaxPlace.html",{'place':place})