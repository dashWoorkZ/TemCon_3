#!/usr/bin/env python
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# Required for APIKEY
# ===============================
import requests                #=
from tkinter import messagebox #=
# ===============================
            
                
#Main Window
window = tk.Tk()

# Center The Main Program Window When Launched
width = 310
height = 350
x = (window.winfo_screenwidth()//2)-(width//2)
y = (window.winfo_screenheight()//2)-(height//2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.title("TemCon 3")
window.configure(background="burlywood")
style=ttk.Style()   # ttk Style Library
menu = tk.Menu(window, background="antiquewhite")
style.theme_use("clam")

#                    GNU GENERAL PUBLIC LICENSE
#                       Version 3, 29 June 2007
#
# Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
# Everyone is permitted to copy and distribute verbatim copies
# of this license document, but changing it is not allowed.
#     You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# ================================================================================================================================================================
# ================================================= Start of Conversion Styling =============================================================================
# ================================================================================================================================================================

style.configure("lawfulLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#ffe4c4", foreground="#5c3608", highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("tcttkLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#ffe4c4", foreground="#5c3608", highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("convertedScaleLableFrameLableLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"),  ipadx=5, ipady=10, background="#4f788a", foreground="#00ffff", highlightbackground='##ffebcd', highlightcolor='#48d1cc', highlightthickness=3, takefocus=True)
style.configure("convertedScaleLableFrameLableDark.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), ipadx=5, ipady=10, background="#fb8604", foreground="#ffff00",  highlightbackground='#48d1cc', highlightcolor='#ffebcd', highlightthickness=3, takefocus=True)
style.configure("privacyLight.TLabel", relief=tk.FLAT, takefocus=False, bd=5, highlightthickness=5,bg="#00ffff", fg="#347898", background="#70c5c2", foreground="#347898", highlightbackground='##ffebcd', highlightcolor='#48d1cc', anchor="center")
style.configure("temconConToolLight.TLabel", font=("Times New Roman", 11, "bold"), relief=tk.SUNKEN, takefocus=False, bd=(5, 0, 5, 0), highlightthickness=5,bg="#00ffff", fg="#347898", background="#4f788a", foreground="#00ffff", highlightbackground='##ffebcd', highlightcolor='#48d1cc', anchor="center")
style.configure("ScalesChoiceLight.TLabel",relief=tk.RAISED, direction="below", activebackground="#4f788a",  activeforeground="#00ffff", font=("Times New Roman", 11, "bold"),  background="#4f788a", foreground="#00ffff", highlightbackground='#4f788a', highlightcolor='#48d1cc', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("ScalesChoiceDark.TLabel",relief=tk.RAISED, direction="below", activebackground="#00ffff",  activeforeground="#347898", font=("Times New Roman", 11, "bold"),  background="#fb8604", foreground="#ffff00",  highlightbackground='#48d1cc', highlightcolor='#ffebcd', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("selectedScaleLableFrameLabelLight.TLabel",relief=tk.RAISED, direction="below", activebackground="#347898",  activeforeground="#00ffff", font=("Times New Roman", 11, "bold"),  background="#00ffff", foreground="#0a3f7c", highlightbackground='##ffebcd', highlightcolor='#48d1cc', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("convScalesChoiceLight.TLabel",relief=tk.RAISED, direction="below", activebackground="#3d9fe0",  activeforeground="#4f788", font=("Times New Roman", 11, "bold"),  background="#4f788a", foreground="#00ffff", highlightbackground='#3d9fe0', highlightcolor='#4f788', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("convertedScaleSelected.TLabel",relief=tk.RAISED, direction="below", activebackground="#ffff00",  activeforeground="#3d9fe0", font=("Times New Roman", 11, "bold"),  background="#70d38e", foreground="#008000",  highlightbackground='#48d1cc', highlightcolor='#3d9fe0', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("tested.TLabel",relief=tk.RAISED, direction="below", font=("Times New Roman", 14, "bold"), activebackground="#4f788a",  activeforeground="#00ffff",  background="#4f788a", foreground="#00ffff", highlightbackground='#4f788a', highlightcolor='#48d1cc', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("scaleSetButtonLight.TButton", relief=tk.RAISED, font=("Times New Roman", 11, "bold"), background="#4f788a", foreground="#00ffff", ipady=2, ipadx=5, highlightbackground='##ffebcd', highlightcolor='#48d1cc', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("scaleSetButtonDark.TButton", relief=tk.RAISED, font=("Times New Roman", 11, "bold"),  background="#fb8604", foreground="#ffff00", ipady=2, ipadx=5,   highlightbackground='#48d1cc', highlightcolor='#ffebcd', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("setTempLight.TEntry", background="#4f788a", foreground="#00ffff", insertionwidth=5, insertcolor="#00ffff", font=("Times New Roman", 14, "bold"), selectborderwidth=2, cursor="umbrella", relief=tk.SUNKEN, selectbackground="#99cfe7", selectforeground="#07597f", takefocus=True, fieldbackground="#347898", justify=CENTER, bordercolor="#5c3608")
style.configure("setTempDark.TEntry",  background="#fb8604", foreground="#ffff00", insertionwidth=5, insertcolor="#5c3608", font=("Times New Roman", 14, "bold"), selectborderwidth=2, cursor="umbrella", relief=tk.SUNKEN, selectbackground="#f3e1c9", selectforeground="#ec8c15", takefocus=True, fieldbackground="#fb8604", justify=CENTER, bordercolor="#5c3608")
style.configure("convertedFrameLight.TFrame",  relief=tk.FLAT, takefocus=False, pady=5, background="#00ffff")
style.configure("convertedFrameDark.TFrame",  relief=tk.FLAT, takefocus=False, background="#ffff00")
style.configure("lawfulLight.TFrame",  relief=tk.FLAT,takefocus=False, background="#ffe4c4")
style.configure("lawfulDark.TFrame",  relief=tk.FLAT,takefocus=False, background="burlywood")
style.configure("liveconvDark.TFrame", relief=tk.FLAT, takefocus=False, highlightthickness=0,bg="#00ffff", fg="#347898", background="#4f788a", foreground="#70c5c2", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("liveconvLight.TFrame", relief=tk.FLAT, takefocus=False,  highlightthickness=0,  bg="#347898", fg="#00ffff", background="#70c5c2", foreground="4f788a", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")
style.configure("scalesResponseFrameLight.TFrame", relief=tk.FLAT, takefocus=False,  ipady=5, highlightthickness=0,bg="#00ffff", fg="#347898", background="#00ffff", foreground="#347898", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("scalesResponseFrameDark.TFrame", relief=tk.FLAT, takefocus=False,  highlightthickness=0,  bg="#347898", fg="#00ffff", background="#347898", foreground="#00ffff", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")
style.configure("weatherFrameLight.TFrame", relief=tk.FLAT, takefocus=False, bd=0, highlightthickness=5,bg="#00ffff", fg="#347898", background="#4c7588", foreground="burlywood", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("weatherFrameDark.TFrame", relief=tk.FLAT, takefocus=False, bd=0, highlightthickness=5,  bg="#347898", fg="#00ffff", background="burlywood", foreground="#4c7588", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")
style.configure("temconLight.TLabel", font=("Times New Roman", 12, "bold"), background="#bb9f6a", foreground="#70c5c2", highlightbackground='#ffa500',  highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("temconDark.TLabel", font=("Times New Roman", 12, "bold"), background="#70c5c2", foreground="#bb9f6a", highlightbackground='#deb887',  highlightcolor='#c97911', highlightthickness=3, takefocus=True)
style.configure("heroFrameLabelLight.TLabel", relief=tk.FLAT, takefocus=False, bd=5, highlightthickness=5,bg="#00ffff", fg="#347898", background="#559492", foreground="#07597f", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("convertedScaleLableFrameLight.TLabel", relief=tk.FLAT, takefocus=False, ipadx=5, ipady=10, bg="#00ffff", fg="#347898", bd=5, highlightthickness=5, background="#347898", foreground="burlywood", highlightbackground='#ffff00', highlightcolor='#fb8604', anchor="center")
style.configure("convertedScaleLableFrameDark.TLabel", relief=tk.FLAT, takefocus=False,  ipadx=5, ipady=10, bg="#70c5c2", fg="#00ffff", bd=5, highlightthickness=5,  background="#fb8604", foreground="#ffff00", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")
style.configure("livedescLabelLight.TLabel", relief=tk.FLAT, takefocus=False, bd=5, highlightthickness=5,bg="#00ffff", fg="#347898", background="#4c7588", foreground="#6b9ac9", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("livedescLabelDark.TLabel", relief=tk.FLAT, takefocus=False, bd=5, highlightthickness=5,  bg="#347898", fg="#00ffff", background="#fb8604", foreground="#ffff00", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")
style.configure("livedescLabelLight1.TLabel", relief=tk.FLAT, takefocus=False, font=("Times New Roman", 12, "bold"), highlightthickness=5 ,bg="#00ffff", fg="#347898", background="#347898", foreground="#70c5c2", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("livedescLabelDark1.TLabel", relief=tk.FLAT, takefocus=False, font=("Times New Roman", 12, "bold"), highlightthickness=5,  bg="#347898", fg="#00ffff", background="#ffff00", foreground="#fb8604", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")

# ================================================================================================================================================================
# ============================================================== Styles Used In This Program =====================================================================
# ==== Note: Some styles may have attributes with values, that have not been properly assigned, for the most part it is the highlight colors, bg and anchor, i   =
# ====       find them intrusive with what i had styled, and while i tried to edit them the best i could, i found working with tkinter styling quite annoying in =
# ====       the vanilla form, so i often left them unfinished while i paid attention to issues, i thought to be of more importance, feel free to edit them as   =
# ====       you please, i will be looking to update in some form the way in which styles are being applied, as well as some other edits that i hope will make   =
# ====       the program more stable.    =========================================================================================================================                                                                                                                         ====
# ================================================================================================================================================================

# ================================================================================================================================================================
# ========================================================== End Of Conversion Styling ===========================================================================
# ================================================================================================================================================================

# Apps Menu to Open and Close TempCalc and to Exit the Program
apps_menu = tk.Menu(menu, tearoff = False, activeforeground="#d17c1a", activebackground="#5c3608", background="antiquewhite", foreground="#d17c1a")
apps_menu.add_command(label = "Live", command=lambda: showLive())
apps_menu.add_command(label = "Manual", command=lambda: showManual())
apps_menu.add_command(label = "Home", command=lambda: getMain())
apps_menu.add_command(label = "Exit", command = lambda: quit_main())
menu.add_cascade(label ="Apps", menu = apps_menu, foreground="#854c0c", background="burlywood", activebackground="antiquewhite", activeforeground="burlywood")
# info Menu to display the info page
info_menu = tk.Menu(menu, tearoff = False, activeforeground="antiquewhite", activebackground="#5c3608", background="antiquewhite", foreground="#5c3608")
info_menu.add_command(label = "Lawful Notice", command=lambda: open_privacy_window())
info_menu.add_command(label = "Contact", command=lambda: open_contact_window())
info_menu.add_command(label = "Donate", command=lambda: open_donate_window())
menu.add_cascade(label ="Info", menu = info_menu, activeforeground="antiquewhite", activebackground="#5c3608", background="antiquewhite", foreground="#5c3608")

# List of Function Calls

temp_var =BooleanVar()
temp_var = False

global choice
global temp


def display_selected(choice):
        choice = scale.get()
        scale.set(choice)
        scaleTemp.delete(0, END)
        clearManualTable()
        breakpoint

def store_selected(choice):
        choice = convScale.get()
        convScale.set(choice)
        live_city_temp_entry.delete(0, END)
        clearLiveTable()
        breakpoint
        

def getMain():
        window.geometry("314x347")
        clearLiveTable()
        liveconv_frame.grid_forget()
        manconv_frame.grid_forget()
        hero_frame.grid(row=1, column=0, columnspan=4)
        temcon_frame.grid(row=1, column=0, columnspan=4)
        breakpoint



def showLive():
        window.geometry("435x216")
        clearLiveTable()
        clearLiveWeather()
        manconv_frame.grid_forget()
        live_report_frame.grid_forget()
        temcon_frame.grid_forget()
        hero_frame.grid_forget()
        liveconv_frame.grid(row=1, column=0, columnspan=4)
        breakpoint



def showManual():
        window.geometry("282x292")
        clearManualTable()
        clearManualWeather()
        liveconv_frame.grid_forget()
        weather_report_frame.grid_forget()
        temcon_frame.grid_forget()
        hero_frame.grid_forget()
        manconv_frame.grid(row=1, column=0, columnspan=4)
        breakpoint


# Apps Menu Item to Exit the Program
def quit_main():
        window.quit()
        breakpoint



def clearLiveTable():
        live_city_temp_entry.delete(0, END)
        converted_temps_one_labelframe_label.configure(text="", style="convertedScaleLableFrameLableLight.TLabel")
        converted_temps_two_labelframe_label.configure(text="", style="convertedScaleLableFrameLableLight.TLabel")
        converted_temps_three_labelframe_label.configure(text="", style="convertedScaleLableFrameLableLight.TLabel")
        converted_temps_four_labelframe_label.configure(text="", style="convertedScaleLableFrameLableLight.TLabel")
        breakpoint


def clearManualTable():
        scaleTemp.delete(0, END)
        city_search_entry.delete(0, END)
        converted_scale_one_labelframe_label.configure(text="", style="convertedScaleLableFrameLableDark.TLabel")
        converted_scale_two_labelframe_label.configure(text="", style="convertedScaleLableFrameLableDark.TLabel")
        converted_scale_three_labelframe_label.configure(text="", style="convertedScaleLableFrameLableDark.TLabel")
        converted_scale_four_labelframe_label.configure(text="", style="convertedScaleLableFrameLableDark.TLabel")
        breakpoint



def clearLiveWeather():
        convScale.set(convScaleSet[0])
        live_city_temp_entry.insert(0, "Enter City Here")
        live_icon_label.pack_forget()
        live_city_label.configure(style="livedesclLabelLight.TLabel", text="", anchor="center", wraplength=100)
        live_desc_frame_label.configure(style="livedesclLabelLight.TLabel", text= "", anchor="center")
        live_temperature_label.configure(style="livedesclLabelLight.TLabel", font=("Times New Romant", 30, "bold"), text= "", anchor="center")
        breakpoint


def clearManualWeather():
        scaleTemp.delete(0, END)
        scale.set(scaleSet[0])
        weather_icon_label.pack_forget()
        city_search_entry.insert(0, "Enter City Here")
        city_label.configure(style="livedesclLabelDark.TLabel", text="", anchor="center", wraplength=100)
        description_frame_label.configure(style="livedesclLabelDark.TLabel", text= "", anchor="center")
        temperature_label.configure(style="livedesclLabelDark.TLabel", font=("Times New Romant", 30, "bold"), text= "", anchor="center")
        breakpoint


# ======================================================================================================================================
# ================================================================ Start Main Frame Layout =============================================
# ======================================================================================================================================

temcon_program_frame = tk.Frame(master=window)
temcon_program_frame.pack(fill="both", expand=False, side="top", anchor="center", ipadx=5)
tup_frame = tk.Frame(master=temcon_program_frame)
tup_frame.configure()
tup_frame.grid(row=0, column=0, columnspan=4)
tup_label_title = ttk.Label(tup_frame)
tup_label_title.configure(text="TEMPERATURE CONVERSION TOOL", style="temconConToolLight.TLabel", anchor="center") 
tup_label_title.grid(row=0, column=0, columnspan=4, ipadx=5, ipady=5, sticky="ew")
temcon_frame = tk.Frame(master=tup_frame)
temcon_frame.configure(bg="#4f788a")
temcon_labelframe = ttk.LabelFrame(master = temcon_frame, text="TEMCON", height=100, width=150)
temcon_labelframe.configure(style="tested.TLabel")
temcon_labelframe.grid(row=0, column=0, columnspan=2, sticky=tk.N, pady=5, padx=5)

# ============= Logo in a Canvas ======================#
temcon_banner = Image.open("imgs/tc2024Logo.png")
image_ratio = temcon_banner.size[0] / temcon_banner.size[1]
temconbannertk = ImageTk.PhotoImage(temcon_banner)
canvas4 = tk.Canvas(temcon_labelframe, background="#219399", width=120, height=100, bd=2, highlightthickness=2, relief="ridge")
canvas4.grid(row=0, column=0)
canvas4.create_image(60,50, image = temconbannertk)

# Openweather
weather_labelframe = ttk.LabelFrame(master =temcon_frame, text="OPENWEATHER", height=90, width=150)
weather_labelframe.configure(style="tested.TLabel")
weather_labelframe.grid(row=0, column=2, columnspan=2, sticky=tk.N, pady=5, padx=5)

# ============= Logo in a Canvas ======================#
weather_logo = Image.open("imgs/OWM_logo.png")
image_ratio = weather_logo.size[0] / weather_logo.size[1] * .75
weather_logotk = ImageTk.PhotoImage(weather_logo)
canvas3 = tk.Canvas(weather_labelframe, background="#219399", width=150, height=100, bd=2, highlightthickness=2, relief="ridge")
canvas3.grid(row=0, column=0)
canvas3.create_image(80,50, image = weather_logotk)

# Sponsored Advertising Frame
hero_frame = tk.Frame(temcon_frame)
hero_frame.configure(relief="flat", bg="#519fd2")
hero_frame.grid(row=1, column=0, columnspan=4, rowspan=2, sticky="nsew")
# Sponsored Advertiseing Label
hero_frame_label = ttk.Label(hero_frame)
hero_frame_label.configure(style="heroFrameLabelLight.TLabel", font=("Roboto, sans-serif", 7, "bold"), text="Jeanette's Impressions Art\njeanette.elizabeth@dashwoorkz.ca\nCommunity Services Director", justify="center", anchor="center")
hero_frame_label.grid(row=0, column=0, columnspan=3, ipady=8, padx=8, ipadx=8, sticky="w")

# ============= Logo in a Canvas ======================#
jeia_logo = Image.open("imgs/jeia.png")
image_ratio = jeia_logo.size[0] / jeia_logo.size[1]
jeia_logotk = ImageTk.PhotoImage(jeia_logo)
canvas5 = tk.Canvas(hero_frame, background="#219399",  width=70, height=50, bd=2, highlightthickness=2, relief="ridge")
canvas5.grid(row=0, column=3, sticky="en", padx=8, pady=5)
canvas5.create_image(40,30, image = jeia_logotk)

feedback_frame = tk.Frame(master=hero_frame)
feedback_frame.configure(bg="#4f788a")
feedback_frame.grid(row=1, column=0, columnspan=4, padx= 2)

# ============= Logo  in a Canvas ======================#
dss_logo = Image.open("imgs/dss_logo.png")
image_ratio = dss_logo.size[0] / dss_logo.size[1]
dss_logotk = ImageTk.PhotoImage(dss_logo)
canvas6 = tk.Canvas(feedback_frame, background="#219399",  width=90, height=90, bd=2, highlightthickness=2, relief="ridge")
canvas6.grid(row=0, column=0, pady=5, padx=5, sticky="w")
canvas6.create_image(50,50, image = dss_logotk)

feedback_frame_label = ttk.Label(master=feedback_frame)
feedback_frame_label.configure(style="heroFrameLabelLight.TLabel", font=("Roboto, sans-serif", 7, "bold"), wraplength=155, anchor="center", justify="center", text="FeedBack:\ndashWoorkZ Sovereign Society would welcome any comments or suggestions.\n Email: dashwoorkz@dashwoorkz.ca")
feedback_frame_label.grid(row=0, column=1, padx=5, ipadx=10, ipady=5, sticky="w")
temcon_frame.grid(row=1, column=0, columnspan=4, rowspan=2, sticky="nsew")

# ================================================================================================================================================================
# ================================================================ End Main Frame Layout =========================================================================
# ================================================================================================================================================================

# ================================================================================================================================================================
# =====================================================Start  Live Temperature Conversion Frame Layout ===========================================================
# ================================================================================================================================================================

liveconv_frame = tk.Frame(master=tup_frame)
liveconv_frame.configure(bg="#4f788a")
# Openweather Program
live_report_frame = tk.Frame(master = liveconv_frame)
live_report_frame.configure(borderwidth=5, bg="#519fd2", highlightthickness=0, highlightbackground='#8fbc8f', highlightcolor='#1e90ff')
live_report_frame.grid(row=0, column=0, columnspan=4, sticky="ns", padx=10)
# Weather Frame - Temperature Reported and City
live_temperature = ttk.Frame(master = live_report_frame)
live_temperature.configure(style="weatherFrameLight.TFrame")
live_temperature.pack(fill="both", expand=True, side="left", padx=5, pady=5)
live_city_label = ttk.Label(master = live_temperature)
live_city_label.pack(fill="both", expand=True, side="top")
live_temperature_label = ttk.Label(master = live_temperature)
live_temperature_label.pack(fill="both", expand=True, side="bottom")
# Description of weather and weather icon
live_desc_frame = ttk.Frame(master = live_report_frame)
live_desc_frame.configure(style="weatherFrameLight.TFrame")
live_desc_frame.pack(fill="both", expand=True, side="right", padx=5, pady=5)
live_icon_label = ttk.Label(master = live_desc_frame)
live_icon_label.pack(fill="both", expand=True, side="top")
live_desc_frame_label = ttk.Label(master = live_desc_frame)
live_desc_frame_label.pack(fill="both", expand=True, side="bottom") 
liveconv_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")  

live_desc_frame.lower()
live_icon_label.lift()

live_report_frame.columnconfigure(0, weight=1)
live_report_frame.rowconfigure(0, weight=1)
live_report_frame.columnconfigure(1, weight=1)
live_report_frame.rowconfigure(1, weight=1)
live_report_frame.columnconfigure(1, weight=1)
live_report_frame.rowconfigure(1, weight=1)
live_report_frame.columnconfigure(1, weight=1)
live_report_frame.rowconfigure(1, weight=1)

def tempError675():
        error_screen_window = Toplevel(window)
        error_screen_window.title("!!!Error 675 !!!")
        width = 350
        height = 300
        x = (error_screen_window.winfo_screenwidth()//2)-(width//2)
        y = (error_screen_window.winfo_screenheight()//2)-(height//2)
        error_screen_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        error_screen_window.configure(bg="#f0f0f0")
        error_label = tk.Label(master = error_screen_window)
        error_label.configure(bg="#ca8888", fg="#9932cc", font=("Roboto, sans-serif", 14, "bold"), wraplength=290,  text="!!!Error 675 !!!\n!!! Temperature Not Entered !!!\n Enter A Temperature to Convert!!")
        error_label.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5)


def scaleError629():
        error_screen_window = Toplevel(window)
        error_screen_window.title("!!! Error !!!")
        width = 300
        height = 300
        x = (error_screen_window.winfo_screenwidth()//2)-(width//2)
        y = (error_screen_window.winfo_screenheight()//2)-(height//2)
        error_screen_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        error_screen_window.configure(bg="#f0f0f0")
        error_label = tk.Label(master = error_screen_window)
        error_label.configure(bg="#ca8888", fg="#9932cc", font=("Roboto, sans-serif", 14, "bold"), wraplength=290,  text="!!! Error !!!\n!!! Scale Not Entered !!!\nPlease Choose A Scale To Convert!!")
        error_label.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5)



def cityError642():
        error_screen_window = Toplevel(window)
        error_screen_window.title("!!! Error 642 !!!")
        error_screen_window.configure(bg="#f0f0f0")
        width = 375
        height = 200
        x = (error_screen_window.winfo_screenwidth()//2)-(width//2)
        y = (error_screen_window.winfo_screenheight()//2)-(height//2)
        error_screen_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        error_label = tk.Label(master = error_screen_window)
        error_label.configure(bg="#ca8888", fg="#9932cc", font=("Roboto, sans-serif", 14, "bold"), wraplength=290,  text="!!! Error 642 !!!\n!!! City Not Entered !!!\nPlease Choose A City To Get The Current Weather Information!!")
        error_label.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5)


def completeError700():
        error_screen_window = Toplevel(window)
        error_screen_window.title("!!! Error 642 !!!")
        error_screen_window.configure(bg="#f0f0f0")
        width = 375
        height = 200
        x = (error_screen_window.winfo_screenwidth()//2)-(width//2)
        y = (error_screen_window.winfo_screenheight()//2)-(height//2)
        error_screen_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        error_label = tk.Label(master = error_screen_window)
        error_label.configure(bg="#ca8888", fg="#9932cc", font=("Roboto, sans-serif", 14, "bold"), wraplength=290,  text="!!! Error 642 !!!\n!!! City Not Entered !!!\nPlease Choose A Scale and enter a temperature To Convert!!")
        error_label.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5)


# Attempt at creating a function that gets the city and city temperature 
# and then displays the city and city temperature and the temperature is used to activate the conversion table
#Live Weather Report Frame
# This Weather App is brought to you in part by "Alina Chudnova" from her Youtube Video "Create A Weather App using Python | tutorial for Beginners"
# https://www.youtube.com/watch?v=VaqYFs7Az50

APIKEY = StringVar()
APIKEY = ""

def checkLiveSelected():
        scale = tk.StringVar()
        scale = convScale.get()
        city = tk.StringVar()
        city = live_city_temp_entry.get()
        if scale == "Choose A Scale":
                scaleError629()  
                return  
        elif city == "":
                cityError642()
                return
        else:
                searchTemp()
                breakpoint


# =========================
def get_temperature(city):
        API_key = APIKEY
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
        res = requests.get(url)

        if res.status_code == 404:
                messagebox.showerror("Error", "City Not Found")
                return None
        # Parse the response JSON to get weather information
        weather = res.json()
        icon_id = weather['weather'][0]['icon']
        temperature = weather['main']['temp']
        description = weather['weather'][0]['description']
        city = weather['name']
        country = weather['sys']['country']
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
        return (icon_url, temperature, description, city, country)


# Search weather for a city
def searchTemp():
        city = live_city_temp_entry.get()
        result = get_temperature(city)
        if result is None:
                return
        # if the city is found, unpack the weather information
        icon_url, temperature, description, city, country = result
        icon = ImageTk.PhotoImage(Image.open(requests.get(icon_url, stream=True).raw))
        live_icon_label.configure(style="livedescLabelLight.TLabel", anchor="center", image=icon)
        live_icon_label.pack(fill="both", expand=True, side="top")
        live_icon_label.image = icon
        
        # Get the weather icon
        live_city_label.configure(style="livedescLabelLight1.TLabel", text=f"{city}, {country}", anchor="center", justify="center", wraplength=100)
        live_desc_frame_label.configure(style="livedescLabelLight1.TLabel", text= f"{description}", anchor="center", justify="center")
        window.geometry("415x365")
        live_report_frame.grid(row=0, column=0, columnspan=4, rowspan=2, sticky="nsew")
        ScaleConverted = convScale.get()
        temp = IntVar()
        temp = round((temperature), 1)


        if ScaleConverted == "Kelvin":
                convTemp = round(temp * 1, 1)
                live_temperature_label.configure(style="livedescLabelLight.TLabel", font=("Times New Romant", 20, "bold"), text= f"{convTemp}K", anchor="center")
                converted_temps_one_labelframe_label.configure(style="selectedScaleLableFrameLabelLight.TLabel", text= round(convTemp * 1, 1), width=7, anchor='center', justify="center")
                converted_temps_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(((convTemp - 273.15) * 1.8) + 32, 1), width=7, anchor='center', justify="center")
                converted_temps_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(convTemp - 273.15, 1), width=7, anchor='center', justify="center")
                converted_temps_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(convTemp + 491.67, 1), width=7, anchor='center', justify="center")
                return convScale.set(convScaleSet[0]) 
                
                
        elif ScaleConverted == "Fahrenheit":
                convTemp = round(((temp - 273.15) * 1.8) + 32, 1)
                live_temperature_label.configure(style="livedescLabelLight.TLabel", font=("Times New Romant", 20, "bold"), text= f"{convTemp}F", anchor="center")
                converted_temps_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(((convTemp - 32) / 1.79999999) + 273.15, 1), width=7, anchor='center', justify="center")
                converted_temps_two_labelframe_label.configure(style="selectedScaleLableFrameLabelLight.TLabel", text= round(convTemp * 1, 1), width=7, anchor='center', justify="center")
                converted_temps_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round((convTemp - 32) * (5/9), 1),  width=7, anchor='center', justify="center")
                converted_temps_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(convTemp + 459.67, 1) ,width=7, anchor='center', justify="center")
                return convScale.set(convScaleSet[0]) 


        elif ScaleConverted == "Rankine":
                convTemp = round(((temp - 273.15) * 1.8) + 491.67, 1)
                live_temperature_label.configure(style="livedescLabelLight.TLabel", font=("Times New Romant", 20, "bold"), text= f"{convTemp}R", anchor="center")
                converted_temps_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(((convTemp- 491.67) / 1.79999999) + 273.15, 1), width=7, anchor='center', justify="center")
                converted_temps_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(convTemp - 459.67, 1), width=7, anchor='center', justify="center")
                converted_temps_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round((convTemp - 491.67) / 1.79999999, 1), width=7, anchor='center', justify="center")
                converted_temps_four_labelframe_label.configure(style="selectedScaleLableFrameLabelLight.TLabel", text= round(convTemp * 1, 1), width=7, anchor='center', justify="center")
                return convScale.set(convScaleSet[0]) 


        elif ScaleConverted == "Celcius":
                convTemp = round(temp - 273.15, 1)
                live_temperature_label.configure(style="livedescLabelLight.TLabel", font=("Times New Romant", 20, "bold"), text= f"{convTemp}C", anchor="center")
                converted_temps_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(convTemp  + 273.15, 1), width=7, anchor='center', justify="center")
                converted_temps_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round((convTemp  * (9/5)) + 32, 1), width=7, anchor='center', justify="center")
                converted_temps_three_labelframe_label.configure(style="selectedScaleLableFrameLabelLight.TLabel", text= round(convTemp * 1, 1) , width=7, anchor='center', justify="center")
                converted_temps_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round((convTemp * 1.8) + 459.67, 1), width=7, anchor='center', justify="center")
                return convScale.set(convScaleSet[0]) 
                
global clear
clear = ""


def clearCity(clear):
        clear = StringVar()
        clear = live_city_temp_entry.delete(0, tk.END)
        
        

temp_response_frame = ttk.Frame(master = liveconv_frame)
temp_response_frame.configure(style="liveconvDark.TFrame", borderwidth=5)
temp_response_frame.grid(row=2, column=0, columnspan=3, rowspan=4, sticky="nsew")
temp_frame = ttk.Frame(master = temp_response_frame)
temp_frame.configure(style="convertedFrameLight.TFrame")
temp_frame.pack(fill="both", expand=False, side="top", anchor="center")
cityButton_frame = ttk.Frame(master = temp_frame)
cityButton_frame.configure(style="convertedFrameLight.TFrame")
cityButton_frame.pack(fill="x", expand=False, side="top")
city_description_label = ttk.Label(cityButton_frame)
city_description_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= "Live City Weather Report", anchor='center', justify="center")
city_description_label.pack(fill="x", expand=False, side="top", ipady=5)
live_city_temp_entry = ttk.Entry(master = cityButton_frame)
live_city_temp_entry.configure(style="setTempLight.TEntry", justify="center", text="Enter City Here")
live_city_temp_entry.pack(fill="both", expand=False, side="left")
live_city_temp_entry.bind("<FocusIn>", clearCity)
temp_response_frame.columnconfigure(0, weight=1)
temp_response_frame.rowconfigure(0, weight=1)
temp_response_frame.columnconfigure(1, weight=1)
temp_response_frame.rowconfigure(1, weight=1)
temp_response_frame.columnconfigure(1, weight=1)
temp_response_frame.rowconfigure(1, weight=1)


# creating Option Menu widget
convScaleSet = ['Choose A Scale','Celcius','Fahrenheit', 'Kelvin', 'Rankine']
# setting variable for Integers and Strings
convScale = StringVar()
convScale.set(convScaleSet[0])
convScales = ttk.OptionMenu(
cityButton_frame,
convScale,
*convScaleSet,
command=store_selected
)
convScales.configure(style="convScalesChoiceLight.TLabel", width=20)
convScales.pack(fill="both", expand=True, side="left", ipady=5, anchor="center", before=live_city_temp_entry)
live_city_Search_button = ttk.Button(master = cityButton_frame)
live_city_Search_button.configure(style="scaleSetButtonLight.TButton", takefocus=True, command=checkLiveSelected, text="Get Temp")
live_city_Search_button.pack(fill="y", expand=False, side="right", anchor="ne")
#Converted temp Frame
converted_temps_frame = ttk.Frame(master = temp_frame)
converted_temps_frame.configure(style="scalesResponseFrameLight.TFrame")
converted_temps_frame.pack(fill='both', expand=True, side="bottom", anchor="center")
converted_temps_one_labelframe = ttk.LabelFrame(master = converted_temps_frame)
converted_temps_one_labelframe.configure(style="convertedScaleLableFrameLight.TLabel", text="  Kelvin ", width=7)
converted_temps_one_labelframe.pack(fill="both", expand=True, side="left")
converted_temps_one_labelframe_label = ttk.Label(master = converted_temps_one_labelframe)
converted_temps_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= "", width=7, anchor='center', justify="center")
converted_temps_one_labelframe_label.pack(fill="both", expand=True, side="bottom")
converted_temps_two_labelframe = ttk.LabelFrame(master = converted_temps_frame)
converted_temps_two_labelframe.configure(style="convertedScaleLableFrameLight.TLabel", text=" Fahrenheit ", width=7)
converted_temps_two_labelframe.pack(fill="both", expand=True, side="top", ipady=5)
converted_temps_two_labelframe_label = ttk.Label(converted_temps_two_labelframe)
converted_temps_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= "", width=7, anchor='center', justify="center")
converted_temps_two_labelframe_label.pack(fill="both", expand=True, side="bottom")
converted_temps_three_labelframe = ttk.LabelFrame(master = converted_temps_frame)
converted_temps_three_labelframe.configure(style="convertedScaleLableFrameLight.TLabel", text=" Celcius ", width=7)
converted_temps_three_labelframe.pack(fill="both", expand=True, side="right")
converted_temps_three_labelframe_label = ttk.Label(converted_temps_three_labelframe)
converted_temps_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= "", width=7, anchor='center', justify="center")
converted_temps_three_labelframe_label.pack(fill="both", expand=True, side="bottom", ipady=5)
converted_temps_four_labelframe = ttk.LabelFrame(master = converted_temps_frame)
converted_temps_four_labelframe.configure(style="convertedScaleLableFrameLight.TLabel", text=" Rankine ", width=7)
converted_temps_four_labelframe.pack(fill="both", expand=True, side="right")
converted_temps_four_labelframe_label = ttk.Label(master = converted_temps_four_labelframe)
converted_temps_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= "", width=7, anchor="center", justify="center")
converted_temps_four_labelframe_label.pack(fill="both", expand=True, side="bottom", ipady=5)

temp_response_frame.rowconfigure(0, weight = 1)
temp_response_frame.columnconfigure(0, weight = 1)
temp_response_frame.rowconfigure(1, weight = 1)
temp_response_frame.columnconfigure(1, weight = 1)
temp_response_frame.rowconfigure(2, weight = 1)
temp_response_frame.columnconfigure(2, weight = 1)

# ================================================================================================================================================================
# ===================================================== End of Live Conversion Layout ============================================================================
# ================================================================================================================================================================

# ================================================================================================================================================================
# ================================================= Start of Manual Conversion Layout ============================================================================
# ================================================================================================================================================================

# Temcon and Open Weather Programs
# Openweather Program
manconv_frame = ttk.Frame(master=tup_frame)
manconv_frame.configure(style="weatherFrameDark.TFrame")
manconv_frame.grid(row=1, column=0, columnspan=4)
manual_frame = ttk.Frame(master=manconv_frame)
manual_frame.configure(style="weatherFrameDark.TFrame")
weather_report_frame = ttk.Frame(master = manual_frame)
weather_report_frame.configure(style="temconDark.TFrame")
weather_report_frame.grid(row=0, column=0, columnspan=4, rowspan=2, sticky="nsew")
# Description of weather and weather icon
description_frame = ttk.Frame(master = weather_report_frame)
description_frame.configure(style="weatherFrameDark.TFrame")
description_frame.pack(fill="both", expand=True, side="left", anchor="center")
weather_icon_label = ttk.Label(master = description_frame)
weather_icon_label.pack(fill="both", expand=True, side="top", anchor="center")
# Description Frame - Description of Weather and Weather
description_frame_label = ttk.Label(master = description_frame)
description_frame_label.pack(fill="x", expand=False, side="bottom", ipady=5, ipadx=5)
# Weather Frame - Temperature Reported and City
weather_frame = ttk.Frame(master = weather_report_frame)
weather_frame.configure(style="temconDark.TLabel")
weather_frame.pack(fill="both", expand=True, side="right", anchor="center")
city_label = ttk.Label(master = weather_frame)
city_label.pack(fill="both", expand=True, side="top", anchor="center", ipadx=5)
temperature_label = ttk.Label(master = weather_frame)
temperature_label.pack(fill="both", expand=True, side="bottom", ipadx=5)
manual_frame.pack(fill="both", expand=True, side="top", anchor="center")

description_frame.lower()
weather_icon_label.lift()

# This Weather App is brought to you in part by "Alina Chudnova" from her Youtube Video "Create A Weather App using Python | tutorial for Beginners"
# https://www.youtube.com/watch?v=VaqYFs7Az50
# Weather Report Frame
def checkManualSelected():
        scale = tk.StringVar()
        scale = scale.get()
        temp = tk.StringVar()
        temp = scaleTemp.get()
        if temp == '':
                tempError675()
                return
        else:
                setScaleTemp()
                breakpoint

def checkCity():
        city = tk.StringVar()
        city = city_search_entry.get()
        if city == "":
                cityError642()
                return
        else:
                search()
                breakpoint

def get_weather(city):
        API_key = APIKEY
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
        res = requests.get(url)

        if res.status_code == 404:
                messagebox.showerror("Error", "City Not Found")
                return None
        # Parse the response JSON to get weather information
        weather = res.json()
        icon_id = weather['weather'][0]['icon']
        temperature = weather['main']['temp'] - 273.15
        description = weather['weather'][0]['description']
        city = weather['name']
        country = weather['sys']['country']
        #Get the icon URL and return all the weather information
        icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
        return (icon_url, temperature, description, city, country)


# Search weather for a city
def search():
        city = city_search_entry.get()
        result = get_weather(city)
        if result is None:
                return
        # if the city is found, unpack the weather information
        icon_url, temperature, description, city, country = result
        # Get the weather icon
        icon = ImageTk.PhotoImage(Image.open(requests.get(icon_url, stream=True).raw))   
        weather_icon_label.configure(style="livedescLabelDark.TLabel", anchor="center", image=icon)
        weather_icon_label.pack(fill="x", expand=False, side="top", anchor="center")
        weather_icon_label.image = icon
        city_label.configure(style="livedescLabelDark1.TLabel", text=f"{city}, {country}", anchor="center")
        description_frame_label.configure(style="livedescLabelDark1.TLabel", text= f"{description}", anchor="center")
        temperature_label.configure(style="livedescLabelDark.TLabel", font=("Times New Romant", 30, "bold"), text= f"{round(int(temperature))}C", anchor="center")
        window.geometry("283x430")
        weather_report_frame.grid(row=0, column=0, columnspan=4,sticky="nsew")
        city_search_entry.delete(0, tk.END)

# Scale Temperature Setting

# Function retrieves the Scale Chosen and the Temperature to convert, then displays the Conversion Table
def setScaleTemp():
        if temp_var == True:
                choice = scale.set[0]
                temp = main.temp.get()           
                converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text=int(temp)  + 273.15, width=7, anchor='center', justify="center")
                converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= (int(temp)  * (9/5) + 32), width=7, anchor='center', justify="center")
                converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= int(temp) * 1, width=7, anchor='center', justify="center")
                converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text=((int(temp) * 1.8) + 459.67), width=7, anchor='center', justify="center")
                scales_response_frame.pack( fill="x", expand=True)
                return
        else: 
                choice = scale.get()
                temp = scaleTemp.get()
                if choice == 'Choose A Scale':
                        scaleError629()
                        return
                elif choice == "Kelvin":
                        converted_scale_one_labelframe_label.configure(style="convertedScaleSelected.TLabel", text= round(int(temp) * 1, 2), width=7, anchor='center', justify="center")
                        converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(((int(temp) - 273.15) * 1.8) + 32, 2), width=7, anchor='center', justify="center")
                        converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp) - 273.15, 1), width=7, anchor='center', justify="center")
                        converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp) + 491.67, 1), width=7, anchor='center', justify="center")
                        scales_response_frame.pack( fill="x", expand=True)
                        return
                        
                elif choice == "Fahrenheit":
                        converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(((int(temp) - 32) / 1.79999999) + 273.15, 2), width=7, anchor='center', justify="center")
                        converted_scale_two_labelframe_label.configure(style="convertedScaleSelected.TLabel", text= round(int(temp) * 1, 1), width=7, anchor='center', justify="center")
                        converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round((int(temp) - 32) * (5/9), 2),  width=7, anchor='center', justify="center")
                        converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp) + 459.67, 2) ,width=7, anchor='center', justify="center")
                        scales_response_frame.pack( fill="x", expand=True)
                        return

                elif choice == "Rankine":
                        converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(((int(temp)- 491.67) / 1.79999999) + 273.15, 2), width=7, anchor='center', justify="center")
                        converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp) - 459.67, 2), width=7, anchor='center', justify="center")
                        converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round((int(temp) - 491.67) / 1.79999999, 2), width=7, anchor='center', justify="center")
                        converted_scale_four_labelframe_label.configure(style="convertedScaleSelected.TLabel", text= round(int(temp) * 1, 1), width=7, anchor='center', justify="center")
                        scales_response_frame.pack( fill="x", expand=True)
                        return
                
                elif choice == "Celcius":
                        converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp)  + 273.15, 2), width=7, anchor='center', justify="center")
                        converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp)  * (9/5) + 32, 2), width=7, anchor='center', justify="center")
                        converted_scale_three_labelframe_label.configure(style="convertedScaleSelected.TLabel", text= round(int(temp) * 1, 2) , width=7, anchor='center', justify="center")
                        converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round((int(temp) * 1.8) + 459.67, 2), width=7, anchor='center', justify="center")
                        scales_response_frame.pack( fill="x", expand=True)
                        return


        # Math note: Source of information regarding Rounding Numbers in Python : https://bobbyhadz.com/blog/python-round-float-3-decimal-places
        
                 
