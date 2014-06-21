import requests

LOGINURL = "https://www.onecall.no/minesider/login.php"
SMSURL = "https://www.onecall.no/minesider/sendsmsnow.php"

class OneCallInstance:
    
    def __init__(self, phoneNumber, password):
        self.phoneNumber = phoneNumber
        self.password = password
        self.session = requests.session()

    def login(self):
        loginData = {
            'username': self.phoneNumber,
            'password': self.password,
            'Logg_Inn': "Logg Inn"
        }
        r = self.session.post(LOGINURL, data=loginData) 
        if r.status_code == 200:
            return True
        else:
            return False


class SMS:
    """
    Class for creating a SMS message that can be sent with OneCalls Not-so-official-API.
    """
    
    def __init__(self, toNumber, message, oneCallUser):
        self.toNumber = toNumber
        self.message = message
        self.oneCallUser = oneCallUser

    def isValidMessage(self):
        if len(self.message) > 480:
            return False
        return True

    def isValidNumber(self):
        if len(self.toNumber) > 8:
            return False
        elif not self.toNumber.isdigit():
            return False
        return True

    def prepare_sms_data(self):
        sms = {
            'avsender': self.oneCallUser.phoneNumber,
            'tonumber': 'Nummer',
            # Actual to number
            'nummer': self.toNumber,
            'smsmsg': self.message,
            'cntLen2': len(self.message),
            'numsms': '1',
            'remlen2': 480 - len(self.message)
        }
        return sms

    def send(self):
        if self.isValidNumber():
            pass
        if self.isValidMessage():
            pass
        sms = self.prepare_sms_data()
        session = self.oneCallUser.session
        r = session.post(SMSURL, data=sms)
        print(r.text)


        

