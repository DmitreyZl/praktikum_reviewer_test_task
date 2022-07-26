import datetime as dt


class Record:
    # отсутствует документирование класса
    # """
    # Класс записей для класса Calculator
    # """

    # отсутствует аннотация типов метода
    # def __init__(self, amount: float, comment: str, date: str = None) -> None:
    def __init__(self, amount, comment, date=''):
        # отсутствует документирование метода
        # """Инициализатор класса Record
        #
        # Args:
        #     amount (float): денежная сумма или количество килокалорий
        #     comment (str): комментарий, поясняющий, на что потрачены деньги
        #       или откуда взялись калории.
        #     date (str, optional): дата создания записи. Значение по
        #       умолчанию — текущая дата.
        # """
        self.amount = amount

        # код отформатирован не по PEP8
        # можно исправить так:
        # if date is not None:
        #     self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        # else:
        #     self.date = dt.datetime.now().date()
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


# отсутствует документирование класса
class Calculator:
    # отсутствует аннотация типов метода
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    # отсутствует аннотация типов метода
    def add_record(self, record):
        self.records.append(record)

    # отсутствует аннотация типов метода
    def get_today_stats(self):
        today_stats = 0
        # Не соответствует PEP8
        # 1) Record уже используется для имени класса
        # 2) Переменные именуются с маленькой буквы
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                # можно упростить
                # today_stats += record.amount
                today_stats = today_stats + Record.amount
        # в задании просят округлять до сотых, вероятно нужно так:
        # return "%.2f" % today_stats
        return today_stats

    # отсутствует аннотация типов метода
    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            # В python скобки для условия if не нужны, к тому же можно упростить
            # if 7 > (today - record.date).days >= 0:
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


# отсутствует документирование класса
class CaloriesCalculator(Calculator):
    # отсутствует аннотация типов метода
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        # не верно оформлено документирование метода
        # """Метод получает остаток калорий на сегодня
        #
        # Args:
        #    None
        # """

        # Переменные должны быть названы в соответствии с их смыслом
        # об этом говориться в PEP и в требованиях к заданию
        # Например: calories_balance
        x = self.limit - self.get_today_stats()
        if x > 0:
            # В требованиях к коду написано - "Бэкслеши для переносов не применяются"
            # Нужно вернуть результат с точностью до сотых
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        # else и скобки не нужны, если мы попали в if, то return уже произошел
        else:
            return('Хватит есть!')


# отсутствует документирование класса
class CashCalculator(Calculator):
    # PEP требует давать lowercase имена переменным
    # usd_rate и euro_rate
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    # В условии написано, что данный метод принимает только строку кода валюты
    # USD_RATE и EURO_RATE переменные класса, они и так находятся в области
    # видимости меода, не нужно их передавать
    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        # лишняя переменная, можно и дальше использовать currency
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()

        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            # тут ошибка cash_remained /= 1.00
            cash_remained == 1.00
            currency_type = 'руб'
        # блоки кода следует отделять пустой строкой
        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:

            # В требованиях к коду написано - "Бэкслеши для переносов не применяются"
            # Лишняя пустая строка
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    # Судя по заданию предполагается вывод статистики в
    # определенной валюте в методах get_today_stats и get_week_stats
    # Реализация указанных методов отсуствует
    # Необходимо дописать методы get_today_stats и get_week_stats
    def get_week_stats(self):
        # отсутствует переход на новую строку в конце файла
        # переход необходим согласно стандарту PEP8
        # В требованиях к коду написано
        # Исполняемый код в .py-файлах должен быть закрыт конструкцией
        # if __name__ == ‘__main__’
        super().get_week_stats()
