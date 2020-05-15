from custom_data.monthly_activity import MonthlyActivity
from custom_data.services import Services
from base_model import Model

class AnticipatedActivity():

    def __init__(self, monthly: MonthlyActivity=None, services: Services=None):
        self.swagger_types = {
            'monthly': MonthlyActivity,
            'services': Services
        }

        self.attribute_map = {
            'monthly': 'monthly',
            'services': 'services'
        }

        self.monthly = monthly
        self.services = services