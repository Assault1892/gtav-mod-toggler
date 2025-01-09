# しくみ

Modローダーの実ファイルをリネームしてDLL インジェクションを起こさないようにしてるだけ  
Modローダーのインジェクト自体は多分[こんな感じの方法](https://qiita.com/khsk/items/c5ae73732dbad135cf35#%E7%B5%90%E8%AB%96)で行われてると思います じゃあ自動的に引っ掛けられるDLLのファイル名変えちゃえばいいんじゃねってことで

## 改変するファイル

- `args.txt`
  - 「ScriptHookV」だかなんだかで使うはず？  
    ゲーム起動時BattlEyeを無効化するための引数が書かれている
- `dinput8.dll`
  - 「ScriptHookV」をロードするための踏み台
- `ScriptHookV.dll`
  - 「ScriptHookV」の本体
- `ScriptHookVDotNet2.dll`
- `ScriptHookVDotNet3.dll`
  - 「ScriptHookV」のプラグインを.NETを使って書けるやつ のローダー  
    「ScriptHookVDotNet」の本体
- `mod_flag`
  - このツールが作成するファイル  
    ファイルの中身が `enabled` のときはModが有効、`disabled` のときは無効

`.asi` ファイルや `scripts` ディレクトリ、その他 `.ini` `.xml` ファイルに対しては改変をしません  
`.asi` `scripts` は各種Modのファイルが、 `.ini` `.xml` は各種Modの設定ファイルだったりするため、変に壊しても嫌

## 改変内容

`mod_flag` ファイルを参照してフラグによってファイル名末尾の `.disabled` をつけたり外したりするだけ  
それ以外のことは一切やりません

ゲームがModデータ (`.asi`とか) を読み込む仕組み的に、全てのModデータや `mods` ディレクトリを操作しなくとも、大元の踏み台DLLを読まないようにすればいいので、極論 `.disabled` を末尾につけずとも `.dll` 拡張子を外すだけでもいいです  
でも事故が怖いので念の為 `.disabled` 拡張子をつけたり外したりする方式に