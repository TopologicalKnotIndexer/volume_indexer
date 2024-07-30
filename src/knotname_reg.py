# 桥接：https://github.com/TopologicalKnotIndexer/knotname-reg
import os
DIRNOW = os.path.dirname(os.path.abspath(__file__))
SUBDIR = os.path.join(DIRNOW, "knotname-reg", "src") # 子包路径


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



# 输入合法的扭结名称
# 返回正则化后的扭结名称
def knotname_reg(knot_name: str) -> str:
    return load_module_from_path(SUBDIR, "main").knotname_reg(knot_name)



if __name__ == "__main__": # 测试
    print(knotname_reg("mk4a1,mk6a1,mk6a3"))
