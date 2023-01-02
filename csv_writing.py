from pandas import DataFrame

import ym_parsing as yp
import file_creating as fc


def coordinates_separating():
    coordinates_split = yp.creating_coordinates_list()
    separated_coordinates = []
    for item in coordinates_split:
        separated_coordinates.append(item.split(','))

    return separated_coordinates


def csv_writing():
    adresses = yp.creating_adresses_list()
    coordinates = coordinates_separating()
    longitude = [coordinates[i][0] for i in range(len(coordinates))]
    latitude = [coordinates[i][1] for i in range(len(coordinates))]
    writing = DataFrame({'point_adress': adresses,
                         'longitude': longitude,
                         'latitude': latitude
                         })
    export_csv = writing.to_csv(
        fc.new_file_path, sep=';', index=None, header=True)

csv_writing()
