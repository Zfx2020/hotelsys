from apps import create_app
from database import userinfo_db,hotelinfo_db
from flask import request, jsonify
from utils import psw_processor

app = create_app()

@app.route('/')
def index():
    return jsonify(userinfo_db.get_user_byid(1))

@app.route('/adminLogin')
def adminLogin():
    username = request.args.get('username')

    psw = request.args.get('password')
    print(username,psw)
    return userinfo_db.admin_login(username,psw)

@app.route('/getJson',methods=['GET','POST'])
def getJson():
    json = request.get_json()
    id = int(json.get('id'))
    name = json.get('name')
    address = json.get('address')
    instruction = json.get('instruction')
    phone = int(json.get('phone'))
    star = int(json.get('star'))
    print(id,name,address,instruction,phone,star)
    result = hotelinfo_db.update_by_id(id,name,address,instruction,phone,star)

    return jsonify(hotelinfo_db.get_hotel_byid(id),result)

@app.route('/newHotel',methods=['GET','POST'])
def new_hotel():
    json = request.get_json()
    name = json.get('name')
    address = json.get('address')
    instruction = json.get('instruction')
    phone = int(json.get('phone'))
    star = int(json.get('star'))
    id,result = hotelinfo_db.new_hotel(name,address,instruction,phone,star)
    return jsonify(hotelinfo_db.get_hotel_byid(id),result)

@app.route('/newHotelAdmin',methods=['GET','POST'])
def new_hotel_admin():
    json = request.get_json()
    name = json.get('name')
    password = json.get('password')
    password = psw_processor.to_md5(password)
    phone = int(json.get('phone'))
    id,result = userinfo_db.new_hotel_admin(password,name,phone)
    return jsonify(userinfo_db.get_user_byid(id),result)

if __name__ ==  '__main__':

    app.run(port=8500,debug=True)