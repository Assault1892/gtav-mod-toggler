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

# ------------------------------------ 変数 ------------------------------------ #

# Modの有効/無効フラグ
MOD_FLAG = False

# GTAVのゲームディレクトリ
# 絶対パスで指定！相対パスだとどうなるかわからん！
GTAV_DIR = "C:/Users/Assault/Desktop/GTAVTogglerTest"

# ------------------------------------ 関数 ------------------------------------ #

# フラグをチェック


def check_flag(gamedir):
    # フラグファイルの存在確認
    # 存在しなければローダーのリストと照らし合わせて全てenabledの状態にしてフラグファイル作成
    return False

# Modを有効化


def enable_mod(gamedir, modloader, modflag):
    """Modを有効化する。

    Args:
        gamedir (str): ゲームディレクトリの絶対パス。
        loader (json): 切り替えるModローダーのファイル名のjson。 loader を入れておけばとりあえずこまらん。
        flag (bool): Modローダーのフラグ。Falseじゃないとうけつけません。

    Returns:
        true: Modの有効化に成功。
        false: Modの有効化に失敗。
    """
    # ローダーチェック
    # dinput8.dll が含まれているかチェックする

    logger.info("ローダーチェック")
    for i in modloader["loader"]:
        if i in "dinput8.dll":
            logger.info("dinput8.dllの含まれるjsonを検出")
            break
        else:
            logger.error("このjsonにはdinput8.dllが含まれていません!")

    # フラグチェック
    # flagがTrueならModがすでに有効であるためFalseを返却
    # flagがFalseならModが無効であるため処理を開始
    if modflag is True:  # Modが有効である場合
        logger.error("Modはすでに有効です!")
        return False
    else:
        try:
            # ローダーの中身をforで回して各ファイルを取得

            logger.info("ローダーのリスト取得開始")
            modloader_list = []
            for i in modloader["loader"]:
                modloader_list.append(i)
            logger.info("ローダーのリストの取得完了")
            logger.info("ローダー: " + modloader_list)

            # GTA5のゲームディレクトリ内のファイルの存在確認

            # ローダーのリストと照らし合わせて存在するファイルのみリストに格納
            # ファイル名末尾にある .disabled を元に検出する

            # ファイル名末尾にある .disabled を除去する

            # フラグを反転する

            return True
        except:  # 例外発生、Flake8が怒るけど知らん・・・
            # なんやかんや
            return False
# Modを無効化


def disable_mod(loader, flag):
    # なんやかんや
    return True

# ---------------------------------- メインコード ---------------------------------- #
