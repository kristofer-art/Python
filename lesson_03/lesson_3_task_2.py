from smartphone import Smartphone

catalog = []

catalog.append(Smartphone('Samsung', 'Galaxy S23', '+79001234567'))
catalog.append(Smartphone('Apple', 'iPhone 15', '+79012345678'))
catalog.append(Smartphone('Xiaomi', 'Redmi Note 13', '+79023456789'))
catalog.append(Smartphone('Honor', 'Magic 5', '+79034567890'))
catalog.append(Smartphone('HUAWEI', 'P60', '+79045678901'))

for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.phone_number}')
