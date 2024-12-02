# Day2 - AoC 2024 


from tqdm import tqdm


# 1st Part
# Load data from file 
def load_data(file):
    with open(file) as f:
        data = f.readlines()
        data = [x.strip().split() for x in data]
        data = [[int(x) for x in y] for y in data]
    return data


# Check if all increasing or decresing
def is_monotonic(report):
    return all(x < y for x, y in zip(report, report[1:])) or all(x > y for x, y in zip(report, report[1:]))


# Check if all adjacent levels are within 3 / -3 
def check_adj_levels(lst):
    increasing = lst[1] > lst[0]
    for i in range(1, len(lst)):
        step = lst[i] - lst[i - 1]
        if increasing:
            if step > 3:
                return False
        else:
            if step < -3:
                return False
    return True


def run_part1():
    data = load_data('data/day2_input.txt')
    to_recheck = []
    count = 0
    for i in tqdm(iterable=range(len(data)), desc='Progress Report'):
        if is_monotonic(data[i]):
            if check_adj_levels(data[i]):
                count += 1
    print(count)


# 2nd Part 
def is_almost_monotonic(report):
    monotonic_sub_reports = []
    n = len(report)
    for i in range(n):
        sub_report = report[:i] + report[i+1:]
        if is_monotonic(sub_report):
            monotonic_sub_reports.append(sub_report)
    return monotonic_sub_reports

def is_almost_adj_levels(report):
    monotonic_sub_reports = []
    n = len(report)
    for i in range(n):
        sub_report = report[:i] + report[i+1:]
        if is_monotonic(sub_report):
            monotonic_sub_reports.append(sub_report)
    return monotonic_sub_reports


def run_part2():
    data = load_data('data/day2_input.txt')
    to_recheck_mono = []
    to_recheck_steps = []
    count = 0
    for i in tqdm(iterable=range(len(data)), desc='Progress Report 1 - Normal'):
        if is_monotonic(data[i]):
            if check_adj_levels(data[i]):
                count += 1
            else:
                to_recheck_steps.append(data[i])
        else:
            to_recheck_mono.append(data[i])
    for i in tqdm(iterable=range(len(to_recheck_mono)), desc='Progress Report 2 - Monotonic'):
        sub_reports = is_almost_monotonic(to_recheck_mono[i])
        for sub_report in sub_reports:
            if check_adj_levels(sub_report):
                count += 1
                break 
    for i in tqdm(iterable=range(len(to_recheck_steps)), desc='Progress Report 3 - Steps'):
        report = to_recheck_steps[i]
        n = len(report)
        for i in range(n):
            sub_report = report[:i] + report[i+1:]
            if check_adj_levels(sub_report):
                count += 1
                break
    print(count)


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')

