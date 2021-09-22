from model import Document
from columns import Array,String,Integer
    
class Farmer(Document):
    projects = Array("projects",int)
    partner_id = String("partner_id")

class Produce(Document):
    submission_status = String("submission_status")
    category = String("category")
    project_id = Integer("project_id")
    partner_id = String("partner_id")
    quantity_supplied = Integer("quantity_supplied")
    season=String("season")