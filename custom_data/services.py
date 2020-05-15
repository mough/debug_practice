from typing import Optional, List
from models.base_model import Model

class DomesticWire(Model):
    """Used to indicate if the org expects to send or receive domestic wires."""
    def __init__(self, inbound: bool=None, outbound: bool=None):

        self.inbound = inbound
        self.outbound = outbound

        self.swagger_types = {
            'inbound': bool,
            'outbound': bool
        }

        self.attribute_map = {
            'inbound': 'inbound',
            'outbound': 'outbound'
        }

class ForeignWire(Model):
    """Used to indicate if the org expects to send or receive foreign wires, and
    if so which countries will wires be sent to and/or received from."""
    def __init__(self, inbound: bool=None, outbound: bool=None, origins: Optional[List[str]]=None,
                 destinations: Optional[List[str]]=None):

        self.inbound = inbound
        self.outbound = outbound
        self.origins = origins
        self.destinations = destinations

        self.swagger_types = {
            'inbound': bool,
            'outbound': bool,
            'origins': List[str],
            'destinations': List[str]
        }

        self.attribute_map = {
            'inbound': 'inbound',
            'outbound': 'outbound',
            'origins': 'origins',
            'destinations': 'destinations'
        }

class Ach(Model):
    """Used to indicate if the org expects to send or receive ACH payments."""
    def __init__(self, inbound: bool=None, outbound: bool=None):

        self.inbound = inbound
        self.outbound = outbound

        self.swagger_types = {
            'inbound': bool,
            'outbound': bool
        }

        self.attribute_map = {
            'inbound': 'inbound',
            'outbound': 'outbound'
        }

class Services(Model):
    """Used to indicate which services the org expects to utilize."""
    def __init__(self, ach: Ach=None, domestic_wire: Optional[DomesticWire]=None,
                 foreign_wire: Optional[ForeignWire]=None):

        self.ach = ach
        self.domestic_wire = domestic_wire
        self.foreign_wire = foreign_wire

        self.swagger_types = {
            'ach': Ach,
            'domestic_wire': DomesticWire,
            'foreign_wire': ForeignWire
        }

        self.attribute_map = {
            'ach': 'ach',
            'domestic_wire': 'domesticWire',
            'foreign_wire': 'foreignWire'
        }