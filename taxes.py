class Property:
    name_taxes = 'Базовый налог'

    def __init__(self, worth):
        self.set_worth(worth)

    def set_worth(self, worth):
        self.__worth = worth

    def get_worth(self):
        return self.__worth

    def __str__(self):
        return '{}: {}'.format(self.name_taxes, self.get_worth())

    def tax_calculation(self):
        pass


class Apartment(Property):
    name_taxes = 'Налог на квартиру'

    def __init__(self, worth):
        super().__init__(worth),

    def tax_calculation(self):
        return super().get_worth() / 1000

    def __str__(self):
        return '{}: {}'.format(self.name_taxes, round(self.tax_calculation(), 2))


class Car(Property):
    name_taxes = 'Налог на машину'

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return super().get_worth() / 200

    def __str__(self):
        return '{}: {}'.format(self.name_taxes, round(self.tax_calculation(), 2))


class CountryHouse(Property):
    name_taxes = 'Налог на дачу'

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return super().get_worth() / 500

    def __str__(self):
        return '{}: {}'.format(self.name_taxes, round(self.tax_calculation(), 2))


def input_number(text):
    while True:
        int_text = input(text)
        if int_text.isdigit():
            result = float(int_text)
            if result > 0:
                break
        else:
            print('Сумма должна быть положительным числом')
    return result


amount_money = input_number('Введите имеющуюся сумму денег: ')
worth_apartment = input_number('Введите стоимость квартиры: ')
worth_car = input_number('Введите стоимость машины: ')
worth_countryhouse = input_number('Введите стоимость дачи: ')

tax_apartment = Apartment(worth_apartment)
tax_car = Car(worth_car)
tax_countryhouse = CountryHouse(worth_countryhouse)
print()
print(tax_apartment)
print(tax_car)
print(tax_countryhouse)

summa_tax = tax_apartment.tax_calculation() + tax_car.tax_calculation() + tax_countryhouse.tax_calculation()
if amount_money < summa_tax:
    print('Для уплаты налога вам нехватает: {}'.format(summa_tax - amount_money))