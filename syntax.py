print('hello world')

# 변수 :
# 자료형 : 숫자형, 문자열
# number 와 string은 더할 수 없다

a = 2
b = 3

# str(a) - 숫자형 => 문자형으로 변환

first_name = 'ye seul'
last_name = 'kim'

# 변수 이름 : camelCase, underscore

# List형
# - Zero based
# - Array와 같음

print(first_name+last_name);

a_list = ['사과','감','배',['작은사과','작은배']]

print(a_list[1])
print(a_list[3][0])

a_list.append('수박') # .push()와 같음

# Dictionary형
# - Object와 같음

a_dict = {
    'name' : 'kim',
    'age' : 25
}

a_dict['height']=178

friend_list = ['lee','park','choi']

a_dict['friends']= friend_list

print(a_dict['friends'])

# 조건문
# 띄어쓰기(tab)을 통해 if문 내용인지 알 수 있다.

age = 24

if age > 20:
    print('성인')
else:
    print('청소년')

# 반복문
# for(파라미터)in(변수)

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
count = 0
for fruit in fruits:
    if fruit == '사과':
        count +=1;

print(count)

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    if person['age']>20:
        print(person['name'])

# 파이썬의 내장함수
# 문자열 쪼개기

myemail = 'kim@email.com'

# result = myemail.split('@')

# 문자 변경하기
result = myemail.replace('email','email2')

print(result)