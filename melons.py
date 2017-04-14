"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """An abstract base class from which other Melon Orders inherit."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "christmas":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        #super gets these init attributes from AbstractMelonOrder
        super(DomesticMelonOrder, self).__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        #super gets these init attributes from AbstractMelonOrder
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        #these attributes are specific to InternationalMelonOrder
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            return total + 3
        else:
            return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order with the US government."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        #super gets these init attributes from AbstractMelonOrder
        super(GovernmentMelonOrder, self).__init__(species, qty, "government", None)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Record the fact than an order passed inspection."""

        self.passed_inspection = passed

        return self.passed_inspection

    # an alternative way to do this would be to use super to get get_total
    # from AbstractMelonOrder and pass tax as = 0
    def get_total(self):
        base_price = 5
        if self.species == "christmas":
            base_price = base_price * 1.5
        total = self.qty * base_price

        return total
