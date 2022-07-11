# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) # 5명이서 군인 할인 영화를 보러 갔을 때

# import theater_module as mv # 모듈 이름을 mv 로 대체

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import * # 함수 쓸때, 앞의 이름 붙일 필요 없음.
# # from random import *

# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning # 필요한 함수만 쓰고 싶다.
# price(3)
# price_morning(4)
# price_soldier(5)

from theater_module import price_soldier as price # 하나의 함수만 갖다 써도 as로 변형 시켜서 쓸 수 있음.
price(3)