class Property:

    def __init__(self, worth):
        self.set_worth(worth)

    def set_worth(self, worth):
        if isinstance(worth, int) and worth > 0:
            self.__worth = worth
        else:
            print('Стоимость должна быть числом больше нуля')

    def get_worth(self):
        return self.__worth

    def tax_calculation(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.get_worth() / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.get_worth() / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.get_worth() / 500


while True:
    int_text = input('Введите имеющуюся сумму денег: ')
    if int_text.isdigit():
        amount_money = int(int_text)
        if amount_money > 0:
            break
    else:
        print('Сумма должна быть положительным числом')

int_worth = int(input('Введите стоимость имущества: '))

worth_apartment = Apartment(int_worth)
worth_car = Car(int_worth)
worth_countryHouse = CountryHouse(int_worth)

print(worth_apartment.tax_calculation())
