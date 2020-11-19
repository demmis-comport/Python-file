#ch04ex02.py
#
#뺄셈 문제 만드는 함수 만들기


import random as r

def make_quiz():
    num1 = r.randint(10,20)
    num2 = r.randint(1,10)
    quiz = '{}-{}'.format(num1,num2)
    return quiz


for x in range(5):
    q = make_quiz()
    ans = eval(q)
    # 문제 출제

    usr_ans = int(input('{}='.format(q)))
    if usr_ans == ans:
        print('정답')
    else:
        print('오답! 답은 {}!'.format(ans))
