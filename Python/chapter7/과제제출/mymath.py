pi = 3.14

#반지름 입력
def input_radius():
    try:
        value = input('반지름을 입력하세요: ')
        return float(value)

    except ValueError:
        print('잘못된 값을 입력하였습니다.')
        
#높이 입력
def input_height():
    try:
        height = input('높이를 입력하세요: ')
        return float(height)

    except ValueError:
        print('잘못된 값을 입력하였습니다.')    

#원의 넓이
def circle_area(radius):
    return pi * radius * radius

#원기둥 부피
def cylinder_vol(radius,height):
    return pi * radius * radius * height