from BusinessObjects import *
import psycopg2  #pip install psycopg2

class model:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                database="exam_system",            #write your Dbname
                host="localhost",
                user="asad",
                password="123",      #write your dbPassword
                # port="5432"
                )
            
        except Exception as e:
            print(str(e))
    
    def __del__(self):
        if self.connection != None:
            self.connection.close()


   
    def userSignup(self, name,email,password):
        isEmailExist=self.checkEmailExist(email)
        if isEmailExist:
            abc={
                "error":"Already Exist",
            }
            return abc
        else:
            cursor = None       #not taking profile pic in input
            try:
                if self.connection != None:
                    cursor = self.connection.cursor()
                    query = f'''insert into users(name,email,password) 
                                values ('{name}', '{email}', '{password}');
                                '''
                    cursor.execute(query)
                    self.connection.commit()
                    id = model.getUserID(self ,email)
                    abc={
                        "error":"",
                        "id":id,
                        "status":"success"
                    }
                    return abc
                else:
                    return 0
            except Exception as e:
                print("Exception in insertUser", str(e))
                return False
            finally:
                if cursor != None:
                    cursor.close()
   
    def InsertUser(self, name,email,password):
        cursor = None       #not taking profile pic in input
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = f'''insert into users(name,email,password) 
	                        values ('{name}', '{email}', '{password}');
                            '''
                cursor.execute(query)
                self.connection.commit()
                id = model.getUserID(self ,email) 
                return id
            else:
                return 0
        except Exception as e:
            print("Exception in insertUser", str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()

    # def InsertExaminer(self, name,email,password):
    #     cursor = None       #not taking profile pic in input
    #     try:
    #         if self.connection != None:
    #             cursor = self.connection.cursor()
    #             query = f'''insert into examiners(name,email,password) 
	#                         values ('{name}', '{email}', '{password}');
    #                         '''
    #             cursor.execute(query)
    #             self.connection.commit()
    #             id = model.getUserID(self ,email,"examiners") 
    #             return id
    #         else:
    #             return 0
    #     except Exception as e:
    #         print("Exception in insertUser", str(e))
    #         return False
    #     finally:
    #         if cursor != None:
    #             cursor.close()

    def getUserID(self, email,tableNme="users"): 
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute(f'''select id from {tableNme} where email = '{email}';''')
                id = cursor.fetchone();
                return id[0]
            else:
                return 0
        except Exception as e:
            print("Exception in getUserID", str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()

    def getExaminerID(self, userid): 
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute(f'''select examiner_id from public.examiner where "user_id " = {userid};''')
                id = cursor.fetchone()
                return id[0]
            else:
                return 0
        except Exception as e:
            print("Exception in getExaminerID", str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()

    def InsertExaminer(self, usr_name,usr_email,usr_password,institution,availability,ranking,acceptance_count,rejection_count):  # return examinerID
        cursor = None
        try:
            if self.connection != None:         #there should be a email check weather the user exists or not
                cursor = self.connection.cursor()
                query = f'''insert into examiners("name","email","password","institution","availability","ranking","acceptance_count","rejection_count") 
                            values('{usr_name}', '{usr_email}', '{usr_password}', '{institution}', '{availability}','{ranking}', '{acceptance_count}', '{rejection_count}');
                            '''
                cursor.execute(query)
                self.connection.commit()
                id = model.getUserID(self, usr_email,"examiners")  
                return id
            else:
                print("already exist")
                return 0
        except Exception as e:
            print("Exception in insertExaminer", str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()

    def checkEmailExist(self , usr_email,tableName="users"):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute(f"select email from {tableName};")
                emailList = cursor.fetchall()
               
                for e in emailList:
                    if usr_email == e[0]: 
                        return True
                return False
            else:
                return False
        except Exception as e:
            print("Exception in checkEmailExist", str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()

    def ValidatePassword(self,email, password,tableName="users",userIdTable="users"): #return examiner id
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute(f'''select password from {tableName} where "email" = '{email}';''')
                pwd = cursor.fetchone()
                if(pwd[0].strip() == password.strip()):  
                    uID = model.getUserID(self, email,userIdTable)
                    return uID
                return 0
            else:
                return 0
        except Exception as e:
            print("Exception in ValidatePassword", str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()

        return True

    def InsertExaminerQualification(self,qualification):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = f'''insert into public.qualification("examiner_id", "degree_title", "institution", "starting_date", "ending_date") 
                values('{qualification.examiner_id}', '{qualification.degree_title}', '{qualification.institution}', '{qualification.starting_date}', '{qualification.ending_date}');
                '''
                cursor.execute(query)
                self.connection.commit()
        except Exception as e:
            print("Exception in insertExaminerQualification", str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()

    def InsertExaminerExperience(self, experience): 
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = f'''insert into public.experience("examiner_id", "job_title", "organization", "reference_email", "starting_date", "ending_date") 
                        values('{experience.examiner_id}', '{experience.job_title}', '{experience.organization}','{experience.reference_email}' ,'{experience.starting_date}', '{experience.ending_date}');
                        '''
                cursor.execute(query)
                self.connection.commit()
        except Exception as e:
            print("Exception in insertExaminerExperience", str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()

    def getData(self, tableName):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = f'''select * from public.{tableName};'''
                cursor.execute(query)
                data = cursor.fetchall()
                return data
        except Exception as e:
            print("Exception in getData", str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()

    def deleteAllQuaAndExp(self, tableName, exaimerID):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = f'''delete from {tableName} where examiner_id = {exaimerID};'''   
                cursor.execute(query)
                self.connection.commit() 
                return True
            else:
                return False
        except Exception as e:
            print("Exception in deleteUser", str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()

    def deleteExaminer(self,email):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                userID = model.getUserID(email)
                ExmnrID = model.getExaminerID(userID)
                
                #all qualification and experience are deleted before deleting the examiner...
                model.deleteAllQuaAndExp("public.qualification",ExmnrID)
                model.deleteAllQuaAndExp("public.experience",ExmnrID)

                query = f'''delete from examiner where "user_id " = {userID};'''
                # on  which basis examiner is deleted...  userid????
                # should we delete user as well... if examiner is deleted...???
                cursor.execute(query)
                self.connection.commit()
                return True
            else:
                return False
        except Exception as e:
            print("Exception in deleteExaminer", str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()
                  
    def deleteUser(self, email):
        cursor = None
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                # problem:  examiner not automatically deleted if user deleted...
                # So deleting examiner first...
                model.deleteExaminer(email)
                query = f'''delete from public.user where usr_email = {email};'''   
                cursor.execute(query)
                self.connection.commit() 
                return True
            else:
                return False
        except Exception as e:
            print("Exception in deleteUser", str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()

