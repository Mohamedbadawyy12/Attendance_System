import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    "databaseURL": "https://faceattendancerealtimetantauni-default-rtdb.firebaseio.com"
})


ref = db.reference('Students')

data = {"203027":
        {
            "name": "Mahmoud Mohamed",
            "major": "Mechatronics",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "B",
            "year": 5,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    

    "213285":
        {
            "name": "Mahmoud Salah",
            "major": "Mechatronics",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "B",
            "year": 5,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    
    
    
    
    "213403":
        {
            "name": "Samir Mahmoud",
            "major": "Mechatronics",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "B",
            "year": 5,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    
    
    "193253":
        {
            "name": "Mohamed El-Borhamy",
            "major": "Mechatronics",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "B",
            "year": 5,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "203219":
        {
            "name": "Mohamed Badawy",
            "major": "Mechatronics",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "213603":
        {
            "name": "Ezzat Ibrahim",
            "major": "Mechatronics",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "B",
            "year": 5,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "203025":
        {
            "name": "Mohamed Elsaka",
            "major": "Mechatronics",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "B",
            "year": 5,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
        "203024":
        {
            "name": "Mohamed Tarek",
            "major": "Mechatronics",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "B",
            "year": 5,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)