# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
input_ip = input ("Введите IP-сети: ")
a = input_ip.split("/")
ip = a[0].split(".")
ip1 = int(ip[0])
ip2 = int(ip[1])
ip3 = int(ip[2])
ip4 = int(ip[3])
mask = int(a[-1])
maskb = (mask*"1"+((32-mask)*"0"))
mask1 = int(maskb[0:8],2)
mask2 = int(maskb[8:16],2)
mask3 = int(maskb[16:24],2)
mask4 = int(maskb[24:32],2)

print (f'''
Network:
{ip1:<8} {ip2:<8} {ip3:<8} {ip4:<8}
{ip1:08b} {ip2:08b} {ip3:08b} {ip4:08b}

Mask:
/{mask:<1}
{mask1:<8} {mask2:<8} {mask3:<8} {mask4:<8}
{mask1:08b} {mask2:08b} {mask3:08b} {mask4:08b}
''')

