import xml.etree.ElementTree as et
import random

tree = et.parse("saves.xml")
root = tree.getroot()


def insert():
    new_element = et.Element(str(input('Word')))
    new_element.text = str(input('Definition'))
    root.append(new_element)
    tree.write("saves.xml")


def view(times):
    for n in range(times - 5, times):
        try:
            print(root[n].tag, '\t''-''\t', root[n].text)
        except:
            print('no more words')
            return
    opt = str(input('To view more enter "y" to exit enter "n"'))
    if opt == 'y':
        view(times + 5)
    if opt == 'n':
        return


def quiz():
    def set_answer(n):

        answers = []
        order = [n]
        random_list(order, 4)
        random.shuffle(order)

        for ans in range(0, 4):
            answers.append(root[order[ans]].text)

        return answers

    def random_list(order, no_of_choices):
        while len(order) < no_of_choices:
            num = random.randint(0, int(len(list(root))) - 1)
            if num not in order:
                order.append(num)
        return order

    def run(li: list, score, attempt):

        n = random.randint(0, int(len(list(root))) - 1)
        if n not in li:
            print(root[n].tag)
            answers = set_answer(n)
            ans = input(
                '1.' + answers[0] + '\n' +
                '2.' + answers[1] + '\n' +
                '3.' + answers[2] + '\n' +
                '4.' + answers[3] + '\n'
            )
            li.append(n)
            if answers[int(ans) - 1] == root[n].text:
                print('correct')
                score = score + 1
            else:
                print('incorrect')
        opt = input('to continue press "y" or Press "n" to exit')
        if opt == 'y':
            attempt = attempt + 1
            try:
                run(li, score, attempt)
            except:
                print('somthing went wrong')
        elif opt == 'n':
            print('YOUR SCORE IS', score, '\n' + 'PERCENTAGE =', (score / attempt) * 100, '%')
            return
        else:
            print('somthing went wrong')

    run([], 0, 1)


def main_menu():
    opt = input('1.ADD NEW WORDS\n2.QUIZ\n3.VIEW ALL\n4.EXIT\n')
    if opt == '1':
        insert()
    elif opt == '2':
        quiz()
    elif opt == '3':
        view(5)
    elif opt == '4':
        exit()
    else:
        print('invalid argument')
    main_menu()


main_menu()
