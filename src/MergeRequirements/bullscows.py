from collections import Counter
import random
from urllib import request
import argparse
import os
import pprint
import cowsay

def bullscows(guess: str, secret: str) -> (int, int):
    bulls_count = sum(g==s for g,s in zip(guess, secret))
    cows_count = (Counter(guess) & Counter(secret)).total()
    return bulls_count, cows_count

def ask(prompt: str, valid: list[str] = None) -> str:
    # word = input(prompt)
    print(cowsay.cowsay(prompt, width=80, preset='w'))
    word = input('>>> ')

    if valid is not None:
        while word not in valid:
            # print('repeat input, word not in approved list')
            print(cowsay.cowsay('repeat input, word not in approved list', width=80, preset='d'))
            word = input(prompt)
    return word

def inform(format_string: str, bulls: int, cows: int) -> None:
    # print(format_string.format(bulls, cows))
    print(cowsay.cowsay(format_string.format(bulls, cows), width=80, preset='g'))



def gameplay(ask: callable, inform: callable, words: list[str], verbose: bool) -> int:
    secret = random.choice(words)
    if verbose:
        print('secret word is', secret)
    attempts_count = 0
    while True:
        guess = ask("Введите слово: ", words)
        attempts_count += 1
        b, c = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", b, c)
        if guess == secret:
            break
    return attempts_count

def run_game(words: list[str], verbose: bool):
    return gameplay(ask, inform, words, verbose)

def get_all_downloaded_vocab() -> dict[str, list]:
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, 'vocabs')
    vocabs = {'ru':  [], 'en': []}
    for vocab_file in os.listdir(path):
        fullname = os.path.join(path, vocab_file)
        with open(fullname, 'r', encoding='utf-8') as file:
            if file.readline().rstrip().isascii():
                vocabs['en'].append(fullname)
            else:
                vocabs['ru'].append(fullname)
    return vocabs

if __name__ == '__main__':
    import sys
    print(sys.path[0])
    print(os.getcwd())
    parser  = argparse.ArgumentParser()
    parser.add_argument('vocabulary', help='url address to download vocabulary or path to downloaded vocabulary', nargs='?')
    parser.add_argument('word_length', type=int, default=5, help='control the length of the guessed word', nargs='?')
    parser.add_argument('-v', '--verbose', action='store_true', help='get immediately secret word')
    parser.add_argument('-l', '--list-words', action='store_true', help='only get words from chosen vocabulary')

    voc_group = parser.add_argument_group('take random vocabulary from the box', 'choose only one options below and first argument to this script keep empty')
    voc_exc_group = parser.add_mutually_exclusive_group()
    voc_exc_group.add_argument('--random-ru', help='take random vocabulary with russian words', action='store_true')
    voc_exc_group.add_argument('--random-en', help='take random vocabulary with english words', action='store_true')

    vocabs = get_all_downloaded_vocab()

    args = parser.parse_args()

    if args.verbose:
        print('Set up mode with hint secret word to debugging')


    vocab = args.vocabulary
    if args.vocabulary is None:
        opt = 'en'
        if args.random_ru:
            opt = 'ru'
        vocab = random.choice(vocabs[opt])
        if args.verbose:
            print(f'use the random vocabulary with {"english" if opt == "en" else "russian"} words\nhis defined in dir "vocab" near script and located in {vocab}')

    # print(args)

    if os.path.exists(vocab) and os.path.isfile(vocab):
        temporary_file = False
        fp = vocab
        code = 'utf-8'
    else:
        temporary_file = True
        fp, headers = request.urlretrieve(args.vocabulary)
        code = headers.get_content_charset()

    with open(fp, 'r', encoding=code) as file:
        words = file.read().split('\n')
        if not words[-1]: words.pop(-1)
    if temporary_file: os.remove(fp)
    words = [w for w in words if len(w) == args.word_length]

    # parser.print_help()

    if args.list_words:
        pprint.pprint(", ".join(words), width=160)
        parser.exit()

    attempts_count = run_game(words, args.verbose)
    # print('count of attempts is {}'.format(attempts_count))
    print(cowsay.cowsay('YOU WIN\ncount of attempts is {}'.format(attempts_count), width=80, preset='w'))
    parser.exit()

