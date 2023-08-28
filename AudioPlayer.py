from tkinter import * 
import pygame
from tkinter import filedialog

class Music:
    def __init__(self,master):
        #self.master = Tk()
        #self.master.title("Annoucement")
        #self.master.iconbitmap('train.ico')
        #self.master.geometry('500x300')
        pygame.mixer.init()
        play_img = PhotoImage(file='D:/python/play51.png')
        pause_img = PhotoImage(file='D:/python/pause51.png')

        controls_frame = Frame(master)
        controls_frame.pack()


        self.play_btn = Button(controls_frame,image= play_img,borderwidth=0,command=self.play)
        self.pasue_btn = Button(controls_frame,image= pause_img,borderwidth=0,command=self.stop)

        self.play_btn.grid(row=0,column=2)
        self.pasue_btn.grid(row=0,column=3)

        my_menu = Menu(master)
        master.config(menu = my_menu)

        add_song_menu = Menu(my_menu)
        my_menu.add_cascade(label="Add song", menu=add_song_menu)
        add_song_menu.add_command(label="Add one song to playlist",command=self.add_song)
        self.song_box = Listbox(master,bg="black",fg='green',width=60, selectbackground="gray",selectforeground="black")
        self.song_box.pack(pady=20)
        master.mainloop()
    def add_song(self):
        song = filedialog.askopenfilename(initialdir='‪D:/python/',title="choose A song", filetypes=(("mp3 Files", "*.mp3"),))
        song = song.replace('D:/python/' , "")
        song = song.replace(".mp3" , "")
        
        self.song_box.insert(END,song)

    def play(self):
        pygame.mixer.init()
        song = self.song_box.get(ACTIVE)
        song = f'D:/python/{song}.mp3'

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)    

    def stop(self):
        pygame.mixer.init()
        pygame.mixer.music.stop()
        self.song_box.select_clear(ACTIVE)    





    