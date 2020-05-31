import sys, os
import datetime
import subprocess
import urllib.parse

# __pycache__を生成させない
sys.dont_write_bytecode = True

# 実行ディレクトリ名
PJTPATH = os.path.dirname(os.path.abspath(__file__))

# URLで使えない文字
cant_use_chars = [
    '\\', "'", '|', '`', '^', '"', '<', '>', ')', '(', '}', '{', ']', '[', ';',
    '/', '?', ':', '@', '&', '=', '+', '$', ',', '%', '#', '.'
]


# コマンドライン引数を取得
def get_args():
    import argparse
    from argparse import RawTextHelpFormatter

    ap = argparse.ArgumentParser(
        prog="templatecreator.py",
        usage="create markdown template that depends on layout.",
        description="""example:
    # create page
        $ python templatecreator.py page python blog/language/python
    # create post
        $ python templatecreator.py post "i love python <3" blog/language/python -c python
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

    args = ap.parse_args()

    return args.layout, args.title, args.path, args.categories


class TemplateCreator:
    def __init__(self, *args):
        layout, self.title, path, categories = args
        path = path.strip('/')

        self.categories = self._get_categories(
            os.path.split(path)[-1], categories)
        self.tmp_str = self._get_tmp_str(layout)
        self.norm_path = self._get_norm_path(path)
        self.out_path, self.content = {
            'page': self._init_page_tmp,
            'post': self._init_post_tmp
        }[layout]()

        # 指定パスがなければフォルダを作成
        out_dir = os.path.dirname(self.out_path)
        if not os.path.exists(out_dir): os.makedirs(out_dir)

    # テンプレート出力
    def create(self):
        if os.path.exists(self.out_path):
            print(f"{self.out_path} is already exist.")
            return False

        with open(self.out_path, 'wb') as f:
            f.write(self.content.encode('utf-8'))
        return True

    def _get_categories(self, main_category, categories):
        if not main_category in categories:
            categories.append(main_category)
        return categories

    # jekyllに準拠したフォーマットの日付を取得(yyyy-mm-dd HH-MM-SS +/-hhmm)
    def _get_date(self):
        # 0: year, 1: month, 2: day, 3: hour, 4: minutes, 5: seconds
        now_date = datetime.datetime(
            *datetime.datetime.today().timetuple()[:6])
        utc_date = datetime.datetime(*now_date.utcnow().timetuple()[:6])
        tz = datetime.timezone(now_date - utc_date)
        return f"{now_date.astimezone(tz):%Y-%m-%d %H:%M:%S %z}"

    def _get_filename(self):
        fn = self.norm_path.split('/')[-1]
        date = datetime.date.today()

        out_dir = os.path.join(PJTPATH, "_posts", self.norm_path)

        if not os.path.exists(out_dir): return fn

        lisd_dir = [
            f for f in os.listdir(out_dir)
            if os.path.isfile(os.path.join(out_dir, f))
        ]

        for i in range(2 * 10):
            fn_num = f"{fn}_{i + 1}"
            if not f"{date}-{fn_num}.md" in lisd_dir:
                return fn_num

    # 文字列の正規化(使用できない文字は16進数文字に置き換える)
    def _get_norm_str(self, s):
        if s.isascii() and len([c for c in cant_use_chars if c in s]) == 0:
            return s

        # 置き換え対象となる文字列と置き換える文字列
        before_after = {
            c: c.encode().hex()
            for c in s if not c.isascii() or c in cant_use_chars
        }

        for before, after in before_after.items():
            s = s.replace(before, after)

        return s

    # パスの正規化
    def _get_norm_path(self, path):
        return '/'.join(
            [self._get_norm_str(p) for p in path.split('/') if p != ''])

        # リスト内要素をスラッシュで連結
    def _get_permalink(self, *args):
        return f"/{'/'.join(args)}/"

    # template文字列を取得
    def _get_tmp_str(self, layout):
        with open(os.path.join(PJTPATH, '_template', layout, '__temp__'),
                  'r') as f:
            return f.read()

    # pageテンプレート作成
    def _init_page_tmp(self):
        return os.path.join(PJTPATH, self.norm_path, "index.md"), \
            self.tmp_str.format(self.title, self._get_date(), self.title, self._get_permalink(self.norm_path))

    # postテンプレート作成
    def _init_post_tmp(self):
        file_name = self._get_filename()
        date = datetime.date.today()

        return os.path.join(PJTPATH, "_posts", self.norm_path, f"{date}-{file_name}.md"), \
               self.tmp_str.format(self.title, self._get_date(), str(self.categories),
                                   self._get_permalink(self.norm_path, f"{datetime.date.today():%Y/%m/%d}", file_name).strip('/'))


if __name__ == '__main__':
    TemplateCreator(*get_args()).create()