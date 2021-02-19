import sys


def validate(string):
    pair_symbols = {'(': ')', '[': ']', '{': '}'}
    result = True
    queue = []
    
    for i, s in enumerate(string):
        if pair_symbols.get(s):
            queue.append(s)
        else:
            if queue and pair_symbols.get(queue[-1]) == s:
                queue.pop()
            else:
                result = False
    return result


def main(argv):
	string = argv[0]
	print(validate(string))


if __name__ == '__main__':
#	for param in sys.argv:
#		print(param)
	arg = sys.argv[1:]
	if len(arg) != 1:
		sys.exit('Input must be without spaces')
	else:
		main(arg)