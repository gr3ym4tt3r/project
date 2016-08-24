from __future__ import print_function
from re import search, sub
from os import listdir, rename
from shutil import move, rmtree

source = 'D:\\CompleteDownload\\Finished\\'
dest = 'D:\\Movies\\Moovies\\'

def clean(movieName):
    movie = search('^[^\d{3,4}p]+', movieName)
    return sub('\.', ' ', movie.group())[:-1]

if __name__ == '__main__':
    for movies in listdir(source):
        path = '{}{}\\'.format(source, movies)
        for movies in listdir(path):
            if movies.endswith('mp4'):
                print('[+] Found: {}'.format(movies))
                print('[+] Renaming {} to {}.mp4'.format(movies, clean(movies)))
                rename('{}{}'.format(path, movies), '{}{}.mp4'.format(path, clean(movies)))
                print('[+] Moving {} to {}\n'.format(clean(movies), dest))
                move('{}\\{}.mp4'.format(path, clean(movies)), dest)
                rmtree(path, ignore_errors=True)
