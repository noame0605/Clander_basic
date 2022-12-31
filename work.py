#導入

import calendar
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

datetime = calendar.datetime.datetime
timedelta = calendar.datetime.timedelta

root = tk.Tk()

# 定義基本屬性

Year = datetime.now().year
Month = datetime.now().month
today = datetime.now().strftime("%d")
fwday = calendar.SUNDAY
font = tkFont.Font()

# 年份標籤

def _label_y_m():


    _y_m = f"{Year}/{'%02d' % Month}"

    Y_label = tk.Label(
        Cframe,
        bg = '#625B57',
        fg = 'white',
        font = ('Forte', 15),
    )

    Y_label.config(text = _y_m)

    Y_label.place(x = 0, y = 0, width = 295, height = 30)

# 調整日期按鍵

    B_style = ttk.Style()

    B_style.configure(
        'B.TButton',
        background = '#625B57',
        foreground = 'white',
        font = ('',8,'bold'),
        padding = (0,0,0,0),
        relief = 'flat',
        bd = '0'
    )

    lbtn = ttk.Button(
        Y_label,
        text = '〈',
        style = 'B.TButton',
        width = 0,
        takefocus = 0,
        command = _prev_month,
        cursor = 'hand2'
    )

    lbtn.pack(side = 'left', padx = 10, pady = 5)

    rbtn = ttk.Button(
        Y_label,
        text = '〉',
        style = 'B.TButton',
        width = 0,
        takefocus = 0,
        command = _next_month,
        cursor = 'hand2'
    )

    rbtn.pack(side = 'right', padx = 10, pady = 5)
    
#建立日曆

def _build_Cal(Year, Month):

    cal = _cal.monthdayscalendar(Year, Month) 

    for indx, item in enumerate(_items):

        week = cal[indx] if indx < len(cal) else []

        fmt_week = [('%02d' % day) if day else '' for day in week]

        Calendar_.item(item, values = fmt_week, tags = 'header')

    _label_y_m()

# 下個月

def _prev_month():
    
    global Year, Month

    Date_ = datetime(Year, Month, 1)

    Date_ = Date_ - timedelta(days=1)

    Date_ = datetime(Date_.year, Date_.month, 1)

    Year,Month = Date_.year, Date_.month

    _build_Cal(Year,Month)
  
# 上個月
    
def _next_month():

    global Year, Month

    Date_ = datetime(Year, Month, 1)

    Date_ = Date_ + timedelta(
            days = calendar.monthrange(Year, Month)[1] + 1 )

    Date_ = datetime(Date_.year, Date_.month, 1)

    Year,Month = Date_.year, Date_.month

    _build_Cal(Year, Month)

# 框架

Cframe = tk.LabelFrame(
    root, 
    text = 'CALENDER', 
    font = ('Stencil', 15, 'bold'), #,'overstrike'
    labelanchor = 'n',  
    bg = '#625B57', 
    fg = 'white', 
    relief = 'groove',
    bd = 0,
)

Cframe.place(x = 0, y = 15, width = 295, height = 270)

# 設定treeview的樣式

C_style = ttk.Style()

C_style.theme_use('clam')

C_style.configure(
    'Treeview',
    rowheight = 30,
)

Calendar_ = ttk.Treeview(
    Cframe,
    show = ' ',
    selectmode = 'none',
    height = 7
)

Calendar_.place(x = 10, y = 30, width= 275)

# 建立日曆

cols = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

Calendar_['columns'] = cols

Calendar_.tag_configure(
    'header',
    background = "#625B57",
    foreground = 'white',
    font = ('', 10, 'bold')
)

Calendar_.insert('', 'end', values = cols, tag = 'header')

maxwidth = max(font.measure(col) for col in  cols)

for col in cols:

    Calendar_.column(
        col,
        width = maxwidth,
        minwidth = maxwidth,
        anchor = 'center'
    )

_items = [Calendar_.insert('', 'end', values = '') for _ in range(6)]

_cal = calendar.TextCalendar(fwday)

_build_Cal(Year,Month)

_label_y_m()

# 主視窗設定(大小、背景、圖示等等)

root.title(string='')

root.geometry("295x300-10+10")

root.resizable(0, 0)

root.attributes('-alpha', 0.8)

root.attributes('-toolwindow', 1)

root.attributes('-topmost', 1)

root.configure(bg = '#625B57')

# root.overrideredirect(1)



root.mainloop()