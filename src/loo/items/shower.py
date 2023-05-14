class Shower:

    __condition = None
    CONDITION_NEW = "new"
    CONDITION_USED = "used, but okayish"
    CONDITION_DEFECT = "defect"
    turned_on = False

    def __init__(self, condition=CONDITION_NEW):
        self.__condition = condition

    def get_condition(self):
        return self.__condition

    def set_condition(self, condition):
        self.__condition = condition

    def turn_on(self):
        self.turned_on = True

    def turn_off(self):
        self.turned_on = False

    def is_turned_on(self):
        return self.turned_on

    def is_turned_off(self):
        return not self.turned_on
