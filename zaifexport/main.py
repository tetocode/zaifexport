import os
import sys

from docopt import docopt

from .exporter import Exporter


def main():
    args = docopt("""
    Usage:
      {f} [options] KEY SECRET EXPORT_TYPE [FILE]
    
    Arguments:
      KEY  APIキー
      SECRET  APIシークレット
      EXPORT_TYPE  spot(現物), margin(信用), future(先物), deposit(入金), withdrawal(出金) のいずれかを指定
      FILE  出力先ファイル名の指定、省略時は標準出力

    Options:
      --wait-interval SECONDS  API呼び出しリトライ時の待ち時間 [default: 30.0]
      --limit LIMIT  1回あたりの取得件数 [default: 1000]
      --cache-limit LIMIT  IDキャッシュエントリ数 [default: 10000]
      --currencies CURRENCIES  入金、出金で対象通貨を絞り込みたい場合にカンマ区切りで指定

    Example:
      {f} 11111111-2222-3333-4444-555555555555 aaaaaaaa-bbbb-cccc-eeee-eeeeeeeeeeee spot spot.csv
      
    """.format(f=os.path.basename(sys.argv[0])))

    key = args['KEY']
    secret = args['SECRET']
    export_type = args['EXPORT_TYPE']
    file_name = args['FILE']
    wait_interval = float(args['--wait-interval'])
    limit = int(args['--limit'])
    cache_limit = int(args['--cache-limit'])
    currencies = args['--currencies']
    if currencies:
        currencies = currencies.split(',')

    exporter = Exporter(api_key=key, api_secret=secret,
                        wait_interval=wait_interval,
                        limit=limit,
                        cache_limit=cache_limit,
                        currencies=currencies)
    file = open(file_name, 'w') if file_name else sys.stdout
    try:
        method = 'export_{}'.format(export_type)
        assert method in dir(exporter), 'unknown EXPORT_TYPE: {}'.format(export_type)
        gen = getattr(exporter, method)()
        exporter.write_csv(gen, file)
    finally:
        file.close()


if __name__ == '__main__':
    main()
