import json
import fileinput
import sys
import itertools

def output(stem, meaning, examples, origin):
    output_dict = {'question': 'Stem: {}\nExamples: {}\nOrigin: {}\n'.format(stem, examples, origin),
                   'answer': meaning}
    return output_dict

if __name__ == '__main__':
    output_array = []
    with open(sys.argv[1]) as f:
        try:
            while True:
                bits = list(itertools.islice(f, 0, 4))
                if len(bits) == 0:
                    break
                (stem, meaning, examples, origin) = bits
                output_array.append(output(stem, meaning, examples, origin))
        except StopIteration:
            pass
        print json.dumps(output_array, indent=4)
