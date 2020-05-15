from typing import Optional
from models.base_model import Model

class Cash(Model):
    def __init__(self, deposits: int=None, withdrawals: int=None):

        self.deposits = deposits
        self.withdrawals = withdrawals

        self.swagger_types = {
            'deposits': int,
            'withdrawals': int
        }

        self.attribute_map = {
            'deposits': 'deposits',
            'withdrawals': 'withdrawals'
        }

class DomesticWire(Model):
    """Used to indicate the count or amount of monthly domestic wires."""
    def __init__(self, inbound: int=None, outbound: int=None):

        self.inbound = inbound
        self.outbound = outbound

        self.swagger_types = {
            'inbound': int,
            'outbound': int
        }

        self.attribute_map = {
            'inbound': 'inbound',
            'outbound': 'outbound'
        }

class ForeignWire(Model):
    """Used to indicate the count or amount of monthly foreign wires."""
    def __init__(self, inbound: int=None, outbound: int=None):

        self.inbound = inbound
        self.outbound = outbound

        self.swagger_types = {
            'inbound': int,
            'outbound': int
        }

        self.attribute_map = {
            'inbound': 'inbound',
            'outbound': 'outbound'
        }

class Counts(Model):
    def __init__(self, deposit: int=None, cash: Cash=None, domestic_wire: Optional[DomesticWire]=None,
                 foreign_wire: Optional[ForeignWire]=None):

        self.deposit = deposit
        self.cash = cash
        self.domestic_wire = domestic_wire
        self.foreign_wire = foreign_wire

        self.swagger_types = {
            'deposit': int,
            'cash': Cash,
            'domestic_wire': DomesticWire,
            'foreign_wire': ForeignWire
        }

        self.attribute_map = {
            'deposit': 'deposit',
            'cash': 'cash',
            'domestic_wire': 'domesticWire',
            'foreign_wire': 'foreignWire'
        }

class Amounts(Model):
    def __init__(self, deposit: int=None, cash: Cash=None, domestic_wire: Optional[DomesticWire]=None,
                 foreign_wire: Optional[ForeignWire]=None):

        self.deposit = deposit
        self.cash = cash
        self.domestic_wire = domestic_wire
        self.foreign_wire = foreign_wire

        self.swagger_types = {
            'deposit': int,
            'cash': Cash,
            'domestic_wire': DomesticWire,
            'foreign_wire': ForeignWire
        }

        self.attribute_map = {
            'deposit': 'deposit',
            'cash': 'cash',
            'domestic_wire': 'domesticWire',
            'foreign_wire': 'foreignWire'
        }

class MonthlyActivity(Model):
    def __init__(self, counts: Counts=None, amounts: Amounts=None):

        self.counts = counts
        self.amounts = amounts

        self.swagger_types = {
            'counts': Counts,
            'amounts': Amounts
        }

        self.attribute_map = {
            'counts': 'counts',
            'amounts': 'amounts'
        }