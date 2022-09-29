def log_info(info):
    with open('base.txt', 'a', encoding='utf-8') as f:
        if len(info.split()) == 1:
            f.write(f'{info}' + '\n')
        else:
            f.write(f'{info}' + '\n')