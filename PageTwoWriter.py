from pprint import pprint
from FileReader import FileReader
from openpyxl import load_workbook
from PageTwo import PageTwo


class PageTwoWriter:
    def __init__(self, stylesheet_two, file_url):
        self.stylesheet_two = stylesheet_two
        self.file_url = file_url

    def add_data(self):
        file = open(self.file_url, "r")

        file_reader = FileReader(file)
        list_of_lists = file_reader.getDataFromPageTwo()
        general_list = list_of_lists[0]
        kitchen_list = list_of_lists[1]
        restroom_list = list_of_lists[2]
        living_room_list = list_of_lists[3]

        self.add_data_to_stylesheet_page_two(general_list, PageTwo.general_start_row)
        self.add_data_to_stylesheet_page_two(kitchen_list, PageTwo.kitchen_start_row)
        self.add_data_to_stylesheet_page_two(restroom_list, PageTwo.restroom_start_row)
        self.add_data_to_stylesheet_page_two(living_room_list, PageTwo.living_room_start_row)

        file.close()

    def add_data_to_stylesheet_page_two(self, list, row):
        row = row + 1
        for item in list:
            self.add_to_columns(row, item)
            row += 1

    def add_to_columns(self, row, item):
        self.stylesheet_two['B' + str(row)] = item.title
        self.stylesheet_two['C' + str(row)] = item.year
        ##Hvis indholdet er tomt skal der ikke skrives til filen da formlen ikke virker hvis der gør
        if item.expenditure != '' and item.expenditure != ' ':
            self.stylesheet_two['D' + str(row)] = item.expenditure

        self.stylesheet_two['E' + str(row)] = item.appendix
        self.stylesheet_two['F' + str(row)] = item.quantity
        self.stylesheet_two['G' + str(row)] = item.age
        self.stylesheet_two['H' + str(row)] = item.years_curve
        self.stylesheet_two['I' + str(row)] = item.written_down_to
        self.stylesheet_two['J' + str(row)] = item.owners_work

        if item.number_of_hours != ' ' and item.number_of_hours != '':
            self.stylesheet_two['K' + str(row)] = item.number_of_hours

        if item.cost != ' ' and item.cost != '':
            self.stylesheet_two['L' + str(row)] = item.cost
