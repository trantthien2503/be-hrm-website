from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
class Staffinfo:
    id = Column(String(50), primary_key=True)
    counter = Column(Integer)
    countersalary = Column(Integer)
    usercode = Column(String(20), nullable=False)
    hocode = Column(String(20))
    cardnumber = Column(String(20))
    firstname = Column(String(200))
    lastname = Column(String(50))
    name2 = Column(String(100)) 
    female = Column(Integer)
    imagedata = Column(String(5000))
    thumb = Column(String(5000))
    datebirth = Column(DateTime)
    placeborn = Column(String(200))
    domicile = Column(String(200))
    dateapply = Column(DateTime)
    trydate = Column(DateTime)
    departmentsys = Column(String(20))
    department1 = Column(String(20))
    department2 = Column(String(20))
    department3 = Column(String(20))
    department4 = Column(String(20))
    department5 = Column(String(20))
    department6 = Column(String(20))
    department7 = Column(String(20))
    department8 = Column(String(20))
    department9 = Column(String(20))
    department10 = Column(String(20))
    regencycode = Column(String(20))
    jobtitlecode = Column(String(20))
    email = Column(String(200))
    stafftype = Column(String(20))
    skillwork = Column(String(150))
    veterans = Column(String(20))
    numberinsurance = Column(String(20))
    dateregisterinsurance = Column(DateTime)
    address = Column(String(500))
    provincecode = Column(String(20))
    viillage = Column(String(20))
    wards = Column(String(20))
    address2 = Column(String(500))
    provincecode2 = Column(String(20))
    viillage2 = Column(String(50))
    wards2 = Column(String(50))
    citizenshipcode = Column(String(20))
    ethniccode = Column(String(50))
    religioncode = Column(String(50))
    nationalcode = Column(String(20))
    numberbank = Column(String(30))
    bankname = Column(String(250))
    taxcode = Column(String(20))
    isdoctor = Column(Boolean)
    educationallevel = Column(String(20))
    healthcode = Column(String(20))
    height = Column(Float(precision=3))
    weight = Column(Float(precision=3))
    bloodtype = Column(String(10))
    phonenumber = Column(String(20))
    cellphone = Column(String(20))
    idcode = Column(String(20))
    daterange = Column(DateTime)
    placeidcode = Column(String(20))
    registerhospital = Column(String(20))
    numbermedical = Column(String(80))
    placemedical = Column(String(20))
    datemedical = Column(DateTime)
    isforeigner = Column(Boolean)
    istablets = Column(Boolean)
    isunionists = Column(Boolean)
    isfederation = Column(Boolean)
    isleaders = Column(Boolean)
    isparttime = Column(Boolean)
    isado = Column(Boolean)
    iscoo = Column(Boolean)
    iscfo = Column(Boolean)
    urlsignature = Column(String(5000))

    def __init__(self, staff_info = None):
        if staff_info:
            for attr, value in staff_info.items():
                setattr(self, attr, value)
        else: 
            pass

    # Getter setter for id
    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value


    # Getter setter for counter
    def get_counter(self):
        return self.counter

    def set_counter(self, value):  
        self.counter = value


    # Getter setter for countersalary
    def get_countersalary(self):
        return self.countersalary

    def set_countersalary(self, value):
        self.countersalary = value

    
    # Getter setter for usercode  
    def get_usercode(self):
        return self.usercode

    def set_usercode(self, value):
        self.usercode = value


    # Getter setter for hocode
    def get_hocode(self):
        return self.hocode 

    def set_hocode(self, value):
        self.hocode = value

    # Getter setter for cardnumber
    def get_cardnumber(self):
        return self.cardnumber

    def set_cardnumber(self, value):
        self.cardnumber = value


    # Getter setter for firstname  
    def get_firstname(self):
        return self.firstname

    def set_firstname(self, value):
        self.firstname = value


    # Getter setter for lastname
    def get_lastname(self):
        return self.lastname 

    def set_lastname(self, value):
        self.lastname = value


    # Getter setter for name2
    def get_name2(self):
        return self.name2

    def set_name2(self, value):
        self.name2 = value


    # Getter setter for female
    def get_female(self):
        return self.female

    def set_female(self, value):
        self.female = value

    #Getter setter for imagedata
    def get_imagedata(self):
        return self.imagedata

    def set_imagedata(self, value):
        self.imagedata = value


    # Getter setter for thumb
    def get_thumb(self):
        return self.thumb

    def set_thumb(self, value):
        self.thumb = value


    # Getter setter for datebirth  
    def get_datebirth(self):
        return self.datebirth

    def set_datebirth(self, value):
        self.datebirth = value


    # Getter setter for placeborn
    def get_placeborn(self):
        return self.placeborn

    def set_placeborn(self, value):
        self.placeborn = value


    # Getter setter for domicile
    def get_domicile(self):
        return self.domicile 

    def set_domicile(self, value):
        self.domicile = value


    # Getter setter for dateapply
    def get_dateapply(self):
        return self.dateapply

    def set_dateapply(self, value):
        self.dateapply = value

    # Getter setter for trydate
    def get_trydate(self):
        return self.trydate

    def set_trydate(self, value):
        self.trydate = value

    # Getter setter for departmentsys
    def get_departmentsys(self):
        return self.departmentsys

    def set_departmentsys(self, value):
        self.departmentsys = value


    # Getter setter for department1
    def get_department1(self):
        return self.department1 

    def set_department1(self, value):
        self.department1 = value


    # Getter setter for department2
    def get_department2(self):
        return self.department2

    def set_department2(self, value):
        self.department2 = value


    # Getter setter for department3
    def get_department3(self):
        return self.department3

    def set_department3(self, value):
        self.department3 = value


    # Getter setter for department4
    def get_department4(self):
        return self.department4

    def set_department4(self, value):
        self.department4 = value

    # Getter setter for department5 
    def get_department5(self):
        return self.department5

    def set_department5(self, value):
        self.department5 = value


    # Getter setter for department6
    def get_department6(self):
        return self.department6 

    def set_department6(self, value):
        self.department6 = value


    # Getter setter for department7
    def get_department7(self):
        return self.department7

    def set_department7(self, value):
        self.department7 = value


    # Getter setter for department8
    def get_department8(self):
        return self.department8

    def set_department8(self, value):
        self.department8 = value


    # Getter setter for department9
    def get_department9(self):
        return self.department9

    def set_department9(self, value):
        self.department9 = value

    # Getter setter for department10
    def get_department10(self):
        return self.department10

    def set_department10(self, value):
        self.department10 = value


    # Getter setter for regencycode
    def get_regencycode(self):
        return self.regencycode

    def set_regencycode(self, value):
        self.regencycode = value


    # Getter setter for jobtitlecode
    def get_jobtitlecode(self):
        return self.jobtitlecode

    def set_jobtitlecode(self, value):
        self.jobtitlecode = value


    # Getter setter for email
    def get_email(self):
        return self.email 

    def set_email(self, value):
        self.email = value


    # Getter setter for stafftype
    def get_stafftype(self):
        return self.stafftype

    def set_stafftype(self, value):
        self.stafftype = value


    # Getter setter for skillwork
    def get_skillwork(self):
        return self.skillwork

    def set_skillwork(self, value):
        self.skillwork = value

    
    # Getter setter for veterans
    def get_veterans(self):
        return self.veterans 

    def set_veterans(self, value):
        self.veterans = value


    # Getter setter for numberinsurance
    def get_numberinsurance(self):
        return self.numberinsurance

    def set_numberinsurance(self, value):
        self.numberinsurance = value

    
    # Getter setter for dateregisterinsurance
    def get_dateregisterinsurance(self):
        return self.dateregisterinsurance

    def set_dateregisterinsurance(self, value):
        self.dateregisterinsurance = value

    
    # Getter setter for address 
    def get_address(self):
        return self.address

    def set_address(self, value):
        self.address = value

    # Getter setter for provincecode
    def get_provincecode(self):
        return self.provincecode

    def set_provincecode(self, value):
        self.provincecode = value

    
    # Getter setter for village
    def get_village(self):
        return self.village  

    def set_village(self, value):
        self.village = value

    
    # Getter setter for wards
    def get_wards(self):
     return self.wards

    def set_wards(self, value):
        self.wards = value

    
    # Getter setter for address2
    def get_address2(self):
        return self.address2

    def set_address2(self, value):
        self.address2 = value

    
    # Getter setter for provincecode2
    def get_provincecode2(self):
        return self.provincecode2 

    def set_provincecode2(self, value):
        self.provincecode2 = value

    # Getter setter for viillage2
    def get_village2(self):
        return self.village2

    def set_village2(self, value):
        self.village2 = value

    
    # Getter setter for wards2  
    def get_wards2(self):
        return self.wards2

    def set_wards2(self, value):
        self.wards2 = value

    
    # Getter setter for citizenshipcode
    def get_citizenshipcode(self):
        return self.citizenshipcode

    def set_citizenshipcode(self, value):
        self.citizenshipcode = value

    
    # Getter setter for ethniccode
    def get_ethniccode(self):
        return self.ethniccode

    def set_ethniccode(self, value):
        self.ethniccode = value

    
    # Getter setter for religioncode  
    def get_religioncode(self):
        return self.religioncode 

    def set_religioncode(self, value):
        self.religioncode = value


    # Getter setter for nationalcode
    def get_nationalcode(self):
        return self.nationalcode

    def set_nationalcode(self, value):
        self.nationalcode = value


    # Getter setter for numberbank
    def get_numberbank(self):
        return self.numberbank

    def set_numberbank(self, value):
        self.numberbank = value


    # Getter setter for bankname  
    def get_bankname(self):
        return self.bankname

    def set_bankname(self, value):
        self.bankname = value


    # Getter setter for taxcode
    def get_taxcode(self):
        return self.taxcode

    def set_taxcode(self, value):
        self.taxcode = value


    # Getter setter for isdoctor
    def get_isdoctor(self):
        return self.isdoctor

    def set_isdoctor(self, value):
        self.isdoctor = value

    # Getter setter for educationallevel
    def get_educationallevel(self):
        return self.educationallevel

    def set_educationallevel(self, value):
        self.educationallevel = value


    # Getter setter for healthcode
    def get_healthcode(self):
        return self.healthcode 

    def set_healthcode(self, value):
        self.healthcode = value


    # Getter setter for height
    def get_height(self):
        return self.height

    def set_height(self, value):
        self.height = value


    # Getter setter for weight
    def get_weight(self):
        return self.weight

    def set_weight(self, value):
        self.weight = value


    # Getter setter for bloodtype
    def get_bloodtype(self):
        return self.bloodtype

    def set_bloodtype(self, value):
        self.bloodtype = value


    # Getter setter for phonenumber
    def get_phonenumber(self):
        return self.phonenumber

    def set_phonenumber(self, value):
        self.phonenumber = value


    # Getter setter for cellphone
    def get_cellphone(self):
        return self.cellphone

    def set_cellphone(self, value):
        self.cellphone = value


    # Getter setter for idcode
    def get_idcode(self):
        return self.idcode 

    def set_idcode(self, value):
        self.idcode = value


    # Getter setter for daterange
    def get_daterange(self):
        return self.daterange

    def set_daterange(self, value):
        self.daterange = value


    # Getter setter for placeidcode
    def get_placeidcode(self):
        return self.placeidcode

    def set_placeidcode(self, value):
        self.placeidcode = value


    # Getter setter for registerhospital
    def get_registerhospital(self):
        return self.registerhospital

    def set_registerhospital(self, value):
        self.registerhospital = value


    # Getter setter for numbermedical
    def get_numbermedical(self):
        return self.numbermedical 

    def set_numbermedical(self, value):
        self.numbermedical = value


    # Getter setter for placemedical
    def get_placemedical(self):
        return self.placemedical

    def set_placemedical(self, value):
        self.placemedical = value


    # Getter setter for datemedical
    def get_datemedical(self):
        return self.datemedical

    def set_datemedical(self, value):
        self.datemedical = value


    # Getter setter for isforeigner
    def get_isforeigner(self):
        return self.isforeigner

    def set_isforeigner(self, value):
        self.isforeigner = value


    # Getter setter for istablets
    def get_istablets(self):
        return self.istablets

    def set_istablets(self, value):
        self.istablets = value


    # Getter setter for isunionists  
    def get_isunionists(self):
        return self.isunionists

    def set_isunionists(self, value): 
        self.isunionists = value


    # Getter setter for isfederation
    def get_isfederation(self):
        return self.isfederation

    def set_isfederation(self, value):
        self.isfederation = value


    # Getter setter for isleaders
    def get_isleaders(self):
        return self.isleaders

    def set_isleaders(self, value):
        self.isleaders = value


    # Getter setter for isparttime
    def get_isparttime(self):
        return self.isparttime

    def set_isparttime(self, value):
        self.isparttime = value

    # Getter setter for isado
    def get_isado(self):
        return self.isado

    def set_isado(self, value):
        self.isado = value


    # Getter setter for iscoo
    def get_iscoo(self):
        return self.iscoo

    def set_iscoo(self, value):
        self.iscoo = value


    # Getter setter for iscfo
    def get_iscfo(self):
        return self.iscfo

    def set_iscfo(self, value):
        self.iscfo = value


    # Getter setter for urlsignature
    def get_urlsignature(self):
        return self.urlsignature

    def set_urlsignature(self, value):
        self.urlsignature = value