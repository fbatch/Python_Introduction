# №2 Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
a = int(input('Введите время в секундах:\n'))
hours = a // 3600
minutes = (a - hours * 3600) // 60
seconds = a - minutes * 60 - hours * 3600
if minutes < 10:
    minutes = '0' + str(minutes)
if hours < 10:
    hours = '0' + str(hours)
if seconds < 10:
    seconds = '0' + str(seconds)
print('{}:{}:{}'.format(hours, minutes, seconds))
