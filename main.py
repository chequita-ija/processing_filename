# coding: utf-8

import os.path
import datetime

def processing_filename(dir_filename, timestamp):
    
    # split()でディレクトリのパスとファイル名を分割
    directory, filename = os.path.split(dir_filename)
    # splitext()で文字列と拡張子を分割
    name, extension = os.path.splitext(directory)
    
    # (文字列+Stringに変換したタイムスタンプ+拡張子)でStringの結合
    print(name+'_'+str(timestamp)+extension)
    
def main():

    dir_filename = 'huga/hoge.jpg'
    timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    processing_filename(dir_filename, timestamp)

if __name__ == '__main__':

    main()
