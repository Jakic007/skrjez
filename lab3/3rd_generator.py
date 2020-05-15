import argparse
import random
import os
from math import floor, ceil

# Author: Kristijan Ceple

names = [
    'Marko', 'Ante', 'Pero', 'Matija', 'Senka', 'Anastasija', 'Ana', 'Marija', 'Anamarija',
    'Nikolija', 'Stanija', 'Nikolina', 'Nikola', 'Marijana', 'Cecilija', 'Dragoslav', 'Hrvoje',
    'Jan', 'Ivica', 'Ivan', 'Marin', 'Frano', 'Izabela', 'Izet', 'Sanja'
]

surnames = [
    'Ibrahimovic', 'Peric', 'Ivic', 'Nuic', 'Keric', 'Skriptic', 'Vladislavljevic', 'Snur',
    'Snajder', 'Pusic', 'Selenic', 'Radisavljevic', 'Misic', 'Epiric', 'Veneric', 'Icinic',
    'Frajeric', 'Wojtek', 'Zezek', 'Tutek', 'Isafek', 'Domazet', 'Senehos', 'Krznaric'
]


def generate_students(to_ret_num: int):
    to_ret = {}

    to_add_names = random.choices(names, k=to_ret_num)
    to_add_surnames = random.choices(surnames, k=to_ret_num)

    for (surname, name) in zip(to_add_surnames, to_add_names):
        # Generate JMBAG now
        suffix = [random.randint(0, 9) for _ in range(6)]
        jmbag: str = '0036' + ''.join(map(str, suffix))
        if jmbag in to_ret.keys():
            jmbag = '0036' + ''.join(map(str, suffix))  # Re-generate the jmbag

        to_ret[jmbag] = {
            'surname': surname,
            'name': name
        }

    return to_ret


random.seed()  # Initialise the Mersenne twister
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir", type=str,
                    help="Name of directory where the files will be saved to. Defaults to 3rd_asg_def.",
                    default="3rd_asg_def")
parser.add_argument("-s", "--students_num", type=int,
                    help="Number of students. Defaults to 50",
                    default=50)
parser.add_argument("-l", "--labs_num", type=int,
                    help="Number of laboratories. Defaults to 4.",
                    default=4)
parser.add_argument("-g", "--groups_num", type=int,
                    help="Number of lab groups. Defaults to 8.",
                    default=8)
parser.add_argument("-p", "--max_points", type=float,
                    help="Maximum number of points in a single lab. Defaults to 10",
                    default=10)
parser.add_argument("-gs", "--students_max_in_group", type=int,
                    help="Maximum number of students in a single group. Defaults to ceil(students_num/groups_num)",
                    default=0)
parser.add_argument("-e", "--errors", action="store_true",
                    help="Will generate multiple students in the same lab group"
                         "(this should cause the assignment to malfunction)")
args = parser.parse_args()

if args.students_max_in_group > args.students_num:
    raise ValueError("More students in a group than total number of students!")
if args.students_max_in_group <= 0:
    args.students_max_in_group = ceil(args.students_num/args.groups_num)


students = generate_students(args.students_num)

# First need to create the director if it doesn't already exist
if not os.path.exists(args.dir):
    os.mkdir(args.dir)

# Write students
with open(args.dir + '/studenti.txt', 'w') as students_file:
    for (jmbag, stud_data) in students.items():
        # to_write = ' '.join(student)
        to_write = ' '.join((jmbag, stud_data['surname'], stud_data['name']))
        students_file.write(to_write)
        students_file.write('\n')

# Create labs
for lab in range(1, args.labs_num + 1):
    jmbags_draw_from = list(students.keys())
    stud_lab_sum = 0

    for group in range(args.groups_num):
        # First pick a random amount of students
        if group != args.groups_num - 1:
            how_many = min(len(jmbags_draw_from),
                            random.randint(int(args.students_max_in_group * 0.75), args.students_max_in_group))
            stud_lab_sum += how_many
        else:
            # Last group, pick up the left overs
            how_many = args.students_num - stud_lab_sum

        students_jmbags = []
        if not args.errors:
            students_jmbags = random.sample(jmbags_draw_from, how_many)
            for element in students_jmbags:
                jmbags_draw_from.remove(element)
        else:
            students_jmbags = random.sample(jmbags_draw_from, how_many)

        write_file_name = 'Lab{:02d}_g{:02d}.txt'.format(lab, group)
        with open(args.dir + '/' + write_file_name, 'w') as write_file:
            for jmbag in students_jmbags:
                points = random.random() * args.max_points
                to_write = ' '.join((jmbag, str(round(points, 1))))
                write_file.write(to_write)
                write_file.write('\n')

# All done
print("Generation done!")
