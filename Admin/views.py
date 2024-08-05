from django.shortcuts import render,redirect
from DjangoPostgreSQL.settings import conn
# Create your views here.

cursor = conn.cursor()

def district(request):
    cursor.execute("select * from tbl_district")
    district = cursor.fetchall()
    # print(district)
    # for i in district:
    #     # print(type(i))
    #     print(i[1])
    if request.method == "POST":
        district = request.POST.get('txt_district')
        # print(request.POST.get('txt_district'))
        cursor.execute("insert into tbl_district(district_name) values('"+ district +"')")
        conn.commit()
        return redirect("Admin:district")
    else:
        return render(request, 'Admin/District.html',{"district": district})

def deletedistrict(request, id):
    cursor.execute("delete from tbl_district where district_id = '"+ str(id) +"'")
    conn.commit()
    return redirect("Admin:district")

def editdistrict(request, id):
    cursor.execute("select * from tbl_district where district_id = '"+ str(id) +"'")
    district = cursor.fetchone()
    if request.method == "POST":
        district = request.POST.get('txt_district')
        cursor.execute("update tbl_district set district_name = '"+ district +"' where district_id = '"+ str(id) +"'")
        conn.commit()
        return redirect("Admin:district")
    else:
        return render(request, 'Admin/District.html',{"districtdata": district})

def place(request):
    cursor.execute("select * from tbl_district")
    district = cursor.fetchall()
    cursor.execute("select * from tbl_place p inner join tbl_district d on p.district_id=d.district_id")
    place = cursor.fetchall()
    # print(place)
    if request.method == "POST":
        district = request.POST.get('sel_dis')
        place = request.POST.get('txt_place')
        cursor.execute("insert into tbl_place(place_name,district_id) values('"+ place +"','"+ district +"')")
        conn.commit()
        return redirect("Admin:place")
    else:
        return render(request, 'Admin/Place.html',{"district":district,"place":place})

def deleteplace(request, id):
    cursor.execute("delete from tbl_place where place_id = '"+ str(id) +"'")
    conn.commit()
    return redirect("Admin:place")

def editplace(request, id):
    cursor.execute("select * from tbl_place where place_id = '"+ str(id) +"'")
    place = cursor.fetchone()
    cursor.execute("select * from tbl_district")
    district = cursor.fetchall()
    if request.method == "POST":
        district = request.POST.get('sel_dis')
        place = request.POST.get('txt_place')
        cursor.execute("update tbl_place set place_name = '"+ place +"',district_id = '"+ district +"' where place_id = '"+ str(id) +"'")
        conn.commit()
        return redirect("Admin:place")
    else:
        return render(request, 'Admin/Place.html',{"district":district,"placedata":place})

def adminreg(request):
    if request.method == "POST":
        cursor.execute("insert into tbl_admin(admin_name,admin_email,admin_password) values('"+request.POST.get("txt_name")+"','"+request.POST.get("txt_email")+"','"+request.POST.get("txt_password")+"')")
        conn.commit()
        return redirect("Admin:adminreg")
    else:
        return render(request,"Admin/Admin_Reg.html")

def newshop(request):
    cursor.execute("select * from tbl_shop s inner join tbl_place p on s.place_id=p.place_id inner join tbl_district d on p.district_id=d.district_id where shop_status=0")
    shop = cursor.fetchall()
    return render(request,"Admin/NewShop.html",{"shop":shop})