from moviepy.editor import VideoFileClip

VIDEO_PATH_TARGET = "E:/Filmy/Shrek 2 (2004) [1080p]/Shrek.2.2004.1080p.BluRay.x264.YIFY.mp4"
VIDEO_PATH_AUDIO_SRC = "E:/Filmy/BAJKI/Shrek 1-4/Shrek2.DVDRip.PLdub.WS.avi"
# audioclip = AudioFileClip("some_audiofile.mp3")
# audioclip = AudioFileClip("some_video.avi")

videoclip_audio_trgt = VideoFileClip(VIDEO_PATH_TARGET)
videoclip_audio_src = VideoFileClip(VIDEO_PATH_AUDIO_SRC)

audioclip = videoclip_audio_src.audio

new_video = videoclip_audio_trgt.set_audio(audioclip)
new_video.write_videofile("movie.mp4", fps=videoclip_audio_trgt.fps)
