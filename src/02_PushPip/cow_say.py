import argparse
import cowsay

# in the future can be to add following options
# --verbose -v
# --help -h - default exist
# --version

# todo: rewrite help from https://pypi.org/project/python-cowsay/
# todo: not processed cowfile argument in source code

# reminder
# distinguish const, default parameters in add_argument !!!

# docs:
# 1 https://linux.die.net/man/1/cowsay
# 2 https://pypi.org/project/python-cowsay/

parser = argparse.ArgumentParser(description="cowsay console wrapper used argparse packet",
                                 prog="cowsay argparse script",
                                 usage="hard to describe why it need to you",
                                 add_help=True, # --help, -h
                                 epilog="output in console text before help by any accepted argument",
                                 )

parser.add_argument("message", type=str, action='store', help='the message to be displayed')
parser.add_argument("--cow", type=str, action='store', help='use -f to know available cows can be found by calling list_cows', default='default',
                    choices=cowsay.list_cows(), nargs='?') # if specify the const par, then --cow without value seem strange
parser.add_argument("-l", "--list_cows", action='store_true', help='available cows can be found by calling list_cows')
parser.add_argument('-e', '--eyes', '--eye_string', help='-e or --eye_string')
parser.add_argument('-T', '--tongue', '--tongue_string', help='-T or --tongue_string')
parser.add_argument('-W', '--width', '--column', help='-W or --width', type=int)
parser.add_argument('--wrap_text', action='store', type=bool, help='--wrap_text')
parser.add_argument('-n', action='store_true')
parser.add_argument('-f', '--cowfile', help='a string containing the cow file text (chars are not'
    ' decoded as they are in read_dot_cow) if this parameter is provided the'
    ' cow parameter is ignored',default=None,type=str)
parser.add_argument('--random', action='store_true', help='If provided, picks a random cow from the COWPATH.'
        '\nIs superseded by the -f option')
# parser.add_argument('-h', '--help', action='store_true', help='execute print_help method')
parser.add_argument('--usage', action='store_true', help='execute print_usage method')

for cow_customization in cowsay.COW_OPTIONS:
    parser.add_argument('-{}'.format(cow_customization), action='store_true', help='customize tongue and eyes from the box')

args = parser.parse_args()
print(args)
#
# if args.list_cows:
#     print('list of available cows is: ', cowsay.list_cows())


# if args.help:
#     parser.print_help()
if args.usage:
    parser.print_usage()


# exist debuging options: --list_of_cows and another
# cowsay.cowsay(args.message, )
# {action: getattr(action, 'dest') for action in parser._actions if action.option_strings}
# [param_name for param_name in args.__dict__ if ]

# cowsay.cowsay()

# if args.random:
#     cow = cowsay.get_random_cow()
#     if args.cow !=
# todo: finish it

parser.exit()
