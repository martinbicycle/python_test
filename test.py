# Comment
# print("Hello World!")

# print("pythonのテスト")

# print("python 難しい"

# 演算
# print(1+1)
# print(1-1)
# print(2*2)
# print(10/2)
# print(5%3)

# 変数
# title = "20文字"
# title_length = 0
# title_times =  5.5

# print(type(title))
# print(type(title_length))
# print(type(title_times))

# title_problem = False
# print(title_problem)

# first_name = "太郎"
# last_name = "佐藤"
# full_name = last_name + first_name
# print(full_name)


# format文
# animal = 'cat'

# print('This is {}.'.format(animal))

# 条件分岐と関係演算子
# if else elif
# ==, !=, <, >, >=, <=

# if title != '10文字':
#   print('長い')

# if title_length > 6:
#   print('長い')
# elif title_length == 0:
#   print('無い')
# else:
#   print('短い')

# 関数
# def title(arg):
#     title_status = arg

#     if (title_status < 10):
#         return 'まだ大丈夫'
#     else:
#         return 'やばい'

# print(title(12))


# list
title_list = ['title_small', 'title_medium', 'title_large']
# print(title_list[0])
for index, lis in enumerate(title_list):
    print(index, ':', lis)


# for
# for index in range(11):
#     print(title(index))

# for item in title_list:
#   print(item)

# with
# open()
# with open('./title.txt', 'r') as file:
#   print(file.read())

# while文
# time = 60
# while time > 0:
#     print('残り', time, '秒')
#     time -= 1

# print('試合終了')


# classとインスタンス
# class Card:
#     def __init__(self, date, user_name):
#         self.date = date
#         self.user_name = user_name

#     def message(self):
#         return 'この投稿は' + self.user_name + 'さんが' + self.date + 'に投稿しました'


# date_a = '2021-01-01'
# user_name_a = 'Taro'

# card_a = Card(date_a, user_name_a)

# date_b = '2021-01-03'
# user_name_b = 'risa'
# card_b = Card(date_b, user_name_b)

# print(card_b.message())

# import
# import math
# print(math.pi)

# import numpy

# numpy_list = [3, 1, 5, 10, 2093, 304, 103]
# print(numpy.sum(numpy_list))
