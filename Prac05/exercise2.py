__author__ = 'jc443852'

a_string = input('text:')
word_list = a_string.split()

count_dict = {}
for word in word_list:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
print(count_dict)

for key,value in count_dict.items():
  print(key,value)