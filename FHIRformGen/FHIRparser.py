import json

class FHIRParser:
    """
    Class that parses a FHIR record (json) and obtains the key 
    information. Getters will allow access to the information.

    Methods
    ----------
    getPatientID : str -> returns the patient ID
    getResourceType : str -> returns the type of record (e.g. patient)
    getLastUpdated : str -> returns when the record was last modified
    getMothersMaiden : str -> returns patients mothers maiden name
    getSex : str -> returns sex of patient
    getBirthAddress : str -> returns where the patient was born
    getMedicalRecordNumber : str -> returns patients medical number
    getSocialSecurityNumber : str -> returns paitents social security number
    getDriversLicense : str -> returns patients drivers license
    getPassportNumber : str -> returns patients passport number
    getFamilyName : str -> returns paitents last name
    getGender : str -> returns patients gender
    getBirthDate : str -> returns patients birthday (yyyy/mm/dd)
    getMaritalStatus : str -> returns M for married
    getLanguage : str -> returns patients spoken language
    getGivenName : str -> returns patients name
    getPrefix : str -> returns Mr, Mrs etc
    getCurrentAddress : str -> returns the patients current address
    getContactDetails : str -> returns a phone number and the patients use for the phone
    
    """

    def __init__(self, FHIRrecord):
        #defining all instance variables from the record
        self.data = json.load(FHIRrecord)
        self.patientID = self.data['id']
        self.resourceType = self.data['resourceType']
        self.lastUpdated = self.data['meta']['lastUpdated'][:10]
        self.mothersMaiden = self.data['extension'][2]['valueString']
        self.sex = self.data['extension'][3]['valueCode']
        self.birthAddress = self.data['extension'][4]['valueAddress']['city'] + ", " + self.data['extension'][4]['valueAddress']['state'] + ", " + self.data['extension'][4]['valueAddress']['country']
        self.medicalRecordNumber = self.data['identifier'][1]['value']
        self.socialSecurityNumber = self.data['identifier'][2]['value']
        self.driverLicense = self.data['identifier'][3]['value']
        self.passportNumber = self.data['identifier'][4]['value']
        self.familyName = self.data['name'][0]['family']
        self.gender = self.data['gender']
        self.birthDate = self.data['birthDate']
        self.maritalStatus = self.data['maritalStatus']['text']
        self.language = self.data['communication'][0]['language']['text']

        gn = ""
        for name in self.data['name'][0]['given']:
            gn = gn + name + " "
        self.givenName = gn

        pref = ""
        for pre in self.data['name'][0]['prefix']:
            pref = pref + pre + " "
        self.prefix = pref

        for contact in self.data['telecom']:
            self.contactDetails = contact['system'] + " " + contact['use'] + " " + contact['value']

        ad = ""
        for line in self.data['address'][0]['line']:
            ad = ad + line + ", "
        self.address = ad + self.data['address'][0]['city'] + ", " + self.data['address'][0]['state'] + ", " + self.data['address'][0]['country']


    def getPatientID(self):
        return self.patientID

    def getResourceType(self):
        return self.resourceType

    def getLastUpdated(self):
        return self.lastUpdated

    def getMothersMaiden(self):
        return self.mothersMaiden

    def getSex(self):
        return self.sex

    def getBirthAddress(self):
        return self.birthAddress

    def getMedicalRecordNumber(self):
        return self.medicalRecordNumber

    def getSocialSecurityNumber(self):
        return self.socialSecurityNumber

    def getDriversLicense(self):
        return self.driverLicense

    def getPassportNumber(self):
        return self.passportNumber

    def getFamilyName(self):
        return self.familyName

    def getGender(self):
        return self.gender

    def getBirthDate(self):
        return self.birthDate

    def getMaritalStatus(self):
        return self.maritalStatus

    def getLanguage(self):
        return self.language

    def getGivenName(self):
        return self.givenName

    def getPrefix(self):
        return self.prefix

    def getCurrentAddress(self):
        return self.address

    def getContactDetails(self):
        return self.contactDetails