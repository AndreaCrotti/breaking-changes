import argparse
import yaml
import json

from pprint import pprint

from breaking_changes.inspector import analyze


def parse_arguments():
    parser = argparse.ArgumentParser(description='Analyze signatures')

    parser.add_argument('-p', '--path',
                        required=True,
                        help='path to analyze')

    parser.add_argument('-o', '--output',
                        help='yaml output file')

    parser.add_argument('--skip-tests',
                        help='skip test directories',
                        action='store_true')

    return parser.parse_args()


def main():
    args = parse_arguments()

    result = dict(analyze(root=args.path))
    if args.output:
        with open(args.output, 'w') as yml_out:
            # json.dump(result, yml_out)
            yaml.dump(result, yml_out)
    else:
        pprint(result)
