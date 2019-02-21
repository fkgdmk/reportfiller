from GeneralInfo import GeneralInfo

class PageOne:

    def __init__(self, address=0, owner=0, date=0, id=0, inspection_date=0, people_at_inspection=[],
                 maintance_condition=0, appendix=False, last_report=0, owners_report=0, apartment_takeover=0,
                 reconstruction=False, construction_project=GeneralInfo, VVS_approval=GeneralInfo,
                 drain_approval=GeneralInfo, gas_approval=GeneralInfo, electricity_approval=GeneralInfo, comments=[]
                 ):
        self.address = address
        self.owner = owner
        self.date = date
        self.id = id
        self.inspection_date = inspection_date
        self.people_at_inspection = people_at_inspection
        self.maintance_condition = maintance_condition
        self.appendix = appendix
        self.last_report = last_report
        self.owners_report = owners_report
        self.apartment_takeover = apartment_takeover
        self.reconstruction = reconstruction
        self.construction_project = construction_project
        self.VVS_approval = VVS_approval
        self.drain_approval = drain_approval
        self.gas_approval = gas_approval
        self.electricity_approval = electricity_approval
        self.comments = comments
