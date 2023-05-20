import firebase_admin
from firebase_admin import db,credentials


class Database:
    def __init__(self):
        self.cred = credentials.Certificate('camerabotDatabase.json')
        firebase_admin.initialize_app(self.cred, {'databaseURL' : "https://camerabot-c643f-default-rtdb.firebaseio.com/"})
        self.ref = db.reference()
        #Database datas
        self.connectButton = 0
        self.robotOnline = 0
        self.robotMode = 0

    def GetDatabase(self):
        data = self.ref.get()
        self.connectButton = data['connectButton']
        self.robotOnline = data['robotConnected']
        self.robotMode = data['robotMode']


    def SetData(self,id,data):
        self.ref.update({
            id:data
        })

    def ConnectionControl(self):
        if(self.connectButton == "1"):
            self.robotOnline = 1
            self.SetData('robotConnected',1)
        else:
            self.robotOnline = 0
            self.SetData('robotConnected',0)


