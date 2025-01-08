# ---------------------------------------------------------------------------- #
#                            GTAV Mod Loader Toggler                           #
# ---------------------------------------------------------------------------- #

# ---------------------------- 各種モジュールをロード ---------------------------- #

import json
import os

from logging import getLogger, config
with open("log_config.json", "r") as cf:
    log_conf = json.load(cf)
config.dictConfig(log_conf)
logger = getLogger(__name__)

# ------------------------ 操作するファイルリストを読み込み ------------------------ #
# -------------------- 将来的にはGUIから操作できるようにする予定 -------------------- #

with open("loader.json", "r") as f:
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
    # ローダーチェック
    # dinput8.dll が含まれているかチェックする

    for i in loader["loader"]:
        if i in "dinput8.dll":
            logger.info("dinput8.dllの含まれるjsonを検出しました")
            break
        else:
            logger.error("このjsonにはdinput8.dllが含まれていません!")

    # フラグチェック
    # flagがTrueならModがすでに有効であるためFalseを返却
    # flagがFalseならModが無効であるため処理を開始
    if flag is True:  # Modが有効である場合
        logger.error("Modはすでに有効です!")
        return False
    else:
        try:
            # ローダーの中身をforで
            return True
        except:  # 例外発生、Flake8が怒るけど知らん・・・
            # なんやかんや
            return False


def change_flag(new_flag):
    # フラグを変更するだけ、バグのもとかも・・・
    global MOD_FLAG
    MOD_FLAG = new_flag
