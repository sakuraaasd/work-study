#继承
class Phone:
    IMEI = None
    producer = 'HM'

    def call_by_4g(self):
        print("4g")

class Phone2022(Phone):
    face_id = '10001'

    def call_by_5g(self):
        print('2022 new ,5g')

phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

#多继承
#class 类名（父1，父2，父3...）：
class Nfc_reader:
    nfc_type = '5 dai'
    producer = 'HM'

    def read_card(self):
        print('NFC reade')
    
    def write_card(self):
        print('NFC write')

class RemoteControl:
    rc_type = '红外'

    def control(self):
        print('open 红外')

class My_phone(Phone,Nfc_reader,RemoteControl):
    pass

phone = My_phone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

#多继承，同名成员属性，成员方法，顺序从左到右
