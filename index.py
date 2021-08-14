from flask_cors import cross_origin

from apps import create_app
from database import userinfo_db,hotelinfo_db,roominfo_db
from flask import request, jsonify
from utils import psw_processor

app = create_app()

@app.route('/')
def index():
    return jsonify(userinfo_db.get_user_byid(1))

@app.route('/login')
def adminLogin():
    username = request.args.get('username')

    psw = request.args.get('password')
    print(username,psw)
    return userinfo_db.admin_login(username,psw)

@app.route('/getHotelById')
def getHotelById():
    hotelid = request.args.get('hotelid')

    return jsonify(hotelinfo_db.get_hotel_byid(hotelid))

@app.route('/getRoomById')
def getRoomById():
    roomid = request.args.get('roomid')

    return jsonify(roominfo_db.get_room_byid(roomid))

@app.route('/getHotel')
def getHotel():
    hotels = hotelinfo_db.get_all_hotel()
    result = {}
    result.update({'hotels':hotels})
    return jsonify(result)

@app.route('/getRoom')
def getRoom():
    rooms = roominfo_db.get_all_room()
    result = {}
    result.update({'rooms':rooms})
    return jsonify(result)

@app.route('/updateHotelInfo',methods=['GET','POST'])
def getJson():
    result = {}
    result.update({'status': 404, 'desc': '本版本没有此功能'})
    return jsonify(result)

@app.route('/updateRoomInfo',methods=['GET','POST'])
def updateRoomInfo():
    json = request.get_json()
    print(json)
    id = int(json.get('id'))
    name = json.get('name')
    square = int(json.get('square'))
    price = int(json.get('price'))
    num = int(json.get('num'))
    print(id,name)
    result = roominfo_db.update_by_id(id,name,square,price,num)

    return jsonify(roominfo_db.get_room_byid(id),result)

@app.route('/newHotel',methods=['GET','POST'])
def new_hotel():
    result = {}
    result.update({'status': 404, 'desc': '本版本没有此功能'})
    return jsonify(result)

@app.route('/newHotelAdmin',methods=['GET','POST'])
def new_hotel_admin():
    json = request.get_json()
    name = json.get('username')
    password = json.get('password')
    password = psw_processor.to_md5(password)
    phone = int(json.get('phone'))
    id,result = userinfo_db.new_hotel_admin(password,name,phone)
    return jsonify(userinfo_db.get_user_byid(id),result)

if __name__ ==  '__main__':

    app.run(port=8500,debug=True)