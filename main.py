import inspect
import os
from getTiebaEmotion import TiebaEmotion


def get_tiebe_emoji():
    save_dir = './emotion/Tieba'  # 保存路径

    # 判断保存路径是否已经创建
    os.makedirs(save_dir, exist_ok=True)

    tb = TiebaEmotion()
    # get all information(method name, variable name) of a class
    all_members = inspect.getmembers(tb)
    # select all the instance methods
    instance_method = [
        name for name, member in all_members
        if inspect.ismethod(member) and not name.startswith('__')
    ]
    # recursively call all instance methods of the class
    for mathod_name in instance_method:
        method = getattr(tb, mathod_name)
        method(save_dir)


if __name__ == "__main__":
    get_tiebe_emoji()