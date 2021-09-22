from models import Produce
from funcs import sum_,alias
from logicals import and_
from base import DB    
db = DB()

#available produce
result = db.select(alias(sum_(
    Produce.quantity_supplied),"total")).from_("test").filter(and_(
    Produce.category=="produce_bulked",Produce.partner_id=="AK/OT/0008",
    Produce.season=="2021-A",Produce.status=="active",Produce.submission_status=="submitted")).get()
print(result)