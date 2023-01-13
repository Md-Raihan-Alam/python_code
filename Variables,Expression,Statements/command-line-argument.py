import sys
import argparse
# 1st method
name=sys.argv[1]
print("Hello "+name)

#2nd method
parser=argparse.ArgumentParser(description='This program prints the name of my dogs')
parser.add_argument('-c','--color',metavar='color',required=True,choices={'red','yellow'},help='the color to search for')
args=parser.parse_args()
print(args.color)