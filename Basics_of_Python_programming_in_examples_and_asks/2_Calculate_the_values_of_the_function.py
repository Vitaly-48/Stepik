result = 3.141569
n = 10

print("R=%4.2f, n=%3d" % (result, n))
print("R=%4.2f, n=%3.1f" % (result, n))
print("R=%6.5f, n=%2d" % (result, n))
print("R=%5d, n=%4d" % (result, n))
# error print("R=%6.5, n=%2d" % (result, n))


import math

# t = 3.5
def f_x(x):
   try:
       y = 1 / (x+1) + x / (x-3)
   except:
       y = math.inf
   return y

t = float(input("t = "))
y = f_x(t)
print("f(", t, ") = ", y)
# f( 3.5 ) =  7.222222222222222
print("%8d" %(y)) # целое число размещается в 8 позициях, прижато к правому краю.
# 7


# t = 3.5
def f_x(x):
   try:
       y = 1 / (x+1) + x / (x-3)
   except:
       y = math.inf
   return y

t = float(input("t = "))
y = f_x(t)
print("f(", t, ") = ", y)
#  f( 3.5 ) =  7.222222222222222
print("%-8d" %(y)) # целое число размещается в 8 позициях, прижато к левому краю.
# 7


# t = 3.5
def f_x(x):
   try:
       y = 1 / (x+1) + x / (x-3)
   except:
       y = math.inf
   return y

t = float(input("t = "))
y = f_x(t)
print("f(", t, ") = ", y)
# f( 3.5 ) =  7.222222222222222
print("%8.4f" %(y)) # вещественное число размещается в 8 позициях, выводится 4 знака после запятой,
# прижато к правому краю, # незаполненные позиции после запятой заполняются 0.
# 7.2222


# t = 3.5
def f_x(x):
   try:
       y = 1 / (x+1) + x / (x-3)
   except:
       y = math.inf
   return y

t = float(input("t = "))
y = f_x(t)
print("f(", t, ") = ", y)
#  f( 3.5 ) =  7.222222222222222
print("%-8.4f" %(y)) # вещественное число размещается в 8 позициях, выводится 4 знака после запятой,
# прижато левому краю, незаполненные позиции после запятой заполняются 0.
# 7.2222


# t = 3.5
def f_x(x):
   try:
       y = 1 / (x+1) + x / (x-3)
   except:
       y = math.inf
   return y

t = float(input("t = "))
y = f_x(t)
print("f(", t, ") = ", y)
#  f( 3.5 ) =  7.222222222222222
print("%8s" %(y)) # если длина строки меньше 8 символов, то она размещается в 8 позициях,
# прижата к правому краю, в противном случае формат не учитывается.
# 7.222222222222222


# t = 3.5
def f_x(x):
   try:
       y = 1 / (x+1) + x / (x-3)
   except:
       y = math.inf
   return y

t = float(input("t = "))
y = f_x(t)
print("f(", t, ") = ", y)
# f( 3.5 ) =  7.222222222222222
print("%-8s" %(y)) # если длина строки меньше 8 символов, то она размещается в 8 позициях,
# прижата к левому краю, в противном случае формат не учитывается.
# 7.222222222222222


# 4.5
def f_x(x):
   y = 1 / (x+1) + x / (x-3)
   return y

t = 4.5
y = f_x(t)
print("f(", t, ") = ", y)
# 3.1818181818181817


# 1.8
t = float(input("t = "))
y = f_x(t)
print("f(", t, ") = ", y)
# -1.1428571428571428


# -3.5
t = float(input("t = "))
y = f_x(t)
print("f(", t, ") = ", y)
# 0.1384615384615384


"""блок try, где размещаются операторы, в которых может возникнуть ошибка;
блок except, в нем размещаются операторы, выполняемые при возникновении ошибок в блоке try."""
# 3 ZeroDivisionError: float division by zero
import math

def f_x(x):
   try:
       y = 1 / (x+1) + x / (x-3)
   except:
       y = math.inf
   return y

t = float(input("t = "))
y = f_x(t)
print("f(", t, ") = ", y)
# f( 3.0 ) =  inf


def f_x(x):
   try:
       y = 1 / (x+1) + x / (x-3)
   except:
       y = math.inf
   return y

t = float(input("t = "))
y = f_x(t)
print("f(", t, ") = ", y)
# f( 3.0 ) =  inf
print("%8.4f" %(y))