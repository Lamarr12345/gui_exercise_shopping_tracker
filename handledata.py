import json

class HandleData():
    def __init__(self,mainwindow,filepath="userbase.json"):

        self.main_window = mainwindow

        self.file_path = filepath

        self.__loadDataFromFile() #self.user_base gets initialized
        self.current_user_data = None
        self.current_user_data_logged_in = None
        self.current_user_purchase_history = None

    #--------------------------------------------------------------------------------

    #Public methods

    def addUserToDataBaseUserBase(self,username,password,phone_number):

        self.user_base.append(
                {
                "username" : username,
                "loggedIn" : False,
                "user_data" :{
                    "password":self.__encryptPassword(password),
                    "phone_number": phone_number,
                    "purchase_history" : []
                }
            }
        )

        self.__writeDataToFile()
    

            


    def checkIfUsernameTaken(self,username):
        if not self.user_base:
            return False
        else:
            return len([x for x in self.user_base if x["username"] == username]) != 0


    def getCurrentUserData(self):
        pass

    def setCurrentUserData(self):
        pass


    def getCurrentUserLoggedIn(self):
        pass
    
    def setCurrentUserLoggedIn(self):
        pass


    def getCurrentUserPurchaseHistory(self):
        pass

    def addItemToCurrentUserPurchaseHistory(self):
        pass

    #----------------------------------------------------------------------------------------------

    # Private methods 

    def __loadDataFromFile(self):
        try: 
            with open(self.file_path,"r") as openfile:
                self.user_base = list(json.load(openfile))

        except ValueError as e:
            print("There is a value error with the JSON file. See if it has the correct format ({} if empty):",e)
            self.main_window.quitApp()

        except Exception as e:
            print("Something went wrong with loading JSON file:",e)
            self.main_window.quitApp()



    def __writeDataToFile(self):
        try: 
            with open(self.file_path,"w") as openfile:
                json.dump(self.user_base, openfile)

        except ValueError as e:
            print("There is a value error with the JSON file. See if it has the correct format ({} if empty):",e)
            self.main_window.quitApp()

        except Exception as e:
            print("Something went wrong with loading JSON file:",e)
            self.main_window.quitApp()



    def __encryptPassword(self,password:str):
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"

        alpha_count = len([x for x in password if x.isalpha()])
        num_count = len([x for x in password if x.isnumeric()])

        rev_pw = password[::-1]
        enc_pw = ""

        for char in rev_pw:
            if char.isalpha():
                enc_pw = enc_pw + alphabet[(alphabet.index(char)+num_count)%52]
            elif char.isnumeric():
                enc_pw = enc_pw + numbers[(numbers.index(char)+(10-alpha_count))%10]
            else:
                enc_pw = enc_pw + char
        
        return enc_pw