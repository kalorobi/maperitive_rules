def readname(e):
    str_list = []
    for set in e.tagSets:
        if set.hasTag('name'):
            str_list.append(set['name'])

    str_list.sort()
    return '+'.join(str_list)
