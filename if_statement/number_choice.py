import random

count = 0
number = random.randint(1, 99)
print("1, 99 까지 제가 생각한 숫자를 맞춰 보세요")

while count < 10:
    count += 1
    user_input = int(input("몇일까요? : "))
    if user_input == number:
        break
    if user_input < number:
        print("너무 낮은 숫자 입니다.")
    if user_input > number:
        print("너무 큰 숫자 입니다.")

if user_input == number:
    print("성공!! 제가 생각하는 숫자는 {}가 맞습니다.".format(number))
else:
    print("실패!! 제가 생각하는 숫자는 {}가 입니다.".format(number))
