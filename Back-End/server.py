from flask import *
from werkzeug.wrappers import response
from Model import model
from datetime import datetime
# pip install flask_cors
from flask_cors import CORS
from fileinput import filename
import os
from pathlib import Path
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from BusinessObjects import *

app = Flask(__name__)
CORS(app)
app.config.from_object("config")
app.secret_key = app.config["SECRET_KEY"]


@app.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body



@app.route('/UserSignup', methods=["POST"])
def UserSignup() :
	data=request.json

	usr_name = data['username']
	usr_email =data["email"]
	usr_password = data["password"]
	
	m = model()
	if (m.checkEmailExist(usr_email) == False) :
		user_id = m.InsertUser(usr_name,usr_email,usr_password)  		#insertion function return userid
		session["user_id"] = user_id
		session["user_email"] = usr_email
		session["user_name"] = usr_name	
		error = "Error " if user_id == 0 else ""
		returnObj={
			"error":error,
			"status":"success",
			"id":user_id
		}	
		return returnObj
	else :
		returnObj={
			"error":"Email already exist"
		}
		return returnObj
		

@app.route('/UserLogin', methods=["POST"])
def UserLogin() :
	data=request.json
	email = data["email"]
	password = data["password"]
	m = model()

	m.getUserID(email)
	#chk email exist
	if (m.checkEmailExist(email)) :
		user_id = m.ValidatePassword(email, password)
		if (user_id > 0) :									
			session["user_id"] = user_id
			error = "Error " if user_id == 0 else ""
			returnObj={
			"error":error,
			"status":"success",
			"id":user_id
		}	
			return returnObj
		else :
			returnObj={
			"error":" password is incorrect"
		}
			return returnObj
	else :
		returnObj={
			"error":"Email does not exist"
		}
		return returnObj
		

@app.route('/ExaminerSignup', methods=["POST", "GET"])
def SignUpExaminerInfo() :
	data=request.json

	usr_name = data['username']
	usr_email =data["email"]
	usr_password = data["password"]
	institution=data["institution"]
	availability = True
	ranking = 0
	acceptance_count = 0
	rejection_count = 0	
	
	m = model()
	if (m.checkEmailExist(usr_email,"examiners") == False) :
		user_id = m.InsertExaminer(usr_name,usr_email,usr_password,institution,availability,ranking,acceptance_count,rejection_count)  		#insertion function return userid
		session["examiner_id"] = user_id
		session["examiner_email"] = usr_email
		session["examiner_name"] = usr_name	
		error = "Error " if user_id == 0 else ""
		returnObj={
			"error":error,
			"status":"success",
			"id":user_id
		}	
		return returnObj
	else :
		returnObj={
			"error":"Email already exist"
		}
		return returnObj


@app.route('/ExaminerLogin', methods=["POST"])
def ExaminerLogin() :
	data=request.json
	email = data["email"]
	password = data["password"]
	m = model()

	m.getUserID(email,"examiners")
	#chk email exist
	if (m.checkEmailExist(email,"examiners")) :
		user_id = m.ValidatePassword(email, password,"examiners","examiners")
		if (user_id > 0) :									
			session["examiner_id"] = user_id
			error = "Error " if user_id == 0 else ""
			returnObj={
			"error":error,
			"status":"success",
			"id":user_id
		}	
			return returnObj
		else :
			returnObj={
			"error":" password is incorrect"
		}
			return returnObj
	else :
		returnObj={
			"error":"Email does not exist"
		}
		return returnObj



@app.route('/ExaminerQualification', methods=["POST", "GET"])
def ExaminerQualification() :
	degree_title = request.form["degree_title"]
	institution = request.form["institution"]
	starting_date = request.form["starting_date"]
	ending_date = request.form["ending_date"]
	transcript = request.form["transcript"]
	examiner_id = session.get("examiner_id")
	data = qualification(examiner_id, degree_title, transcript, institution, starting_date, ending_date)
	m = model()
	m.InsertExaminerQualification(data)
	print("Qualification inserted")
	return jsonify("Home") 

@app.route('/ExaminerExperience', methods=["POST", "GET"])
def ExaminerExperience() :
	job_title = request.form["job_title"]
	organization = request.form["organization"]
	reference_email = request.form["reference_email"]
	starting_date = request.form["starting_date"]
	ending_date = request.form["ending_date"]
	ExperianceLetter = request.form["ExperianceLetter"]
	examiner_id = session.get("examiner_id")
	data = experience(examiner_id, job_title, ExperianceLetter, organization, reference_email, starting_date, ending_date)
	m = model()
	m.InsertExaminerExperience(data)
	print("Experience inserted")
	name = session.get("usr_name")
	# Email = session.get("usr_email")
	Email = "bitf19a008@pucit.edu.pk"
	text = '''\
                <html>
                <body>
                    <p>Hi <b>{name}</b>,<br><br>
                    Welcome to Affliated college management system...!!<br>
                    Hope you have a great experience :)
                    </p>
                </body>
                </html>
                '''
	text = MIMEText(text.format(name = name),"html")
	mail(Email,text)
	print("succeed")
	return jsonify("home") #ya abhi nae ata

# @app.route('/ExaminerLogin', methods=["POST", "GET"])
# def ExaminerLogin() :
# 	email = request.form["email"]
# 	password = request.form["password"]
# 	m = model()
# 	m.getUserID(email)
# 	#chk email exist
# 	if (m.checkEmailExist(email)) :
# 		examiner_id = m.ValidatePassword(email, password)
# 		if (examiner_id > 0) :									
# 			session["examiner_id"] = examiner_id
# 			print("logged in")
# 			return jsonify("dashboard")
# 		else :
# 			return jsonify("Invalid Password")
# 	else :
# 		return jsonify("Email does not exist")

@app.route('/userdata', methods=['GET'])
def userdata():
    userdata = {
        'name': 'John',
        'age': '43',
        'status': 'Active',
        'password': 'ABC123',
        'email': 'john@example.com'
    }
    return jsonify(userdata)

def mail(email,text):
        senderMail = "ayeshasiddique1306@gmail.com"
        message = MIMEMultipart("alternative")
        message.attach(text)
        message = message.as_string()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(senderMail, "Ayesha@1284356", True)
            server.sendmail(
                senderMail, email, message
            )

# Running app
if __name__ == '__main__':
	app.run(debug=True)