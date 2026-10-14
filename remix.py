#!/usr/bin/env python3

from calico_lib import Contest, run_cli
from calico_lib import judge_api
from calico_lib.cli import set_contest_id
from calico_lib.config import load_secrets
from calico_lib.contest import link_external_problem

load_secrets()
# c = Contest('fa', '25')
# c.create_contest('Remix')

problems = [
        ('gta6_main', 1),
        ('caliconstruction_final_main', 1),
        ('circle_final_main', 1),
        ('circle_final_bonus', 3, 'b1'),
        ('bridge_final_main', 2),
        ('bridge_final_bonus', 2, 'b1'),
        ('reservoir_final_main', 2),
        ('reservoir_final_bonus', 3, 'b1'),
        ('debt_main', 2),
        ('gates_final_main', 3),
        ('gates_final_bonus', 3, 'b1'),
        ('boxcars_main', 3),
        ('boxcars_bonus', 3, 'b1'),
        ('cylinder_updated', 4),
        ('fries_main', 2),
        ('fries_bonus', 3, 'b1'),
        ('fries_bonus2', 4, 'b2'),

        # ('berkeleytime_main',  1),
        # ('doubleit_final_main',  1),
        # ('quickstack_main',  1),
        # ('quickstack_bonus',  2, 'b1'),
        # ('stickdrift_final_main', 2),
        # ('sausages_main',  2),
        # ('sausages_bonus_1',  2, 'b1'),
        # ('sausages_bonus_2',  3, 'b2'),
        # ('sausages_bonus_3',  4, 'b3'),
        # ('tower_main', 3),
        # ('tower_bonus', 3, 'b1'),
        # ('explorer_final_main', 3),
        # ('explorer_final_bonus', 3, 'b1'),
        # ('cylinder_updated', 4),
        # ('vector_final_main', 4),
        ]

i = 0

for p in problems:
    if len(p) < 3:
        i += 1
        tag = str(i)
    else:
        tag = str(i) + p[2]
    link_external_problem('remix-sp26', p[0], tag, p[1])
