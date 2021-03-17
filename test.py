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
def title(arg):
    title_status = arg

    if (title_status < 10):
        return 'まだ大丈夫'
    else:
        return 'やばい'

# print(title(12))


# list
title_list = ['title_small', 'title_medium', 'title_large']
# print(title_list[0])


# for
# for index in range(11):
#     print(title(index))

for item in title_list:
  print(item)