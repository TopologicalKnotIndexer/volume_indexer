# 桥接：https://github.com/TopologicalKnotIndexer/volume_solver
import os
DIRNOW = os.path.dirname(os.path.abspath(__file__))
SUBDIR = os.path.join(DIRNOW, "volume_list", "src", "volume_solver", "src") # 子包路径

# ======================================== BEGIN IMPORT FROM PATH ======================================== #
import importlib
import json
import sys
def load_module_from_path(path: str, mod_name: str): # 从指定路径导入一个包
    assert os.path.isdir(path)                       # 路径必须存在
    path         = os.path.abspath(path)             # 获得绝对路径
    old_sys_path = json.loads(json.dumps(sys.path))  # 存档旧的 sys.path
    sys.path     = [path] + sys.path                 # 将新的路径加入 sys.path
    mod          = importlib.import_module(mod_name) # 加载指定的包
    sys.path     = old_sys_path                      # 恢复旧的 sys.path
    return mod
# ======================================== END IMPORT FROM PATH ======================================== #

def get_volume(knot_pdcpde: str) -> list:
    return load_module_from_path(SUBDIR, "reliable_volume_solver").get_volume_safe(knot_pdcpde)

if __name__ == "__main__":
    ans = get_volume([[4,2,5,1],[15,22,16,1],[10,3,11,4],[2,11,3,12],[9,17,10,16],[7,19,8,18],[17,9,18,8],[19,13,20,12],[5,14,6,15],[13,21,14,20],[21,7,22,6]])
    print("%.20f" % ans)
    ans = get_volume([[4, 1, 5, 2], [15, 1, 16, 22], [10, 4, 11, 3], [2, 12, 3, 11], [9, 16, 10, 17], [7, 18, 8, 19], [17, 8, 18, 9], [19, 12, 20, 13], [5, 15, 6, 14], [13, 20, 14, 21], [21, 6, 22, 7]])
    print("%.20f" % ans)
    ans = get_volume([[4, 2, 5, 1], [10, 4, 11, 3], [11, 17, 12, 16], [5, 15, 6, 14], [15, 9, 16, 8], [20, 8, 21, 7], [21, 12, 22, 13], [13, 18, 14, 19], [6, 20, 7, 19], [17, 1, 18, 22], [2, 10, 3, 9]])
    print("%.20f" % ans)
