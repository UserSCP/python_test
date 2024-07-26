from tkinter import *
from pytube import YouTube
from tkinter import messagebox
import os
from moviepy.editor import VideoFileClip, AudioFileClip
"""
-api que utilice, si no lo bajas no te anda

python -m venv myenv
.\myenv\Scripts\activate
----
python -m pip install --upgrade pip
pip install pytube moviepy

"""
def Downloader():
    try:
        url = link.get()
        if not url:
            raise ValueError("Por favor, ingresa un enlace de YouTube")
        yt = YouTube(url)
        messagebox.showinfo("Descargando", "La descarga ha comenzado...")
        video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()
        audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).first()
        video_path = video_stream.download(filename='video.mp4')
        audio_path = audio_stream.download(filename='audio.mp4')
        final_path = 'final_video.mp4'
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)
        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile(final_path, codec='libx264')
        os.remove(video_path)
        os.remove(audio_path)
        messagebox.showinfo("Éxito", "Video descargado exitosamente con audio")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {e}")
root = Tk()
root.geometry("400x300")
root.resizable(0, 0)
root.title("Descargador de YouTube por UserSCP")
root.configure(bg="#AACDE2")
Label(root, text="Descarga tus videos", font='arial 20 bold', bg='#AACDE2').place(x=60, y=30)
link = StringVar()
Label(root, text='Pega el link aquí:', font='arial 12', bg='#AACDE2').place(x=32, y=90)
link_enter = Entry(root, width=55, textvariable=link).place(x=32, y=120)
Button(root, text='Descargar', font='arial 13 bold italic', bg='#B57199', padx=2, command=Downloader).place(x=150, y=180)
#Video de prueba
#https://www.youtube.com/watch?v=ZhIsAZO5gl0
root.mainloop()
