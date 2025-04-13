import csv

def mapReader(map_name):
    map_library = {}

    _map_ = map_library.get(map_name)
    if _map_ is None:
        _map_ = []
        input_file = csv.DictReader(open('snakeApp\\maps\\' + map_name))
        for row in input_file:
            _row_ = []
            for cell in range(0, 40):
                _row_.append(row[str(cell)])
            _map_.append(_row_)
        map_library[map_name] = _map_
    return _map_