"""

Package creates pdfs and word documents (docx) based on a JSON FHIR
record provided.

The package contains three main components. FHIRparser.py parses the 
record and provides getter functions to obtain the key information from
the record. pdfGenerator and wordGenerator both use FHIRparser to create 
standard pdf and word documents for patients data.

The package requires both the FPDF and docx packages to be installed.

pdfGenerator can be used in two ways:
1 - pdfGenerator.createPDF(FHIRrecord, nameOfPDF) 
    saves a pdf based on the FHIR record provided
2 - pdfGenerator.getPDF(FHIRrecord) 
    returns a pdf based on the FHIR record provided

wordGenerator can be used in two ways:
1 - wordGenerator.createDocument(FHIRrecord, nameOfPDF) 
    saves a docx based on the FHIR record provided
2 - wordGenerator.getDocument(FHIRrecord) 
    returns a docx based on the FHIR record provided

"""