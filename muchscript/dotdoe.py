
def load_dotdoe(doe_path=None):
    if doe_path is None:
        f = open('.doe', 'r')
    else:
        f = open(doe_path, 'r')

    text = f.read()
    lines = text.split('\n')

    dictionary = {}

    for line in lines:

        if line == '':
            pass
        else:
            variable = line.split(' > ')[0]
            content = line.split(' > ')[1]

            dictionary[variable] = content

    f.close()

    # print(lines)
    return dictionary
