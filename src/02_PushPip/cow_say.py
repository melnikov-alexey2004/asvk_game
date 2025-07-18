import argparse
import cowsay

# in the future can be to add following options
# --verbose -v
# --help -h - default exist
# --version

# todo: rewrite help from https://pypi.org/project/python-cowsay/
# todo: not processed cowfile argument in source code
# todo: how --version -v control output

# reminder
# distinguish const, default parameters in add_argument !!!

# docs:
# 1 https://linux.die.net/man/1/cowsay
# 2 https://pypi.org/project/python-cowsay/

parser = argparse.ArgumentParser(description="cowsay console wrapper used argparse packet",
                                 prog="cowsay argparse command line script",
                                 usage="fast run cowsay with good support of additional options",
                                 add_help=True, # --help, -h
                                 epilog="output in console text before help by any accepted argument",
                                 formatter_class=lambda prog: argparse.HelpFormatter(prog, width=60)
                                 )


parser.add_argument("message", type=str, action='store', help='the message to be displayed')

info_group = parser.add_argument_group("informative options", "only debugging output in console without running cowsay")
info_group.add_argument("-l", "--list_cows", action='store_true', help='available cows can be found by calling list_cows')
parser.add_argument('--usage', action='store_true', help='execute print_usage method')
parser.add_argument('--version', action='version', help='get current version', version='%(prog)s v1.0.0') # alias for prog parameter
parser.add_argument('--verbose', action='store_true', help='display cow name and where is located (absolute path to file)')

text_group = parser.add_argument_group("text display setting", "customize output")
text_group.add_argument('-W', '--width', '--column', help='-W or --width', type=int, dest='width')
text_exc_group = text_group.add_mutually_exclusive_group()
text_exc_group.add_argument('--wrap_text', action='store_true', help='wrap text or not')
# -n from https://linux.die.net/man/1/cowsay
text_exc_group.add_argument('-n', action='store_const', default=True, const=False,
                    help='control wrap text if length in line > width option. if specified then without it') # related with wrap text, is implementation of yet existing action="store_false" or se action='count' with additional logic

cow_groups = parser.add_argument_group('cow customization', description='options that control how the entity will look')
cow_exc_groups = cow_groups.add_mutually_exclusive_group()
cow_exc_groups.add_argument("--cow", type=str, action='store', help='use -f to know available cows can be found by calling list_cows', default='default',
                    choices=cowsay.list_cows(), nargs='?') # if specify the const par, then --cow without value seem strange
cow_exc_groups.add_argument('-f', '--cowfile', help='a string containing the cow file text (chars are not'
    ' decoded as they are in read_dot_cow) if this parameter is provided the'
    ' cow parameter is ignored', default=None, type=str)
cow_exc_groups.add_argument('--random', action='store_true', help='If provided, picks a random cow from the COWPATH.'
        '\nIs superseded by the -f option')

cow_opt_group = parser.add_argument_group('cow options', 'use yet prepared tongue and eyes from the box')

cow_opt_exc_group = cow_opt_group.add_mutually_exclusive_group()
for cow_customization, fill_option in cowsay.COW_OPTIONS.items():
    cow_opt_exc_group.add_argument(f"-{cow_customization}", action='store_true',
                               help=f'eyes={fill_option.eyes}, tongue={fill_option.tongue}')

cow_opt_group.add_argument('-e', '--eyes', '--eye_string', help=f'-e or --eye_string, by default is {cowsay.Option.eyes}', default=cowsay.Option.eyes)
cow_opt_group.add_argument('-T', '--tongue', '--tongue_string', help=f'-T or --tongue_string, by default is {cowsay.Option.tongue}', default=cowsay.Option.tongue)

args = parser.parse_args()
print(args)

#
# if args.list_cows:
#     print('list of available cows is: ', cowsay.list_cows())


# if args.help:
#     parser.print_help()


if args.usage:
    parser.print_usage()
    parser.exit()

if args.list_cows:
    print('list cows: ', cowsay.list_cows())
    parser.exit()

# exist debugging options: --list_of_cows and another
# cowsay.cowsay(args.message, )
# {action: getattr(action, 'dest') for action in parser._actions if action.option_strings}
# [param_name for param_name in args.__dict__ if ]

# cowsay.cowsay()

# if args.random:
#     cow = cowsay.get_random_cow()
#     if args.cow !=
# todo: finish it

# cowsay.cowsay(
#     args.message,
#     cow = args.cow,
#     # preset,
#     eyes = args.eyes,
#     tongue = args.tongue,
#     width = args.width,
#     wrap_text = args.
# )

parser.print_help()

parser.exit()
