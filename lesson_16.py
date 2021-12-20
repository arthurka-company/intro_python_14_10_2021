# https://documenter.getpostman.com/view/1134062/T1LJjU52#4829d16f-0f4e-43ec-886e-68ebad1221d8

'''

python3 script_name.py dir_name value
python3 script_name.py -dir=dir_name -value=value
python3 script_name.py --d dir_name --v value

'''

# import sys
#
#
# if __name__ == '__main__':
#     print(sys.argv)
#
#     args = sys.argv
#
#     assert args[1] in ['test', 'prod', 'value']
#     if len(args) != 3:
#         print('Not enough args')
#         sys.exit()
#     print('Run')
#
#     # if os.path.isdir(value):
#     #     pass


import argparse


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Program args parser')
#     parser.add_argument('mode', type=str, help='Mode of the program')
#     parser.add_argument('value', type=int, help='Iterations')
#     parser.add_argument('--optional', type=int, help='Iterations default=5')
#     args = parser.parse_args()
#     print(args)
#     print(type(args))
#     print(args.mode, args.value, args.optional)

import click


@click.command()
@click.argument('mode', default='ttt')
def main(mode):
    print(mode)
    # pass


if __name__ == '__main__':
    main()
