# def select(input_func):
#     def output_func():
#         print("*******************")
#         input_func()
#         print("*******************")
#
#     return output_func
#
#
# @select
# def hello():
#     print("Hello zero-to-hero.dev")
#
#
# hello()
def check(input_func):
    def output_func(*args):
        result = input_func(*args)
        if result < 0:
            result = 0
        return result

    return output_func


@check
def sum(a, b):
    return a + b


result = sum(10, 20)
print(result)
result = sum(10, -20)
print(result)