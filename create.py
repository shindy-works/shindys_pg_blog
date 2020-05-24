import sys, os
import argparse
from argparse import RawTextHelpFormatter
import datetime
import subprocess
import urllib.parse

# __pycache__を生成させない
sys.dont_write_bytecode = True

# 実行ディレクトリ名
PJTPATH = os.path.join(os.path.dirname(__file__))

ap = argparse.ArgumentParser(
    prog="create.py",
    usage="create markdown template that depends on layout.",
    description="""
example:
- create page
 python create.py page python blog/language/python

- create post
 python create.py post "i love python <3" blog/language/python -c python
""",
    add_help=True,
    formatter_class=RawTextHelpFormatter)

ap.add_argument('layout', help="page layout.")
ap.add_argument('title', help="page title.")
ap.add_argument('path', help="page path. extention")
ap.add_argument('-c', '--categories', help="page categories (only post)", default=[], nargs='*')

# TODO: フォルダ生成時に日本語が含まれていないか確認したい

# URLで使えない文字
cant_use_char = [
    '\\', "'", '|', '`', '^', '"', '<', '>', ')', '(', '}', '{', ']', '[', ';',
    '/', '?', ':', '@', '&', '=', '+', '$', ',', '%', '#'
]


# 引数処理
def get_args(args):
    if args.layout == 'post':
        if not os.path.split(args.path)[-1] in args.categories:
            args.categories.append(os.path.split(args.path)[-1])

        return args.layout, args.title, args.path, args.categories

    return args.layout, args.title, args.path

# jekyllに準拠したフォーマットの日付を取得(yyyy-mm-dd HH-MM-SS +/-hhmm)
def get_date():
    # 0: year, 1: month, 2: day, 3: hour, 4: minutes, 5: seconds
    now_date = datetime.datetime(*datetime.datetime.today().timetuple()[:6])
    utc_date = datetime.datetime(*now_date.utcnow().timetuple()[:6])
    tz = datetime.timezone(now_date - utc_date)
    return f"{now_date.astimezone(tz):%Y-%m-%d %H:%M:%S %z}"

# template文字列を取得
def get_tmp_str(layout):
    with open(os.path.join(PJTPATH, '_template', layout, '__temp__'), 'r') as f:
        return f.read()

# 文字列の正規化(使用できない文字は16進数文字に置き換える)
def get_norm_str(s):
    for c in cant_use_char:
        s = s.replace(c, c.encode().hex())
    return s

# パスの正規化
def get_norm_path(path):
    return '/'.join([get_norm_str(p) for p in path.split('/')])

# リスト内要素をスラッシュで連結
def slash_join(*args):
    return '/'.join(args)


# テンプレート作成
def create_tmp(*args):
    return {'page': create_page, 'post': create_post}[args[0]](*args)

# postテンプレート作成
def create_post(*args):
    layout, title, path, cate = args[:4]

    tmp_str = get_tmp_str(layout)
    
    # ファイル名は日本語が未対応なため、16進数に置き換える
    file_name = title.encode().hex()
    
    # 正規化されたパス
    norm_path = get_norm_path(path)

    date = datetime.date.today()

    # 出力パス
    out_path = os.path.join(PJTPATH, "_posts", norm_path, f"{date}-{file_name}.md")

    # 指定パスがなければフォルダを作成
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    # 出力データ
    out_str = tmp_str.format(title, get_date(), str(cate),
                         slash_join('', norm_path, f"{date:%Y/%m/%d}", file_name))

    with open(out_path, 'wb') as f:
        f.write(out_str.encode('utf-8'))

    return out_path


# pageテンプレート作成
def create_page(*args):
    layout, title, path = args[:3]
    tmp_str = get_tmp_str(layout)

    norm_path = get_norm_path(path)

    # 出力パス
    out_path = os.path.join(PJTPATH, norm_path, "index.md")

    # 指定パスがなければフォルダを作成
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    out_str = tmp_str.format(title, get_date(), os.path.split(path)[-1], slash_join('', norm_path, ''))

    with open(out_path, 'wb') as f:
        f.write(out_str.encode('utf-8'))

    return out_path


if __name__ == '__main__':
    f_path = create_tmp(*get_args(ap.parse_args()))

    # 作成したテンプレートをエディタで開く
    fp = os.path.abspath(os.path.join(os.path.dirname(__file__), f_path))
    subprocess.run(fp, shell=True)
