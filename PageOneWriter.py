from PageOne import PageOne
from GeneralInfo import GeneralInfo
from pprint import pprint
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from FileReader import FileReader

class PageOneWriter:
    def __init__(self, stylesheet_1, file_url):
        self.stylesheet_1 = stylesheet_1
        self.file_url = file_url

    def add_data_to_page_one(self):
        file = open(self.file_url, "r")

        file_reader = FileReader(file)
        page1 = file_reader.getDataFromPageOne()

        self.stylesheet_1['B5'] = page1.address
        self.stylesheet_1['B6'] = page1.owner
        self.stylesheet_1['K5'] = page1.date
        self.stylesheet_1['K7'] = page1.inspection_date

        self.add_inspectors(page1.people_at_inspection)
        self.add_maintance_condition(page1.maintance_condition)
        self.add_appendix(page1.appendix)

        self.stylesheet_1['K26'] = page1.last_report
        self.stylesheet_1["K27"] = page1.owners_report

        # Generelle oplysninger
        self.stylesheet_1["H28"] = page1.apartment_takeover
        self.set_reconstruction(page1.reconstruction)
        self.set_general_info_table(page1.construction_project, "35")
        self.set_general_info_table(page1.VVS_approval, "36")
        self.set_general_info_table(page1.drain_approval, "37")
        self.set_general_info_table(page1.gas_approval, "38")
        self.set_general_info_table(page1.electricity_approval, "39")
        # Tilføj bemærkninger
        self.add_comments(page1.comments)

        file.close()

    def add_inspectors(self, inspectors):
        row = 9
        for person in inspectors:
            self.stylesheet_1['I' + str(row)] = person
            row += 1

    def add_maintance_condition(self, condition):
        if condition != 0:
            conditions = condition.split('-')
            for condition in conditions:
                if condition == "1":
                    self.stylesheet_1['K20'] = 'X'
                if condition == "2":
                    self.stylesheet_1['K19'] = 'X'
                if condition == "3":
                    self.stylesheet_1['K18'] = 'X'
                if condition == "4":
                    self.stylesheet_1['K17'] = 'X'
                if condition == "5":
                    self.stylesheet_1['K16'] = 'X'

    def add_appendix(self, appendix):
        if appendix:
            self.stylesheet_1["I24"] = "X"
        else:
            self.stylesheet_1["K24"] = "X"

    def set_reconstruction(self, reconstruction_done):
        if reconstruction_done:
            self.stylesheet_1["K29"] = "X"
        else:
            self.stylesheet_1["K30"] = "X"

    def set_general_info_table(self, case, row):

        status_columns = {'IB': 'E', 'F': 'F', 'N': 'G', 'A': 'H'}
        column = status_columns.get(case.status[0])
        if column is not None:
            field = column + row
            self.stylesheet_1[field] = "X"

        # Sætter kommentar felt
        self.stylesheet_1["I" + row] = case.comment

    def add_comments(self, comments):
        row = 41
        for comment in comments:
            self.stylesheet_1['A' + str(row)] = comment
            self.stylesheet_1['A' + str(row)].alignment = Alignment(wrap_text=True)
            row += 1
