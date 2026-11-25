from address import Address
from mailing import Mailing

to_address = Address('424000', 'Йошкар-Ола', 'ул. Ленина', '10', '25')
from_address = Address('101000', 'Москва', 'ул. Тверская', '1', '1')

my_mailing = Mailing(to_address, from_address, 350, 'TRACK123456RU')

print(
    f'Отправление {my_mailing.track} '
    f'из {my_mailing.from_address.index}, {my_mailing.from_address.city}, '
    f'{my_mailing.from_address.street}, {my_mailing.from_address.house} '
    f'- {my_mailing.from_address.apartment} '
    f'в {my_mailing.to_address.index}, {my_mailing.to_address.city}, '
    f'{my_mailing.to_address.street}, {my_mailing.to_address.house} '
    f'- {my_mailing.to_address.apartment}. '
    f'Стоимость {my_mailing.cost} рублей.'
)
