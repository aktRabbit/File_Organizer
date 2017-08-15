import os
os.chdir('/media/akt/Windows/Users/Akt/Downloads') #Enter the path
path=os.getcwd()
lists=os.listdir(path)
dir={".zip":"ZIP_Files",".c":"C",".java":"Java",".py":"Python",".cpp":"C++",".mp3":"mp3_song",".MP3":"mp3_song",".VOB":"Video_songs",".FLV":"Video_songs",".mp4":"Video_songs",".doc":"Documnets",".docx":"Documnets",".rtf":"Documnets",".MP4":"Video_songs",".wmv":"Video_songs",".png":"Images",".jpg":"Images",".mkv":"Video_songs",".mpg":"Video_songs",".MKV":"Video_songs",".wav":"Video_songs",".txt":"text_files",".avi":"Video_songs",".3gp":"Video_songs",".mpeg":"Video_songs",".flv":"Video_songs",".pdf":"PDF",".exe":"program",".srt":"SRT"}
for list in lists:
    file , ext=os.path.splitext(list)
    try:
        if (ext==".mp4" or ext==".wav" or ext==".avi" or ext==".flv" or ext==".mkv") and os.path.getsize(list)>100000000 :
            if (os.path.exists('Movies') == False):
                os.mkdir('Movies')
            os.rename(list,'./Movies/'+list)
        else:
            if (os.path.exists(dir[ext]) == False):
                os.mkdir(dir[ext])
            os.rename(list,'./'+dir[ext]+'/'+list)
    except Exception as e:
        pass


