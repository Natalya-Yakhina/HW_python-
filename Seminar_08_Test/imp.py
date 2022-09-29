def impo(some_person):
    with open('base.txt', 'a', encoding='utf-8') as f:
        f.write(some_person + '\n')