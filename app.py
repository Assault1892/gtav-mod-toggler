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
    MOD_LOADER = json.load(f)

logger.info("ローダーのJSONのロード完了")

# ------------------------------------ 変数 ------------------------------------ #

# Modの有効/無効フラグ
MOD_FLAG = False

# GTAVのゲームディレクトリ
# 絶対パスで指定！相対パスだとどうなるかわからん！
GTAV_DIR = "C:/Users/Assault/Desktop/GTAVTogglerTest"

# ------------------------------------ 関数 ------------------------------------ #

# フラグをチェック。フラグ変数に破壊的変更を加えるため注意！
# めちゃくちゃ行儀が悪い関数になってしまった・・・


def check_flag(gamedir):
    global MOD_FLAG  # フラグ変数を操作可能に
    flag_path = os.path.join(gamedir + "mod_flag")
    # フラグファイルの存在確認
    # 存在しなければローダーのリストと照らし合わせて全てenabledの状態にしてフラグファイル作成
    if os.path.exists(flag_path):
        logger.info("フラグファイルを検出")
        # フラグファイルの中身を読み出してフラグ変数を上書き
        with open(flag_path, "r") as ff:
            flaginfo = ff.read()  # フラグファイルをロード
        logger.info("フラグファイルをロード")
        # フラグファイルの中身が enabled ならフラグ変数をTrueに変更
        # disabled ならFalseに変更
        if flaginfo == "enabled":
            logger.info("フラグ: enabled")
            MOD_FLAG = True
        elif flaginfo == "disabled":  # フラグがdisabledの場合
            logger.info("フラグ: disabled")
            MOD_FLAG = False
        else:
            logger.error("フラグファイルが不正です!")  # ここのエラーハンドリングどうしよう？
    else:
        logger.info("フラグファイルが存在しません")
        logger.info("Modファイルを有効化し、フラグファイルを作成...")
        MOD_FLAG = True  # 強制的にフラグをTrueに変更
        enable_mod(GTAV_DIR, MOD_LOADER)  # Modを有効化

# Modを有効化


def enable_mod(gamedir, modloader):
    """Modを有効化する。

    Args:
        gamedir (str): ゲームディレクトリの絶対パス。
        loader (json): 切り替えるModローダーのファイル名のjson。 loader を入れておけばとりあえずこまらん。

    Returns:
        true: Modの有効化に成功。
        false: 何らかの原因でModの有効化に失敗。
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
            return False

    # フラグチェック
    # flagがTrueならModがすでに有効であるためFalseを返却
    # flagがFalseならModが無効であるため処理を開始
    if MOD_FLAG is True:  # Modが有効である場合
        logger.error("Modはすでに有効です!")
        return False
    else:  # Modが無効
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

            # フラグファイルを enabled に変更する

            return True
        except FileNotFoundError:  # ファイルが存在しない場合
            # なんやかんや
            return False
# Modを無効化


def disable_mod(loader, flag):
    # なんやかんや
    return True

# ---------------------------------- メインコード ---------------------------------- #


print(" ---------------------------------------------------------------------------- #")
print("#                            GTAV Mod Loader Toggler                           #")
print(" ---------------------------------------------------------------------------- #")

print("")
