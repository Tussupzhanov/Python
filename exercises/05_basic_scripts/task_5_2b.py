# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv
input_ip = argv[1]
a = input_ip.split("/")
ip = a[0].split(".")
ip1 = int(ip[0])
ip2 = int(ip[1])
ip3 = int(ip[2])
ip4 = int(0)
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

