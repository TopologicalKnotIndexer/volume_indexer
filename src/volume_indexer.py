from get_volume_interface       import get_volume
from volume_info_list_interface import load_volume_info_list
from knotname_reg               import knotname_reg

EPS = 1e-4 # 精度误差

def volume_indexer(knot_pdcode: list) -> list: # 给定扭结 PD_CODE，返回所有具有相近 volume 的扭结名称
    volume           = get_volume(knot_pdcode)
    volume_info_list = load_volume_info_list()
    arr = []
    for knotname, knot_volume in volume_info_list:
        if abs(knot_volume - volume) < EPS:
            arr.append(knotname_reg(knotname))
    return list(set(arr))

def main():
    print(volume_indexer([[1, 7, 2, 6], [4, 13, 5, 14], [5, 9, 6, 8], [7, 3, 8, 2], [10, 15, 11, 16], [12, 9, 13, 10], [14, 3, 15, 4], [16, 11, 1, 12]]))

if __name__ == "__main__":
    main()