# ---------------------------------------------------------------------------- #
#                            GTAV Mod Loader Toggler                           #
# ---------------------------------------------------------------------------- #

# ---------------------------- 各種モジュールをロード ---------------------------- #

import json
import os

# ------------------------ 操作するファイルリストを読み込み ------------------------ #
# -------------------- 将来的にはGUIから操作できるようにする予定 -------------------- #

with open("loader.json") as f:
    loader = json.load(f)

# --------------------------------- フラグリスト -------------------------------- #

# Modの有効/無効フラグ
MOD_FLAG = False

# ------------------------------------ 関数 ------------------------------------ #


def enable_mod(loader, flag):
    """Modを有効化する。

    Args:
        loader (json): 切り替えるModローダーのファイル名のjson。 loader を入れておけばとりあえずこまらん。
        flag (bool): Modローダーのフラグ。Falseじゃないとうけつけません。

    Returns:
        true: Modの有効化に成功。
        false: Modの有効化に失敗。
    """
    # フラグチェック
    # flagがTrueならModがすでに有効であるためFalseを返却
    # flagがFalseならModが無効であるため処理を開始
    if flag is True:  # Modが有効である場合
        print("[ERROR]; Modはすでに有効です!")
        return False
    else:
        try:
            # なんやかんや
            return True
        except:  # 例外発生、Flake8が怒るけど知らん・・・
            # なんやかんや
            return False


def change_flag(new_flag):
    # フラグを変更するだけ、バグのもとかも・・・
    global MOD_FLAG
    MOD_FLAG = new_flag
