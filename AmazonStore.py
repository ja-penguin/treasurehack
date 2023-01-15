# Description: Finding the profit margins of an amazon store by seeing the total sales for a particular item
#              and finding the total profit for each individual item as well as the store profit total.


class AmazonItem:
    """
    Represents items that will be offered for sale at an Amazon storefront from a seller that is buying their
    items from a
    """
    def __init__(self, name, wholesale_cost, selling_price):
        """Creates a new menu item with a name, wholesale cost and the price it will be sold at"""
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """Returns the name of the item on the store"""
        return self._name

    def get_wholesale_cost(self):
        """Returns the price of them item on wholesale"""
        return self._wholesale_cost

    def get_selling_price(self):
        """Returns the price the item will be sold at"""
        return self._selling_price

class SalesForDay:
    """Represents the sales of a particular day"""
    def __init__(self, day, sales_dict):
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        """Returns the particular day the store is calculating sales for"""
        return self._day

    def get_sales_dict(self):
        """Returns the numbers of those items sold for that day"""
        return self._sales_dict

class InvalidSalesItemError(Exception):
    pass

class AmazonStoreFront:
    """
    Represents an Amazon store front that has 4 data members
    """
    def __init__(self, name):
        self._name_of_stand = name
        self._menu_dict = {}
        self._sales_for_day = []
        self._current_day = 0

    def get_name(self):
        """Returns the name of the Amazon storefront"""
        return self._name_of_stand

    def add_store_item(self, store_item):
        """Will add an item to the store"""
        self._menu_dict[store_item.get_name()] = store_item

    def enter_sales_for_today(self, sales):
        """Will compare the amount of money made for the Amazon storefront for 'today' in comparison to other days"""
        for today in sales:
            if today not in self._menu_dict:
                raise InvalidSalesItemError
        self._sales_for_day.append(SalesForDay(self._current_day, sales))
        self._current_day += 1
        # current day started at 0, with each passing day (+=) the sales entered for "today" will be a day after 0

    def get_sales_dict_for_day(self, particular_day):
        """Will get the amount of money that was generated for the Amazon seller on a particular day"""
        for a_day_of_sale in self._sales_for_day:
            if a_day_of_sale.get_day() == particular_day:
                return a_day_of_sale.get_sales_dict()

    def total_sales_for_store_item(self, name_of_store_item):
        """Will find the amount of a particular item was sold"""
        total_sales = 0     # at the start of the day any particular item had not been sold,
                            # so at the start of the day: zero of that item was given to a customer
        for entire_sale_of_one_store_item in self._sales_for_day:        # when looking at the total cash that
            # was made for one item within all the cash made at the lemonade stand at the end of day
            total_sales += entire_sale_of_one_store_item.get_sales_dict([name_of_store_item])
            # the total_sales will now increase (+=) from zero from the start of day to an increased positive number
        print("total sales for store item = ", total_sales)
        return total_sales


    def total_profit_for_store_item(self, name_of_store_item):
        """Will find the total amount of profit for one particular item in the store"""
        # this will find the amount of money the lemonade stand was able to generate at the end of the day
        step_1 = self._menu_dict[name_of_store_item].get_name()
        # get the selling price of a particular item on the menu by its name from the menu_dict - where all the store
        # names are kept
        step_2 = self.total_sales_for_store_item(name_of_store_item)
        # by finding the total sales for a store item (which will be picked via parameter) from the method before
        step_3 = step_1 * step_2
        print("total profit for store item =", step_3)
        return step_3

    def total_profit_for_store(self):
        """Will return the profit of the Amazon store"""
        total_profit = 0
        for all_cash_made in self._menu_dict:
            total_profit += self.total_profit_for_store_item(all_cash_made)
        print("total profit for store = ", total_profit)
        return total_profit


store = AmazonStoreFront("Lily's Clothes")
item1 = AmazonItem('High rise jeans', 1, 75)
store.add_store_item(item1)
item2 = AmazonItem('V neck blouse', 2, 35)
store.add_store_item(item2)
item3 = AmazonItem('Baby Blue Knit sweater', 1, 115)
store.add_store_item(item3)
day1 = {
    'High rise jeans'             : 15,
    'V neck blouse'               : 32,
    'Baby Blue Knit sweater'      : 67,
}
day2 = {
    'High rise jeans'             : 38,
    'V neck blouse'               : 43,
    'Baby Blue Knit sweater'      : 54,
}
day3 = {
    'High rise jeans'             : 24,
    'V neck blouse'               : 25,
    'Baby Blue Knit sweater'      : 2,
}