def clearManCity(clear):
        clear = StringVar()
        clear = city_search_entry.delete(0, tk.END)
        
        
# Main Frame
temperature_frame = ttk.Frame(master = manual_frame)
temperature_frame.configure(style="convertedFrameDark.TFrame") 
temperature_frame.grid(row=1, column=0, columnspan=4, rowspan=4, sticky="nsew")
# ========= Manual City Search Frame Start =======================
manual_search_frame = ttk.Frame(master = temperature_frame)
manual_search_frame.configure(style="convertedFrameDark.TFrame") 
manual_search_frame.pack(fill="both", expand=True, side="top")
city_description_label = ttk.Label(manual_search_frame)
city_description_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= "Manual City Weather Report", anchor='center', justify="center")
city_description_label.pack(fill="x", expand=False, side="top", ipady=5) 
city_search_entry = ttk.Entry(master = manual_search_frame)
city_search_entry.configure(style="setTempDark.TEntry", justify="center") 
city_search_entry.pack(fill="both", expand=True, side="left", anchor="nw")
city_search_entry.bind("<FocusIn>", clearManCity)
citySearch_button = ttk.Button(master = manual_search_frame)
citySearch_button.configure(style="scaleSetButtonDark.TButton", takefocus=True, command=lambda: checkCity(), text="Search")
citySearch_button.pack(fill="y", expand=True, side="right", anchor="ne")
# =========  Scale Choice Frame Start =======================


