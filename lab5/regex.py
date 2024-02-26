import re

#1

pattern1 = re.compile('^ab*')
print(pattern1.search('abbbbb'))

#2

pattern2 = re.compile('^ab{2,3}')
print(pattern2.search('abbb'))

#3

pattern3 = re.compile('([a-z]_)+[a-z]')
print(pattern3.search('a_a_a_a_aa'))

#4

pattern4 = re.compile('[A-Z]{1}[a-z]+')
print(pattern4.search('Akbtu'))

#5

pattern5 = re.compile('^a.*b$')
print(pattern5.search('a%4kb'))

#6

pattern6 = 'It is,my.code'
x = re.sub('[\s.,]',':',pattern6)
print(x)

#7

snake_case_string = 'there_is_my_code'
camel_case_string = re.sub('_[a-z]',lambda x: x.group(0)[1].capitalize(), snake_case_string)
print(camel_case_string)

#8

word = 'kbtuBestUniversity'
x = re.split('(?=[A-Z])',word)
print(x)

#9

word2 = 'HelloWorldOfWarcraft'
x = re.split('(?=[A-Z])',word2)
print(' '.join(x).strip())

#10

camel_string = 'thereIsMyCode'
snake_string = re.sub('[A-Z]', lambda x: '_'+x.group(0).lower(),camel_string)
print(snake_string)