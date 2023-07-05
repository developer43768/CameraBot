import firebase_admin
from firebase_admin import db,credentials
#import pyrebase as pb


config = {
  "apiKey" : "AIzaSyBiWHjBEtoxFvdNWJJcBFEqLO76xa0zeeg",
  "authDomain" : "camerabot-c643f.firebaseapp.com",
  "databaseURL" : "https://camerabot-c643f-default-rtdb.firebaseio.com",
  "projectId" : "camerabot-c643f",
  "storageBucket" : "camerabot-c643f.appspot.com",
  "messagingSenderId" : "990465513611",
  "appId" : "1:990465513611:web:153f462b40869b47ab5c8e",
  "measurementId" : "G-V162KYWDMW"
}


class Database:
    def __init__(self):
        self.cred = credentials.Certificate('camerabotDatabase.json')
        firebase_admin.initialize_app(self.cred, {'databaseURL' : "https://camerabot-c643f-default-rtdb.firebaseio.com/"})
        self.ref = db.reference()
        #-----------------------
        """
        self.firebase = pb.initialize_app(config)
        self.storage = self.firebase.storage()
        self.database = self.firebase.database()
        """
        #Database datas
        self.connectButton = 0
        self.robotOnline = 0
        self.robotMode = 0

    def GetDatabase(self):
        data = self.ref.get()
        #data = self.database.get()
        print(data)
        self.connectButton = data['connectButton']
        self.robotOnline = data['robotConnected']
        self.robotMode = data['robotMode']


    def SetData(self,id,data):
        
        self.ref.update({
            id:data
        })
        """
        self.database.update({
            id:data
        })
        """
    def ConnectionControl(self):
        if(self.connectButton == "1"):
            self.robotOnline = 1
            self.SetData('robotConnected',1)
        else:
            self.robotOnline = 0
            self.SetData('robotConnected',0)