scaleChoice_title = ttk.Frame(master = temperature_frame)
scaleChoice_title.configure(style="convertedFrameDark.TFrame")
scaleChoice_title.pack(fill="both", expand=True, side="top")
scaleChoice_label = ttk.Label(scaleChoice_title)
scaleChoice_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text='Enter a Number To Convert', justify="center", anchor="center")
scaleChoice_label.pack(fill="x", expand=True, side="right", ipady=5)
# =========  Temperature Setting Frame Start =================
scaleChoice = ttk.Frame(master = temperature_frame)
scaleChoice.configure(style="convertedFrameDark.TFrame")
scaleChoice.pack(fill="both", expand=True, side="top")                        
temperature_setting_frame = ttk.Frame(master = scaleChoice) 
temperature_setting_frame.configure(style="convertedFrameDark.TFrame")
temperature_setting_frame.pack(side="top", fill="both", expand=True)
scaleSet_button = ttk.Button(master = temperature_setting_frame)
scaleSet_button.configure(style="scaleSetButtonDark.TButton", takefocus=True, command=lambda: checkManualSelected(), text="Convert")
scaleSet_button.pack(fill="x", expand=False, padx=(3, 0), side="right")
# Scale Temperature Setting ===================================
scaleTemp = ttk.Entry(master = temperature_setting_frame)
scaleTemp.configure(style="setTempDark.TEntry", width=4, justify="center") 
scaleTemp.pack(fill="x", expand=False, padx=3, side="right", ipadx=2, ipady=2)
# creating Option Menu widget ==================================
scaleSet = ['Choose A Scale','Celcius','Fahrenheit', 'Kelvin', 'Rankine']
# setting variable for Integers and Strings ========================
scale = StringVar()
scale.set(scaleSet[0])
scales = ttk.OptionMenu(
temperature_setting_frame,
scale,
*scaleSet,
command=display_selected)
scales.configure(style="ScalesChoiceDark.TLabel", width=7)
scales.pack(fill="both", expand=True, side="left", ipady=5, ipadx=5, anchor="center")
# ====== Scales Conversion Frame 
scales_response_frame = ttk.Frame(master = scaleChoice)
scales_response_frame.configure(style="scalesResponseFrameDark.TFrame")
scales_response_frame.pack( fill="both", expand=True, ipady=5)
setTemp = StringVar()
temp = 0

