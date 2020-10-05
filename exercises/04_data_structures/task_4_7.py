# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"
mac_split = mac.split(":")
macb1 = str(bin(int(mac_split[0],16)))
macb2 = str(bin(int(mac_split[1],16)))
macb3 = str(bin(int(mac_split[2],16)))
macbstr = macb1.replace("0b","")+macb2.replace("0b","")+macb3.replace("0b","")
print (macbstr)
