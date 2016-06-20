from test_ts import *

def assertWrapper(func):
    try:
        func()
    except AssertionError:
        print('F',end='')
    
def main():
    assertWrapper(test_two_words)
    assertWrapper(test_three_words)
    assertWrapper(test_list_of_words)
    assertWrapper(test_extract_decimal)
main()
