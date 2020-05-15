from json import dumps

from custom_data.anticipated_activity import AnticipatedActivity
from custom_data.services import Services, Ach, ForeignWire as ServiceForeignWire, \
    DomesticWire as ServiceDomesticWire
from custom_data.monthly_activity import MonthlyActivity, Amounts, Counts, ForeignWire, \
    DomesticWire, Cash

print("Dumping JSON of current anticipated activity.")
anticipated_activity_json = dumps(AnticipatedActivity(MonthlyActivity(counts=Counts(
                deposit=1212,
                cash=Cash(deposits=1414,
                          withdrawals=1616),
                domestic_wire=DomesticWire(inbound=2525,
                                           outbound=2727),
                foreign_wire=ForeignWire(inbound=2929,
                                         outbound=3232)),
                amounts=Amounts(deposit=1313,
                                cash=Cash(deposits=1515,
                                          withdrawals=1717),
                                domestic_wire=DomesticWire(inbound=2626,
                                                           outbound=2828),
                                foreign_wire=ForeignWire(inbound=3131,
                                                         outbound=3434))),
                Services(ach=Ach(inbound=True, outbound=True),
                         domestic_wire=ServiceDomesticWire(inbound=True, outbound=True),
                         foreign_wire=ServiceForeignWire(inbound=True, outbound=True, origins=[
                             "India", "Laos"
                         ], destinations=["Hungary", "Serbia"]),
                         )).to_dict())

print(anticipated_activity_json)
print("Complete!")