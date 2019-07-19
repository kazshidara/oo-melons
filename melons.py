"""Classes for melon orders."""
import random
import datetime

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from"""

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

        if self.qty > 100:
            raise TooManyMelonsError

    def get_base_price(self):
        """ Gets a random base price between 5 and 9"""
        base_price = random.randint(5,9)
        print(base_price)

        # see if the order was placed during rush hour
        now = datetime.datetime.now()

        dow = now.weekday() # Mon is 0, Sun is 6
        hour = now.hour

        if hour >= 8 and hour < 11 and dow >= 0 and dow < 5:
            base_price += 4

        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total
   
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08
    order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    order_type = "international"

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)        
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        """Calculate price, including tax."""
        total = super().get_total()

        if self.qty < 10:
            total += 3

        return total

class GovernmentMelonOrder(AbstractMelonOrder):
    """Melon Order with US Government"""
    tax = 0

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.passed_inspection = False 

    def mark_inspection(self, passed):

        if passed:
            self.passed_inspection = True

        return True

class TooManyMelonsError(ValueError):
    """ Error Class"""

    pass
    # def __init__(self, expression, message):
    #     # self.expression = expression
    #     # self.message = message
    #     super().__init__("TooManyMelonsError",": Can't have more than 100 melons")
