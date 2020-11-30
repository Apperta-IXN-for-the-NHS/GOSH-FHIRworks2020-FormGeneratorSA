Created by Sami Al Alawi for GoshFHIRworks hackathon

Package creates pdfs and word documents (docx) based on a JSON FHIR
record provided.

The package contains three main components. FHIRparser.py parses the 
record and provides getter functions to obtain the key information from
the record. pdfGenerator and wordGenerator both use FHIRparser to create 
standard pdf and word documents for patients data.

The package requires both the FPDF and docx packages to be installed.