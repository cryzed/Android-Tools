#!/usr/bin/env python

import argparse

import persistent_properties_pb2

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('path')
argument_parser.add_argument('keys', nargs='+')


def main(arguments):
    keys = set(arguments.keys)
    with open(arguments.path, 'rb') as file:
        content = file.read()

    properties = persistent_properties_pb2.PersistentProperties()
    properties.ParseFromString(content)

    offset = 0
    for index, property_ in enumerate(properties.properties):
        if property_.name in keys:
            assert property_ is properties.properties[index - offset]
            print('Deleting', property_.name)
            del properties.properties[index - offset]
            offset += 1

    with open(arguments.path + '.out', 'wb') as file:
        file.write(properties.SerializeToString())


if __name__ == '__main__':
    arguments = argument_parser.parse_args()
    main(arguments)
