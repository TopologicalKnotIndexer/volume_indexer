import os
import re
DIRNOW = os.path.dirname(os.path.abspath(__file__))
VOLUME_INFO_LIST_FILE = os.path.join(DIRNOW, "volume_list", "src", "volume_info_list.txt")
assert os.path.isfile(VOLUME_INFO_LIST_FILE)

def load_volume_info_list() -> list: # 获取所有已知的扭结的 volume
    arr = []
    for line in open(VOLUME_INFO_LIST_FILE):
        line = line.strip()
        if line == "" or line[0] == "#": # 跳过空行以及注释行
            continue
        assert re.match(r"^\[.*\|.*\]$", line) is not None
        knotname, volume = line[1:-1].split("|", 1)
        arr.append((knotname, float(volume)))
    return sorted(arr, key=lambda x:x[1]) # 按照 volume 递增排序

def main():
    for line in load_volume_info_list():
        print(line)

if __name__ == "__main__":
    main()