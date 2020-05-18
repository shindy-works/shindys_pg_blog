import sys, os
import argparse
from argparse import RawTextHelpFormatter
import datetime
import subprocess
import urllib.parse

sys.dont_write_bytecode = True

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
ap.add_argument('-c',
                '--categories',
                help="page categories (only post)",
                default=[],
                nargs='*')

# not using
month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

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
def get_tmp(layout):
    with open(os.path.join(PJTPATH, '_template', layout, '__temp__'),
              'r') as f:
        return f.read()


def norm_str(s):
    for c in cant_use_char:
        s = s.replace(c, c.encode().hex())
    return s


# テンプレート作成
def create_tmp(*args):
    return {'page': create_page, 'post': create_post}[args[0]](*args)


# postテンプレート作成
def create_post(*args):
    layout, title, path, cate = args[:4]
    tmp = get_tmp(layout)

    norm_path = '/'.join([norm_str(p) for p in path.split('/')])

    hex_title = title.encode().hex()

    date = datetime.date.today()

    # 出力パス
    out_path = os.path.join(PJTPATH, "_posts", norm_path,
                            f"{date}-{hex_title}.md")

    # 出力データ
    out_str = tmp.format(title, get_date(), str(cate),
                         f"{norm_path}/{date:%Y/%m/%d}/{hex_title}")

    with open(out_path, 'wb') as f:
        f.write(out_str.encode('utf-8'))

    return out_path


# pageテンプレート作成
def create_page(*args):
    layout, title, path = args[:3]
    tmp = get_tmp(layout)

    norm_path = '/'.join([norm_str(p) for p in path.split('/')])

    out_path = os.path.join(PJTPATH, norm_path, "index.md")
    os.mkdir(os.path.dirname(out_path))

    out_str = tmp.format(title, get_date(), os.path.split(path)[-1], norm_path)

    with open(out_path, 'wb') as f:
        f.write(out_str.encode('utf-8'))

    return out_path


if __name__ == '__main__':
    f_path = create_tmp(*get_args(ap.parse_args()))
    fp = os.path.abspath(os.path.join(os.path.dirname(__file__), f_path))
    subprocess.run(fp, shell=True)
