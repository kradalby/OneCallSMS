import requests

LOGINURL = "https://www.onecall.no/minesider/login.php"
SMSURL = "https://www.onecall.no/minesider/sendsmsnow.php"

class MessageException(Exception):
    pass

class PhoneNumberException(Exception):
    pass

class OneCallSession:
    """
    Class for creating a OneCall session, basicly logging in to OneCalls website.
    """
    
    def __init__(self, phoneNumber, password):
        self.phoneNumber = phoneNumber
        self.password = password
        self.session = requests.session()
    
    def isValidNumber(self):
        if len(self.phoneNumber) > 8:
            raise PhoneNumberException("The phone number has wrong length. Correct is 8")
        elif not self.phoneNumber.isdigit():
            raise PhoneNumberException("The phone number has more than digits")
        return True


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
    Class for creating and sending a SMS message through OneCalls website.
    """
    
    def __init__(self, toNumbers, message, oneCallUser):
        self.toNumbers = toNumbers
        self.message = message
        self.oneCallUser = oneCallUser

    def isValidMessage(self):
        if len(self.message) > 480:
            raise MessageException("Message is to long, Max 480 Chars")
        return True

    def isValidNumber(self):
        for number in self.toNumbers:
            if len(number) > 8:
                raise PhoneNumberException("The phone number has wrong length. Correct is 8")
            elif not number.isdigit():
                raise PhoneNumberException("The phone number has more than digits")
        return True

    def prepare_sms_data(self):
        sms = {
            'avsender': self.oneCallUser.phoneNumber,
            'tonumber': 'Nummer',
            # Actual to number
            'nummer': ";".join(self.toNumbers),
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
        if "Melding er sendt" in r.text:
            print("Sent successfully")
        else:
            print("Message failed")


        

