#!/usr/bin/env python3

from datetime import datetime
from calico_lib import Contest, run_cli

import subprocess

def check_branch_up_to_date(branch: str):
    try:
        diff = subprocess.check_output(['git', 'diff', f'origin/{branch}', branch, '--']).decode()
    except subprocess.CalledProcessError as e:
        print(f'> Can not check branch {branch}... maybe it doesn\'t exist?')
        print(e)
        return
    return len(diff) == 0

def sync_branch(branch: str):
    print('Syncing branch...')
    subprocess.check_output(['git', 'checkout', branch, '--'])
    subprocess.check_output(['git', 'pull'])
    subprocess.check_output(['git', 'push'])

def main():
    problem_list = [
                    # TODO
                    ]
    all_branch = [p.problem_name for p in problem_list]

    subprocess.run(['git', 'fetch'], check=True)

    e = False
    merged_branch = subprocess \
            .check_output(['git', 'branch', '-a', '--merged']).decode().split('\n')
    merged_branch = [s.split(' -> ')[-1] for s in merged_branch]
    merged_branch = [s.strip('*').strip(' ') for s in merged_branch]
    # print(merged_branch)

    if not check_branch_up_to_date('main'):
        print('main not up to date with origin!')
        e = True
    for p in all_branch:
        if p not in merged_branch:
            print(f'{p} not merged!')
            e = True
        if f'remotes/origin/{p}' not in merged_branch:
            print(f'remotes/origin/{p} not merged!')
            e = True
        # if not check_branch_up_to_date(p):
        #     print(f'{p} not up to date with origin!')
        #     # sync_branch(p)
        #     e = True
    if e:
        return

    i = 0
    for p in problem_list:
        i += 1
        p.ordinal = i

    # problem_list = problem_list[4:]

    # c = Contest('calico-fa25-testing',
    #             "[Testing] CALICO Fall '25",
    #             problems = problem_list)
    c2 = Contest('calico-fa25-archive',
                "[Archive] CALICO Fall '25",
                problems = problem_list)
    c = Contest('calico-sp26',
                "CALICO Spring '26",
                 # datetime(2025, 11, 9, 4),
                 datetime(2026, 4, 11, 16), # bro it's 16 not 4
                 '3:00:00',
                 problems = problem_list)
    ct = Contest('calico-sp26-testing',
                "[Testing] CALICO Spring '26",
                 problems = problem_list)

    run_cli(ct)

main()
