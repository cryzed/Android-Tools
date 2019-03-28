#!/usr/bin/env python

import argparse

import persistent_properties_pb2

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('path')
argument_parser.add_argument('keys', nargs='*')


def main(arguments):
    keys = set(arguments.keys)
    with open(arguments.path, 'rb') as file:
        content = file.read()

    properties = persistent_properties_pb2.PersistentProperties()
    properties.ParseFromString(content)

    for property_ in properties.properties:
        if not keys:
            print(f'[{property_.name}]: [{property_.value}]')
        else:
            if property_.name in keys:
                print(property_.value)


if __name__ == '__main__':
    arguments = argument_parser.parse_args()
    main(arguments)
