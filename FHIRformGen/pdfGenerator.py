from fpdf import FPDF
from FHIRformGen import FHIRparser as fp

#constants used to format the text
LEFT_MARGIN = 15
CENTER_MARGIN = 75
TITLE_MARGIN = 10

def createTitle(pdf):
    pdf.set_font("Arial", size=24)
    pdf.text(75, 25, txt="Medical Record")
    pdf.line(10, 35, 200, 35)

def createHeader(pdf, patientValues):
    pdf.set_font("Arial", size=12)
    pdf.text(125, 10, txt="Last updated: " + patientValues.getLastUpdated())

def createIdentificationSection(pdf, patientValues):
    pdf.set_font("Arial", size=12, style="BI")
    pdf.text(TITLE_MARGIN, 40, "Identification")
    pdf.set_font("Arial", size=12)
    pdf.text(CENTER_MARGIN, 46, "Patient ID: " + patientValues.getPatientID())
    pdf.text(LEFT_MARGIN, 46, "Name: " + patientValues.getGivenName())
    pdf.text(CENTER_MARGIN, 50, "Medical record number: " + patientValues.getMedicalRecordNumber())
    pdf.text(LEFT_MARGIN, 50, "Family name: " + patientValues.getFamilyName())
    pdf.text(LEFT_MARGIN, 54, "Sex: " + patientValues.getSex())

def createDetails(pdf, patientValues):
    pdf.line(10, 65, 200, 65)
    pdf.set_font("Arial", size=12, style="BI")
    pdf.text(TITLE_MARGIN, 70, "Details")
    pdf.set_font("Arial", size=12)
    pdf.text(LEFT_MARGIN, 76, "Birthday: " + patientValues.getBirthDate())
    pdf.text(CENTER_MARGIN, 80, "Birth Address: " + patientValues.getBirthAddress())
    pdf.text(CENTER_MARGIN, 76, "Language: " + patientValues.getLanguage())
    pdf.text(LEFT_MARGIN, 80, "Marital Status: " + patientValues.getMaritalStatus())

def createFormalDocs(pdf, patientValues):
    pdf.line(10, 95, 200, 95)
    pdf.set_font("Arial", size=12, style="BI")
    pdf.text(TITLE_MARGIN, 100, "Formal document numbers")
    pdf.set_font("Arial", size=12)
    pdf.text(LEFT_MARGIN, 106, "Social security number: " + patientValues.getSocialSecurityNumber())
    pdf.text(LEFT_MARGIN, 110, "Driver License number: " + patientValues.getDriversLicense())
    pdf.text(LEFT_MARGIN, 114, "Passport number: " + patientValues.getPassportNumber())

def createContact(pdf, patientValues):
    pdf.line(10, 125, 200, 125)
    pdf.set_font("Arial", size=12, style="BI")
    pdf.text(TITLE_MARGIN, 130, "Contact")
    pdf.set_font("Arial", size=12)
    pdf.text(LEFT_MARGIN, 134, "Phone number: " + patientValues.getContactDetails())
    pdf.text(LEFT_MARGIN, 138, "Address: " + patientValues.getCurrentAddress())

def createExtraNotes(pdf, patientValues):
    pdf.line(10, 150, 200, 150)
    pdf.set_font("Arial", size=12, style="BI")
    pdf.text(TITLE_MARGIN, 155, "Extra notes")

def constructPDF(FHIRrecord):
    #calls the parser to get the information from the record
    patientValues = fp.FHIRParser(FHIRrecord)
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    #calls the functions that handle the individual sections
    createHeader(pdf, patientValues)
    createTitle(pdf)
    createIdentificationSection(pdf, patientValues)
    createDetails(pdf, patientValues)
    createFormalDocs(pdf, patientValues)
    createContact(pdf, patientValues)
    createExtraNotes(pdf, patientValues)
    return pdf

def createPDF(FHIRrecord, nameOfPDF):
    """ 
    function that acts as one of the entry points
    The function saves a pdf based on the FHIR record provided

    parameters
    ----------
    FHIRrecord -> a JSON medical record obeying the FHIR standard
    nameOfPDF  -> string that the user wants the pdfs name to be

    """
    pdf = constructPDF(FHIRrecord)
    pdf.output(nameOfPDF + ".pdf")


def getPDF(FHIRrecord):
    """ 
    function that acts as the second entry point
    The function returns a pdf based on the FHIR record provided

    parameters
    ----------
    FHIRrecord -> a JSON medical record obeying the FHIR standard

    """
    return constructPDF(FHIRrecord)