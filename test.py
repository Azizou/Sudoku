import os,sys

wrapper = """def assertWrapper(func):
    try:
        func()
    except AssertionError:
        print('F',end='')
    """
def generate_wrapped_test():
    filename = sys.argv[1]
    _file = open(filename + '.py',"r")
    tests = []
    for line in _file:
        if line.startswith('def '):
            tests.append(line[4:-4])

    outfile = 'wrapper_'+filename + '.py'
    output = open(outfile,'w')
    output.write('from ' + filename + ' import *\n\n')
    output.write(wrapper)
    output.write('\ndef main():\n')
    for line in tests:
        print('    assertWrapper('+line+')',file=output)
    print('main()',file=output)



generate_wrapped_test()
