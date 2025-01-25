# ---------------------------------------------------------------------------- #
#                            GTAV Mod Loader Toggler                           #
# ---------------------------------------------------------------------------- #

# ---------------------------- 各種モジュールをロード ---------------------------- #

from logging import getLogger, config
import json
import os

from win32com.client import Dispatch
shell = Dispatch("Shell.Application")

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

# ------------------------------- inputとかで拾う ------------------------------- #

# Modの有効/無効フラグ
MOD_FLAG = False

# GTAVのゲームディレクトリ
GTAV_DIR = ""

# ------------------------------------ 関数 ------------------------------------ #

# ゲームディレクトリが正しいかチェック
# GTAV.exeの存在確認


def check_gamedir(gamedir):
    ns = shell.NameSpace(gamedir)
    gamefile = os.path.join(gamedir + "GTA5.exe")

    print(ns.Items())

# フラグをチェック関数
# オブジェクト作成時にフラグファイルの存在を確認し、状態によってフラグ変数を変更
# 起動時にフラグファイルが存在しなければ dinput8.dll の状態に応じて変更


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

# Modを有効化

# Modを無効化

# ---------------------------------- メインコード ---------------------------------- #


print(" ---------------------------------------------------------------------------- #")
print("#                            GTAV Mod Loader Toggler                           #")
print(" ---------------------------------------------------------------------------- #")

gamedir = str(input("ゲームディレクトリのパスを入力: "))

check_gamedir(gamedir)
