# Task 2.3
class ServiceRecord():
    def __init__(self,Sender,AccessDate,Status,AppType):
        self.Sender = Sender
        self.AccessDate = AccessDate
        self.Status = Status
        self.AppType = AppType

    def isSuccess(self):
        return self.Status == 200
    def getAppType(self):
        return self.AppType

class AppServiceRecord(ServiceRecord):
    def __init__(self,Sender,AccessDate,Status,AppType):
        super().__init__(Sender,AccessDate,Status,AppType)

    def getAppType(self):
        if self.AppType == 'WA':
            return 'WHATSAPP'
        elif self.AppType == 'FB':
            return 'FACEBOOK MESSENGER'
        else: # not possible
            return None # Null app type 
    def getSuccess(self):
        if self.isSuccess() == True:
            return 'SUCCESS'
        elif self.isSuccess() == False:
            return 'FAILED'
        else: # not possible
            return None

class SmsServiceRecord(ServiceRecord):
    def __init__(self,Sender,AccessDate,Status):
        super().__init__(Sender,AccessDate,Status, None)

    def getAppType(self):
        return 'SHORT MESSAGE SERVICE'
    def getSuccess(self):
        if self.isSuccess() == True:
            return 'SUCCESS'
        elif self.isSuccess() == False:
            return 'FAILED'
        else: # not possible
            return None
