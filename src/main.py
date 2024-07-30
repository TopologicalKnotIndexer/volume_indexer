import sys
from volume_indexer import volume_indexer

def main():
    inp = sys.stdin.read()
    for knotname in volume_indexer(inp):
        print(knotname)

if __name__ == "__main__":
    main()