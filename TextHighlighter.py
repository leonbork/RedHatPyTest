import re


class BColors:
    HEADER = '\033[95m'
    WARNING = '\033[93m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


def txt_highlighter(alltxt, searchtxt):
    txt = re.search(searchtxt, alltxt)
    span = txt.span()
    start = span[0]
    end = span[1]
    result = alltxt[:start] + BColors.WARNING + alltxt[start:end] + BColors.ENDC + alltxt[end:]
    return result


def txt_underscore(alltxt, underscoretxt):
    txt = re.search(underscoretxt, alltxt)
    span = txt.span()
    start = span[0]
    end = span[1]
    result = alltxt[:start] + BColors.UNDERLINE + alltxt[start:end] + BColors.ENDC + alltxt[end:]
    return result


def liner(alltxt, searchtxt):
    for line_i, line in enumerate(alltxt.splitlines()):
        txt = re.search(searchtxt, line)
        if txt:
            span = txt.span()
            start = span[0]
            end = span[1]
            print('Matching Lines: ' + str(line_i) + ":" + str(start) + ":" + str(end))


def main():
    print (txt_highlighter('Lorem Ipsum---', '---'))
    print(txt_underscore('Lorem ipsum dolor sit amet, -- consectetur adipiscing elit.','--'))
    liner('Quisquse ultricies\nimperdiet arcu\nornare lobortis lacus lobortis at', 'us')


if __name__ == "__main__":
    main()
