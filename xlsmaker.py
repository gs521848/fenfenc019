

__author__="liuweihao"

from xlwt import  *
from io import StringIO
from urllib import request
from tkinter import *
from bs4 import BeautifulSoup
from pinyin import *
import datetime
print(datetime.datetime.now().hour)
for n in range(0,10):
    print(n)

raw=0
def setinfo():
    global raw
    w.write(raw, 0, var_gamename.get())
    w.write(raw, 1, var_downline.get())
    w.write(raw, 2, var_sucai.get())
    w.write(raw, 3, var_pjnr.get())
    lb_qudao.insert(0,"游戏名：%s,下载链接：%s,素材页：%s,破解内容:%s"%(var_gamename.get(),var_downline.get(),var_sucai.get(),var_pjnr.get()))
    raw += 1
    var_gamename.set("")
    var_downline.set("")
    var_sucai.set("")
    var_pjnr.set("")
    print("setinfo")

class xlsmaker(object):

    def __init__(self,raw):
        self.raw=raw
    def handle_starttag(self, tag, attrs):
        # print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == "href":
                        self.links.append(value)

    root=Tk()
    root.title("xls生成器")
    root.geometry("600x600")
    root.wm_minsize(600,600)
    Label(root, text="文档生成器", font=("Times",13,"bold"), padx=10, pady=10).pack()

    #上半块
    FrameTOP=Frame(root)
    FrameTOPT=Frame(FrameTOP)
    FrameTOPB=Frame(FrameTOP)
    # 下半块
    FrameBOT=Frame(root)
    FrameBOTT=Frame(FrameBOT)
    FrameBOTT_left=Frame(FrameBOTT)
    FrameBOTT_right = Frame(FrameBOTT)

    FrameBOTB = Frame(FrameBOT)
    FrameBOTB_top=Frame(FrameBOTB)
    FrameBOTB_bot=Frame(FrameBOTB)
    FrameBOTB_bott=Frame(FrameBOTB_bot)
    FrameBOTB_botb=Frame(FrameBOTB_bot)



    # 打包
    FrameTOP.pack()
    FrameTOPT.pack(side=TOP)
    FrameTOPB.pack(side=BOTTOM)

    FrameBOT.pack()
    FrameBOTT.pack(side=TOP)
    FrameBOTT_left.pack(side=LEFT,padx=10,pady=20)
    FrameBOTT_right.pack(side=RIGHT,pady=20)

    FrameBOTB.pack(side=BOTTOM)
    FrameBOTB_top.pack(side=TOP,pady=10)

    FrameBOTB_bot.pack(side=BOTTOM)
    FrameBOTB_bott.pack(side=TOP,pady=10)
    FrameBOTB_botb.pack(side=BOTTOM,pady=10)

    #素材链接
    global var_sucai
    global var_qudao
    global var_gamename
    global var_downline
    global var_pjnr
    global lb_qudao

    l_sucai=Label(FrameTOPT,text="素材链接:",font=(8),padx=10,pady=10).pack(side=LEFT)
    var_sucai=StringVar()

    E_sucai=Entry(FrameTOPT,textvariable=var_sucai,width=50).pack(side=RIGHT)

    #渠道
    var_qudao=StringVar()

    l_qudao=Label(FrameTOPB,text="渠道名",font=(8),padx=10,pady=10).pack(side=TOP)
    lb_qudao=Listbox(FrameTOPB,listvariable=var_qudao, width=50, height=10, font=("Arial", 10))


    lb_qudao.pack(side=BOTTOM)

    #gamename
    l_gamename=Label(FrameBOTT_left,text="游戏名称:",font=(8),padx=10,pady=10).pack(side=LEFT)
    var_gamename=StringVar()
    E_gamename = Entry(FrameBOTT_left, textvariable=var_gamename, width=12).pack(side=RIGHT)

    #downloadline
    l_downline=Label(FrameBOTT_right,text="下载链接:",font=(8),padx=10,pady=10).pack(side=LEFT)
    var_downline=StringVar()
    E_gamename = Entry(FrameBOTT_right, textvariable=var_downline, width=40).pack(side=RIGHT)

    #破解内容
    l_pjnr=Label(FrameBOTB_top,text="破解内容:",font=(8),padx=10,pady=10).pack(side=LEFT)
    var_pjnr = StringVar()
    E_pjnr = Entry(FrameBOTB_top, textvariable=var_pjnr, width=50).pack(side=RIGHT)


    #获取 添加 生成xls
    def getinfo():
        print("getinfo")
        try:
            link = var_sucai.get()
            f = request.urlopen(link)
            data=f.read().decode('UTF-8')
            soup = BeautifulSoup(data,"html.parser")
            #百分
            if link.find("byfen")>0:
                gamenames = str(soup.title.string).split(" v")[0].strip()

                var_gamename.set(gamenames + "破解版")
                s = StringIO()
                isFirst = True
                for strs in gamenames:
                    pin = pinyin.get(strs, format='strip', delimiter="")
                    if isFirst:
                        isFirst = False
                        s.write(pin)
                    else:
                        s.write(pin[0])
                s.write("pjb")
                var_downline.set("http://xiazai.3733.com/pojie/game/%s.apk" % s.getvalue())
                pid = soup.findAll("span", {"class": "text"})
                lanugage= pid[4].string
                var_pjnr.set("1.可玩 2.已破解 3.%s 4.%s" % (var_pjnr.get(),lanugage))
            # 7723
            if link.find("7723")>0:
                gamenames = str(soup.title.string).split("_")[0]
                var_gamename.set(gamenames + "破解版")
                isFirst = True
                s = StringIO()
                for strs in gamenames:
                    pin = pinyin.get(strs, format='strip', delimiter="")
                    if isFirst:
                        isFirst = False
                        s.write(pin)
                    else:
                        s.write(pin[0])
                s.write("pjb")
                var_downline.set("http://xiazai.3733.com/pojie/game/%s.apk" % s.getvalue())
                pid = soup.findAll("ul", {"class": "clearfix"})
                lanugage = str(pid[1]).split("语言：")
                pid2=soup.findAll("ul", {"class": "download-notice","style":"padding: 15px;padding-left: 50px;"})

                var_pjnr.set("1.可玩 2.已破解 3.%s 4.%s" % (str(pid2).split("<li>")[1].split("</li>")[0],lanugage[1][0:2]))
            if link.find("ccplay")>0:
                pid1 = soup.findAll("h2", {"class": "d_name"})
                gamenames = str(pid1).split(">")[1].split("</h2")[0]
                var_gamename.set(gamenames + "破解版")
                isFirst = True
                s = StringIO()
                for strs in gamenames:
                    pin = pinyin.get(strs, format='strip', delimiter="")
                    if isFirst:
                        isFirst = False
                        s.write(pin)
                    else:
                        s.write(pin[0])
                s.write("pjb")
                var_downline.set("http://xiazai.3733.com/pojie/game/%s.apk" % s.getvalue())
                pid2 = soup.findAll("div", {"class": "l msg_part"})
                lanugage=str(pid2).split("语言：")[1].split("<strong>")[1].split("</strong>")[0]
                var_pjnr.set("1.可玩 2.已破解 3.%s 4.%s" % (var_pjnr.get(),lanugage))
            if link.find("25game") > 0:
                gamenames = str(soup.title.string).split("v")[0]
                var_gamename.set(gamenames)

                isFirst = True
                s = StringIO()
                for strs in gamenames:
                    pin = pinyin.get(strs, format='strip', delimiter="")
                    if isFirst:
                        isFirst = False
                        s.write(pin)
                    else:
                        s.write(pin[0])
                s.write("pjb")
                var_downline.set("http://xiazai.3733.com/pojie/game/%s.apk" % s.getvalue())
                pid2 = soup.findAll("div", {"class": "clearfix","style":"color: #5b9921;"})
                pjnr=str(pid2).split(">")[1].split("</")[0].strip()
                lanugage=str(soup.findAll("div",{"class": "app-msg"})).split("语   言：")[1].split("dd>")[1].split("</dd")[0].split("</")[0]
                var_pjnr.set("1.可玩 2.已破解 3.%s 4.%s" % (pjnr, lanugage))

            print(f.read().decode('UTF-8'))
        except ValueError as v:
            print("未输入链接")
#https://android.byfen.com/app/16195
    btn_get=Button(FrameBOTB_bott,text="获取",command=getinfo,padx=50).pack(side=LEFT)
    global ws
    ws = Workbook(encoding="utf-8")
    global w
    w = ws.add_sheet("pj1")



    btn_set = Button(FrameBOTB_bott, text="添加", command=setinfo, padx=50).pack(side=RIGHT)

    def createxls():
        ws.save("E:/MAKEXLS/dist/test.xls")
        print("createxls")

    btn_create = Button(FrameBOTB_botb, text="生成xls", command=createxls, padx=50).pack(side=RIGHT)




    root.mainloop()
    # ws=Workbook(encoding="utf-8")
    # w=ws.add_sheet("test1")
    # w.write(0,0,u"abc")
    # w.write(0,1,u"123")
    #
    # s=StringIO()
    # ws.save("/go019/dist/test.xls")
