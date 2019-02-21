from openpyxl import load_workbook
from openpyxl.styles import Alignment
from FileReader import FileReader
from pprint import pprint
from Report import Report

class PageThreeWriter:
##report = load_workbook('C:\\Users\\Fredrik\\PycharmProjects\\ReportFiller\\Files\\egeskoven-rapport.xlsx')

    def __init__(self, stylesheet_3, file_url):
        self.stylesheet_3 = stylesheet_3
        self.file_url = file_url

    ##stylesheet_3 = Report.get_stylesheet_3()

    def add_data_to_page_three (self):
        file = open(self.file_url, "r")

        file_reader = FileReader(file)
        list_of_content = file_reader.getDataFromPageThree()
        general_data = list_of_content[0]
        hall_data = list_of_content[1]
        kitchen_data = list_of_content[2]
        toilet_data = list_of_content[3]
        living_room_data = list_of_content[4]
        room_1_data = list_of_content[5]
        room_2_data = list_of_content[6]

        file.close()

    ##Generelt
        self.add_data_to_fields(general_data.eltavle, 5)
        self.add_data_to_fields(general_data.hfi, 6)
        self.add_data_to_fields(general_data.stik, 7)
        self.add_data_to_fields(general_data.vinduer, 8)
        self.add_data_to_fields(general_data.vedligeholdse, 9)
        self.add_data_to_fields(general_data.rydning, 10)
        self.add_data_to_fields(general_data.rengøring, 11)

    ##Entre
        self.add_data_to_fields(hall_data.loft, 13)
        self.add_data_to_fields(hall_data.vægge, 14)
        self.add_data_to_fields(hall_data.gulv, 15)
        self.add_data_to_fields(hall_data.træværk, 16)

    ##Køkken
        self.add_data_to_fields(kitchen_data.Loft, 18)
        self.add_data_to_fields(kitchen_data.Vægge, 19)
        self.add_data_to_fields(kitchen_data.Gulv, 20)
        self.add_data_to_fields(kitchen_data.Træværk, 21)
        self.add_data_to_fields(kitchen_data.Skabe, 22)
        self.add_data_to_fields(kitchen_data.Bordplader, 23)
        self.add_data_to_fields(kitchen_data.Vægfliser, 24)
        self.add_data_to_fields(kitchen_data.Afløbsinstallation, 25)
        self.add_data_to_fields(kitchen_data.Vandinstallation, 26)
        self.add_data_to_fields(kitchen_data.Gasinstallation, 27)
        self.add_data_to_fields(kitchen_data.Hvidevarer, 28)

    ##Toilet
        self.add_data_to_fields(toilet_data.Loft, 30)
        self.add_data_to_fields(toilet_data.Vægge, 31)
        self.add_data_to_fields(toilet_data.Gulv, 32)
        self.add_data_to_fields(toilet_data.Træværk, 33)
        self.add_data_to_fields(toilet_data.WC, 34)
        self.add_data_to_fields(toilet_data.Håndvask, 35)
        self.add_data_to_fields(toilet_data.Bruseinstallation, 36)
        self.add_data_to_fields(toilet_data.Vandinstallation, 37)
        self.add_data_to_fields(toilet_data.Afløbsinstallation, 38)
        self.add_data_to_fields(toilet_data.Ventilation, 39)

    ##Stue
        if living_room_data.loft != 0 and living_room_data.gulv != 0:
            self.add_data_for_rooms(living_room_data, 41)

    ##Værelse 1
        self.add_data_for_rooms(room_1_data, 47)

    ##Værelse 2
        self.add_data_for_rooms(room_2_data, 53)

    def add_data_for_rooms (self, data, start_row):
        self.stylesheet_3['A' + str(start_row)] = data.title
        self.add_data_to_fields(data.loft, start_row)
        self.add_data_to_fields(data.vægge, start_row + 1)
        self.add_data_to_fields(data.gulv, start_row + 2)
        self.add_data_to_fields(data.træværk, start_row + 3)
        self.add_data_to_fields(data.radiator, + start_row + 4)

    def add_data_to_fields(self, data, row):
        if data != 0:
            self.add_condition(data.condition, row)
            self.add_payed_by(data.payed_by, row)
            if data.comment != '':
                self.add_comment(data.comment, row)
            if data.retention_sum != 0:
                self.add_retention_sum(data.retention_sum, row)

            if data.deduction != 0:
                self.add_deduction(data.deduction, row)
        else:
            print("FEJL! Række:", row, "Data:", data)


    def add_condition(self, condition, row):
        x = 'X'
        if '(' in condition:
            x = '(X)'
        if 'G' in condition:
            self.stylesheet_3['D' + str(row)] = x
        if 'M' in condition:
            self.stylesheet_3['E' + str(row)] = x
        if 'D' in condition:
            self.stylesheet_3['F' + str(row)] = x

    def add_payed_by(self, payed_by, row):
        x = 'X'
        if '(' in payed_by:
            x = '(X)'

        if payed_by == 'B':
            self.stylesheet_3['G' + str(row)] = x
        if payed_by == 'F':
            self.stylesheet_3['H' + str(row)] = x

    def add_comment (self, comment, row):
        if comment[0] == ' ':
            comment = comment[1:]

        self.stylesheet_3['K' + str(row)] = comment

    def add_retention_sum (self, retention_sum, row):
        self.stylesheet_3['I' + str(row)] = retention_sum

    def add_deduction (self, deduction_sum, row):
        self.stylesheet_3['J' + str(row)] = deduction_sum



