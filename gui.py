import tkinter as tk
from threading import Thread
from tkinter import filedialog, NW, ALL

import PIL
from PIL import Image, ImageTk
import os
import pyautogui
from PIL.ImageTk import PhotoImage

import draw
import eye_motion_tracking
import iris_detection
import project
import easygui
from tkinter.colorchooser import askcolor


class PhotoApp:

    def __init__(self):
        # Make window
        self.mainwindow = tk.Tk()

        # Centers Window To Screen
        self.screenwidth = self.mainwindow.winfo_screenwidth()
        self.screenheight = self.mainwindow.winfo_screenheight()
        self.place_width = str(int(self.screenwidth / 2 - 400))
        self.place_height = str(int(self.screenheight / 2 - 329))
        self.mainwindow.geometry("+" + self.place_width + "+" + self.place_height)

        # Initial Window Setup
        self.mainwindow.title("pdf reader")
        # self.mainwindow.iconbitmap("unitato.ico")
        self.mainwindow.resizable(width=False, height=False)

        # Variable Declaration
        self.photoindex = 0
        self.currentphoto = ""
        self.photofactor = 0
        self.currentphotopath = ""
        self.currentphotoready = ""
        self.folderpath = ""
        self.lastfolderpath = "IMAGES"
        self.photopath = ""
        self.photolist = []
        self.cwd = "C:/Users/User/Pictures"
        self.rememberme = False
        self.displayatx = 0
        self.displayaty = 0
        self.mouseup = True
        self.zoomlevel = 0
        self.night = False
        self.night2 = False
        self.realpath = ""
        self.image = ""
        self.draw_mark = False
        self.currentimagename = ""
        self.file_path = ""
        # Widget Layout
        self.setup()
        # Initiates Main Loop
        self.mainwindow.mainloop()

    def setup(self):
        print("Setup Begin")
        b_border = 10

        self.frame1 = tk.Frame(self.mainwindow)
        self.frame1.pack(side=tk.TOP)

        self.frame2 = tk.Frame(self.mainwindow)
        self.frame2.pack(side=tk.TOP)

        self.photoframe = tk.Frame(self.frame1, width=600, height=600)
        self.photoframe.pack(side=tk.LEFT)
        self.photoframe.pack_propagate(0)

        self.rightframe = tk.Frame(self.frame1, height=600, width=140,
                                   bd=5, relief=tk.GROOVE)
        self.rightframe.pack(side=tk.LEFT)
        self.rightframe.pack_propagate(0)

        self.canvas = tk.Canvas(self.photoframe, width=600, height=600)
        self.canvas.pack()

        self.leftbutton = tk.Button(self.rightframe, text="Left",
                                    font=("Arial", 14), command=self.moveleft)
        self.leftbutton.pack(side=tk.TOP, fill=tk.X)

        self.rightbutton = tk.Button(self.rightframe, text="Right",
                                     font=("Arial", 14), command=self.moveright)
        self.rightbutton.pack(side=tk.TOP, fill=tk.X)

        self.upbutton = tk.Button(self.rightframe, text="Up",
                                  font=("Arial", 14))  # , command=self.moveup)
        self.upbutton.pack(side=tk.TOP, fill=tk.X)
        self.upbutton.bind("<ButtonPress-1>", self.moveup)

        self.downbutton = tk.Button(self.rightframe, text="Down",
                                    font=("Arial", 14), command=self.movedown)
        self.downbutton.pack(side=tk.TOP, fill=tk.X)

        self.nightbutton = tk.Button(self.rightframe, text="night",
                                     font=("Arial", 14), command=self.conver_to_night)
        self.nightbutton.pack(side=tk.TOP, fill=tk.X)

        self.lightbutton = tk.Button(self.rightframe, text="light",
                                     font=("Arial", 14), command=self.conver_to_light)
        self.lightbutton.pack(side=tk.TOP, fill=tk.X)

        # self.marker = tk.Button(self.rightframe, text="marker",
        #                               font=("Arial", 14), command=self.enable_marker)
        # self.marker.pack(side=tk.TOP, fill=tk.X)


        self.addmarkbutton = tk.Button(self.rightframe, text="add mark",
                                       font=("Arial", 14), command=self.add_page_mark)
        self.addmarkbutton.pack(side=tk.TOP, fill=tk.X)

        self.addrowmarkbutton = tk.Button(self.rightframe, text="row mark",
                                       font=("Arial", 14), command=self.add_row_mark)
        self.addrowmarkbutton.pack(side=tk.TOP, fill=tk.X)

        self.deletemarkbutton = tk.Button(self.rightframe, text="delete mark",
                                       font=("Arial", 14), command=self.delete_page_mark)
        self.deletemarkbutton.pack(side=tk.TOP, fill=tk.X)

        self.screenShotbutton = tk.Button(self.rightframe, text="screenshot",
                                          font=("Arial", 14), command=self.screen_shot)
        self.screenShotbutton.pack(side=tk.TOP, fill=tk.X)

        self.backcolorButton = tk.Button(
            self.rightframe,
            text='back color',
            font=("Arial", 13),
            command=self.change_back_color)
        self.backcolorButton.pack(side=tk.TOP, fill=tk.X)

        self.txtcolorButton = tk.Button(
            self.rightframe,
            text='txt color',
            font=("Arial", 13),
            command=self.change_txt_color)
        self.txtcolorButton.pack(side=tk.TOP, fill=tk.X)
        if not self.draw_mark:
            self.photodisplay = tk.Label(self.photoframe, text="No Photo To Display",
                                         font=("Arial", 14))
            self.photodisplay.place(x=self.zoomsizing_frame()[2],
                                    y=self.zoomsizing_frame()[3],
                                    width=1000, height=1000)

        self.bottomframe = tk.Frame(self.frame2, width=600, height=100, bd=5,
                                    relief=tk.GROOVE)
        self.bottomframe.pack(side=tk.TOP)
        self.photoframe.pack_propagate(0)

        self.previousbutton = tk.Button(self.bottomframe, text="Previous",
                                        font=("Arial", 14), width=10,
                                        command=self.previous)
        self.previousbutton.pack(side=tk.LEFT, anchor=tk.W,
                                 padx=b_border)

        self.zoomout = tk.Button(self.bottomframe, text="(-)",
                                 font=("Arial", 18), command=self.zoomout)
        self.zoomout.pack(side=tk.LEFT, padx=b_border)

        self.folderbutton = tk.Button(self.bottomframe, text="Folder Select",
                                      font=("Arial", 14), width=15, command=self.folderselect)
        self.folderbutton.pack(side=tk.LEFT, padx=b_border)

        self.zoomin = tk.Button(self.bottomframe, text="(+)",
                                font=("Arial", 18), command=self.zoomin)
        self.zoomin.pack(side=tk.LEFT, padx=b_border)

        self.nextbutton = tk.Button(self.bottomframe, text="Next", font=(
            "Arial", 14), width=10, command=self.next)
        self.nextbutton.pack(side=tk.LEFT, padx=b_border)

        x = self.mainwindow.winfo_rootx()
        print(x)
        print("Setup End")

    def zoomsizing_photo(self):
        resolution = [600, 600]
        if self.zoomlevel == 0:
            resolution = [600, 600] ##### was 600 * 600## 2300*2300
        elif self.zoomlevel == 1:
            resolution = [1200, 1200]
        elif self.zoomlevel == 2:
            resolution = [2400, 2400]
        elif self.zoomlevel == -1:
            resolution = [300, 300]
        else:
            resolution = [600, 600]
        return resolution

    def zoomsizing_frame(self):
        resandplace = [1000, 1000, -200, -200]
        if self.zoomlevel == 0:
            resolution = [1000, 1000, -200, -200]
        elif self.zoomlevel == 1:
            resolution = [2000, 2000, -700, -700]
        elif self.zoomlevel == 2:
            resolution = [4000, 4000, -1695, -1695]
        elif self.zoomlevel == -1:
            resolution = [500, 500, 50, 50]
        else:
            resolution = [1000, 1000, -200, -200]
        return resolution

    def zoomin(self):
        self.zoomlevel = self.zoomlevel + 1
        self.reloadphoto()
        print(self.zoomlevel)

    def zoomout(self):
        self.zoomlevel = self.zoomlevel - 1
        self.reloadphoto()
        print(self.zoomlevel)

    def next(self):
        print("Next Begin")
        self.displayatx = 0
        self.displayaty = 0
        self.zoomlevel = 0
        self.currentrotation = 0
        if self.currentphoto != None:
            self.currentphoto.close()
            self.currentphoto = None
        if self.photoindex < len(self.photolist) - 1:
            self.photoindex = self.photoindex + 1
        else:
            self.photoindex = 0

        self.reloadphoto()

        print("Next End")

    def previous(self):
        print("Previous Begin")
        self.displayatx = 0
        self.displayaty = 0
        self.zoomlevel = 0
        self.currentrotation = 0
        if self.currentphoto != None:
            self.currentphoto.close()
            self.currentphoto = None
        if self.photoindex == 0:
            self.photoindex = len(self.photolist) - 1
        else:
            self.photoindex = self.photoindex - 1

        self.reloadphoto()
        print("Previous End")

    def folderselect(self):
        index = 0
        if self.night:
            self.folderpath = self.realpath + "/night"
            self.night = False
            index = self.photoindex
        elif self.night2:
            self.folderpath = self.realpath
            self.night = False
            index = self.photoindex
        else:
            self.file_path = easygui.fileopenbox()
            project.conver_pdf_to_image(self.file_path)
            self.folderpath = f"IMAGES/{os.path.basename(self.file_path)}"
            # project.gray_and_white(folderpath=self.folderpath)
            project.sepia(folderpath=self.folderpath,new=False)
            self.realpath = self.folderpath
            print(self.folderpath)

        if self.folderpath != "" and self.rememberme == False:
            print("Mark 1")
            self.photolist = []
            self.photoindex = 0
            self.displayatx = 0
            self.displayaty = 0
            self.currentphotoready = None
            self.cwd = self.folderpath
            for name in os.listdir(self.folderpath):
                if name.lower().endswith(".jpg") or name.lower().endswith(".png"):
                    self.photolist.append(name)

            if self.photolist != []:
                self.photoindex = index
                self.reloadphoto()
            else:
                self.photodisplay["image"] = ""
                self.photodisplay["text"] = "No photos in this folder."
                print(self.photodisplay["text"], self.photodisplay["image"])

        else:
            self.folderpath = self.lastfolderpath
            if self.photolist != []:
                self.photoindex = index
                self.reloadphoto()
            else:
                self.photodisplay["image"] = ""
                self.photodisplay["text"] = "No photos in this folder."
                print(self.photodisplay["text"], self.photodisplay["image"])

    def enable_marker(self):
        self.draw_mark = not self.draw_mark
        self.reloadphoto()

    # def enable_row_marker(self):
    #     self.draw_mark = not self.draw_mark
    #     self.reloadphoto()

    def do_zoom(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        factor = 1.001 ** event.delta
        is_shift = event.state & (1 << 0) != 0
        is_ctrl = event.state & (1 << 2) != 0
        self.canvas.scale(ALL, x, y,
                          factor if not is_shift else 1.0,
                          factor if not is_ctrl else 1.0)

    def get_x_and_y(self, event):
        global lasx, lasy
        lasx, lasy = event.x, event.y


    def draw_smth(self, event):
        global lasx, lasy
        self.canvas.create_line((lasx, lasy, event.x, event.y),
                                fill='blue',
                                width=2)
        lasx, lasy = event.x, event.y

    def save_as_png(self, fileName):
        # save postscipt image
        self.canvas.postscript(file=fileName + '.eps')
        # use PIL to convert to PNG
        img = PIL.Image.open(fileName + '.eps')
        # img.save(fileName + '.png', 'png') here the problem unable to locate ghostscript


    def change_back_color(self):
        bcolor = askcolor(title="background Color Chooser")
        project.change_back_color(back_color=bcolor, txt_color=bcolor, index=self.photoindex, path=self.folderpath)
        self.reloadphoto()

    def change_txt_color(self):
        tcolor = askcolor(title="txt Color Chooser")
        project.change_text_color(path=self.folderpath,index=self.photoindex,color=tcolor)
        self.reloadphoto()



    def conver_to_night(self):
        self.night = True
        self.night2 = False
        self.folderselect()
        self.reloadphoto()

    def conver_to_light(self):
        self.night = False
        self.night2 = True
        self.folderselect()
        self.reloadphoto()


    def add_page_mark(self):
        for page in range(len(self.photolist)):
            project.conver_one_image(pdfpath=self.file_path, index=page+ 1)

        project.sepia(folderpath=self.folderpath,new=True)

        project.add_book_mark(b_mark="mark.jpg", index=self.photoindex, path=self.realpath)
        project.add_book_mark(b_mark="mark.jpg", index=self.photoindex, path=self.realpath + "/night")
        # project.add_book_mark(b_mark="mark.jpg", index=self.photoindex, path=self.realpath + "/night3")

        self.reloadphoto()

    def add_row_mark(self):
        for page in range(len(self.photolist)):
            project.conver_one_image(pdfpath=self.file_path, index=page+ 1)

        project.row_mark(b_mark="marker1.jpg", index=self.photoindex, path=self.realpath)
        # project.row_mark(b_mark="marker1.jpg", index=self.photoindex, path=self.realpath+"/night")
        # project.add_book_mark(b_mark="mark.jpg", index=self.photoindex, path=self.realpath + "/night")
        # project.add_book_mark(b_mark="mark.jpg", index=self.photoindex, path=self.realpath + "/night3")

        self.reloadphoto()

    def delete_page_mark(self):
        project.conver_one_image(pdfpath=self.file_path,index=self.photoindex+1)
        project.sepia_one_image(filename=self.realpath,index=str(self.photoindex)+".png")
        self.reloadphoto()

    def screen_shot(self):
        eye_motion_tracking.take_screenshot()


    def loadphoto(self):
        print("Load Photo Begin")
        print(self.photoindex)
        if not self.draw_mark:
            self.photodisplay = tk.Label(self.photoframe, text="No Photo To Display",
                                         font=("Arial", 14))
            self.photodisplay.place(x=self.zoomsizing_frame()[2],
                                    y=self.zoomsizing_frame()[3],
                                    width=1000, height=1000)
            self.photodisplay["image"] = ""
        self.currentphotoready = ""
        self.currentimagename = self.photolist[self.photoindex]
        # print(f"\n\n\n\n{name}\n\n\n")
        if self.currentimagename.lower().endswith(".gif"):
            self.gifplayback()
        else:
            if self.folderpath != "":
                self.currentphotopath = self.folderpath + "/" + str(self.photolist[self.photoindex])
                self.currentphoto = Image.open(self.currentphotopath)

        print("Load Photo End")

    def reloadphoto(self):
        self.loadphoto()
        self.photoscale()
        self.displayphoto()

    def displayphoto(self):
        print("Display Photo Begin")
        if self.draw_mark:
            self.image = PhotoImage(file =f"{self.folderpath}/{self.currentimagename}")
            # self.image = self.image._PhotoImage__photo.zoom(2) # zoom in
            self.image = self.image._PhotoImage__photo.subsample(4)# zoom out
            self.canvas.create_image(10, 10, anchor=NW, image=self.image)
            self.canvas.bind("<Button-1>", self.get_x_and_y)
            self.canvas.bind("<B1-Motion>", self.draw_smth)
            # self.save_as_png("IMAGES/xyz")
        # if self.draw_mark:
        #     # self.canvas.bind("<MouseWheel>", self.do_zoom)
        #     # self.canvas.bind('<ButtonPress-1>', lambda event: self.canvas.scan_mark(event.x, event.y))
        #     # self.canvas.bind("<B1-Motion>", lambda event: self.canvas.scan_dragto(event.x, event.y, gain=1))
        #     self.canvas.bind("<Left>", lambda event: self.canvas.xview_scroll(-1, "units"))
        #     self.canvas.bind("<Right>", lambda event: self.canvas.xview_scroll(1, "units"))
        #     self.canvas.bind("<Up>", lambda event: self.canvas.yview_scroll(-1, "units"))
        #     self.canvas.bind("<Down>", lambda event: self.canvas.yview_scroll(1, "units"))
        #     self.canvas.focus_set()
        #     # pyautogui.press('left') press virtual keys
        else:
            self.photodisplay.place(width=self.zoomsizing_frame()[0], height=self.zoomsizing_frame()[1],
                                    x=self.zoomsizing_frame()[2] + self.displayatx,
                                    y=self.zoomsizing_frame()[3] + self.displayaty)
            self.currentphotoready = ImageTk.PhotoImage(self.currentphoto)
            self.photodisplay.config(image=self.currentphotoready)
        print("Display Photo End")

    def photoscale(self):
        print("Photo Scale Begin")
        print(self.currentphoto.width, self.currentphoto.height)
        if self.currentphoto.width > self.currentphoto.height:
            self.photofactor = self.currentphoto.width / self.zoomsizing_photo()[0]
        else:
            self.photofactor = self.currentphoto.height / self.zoomsizing_photo()[1]

        self.currentphoto.thumbnail((int(self.currentphoto.width / self.photofactor),
                                     int(self.currentphoto.height / self.photofactor)), Image.ANTIALIAS)

        print(self.currentphoto.width, self.currentphoto.height)
        print("Photo Scale End")

    def moveleft(self):
        print("moveleft")
        if self.currentphoto != "":
            self.displayatx = self.displayatx + 10
            self.reloadphoto()

    def moveright(self):
        print("moveright")
        if self.currentphoto != "":
            self.displayatx = self.displayatx - 10
            self.reloadphoto()

    def moveup(self, key):
        print("moveup")
        if self.currentphoto != "":
            self.displayaty = self.displayaty + 10
            self.reloadphoto()

    def movedown(self):
        print("movedown")
        if self.currentphoto != "":
            self.displayaty = self.displayaty - 10
            self.reloadphoto()


def main():
    program = PhotoApp()


if __name__ == "__main__":
    Thread(target=main).start()
    # Thread(target=iris_detection.scroll()).start()
    # Thread(target=eye_motion_tracking.take_screenshot).start()
    # Thread(target=draw.get()).start()

def justtest():
    print("test true ")
