# Movies

So I download a lot of movies and it can get pretty lame renaming all your movies and transferring your files.  
Instead, I wrote this to do it for me!  

    D:\Projects\PythonProjects>python project.py
    [+] Found: Blow.2001.1080p.BrRip.x264.BOKUTOX.YIFY.mp4
    [+] Renaming Blow.2001.1080p.BrRip.x264.BOKUTOX.YIFY.mp4 to Blow
    [+] Moving Blow to D:\Movies\Moovies\

    [+] Found: Daylight's.End.2016.1080p.BluRay.x264-[YTS.AG].mp4
    [+] Renaming Daylight's.End.2016.1080p.BluRay.x264-[YTS.AG].mp4 to Daylight's End
    [+] Moving Daylight's End to D:\Movies\Moovies\

    [+] Found: Deadfall.Trail.2009.1080p.BluRay.x264-[YTS.AG].mp4
    [+] Renaming Deadfall.Trail.2009.1080p.BluRay.x264-[YTS.AG].mp4 to Deadfall Trail
    [+] Moving Deadfall Trail to D:\Movies\Moovies\  
    
# Issues 

One thing I have that I didn't try yet was deleting the folder after it's been transferred.  
I was using rmtree, but that doesn't work and it's possibly because contents are in the files  
I'll get that to another time. For now, this will do :)
