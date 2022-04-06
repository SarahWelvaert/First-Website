def get_class():
    with open('classes.csv', 'r') as csvfile:
            data = csv.DictReader(csvfile)
            classes_list = {}
            for yoga in data:
                classes_list[yoga['slug']] = yoga
    return classes_list