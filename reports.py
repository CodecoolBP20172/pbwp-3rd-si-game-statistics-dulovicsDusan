


def import_files(file_name):
    data = []
    files = open(file_name)
    for line in files:
        data.append(line.split("\t"))


def count_games(file_name):
    data = import_files(file_name)
    return len(data)


def decide(file_name, year)
    data = import_files(file_name)
    