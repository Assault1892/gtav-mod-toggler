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

logger.info("モジュールのロード完了")

# ------------------------ 操作するファイルリストを読み込み ------------------------ #
# -------------------- 将来的にはGUIから操作できるようにする予定 -------------------- #

with open("loader.json", "r") as f:
    loader = json.load(f)

logger.info("ローダーのJSONのロード完了")

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

    logger.info("ローダーチェック")
    for i in loader["loader"]:
        if i in "dinput8.dll":
            logger.info("dinput8.dllの含まれるjsonを検出")
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
            # ローダーの中身をforで回して各ファイルを取得

            logger.info("ローダーのリスト取得開始")
            loader_list = []
            for i in loader["loader"]:
                loader_list.append(i)
            logger.info("ローダーのリストの取得完了")

            # GTA5のゲームディレクトリ内のファイルの存在確認

            return True
        except:  # 例外発生、Flake8が怒るけど知らん・・・
            # なんやかんや
            return False
