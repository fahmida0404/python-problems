from PyPDF2 import PdfMerger
import os

#first create a directory and keep some pdf files there
path = "pdf_merging/pdf" 
files = os.listdir(path) #all files of the directory
print(files)
merger = PdfMerger()
merged_file = "pyhton_cheatsheet.pdf"

for file in files:
    if file.endswith(".pdf"):
        merger.append(f"{path}/{file}")

merger.write(f"{path}/{merged_file}")
merger.close()
print(f"Merged as {merged_file}")