def setTemp(temp):
        temp = round(setTemp)

        
#Converted Scales Frame
converted_scales_frame = ttk.Frame(master = scales_response_frame)
converted_scales_frame.configure(style="scalesResponseFrameDark.TFrame")
converted_scales_frame.pack(fill='both', expand=True, ipady=3, side="bottom", anchor="center")
# Converted Scale Kelvin
converted_scale_one_labelframe = ttk.LabelFrame(master = converted_scales_frame)
converted_scale_one_labelframe.configure(style="convertedScaleLableFrameDark.TLabel", text="  Kelvin ", width=7)
converted_scale_one_labelframe.pack(fill="both", expand=True, side="left", ipady=5)
converted_scale_one_labelframe_label = ttk.Label(master = converted_scale_one_labelframe)
converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= "", justify="center", width=7)
converted_scale_one_labelframe_label.pack(fill="both", expand=True, side="bottom")
# Converted Scale Fahrenheit
converted_scale_two_labelframe = ttk.LabelFrame(master = converted_scales_frame)
converted_scale_two_labelframe.configure(style="convertedScaleLableFrameDark.TLabel", text=" Fahrenheit ", width=7)
converted_scale_two_labelframe.pack(fill="both", expand=True, side="top", ipady=5)
converted_scale_two_labelframe_label = ttk.Label(converted_scale_two_labelframe)
converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text="", justify="center", width=7)
converted_scale_two_labelframe_label.pack(fill="both", expand=True, side="bottom")
# Converted Scale Celcius
converted_scale_three_labelframe = ttk.LabelFrame(master = converted_scales_frame)
converted_scale_three_labelframe.configure(style="convertedScaleLableFrameDark.TLabel", text=" Celcius ", width=7)
converted_scale_three_labelframe.pack(fill="both", expand=True, side="right")
converted_scale_three_labelframe_label = ttk.Label(converted_scale_three_labelframe)
converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= "", justify="center", width=7)
converted_scale_three_labelframe_label.pack(fill="both", expand=True, side="bottom", ipady=5)
# Converted Scale Rankine
converted_scale_four_labelframe = ttk.LabelFrame(master = converted_scales_frame)
converted_scale_four_labelframe.configure(style="convertedScaleLableFrameDark.TLabel", text=" Rankine ", width=7)
converted_scale_four_labelframe.pack(fill="both", expand=True, side="right")
converted_scale_four_labelframe_label = ttk.Label(master = converted_scale_four_labelframe)
converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= "", justify="center", width=7)
converted_scale_four_labelframe_label.pack(fill="both", expand=True, side="bottom", ipady=5)

