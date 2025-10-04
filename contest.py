from calico_lib import Contest
from calico_lib.judge_api import set_user
import argparse


parser = argparse.ArgumentParser(
        prog='CALICO contest creation CLI',
        description='CLI to create contest. Actually, it\'s just for auth',
        epilog='')
parser.add_argument('-a', '--auth', help='Username and password for judge, separated by colon.')

args = parser.parse_args()
if args.auth is not None:
    set_user(tuple(args.auth.split(':')))

c = Contest('fa', '25')
c.create_testing_contest()
