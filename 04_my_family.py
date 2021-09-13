#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)

my_family = ['Mother', 'Father', 'Brother', 'I\'m']
Mother = my_family[0]
Father = my_family[1]
Brother = my_family[2]
im = my_family[3]


# список списков приблизителного роста членов вашей семьи

my_family_height = [[Mother, 165], [my_family[0], 165], [Father, 180], [Brother, 175]]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

print(my_family_height[2])
print(my_family_height[1])
print(my_family_height[0])

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print(my_family_height[0][1] + my_family_height[1][1] +my_family_height[2][1] +my_family_height[3][1])