import FileReader
from PageOneWriter import PageOneWriter
from PageTwoWriter import PageTwoWriter
from PageThreeWriter import PageThreeWriter
from Report import Report
from openpyxl import load_workbook
import os

###########TODODODDO

##Generelt
#Formaterign af tekst
##Generer færdige rapport navn ud fra klade-rapport-navn
###UI
##Evt lav tjek på om alle kolonner er udfyldt i tabellen på side 2


#Side 1
##Bug ved vedligeholdestilsandt både JA og Nej

##Husk at ændre kolonne størrelser på linje 1 i Bemærkninger
##Når der er flere til stede ved vurderingen tager den kun

####REGLER
###PÅ SIDE 2 SKAL ALLE TITLER SKRIVES PÅ SAMME LINJE (INGEN LINJESKIFT)
###PÅ SIDE 3 SKAL DER VÆRE KOLON BAG TYPEN

####Henter data fra klade

files = os.listdir("C:\\Users\\Fredrik\\PycharmProjects\\ReportFiller\\Files")
drafts = []
reports = []

for file in files:
    if '~$' not in file:
        if '.txt' in file:
            drafts.append(file)
        else:
            reports.append(file)
report_chosen = True
while report_chosen:
    print("Vælg rapport:")
    for index, report in enumerate(reports):
        print("Nr.", index, ":", report)

    report_index = input("\nRapport nr: \n")

    if int(report_index) <= reports.__len__() - 1:
        report_chosen = False
    else:
        print("Det valgte nummer eksisterer ikke!")

draft_chosen = True
while draft_chosen:
    print("Vælg kladde:")
    for index, draft in enumerate(drafts):
        print("Nr.", index, ":", draft)

    draft_index = input("\nKladde nr: ")

    if int(draft_index) <= drafts.__len__() - 1:
        draft_chosen = False
    else:
        print("Det valgte nummer eksisterer ikke!")

report_name = reports[int(report_index)]
draft_name = drafts[int(draft_index)]
print("\nValgt rapport:", reports[int(report_index)])
print("Valgt kladde:", drafts[int(draft_index)])
print("\nRapport udfyldes...")

report = load_workbook('C:\\Users\\Fredrik\\PycharmProjects\\ReportFiller\\Files\\' + report_name)
file = "C:\\Users\\Fredrik\\PycharmProjects\\ReportFiller\\Files\\" + draft_name
newReport = Report(report)
newReport.get_rownumbers_for_page_two()
print("...")
stylesheet_1 = newReport.get_stylesheet_1()
stylesheet_3 = newReport.get_stylesheet_3()
stylesheet_2 = newReport.get_stylesheet_2()
print("...")

page_one_writer = PageOneWriter(stylesheet_1, file)
page_one_writer.add_data_to_page_one()

page_two_writer = PageTwoWriter(stylesheet_2, file)
page_two_writer.add_data()
print("...")
page_three_writer = PageThreeWriter(stylesheet_3, file)
page_three_writer.add_data_to_page_three()
newReport.report.save('færdig.xlsx')
print("Rapport er udfyldt!")
os.system('start færdig.xlsx')




