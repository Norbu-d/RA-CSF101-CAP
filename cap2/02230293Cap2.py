################################
# norbu Dhendup
# SWE
# 02230293
################################
# REFERENCES
# Links that you referred while solving 
# the problem
# http://link.to.an.article/video.com 
################################
# SOLUTION
# Your Solution Score:6474
# Task 1: 6474
# Task 2: 2519
################################

def read_input():
    filename = "cap2/input_3_cap2.txt" 
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def parse_line(line):
    return [[int(num) for num in range_.split('-')] for range_ in line.strip().split(', ')]

def task_1(lines):
    total_people = len(lines) * 2
    total_overlaps = 0

    for line in lines:
        spaces = parse_line(line)
        for i in range(len(spaces)):
            for j in range(i + 1, len(spaces)):
                if max(spaces[i][0], spaces[j][0]) <= min(spaces[i][1], spaces[j][1]):
                    total_overlaps += 1

    print(f"There were {total_people} people assigned and there are {total_overlaps} of overlapping space assignments")

def task_2(lines):
    total_overlaps = 0

    for line in lines:
        spaces = parse_line(line)
        for i in range(len(spaces)):
            for j in range(i + 1, len(spaces)):
                if spaces[i][0] <= spaces[j][0] and spaces[i][1] >= spaces[j][1]:
                    total_overlaps += 1

    print(f"There were {total_overlaps} assignments that overlap completely")

if __name__ == "__main__":
    lines = read_input()
    task_1(lines)
    task_2(lines)