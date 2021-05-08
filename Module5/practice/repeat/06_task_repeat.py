# Написать функцию, определяющую кол-во дней в году.
# В обычном году 365 дней, а в високосном - 366. Каждый четвертый год является високосным,
# кроме столетий, которые не делятся нацело на 400.
# Если год не делится нацело на 4, значит сразу можно сделать вывод, что он не является високосным.
# Если все же делится, то надо исключить столетия: они все нацело делятся на 100, но те,
# которые не делятся нацело на 400, високосными не являются.

def days_in_year(num_year):
    pass
    return (num_year % 4 == 0 and num_year % 100 != 0) or num_year % 400 == 0
year = 2021
if days_in_year(year):
    print(f'В году {year} -  366 дней.')
else:
    print(f'В году {year} -  365 дней.')

