## Шпаргалка по темам

[Подробнее темы рассматриваются в книге](https://pyneng.readthedocs.io/ru/latest/book/Part_I.html),
но на стадии подготовки к курсу, она может не понадобиться.

## Строки

Строка в Python это:

* последовательность символов, заключенная в кавычки
* неизменяемый упорядоченный тип данныхa

```python
line = 'Hello'
line = "Hello"
lines = "line1\nline2\nline3"

text = """long lines
line2
"""
```

Строки можно суммировать. Тогда они объединяются в одну строку:

```python
In [14]: intf = 'interface'

In [15]: tun = 'Tunnel0'

In [16]: intf + tun
Out[16]: 'interfaceTunnel0'

In [17]: intf + ' ' + tun
Out[17]: 'interface Tunnel0'
```

Строку можно умножать на число. В этом случае, строка повторяется
указанное количество раз:

```python
In [18]: intf * 5
Out[18]: 'interfaceinterfaceinterfaceinterfaceinterface'

In [19]: '#' * 40
Out[19]: '########################################'
```

Индексы, срезы

```python
In [20]: string1 = 'interface FastEthernet1/0'

In [21]: string1[0]
Out[21]: 'i'

In [22]: string1[1]
Out[22]: 'n'

In [23]: string1[-1]
Out[23]: '0'

In [24]: string1[0:9]
Out[24]: 'interface'

In [25]: string1[10:22]
Out[25]: 'FastEthernet'

In [26]:  string1[10:]
Out[26]: 'FastEthernet1/0'

In [27]: string1[-3:]
Out[27]: '1/0'
```

### Методы строк

#### join

```python
In [16]: numbers_as_str = ['10', '20', '30']

In [17]: ','.join(numbers_as_str)
Out[17]: '10,20,30'
```


#### lower

```python
In [25]: string1 = 'FastEthernet'

In [27]: string1.lower()
Out[27]: 'fastethernet'
```

#### startswith, endswith

```python
In [40]: string1 = 'FastEthernet0/1'

In [41]: string1.startswith('Fast')
Out[41]: True

In [42]: string1.startswith('fast')
Out[42]: False

In [43]: string1.endswith('0/1')
Out[43]: True

In [44]: string1.endswith('0/2')
Out[44]: False
```

#### replace

```python
In [45]: string1 = 'FastEthernet0/1'

In [46]: string1.replace('Fast', 'Gigabit')
Out[46]: 'GigabitEthernet0/1'
```


#### strip, rstrip, lstrip

По умолчанию метод strip() убирает пробельные символы. В этот набор
символов входят: ``\t\n\r\f\v``
Методу strip можно передать как аргумент любые символы.


```python
In [47]: string1 = '\n\tinterface FastEthernet0/1\n'

In [50]: string1.strip()
Out[50]: 'interface FastEthernet0/1'

In [51]: ad_metric = '[110/1045]'

In [52]: ad_metric.strip('[]')
Out[52]: '110/1045'
```

Метод strip убирает спецсимволы и в начале, и в конце строки. Если
необходимо убрать символы только слева или только справа, можно
использовать, соответственно, методы ``lstrip`` и
``rstrip``.

#### split

Метод ``split`` разбивает строку на части, используя как
разделитель какой-то символ (или символы) и возвращает список строк:

```python
In [53]: string1 = 'switchport trunk allowed vlan 10,20,30,100'

In [54]: commands = string1.split()

In [55]: print(commands)
['switchport', 'trunk', 'allowed', 'vlan', '10,20,30,100']

In [56]: vlans = commands[-1].split(',')

In [57]: print(vlans)
['10', '20', '30', '100']
```