temperature_frame.rowconfigure(0, weight = 1)
temperature_frame.columnconfigure(0, weight = 1)
temperature_frame.rowconfigure(1, weight = 1)
temperature_frame.columnconfigure(1, weight = 1)
temperature_frame.rowconfigure(2, weight = 1)
temperature_frame.columnconfigure(2, weight = 1)
temperature_frame.rowconfigure(3, weight = 1)
temperature_frame.columnconfigure(3, weight = 1)

scales_response_frame.rowconfigure(0, weight = 1)
scales_response_frame.columnconfigure(0, weight = 1)
scales_response_frame.rowconfigure(1, weight = 1)
scales_response_frame.columnconfigure(1, weight = 1)
scales_response_frame.rowconfigure(2, weight = 1)
scales_response_frame.columnconfigure(2, weight = 1)

# ================================================================================================================================================================
# =================================================== End of Manual Conversion Layout ============================================================================
# ================================================================================================================================================================

        # Donation Window
def open_privacy_window():
        lawful_privacy_window = Toplevel(window)
        lawful_privacy_window.title("lawful_privacy")
        width = 313
        height = 572
        x = (lawful_privacy_window.winfo_screenwidth()//2)-(width//2)
        y = (lawful_privacy_window.winfo_screenheight()//2)-(height//2)
        lawful_privacy_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        lawful_privacy_window.configure(bg="#f0f0f0")
        # Lawful Privacy Statement
        lawful_privacy_frame = ttk.Frame(master=lawful_privacy_window)
        lawful_privacy_frame.configure(style="lawfulLight.TFrame")
        privacy_frame = ttk.Frame(master=lawful_privacy_frame)
        privacy_frame.configure(style="privacyLight.TFrame")
        privacy_frame_label = ttk.Label(master=privacy_frame)
        privacy_frame_label.configure(style="privacyLight.TLabel", font=("Times New Roman", 10, "bold"), anchor="center", justify="center", wraplength=290, text="dashWoorkz Sovereign Society\n is a Private Society, we will not invade Your Privacy, or provide anyone any information we may have about you, any information we have about you will have been acquired with Your Consent, if we were to do anything with the information we have about you, it would be with Your Consent")
        privacy_frame_label.pack(fill="x", expand="True", side="top")
        privacy_frame.pack(fill="both", expand=True)
        lawful_frame = ttk.Frame(master=lawful_privacy_frame)
        lawful_frame.configure(style="lawfulLight.TFrame")
        lawful_frame_label = ttk.Label(master=lawful_frame)
        lawful_frame_label.configure(style="lawfulLight.TLabel", font=("Times New Roman", 10, "bold"), justify="center", anchor="center", wraplength=290, text="dashWoorkz Sovereign Society\nEstablished: 2023\nTemCon 3\nWeather Report\nand\nTemperature Conversion Tool\nConverts:\n Celcius, Kelvin, Fahrenheit and Rankine")
        lawful_frame_label.pack(fill="x", expand="True", side="top", ipady=5, ipadx=5)
        lawful_frame.pack(fill="both", expand=True)
        gpl_frame = ttk.Frame(master=lawful_privacy_frame)
        gpl_frame.configure(style="lawfulLight.TFrame")
        lawful_gpl_label = ttk.Label(master = gpl_frame)
        lawful_gpl_label.configure(justify="center", anchor="center", font=("Roboto, sans-serif", 8, "bold"), wraplength=290, background="#f7d4f6", foreground="#9370d8", text="TemCon 3, Live Weather Reporting Temperature Conversion Tool\nCopyright (C) 2024\n  dashWoorkZ Sovereign Society\n\nThis program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.\n\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.\n\n You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.")
        lawful_gpl_label.grid(row=2, column=0, columnspan=4, sticky="nsew", ipady=5, ipadx=5, padx=5)
        gpl_frame.pack(fill="both", expand="True", side="bottom")
        lawful_privacy_frame.grid(row=0, column=0, columnspan=4, rowspan=3)
        
        lawful_privacy_frame.rowconfigure(0, weight = 1)
        lawful_privacy_frame.columnconfigure(0, weight = 1)
        lawful_privacy_frame.rowconfigure(1, weight = 1)
        lawful_privacy_frame.columnconfigure(1, weight = 1)
        lawful_privacy_frame.rowconfigure(2, weight = 1)
        lawful_privacy_frame.columnconfigure(2, weight = 1)
        lawful_privacy_frame.columnconfigure(3, weight = 1)

# End of Lawful Privacy Statement
# ===================

# Donation Window
def open_donate_window():
    donate_window = Toplevel(window)
    donate_window.title("Donate")
    width = 400
    height = 350
    x = (donate_window.winfo_screenwidth()//2)-(width//2)
    y = (donate_window.winfo_screenheight()//2)-(height//2)
    donate_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    donate_window.configure(bg="#f0f0f0")
    donate_label = Label(donate_window)
    donate_label.configure(font=("Times New Roman", 11, "bold"),highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True,  background="#ffe4c4", foreground="#5c3608", text="Donate:\nIf you enjoyed this program and would\n like to contribute to our work:\n\ndashWoorkz Sovereign Society:\ndashwoorkz@dashwoorkz.ca\n\nE-Transfer:\nLord :Dash: La Londe\nManaging Director:\ndash@dashwoorkz.ca\n\n Bitcoin:\nBTC:38YwKspQ8hdxAmGQUPP7LvXPRucdZURNu5\n\n Merchandise Online:\nhttp://everythingdash.creator-spring.com/")
    donate_label.pack(fill="both", expand=True)
    
# End of Donation Window
# ===================

# Contact Information Window
def open_contact_window():
    contact_window = Toplevel(window)
    contact_window.title("Contact Us")
    contact_window.geometry("310x200")
    width = 310
    height = 220
    x = (contact_window.winfo_screenwidth()//2)-(width//2)
    y = (contact_window.winfo_screenheight()//2)-(height//2)
    contact_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    contact_window.configure(bg="#f0f0f0")
    
    label_contact = Label(contact_window, text="Contact Information", foreground="#fd3adf", bg="#f7d4f6", font=("Helvetica", 12, "bold"))
    label_contact.pack(fill="both", expand=True)

    label_society = Label(contact_window, text="dashWoorkZ Sovereign Society", foreground="#4169e1", bg="#99cfe7", font=("Helvetica", 10, "bold"))
    label_society.pack(fill="both", expand=True)
    
    label_email = Label(contact_window, text="Email: dashwoorkz@dashwoorkz.ca", foreground="#4169e1", bg="#99cfe7", font=("Helvetica", 10))
    label_email.pack(fill="both", expand=True)
    
    label_mdirector = Label(contact_window, text="Managing Director:", foreground="#2e8b57", bg="#c4ecc4", font=("Helvetica", 10, "bold"))
    label_mdirector.pack(fill="both", expand=True)
    
    label_mdName = Label(contact_window, text="Lord :Dash: La Londe", foreground="#2e8b57", bg="#c4ecc4", font=("Helvetica", 10))
    label_mdName.pack(fill="both", expand=True)

    label_md_email = Label(contact_window, text="Email: dash@dashwoorkz.ca", foreground="#2e8b57", bg="#c4ecc4", font=("Helvetica", 10, "bold"))
    label_md_email.pack(fill="both", expand=True)

    label_csDirector = Label(contact_window, text="Community Services Director:", foreground="#c27012", bg="#f3e1c9", font=("Helvetica", 10, "bold"))
    label_csDirector.pack(fill="both", expand=True)
    
    label_csdName = Label(contact_window, text="Lady :Jeanette-Elizabeth: Hiuser", foreground="#c27012", bg="#f3e1c9", font=("Helvetica", 10))
    label_csdName.pack(fill="both", expand=True)

    label_cs_email = Label(contact_window, text="Email: jeanette.elizabeth@dashwoorkz.ca", foreground="#c27012", bg="#f3e1c9", font=("Helvetica", 10))
    label_cs_email.pack(fill="both", expand=True)
    
    label_dwrx = Label(contact_window, text="Visit: http://dashwoorkz.ca", foreground="#c27012", bg="#cae8f3", font=("Helvetica", 16))
    label_dwrx.pack(fill="both", expand=True, ipady=5)


def open_splash_window():
        window.withdraw()
        #splash_window = tk.Tk()
        from PIL import ImageTk, Image
        splash_window = Toplevel(window)
        splash_window.overrideredirect(True)
        width = 347
        height = 495
        x = (splash_window.winfo_screenwidth()//2)-(width//2)
        y = (splash_window.winfo_screenheight()//2)-(height//2)
        splash_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        splash_window.configure(bg="#f0f0f0")
        style = ttk.Style()        
        style.theme_use("clam")
        style.configure("splash.Toolbutton", font=("Roboto, sans-serif", 12, "bold"), borderwidth=5, bordercolor="#0000ff", relief=tk.RAISED, foreground="#448d76", background="#c4ecc4")
        style.configure("hover.Toolbutton", font=("Roboto, sans-serif", 12, "bold"), borderwidth=5, bordercolor="#702b85", overrelief=tk.SUNKEN, foreground="#9932cc", background="#07597f")
        splash_window.configure(background="#219399")

        def startLive(event):
                window.deiconify()
                showLive()
                splash_window.destroy()


        def startManual(event):
                window.deiconify()
                showManual()
                splash_window.destroy()

        def startHome(event):
                window.deiconify()
                getMain()
                splash_window.destroy()



        splash_frame = tk.Frame(splash_window)
        splash_frame.configure(bg="#219399")
        temcon_title_frame = tk.Frame(splash_frame)
        temcon_title_frame.configure(bg="#219399")
        tc_frame = tk.Frame(temcon_title_frame)
        # ============= Logo in a Canvas ======================#
        temcon_logo = Image.open("imgs/tc2024Logo.png")
        image_ratio = temcon_logo.size[0] / temcon_logo.size[1]
        temcontk = ImageTk.PhotoImage(temcon_logo)
        canvas2 = tk.Canvas(tc_frame, background="burlywood", width=60, height=60, bd=2, highlightthickness=2, relief="ridge")
        canvas2.grid(row=0, column=0)
        canvas2.create_image((30,30), image = temcontk)
        tc_frame.grid(row=0, column=0, sticky="nsew")
        tc_title_frame = tk.Frame(temcon_title_frame)
        title_label = ttk.Label(tc_title_frame)
        title_label.configure(text="TemCon 3", font=("Roboto, sans-serif", 14, "bold"), anchor="center", justify="center", foreground="#448d76", background="#c4ecc4")
        title_label.grid(row=0, column=0, sticky="nsew", ipadx=10)
        title_desc_label= ttk.Label(tc_title_frame,text="Weather Reporting\n Temperature Conversion Tool", font=("Times New roman", 10, "bold"), anchor="center", justify="center", foreground="#448d76", background="#c4ecc4")
        title_desc_label.grid(row=1, column=0, sticky="nsew", ipady=3, ipadx=10)
        tc_title_frame.grid(row=0, column=1, columnspan=2, rowspan=2, sticky="nsew")
        dss_frame = tk.Frame(temcon_title_frame)
        # ============= Logo in a Canvas ======================#
        dss_logo = Image.open("imgs/dss_logo.png")
        image_ratio = dss_logo.size[0] / dss_logo.size[1]
        dsstk = ImageTk.PhotoImage(dss_logo)
        canvas1 = tk.Canvas(dss_frame, background="burlywood", width=60, height=60, bd=2, highlightthickness=2, relief="ridge")
        canvas1.grid(row=0, column=0)
        canvas1.create_image((30,30), image = dsstk)
        dss_frame.grid(row=0, column=3, sticky="nsew")
        temcon_title_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")
        temcon_body_frame = tk.Frame(splash_frame)
        temcon_body_frame.configure(bg="#219399")
        gpl_alert_label = ttk.Label(temcon_body_frame)
        gpl_alert_label.configure(font=("Timew New Roman", 8, "bold"), padding=20, wraplength=290, justify="center", anchor="center", background='#519fd2',foreground='#9932cc', text="TemCon 3, Live Weather Reporting Temperature Conversion Tool\n\nThis program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.\n\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.")
        gpl_alert_label.grid(row=0, column=0, sticky="ew", ipadx=5, ipady=2)
        temcon_body_frame.grid(row=1, column=0, rowspan=2, sticky="ew", columnspan=4, pady=5)
        def on_home_hover(event):
                home_button.configure(style="hover.Toolbutton")


        def on_leave_home_hover(event):
                home_button.configure(style="splash.Toolbutton")


        def on_live_hover(event):
                live_button.configure(style="hover.Toolbutton")


        def on_leave_live_hover(event):
                live_button.configure(style="splash.Toolbutton")


        def on_manual_hover(event):
                manual_button.configure(style="hover.Toolbutton")


        def on_leave_manual_hover(event):
                manual_button.configure(style="splash.Toolbutton")


        list_frame = tk.Frame(splash_frame, bg="#219399")
        live_button=ttk.Button(list_frame)
        live_button.configure(text='Live', style="splash.Toolbutton", width=8)
        live_button.grid(row=0, column=0, sticky="nse")
        live_button.bind("<Button-1>", startLive)
        live_button.bind("<Enter>", on_live_hover)
        live_button.bind("<Leave>", on_leave_live_hover)
        # live_button.bind("<Leave>", off_hover)
        manual_button= ttk.Button(list_frame)
        manual_button.configure(text='Manual', style="splash.Toolbutton", width=8)
        manual_button.grid(row=0, column=1, sticky="nsew", padx=3)
        manual_button.bind("<Button-1>", startManual)
        manual_button.bind("<Enter>", on_manual_hover)
        manual_button.bind("<Leave>", on_leave_manual_hover)
        home_button=ttk.Button(list_frame)
        home_button.configure(text='Home', style="splash.Toolbutton", width=8)
        home_button.grid(row=0, column=2, sticky="nsw")
        home_button.bind("<Button-1>", startHome)
        home_button.bind("<Enter>", on_home_hover)
        home_button.bind("<Leave>", on_leave_home_hover)
        list_frame.grid(row=3, column=0, sticky="nsew", columnspan=3, ipadx=5, pady=5)
        

        society_frame = tk.Frame(splash_frame, bg="#219399")
        society_frame.configure(relief=tk.SUNKEN)
        society_title_label= ttk.Label(society_frame)
        society_title_label.configure(text="dashWoorkZ Sovereign Society",  justify="center", anchor="center", font=("Times New roman", 12, "bold"), foreground="#448d76", background="#c4ecc4")
        society_title_label.grid(row=0, column=0, columnspan=4, sticky="nsew")
        society_copy_label= ttk.Label(society_frame)
        society_copy_label.configure(text="copyright 2024 - Without Prejudice - All Rights Reserved",  justify="center", anchor="center", font=("Times New roman", 10, "bold"), foreground="#448d76", background="#c4ecc4")
        society_copy_label.grid(row=1, column=0, columnspan=4, sticky="nsew", ipadx=5,)
        society_frame.grid(row=4, column=0, sticky="nsew", rowspan=2, columnspan=4, ipady=5)
        splash_frame.grid(row=0, column=0, sticky="nsew", rowspan=5, columnspan=4, padx=5, pady=5)

        splash_frame.rowconfigure(0, weight=1)
        splash_frame.rowconfigure(1, weight=2)
        splash_frame.rowconfigure(2, weight=1)
        splash_frame.rowconfigure(3, weight=1)
        splash_frame.rowconfigure(4, weight=1)
        
        splash_frame.columnconfigure(0, weight=1)
        splash_frame.columnconfigure(1, weight=1)
        splash_frame.columnconfigure(2, weight=1)
        splash_frame.columnconfigure(3, weight=1)
        
        list_frame.columnconfigure(0, weight=1, minsize=110)
        list_frame.columnconfigure(1, weight=1, minsize=110)
        list_frame.columnconfigure(2, weight=1, minsize=110)
        
        temcon_body_frame.columnconfigure(0, weight=1)
        temcon_body_frame.columnconfigure(1, weight=1)
        temcon_body_frame.columnconfigure(2, weight=1)
        temcon_body_frame.columnconfigure(3, weight=1)
        temcon_body_frame.columnconfigure(4, weight=1)
        temcon_body_frame.columnconfigure(5, weight=1)







window.configure(menu = menu)
open_splash_window()

window.mainloop()



