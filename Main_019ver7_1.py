from Util019ver7_1 import Util019

__author__="liuweihao"
#ver2修改了失败一次之后等到成功了才会开始继续投注  tim不能为0
#ver3修改了失败之后等到成功了二次才会开始继续投注 仅限3-3
#ver4 在ver3的基础上修改了失败第二次结束后将开始1-4时代
#ver4.1  修复了期号不停重复出现的问题
#ver4.2  添加输出余额和盈利,调入即将开始购买弹出,且开始播放中奖声音
#ver4.2.1 在4.2的基础上添加了失败后开始 (不知道怎么搞了)
#ver5.0 加入了Util019属性，使代码更为简洁，加入0-9的出现代码次数统计
#ver5.1 恢复ver3版本 取消狂欢时刻
#ver5.2取消了失败停止投注
#ver5.3添加了数据计算分钟版
from tkinter import *
from urllib import error
import threading
import json
import time
import datetime
import os
from io import StringIO
from xlwt import  *

import winsound
import socket
class Main019(object):
    global lb1
    global lb2
    global get019
    global currentperiod
    # 可输入总金额
    global var1
    #总金额
    global var2
    # 盈利
    global var3
    # 成功收米
    global var4
    # 失败自杀
    global var5
    global var6
    global var7
    #前置次数
    global var8
    #投注次数
    global var9
    global varnm1
    global varnm2
    global varnm3
    global mutti
    global vartext
    global fileskj, fileszj,fileallkj,filenumapper
    fileskj = StringIO()
    fileszj = StringIO()
    fileallkj=StringIO()
    filenumapper=StringIO()

    root=Tk()
    root.title("腾讯分分彩Ver7")
    #打开的大小
    root.geometry("800x850")
    #拖动后最小大小
    root.wm_minsize(500,500)
    # 可拖动
    root.resizable(width=True,height=True)
    #可更改的界面
    vartext=StringVar()
    vartext.set("腾讯分分彩Ver7")
    Entry(root,textvariable=vartext,font=("Arial",10),borderwidth=0,).pack(side=TOP)
    # Frame

    FF1=Frame(root)
    FrameA=Frame(FF1)

    FrameA1=Frame(FrameA)
    #  总金额 盈利 收米 自杀
    FrameA1T=Frame(FrameA1)
    FrmAll1=Frame(FrameA1T)
    FrmAll2 = Frame(FrameA1T)
    # 倍数
    FrameA1B=Frame(FrameA1)
#参数栏
    FrameA2=Frame(FrameA)
    FrameA2L=Frame(FrameA2)
    FrameA2L1=Frame(FrameA2L)
    FrameA2L2=Frame(FrameA2L)
    FrameA2R=Frame(FrameA2)
    FrameA2RL=Frame(FrameA2R)
    FrameA2RL1=Frame(FrameA2RL)
    FrameA2RL2=Frame(FrameA2RL)
    FrameA2RR=Frame(FrameA2R)
    FrameA2RR1=Frame(FrameA2RR)
    FrameA2RR2=Frame(FrameA2RR)
    FrameB=Frame(FF1)
    Frmtop1 = Frame(FrmAll1)
    Frmtop1a=Frame(Frmtop1)
    Frmtop1b=Frame(Frmtop1)

    Frmtop2=Frame(FrmAll1)
    Frmtop2a=Frame(Frmtop2)
    Frmtop2b=Frame(Frmtop2)

    FrmEntry=Frame(FrmAll2)
    FrmEntrya=Frame(FrmEntry)
    FrmEntryb=Frame(FrmEntry)

    FrmList1=Frame(FrameB)
    FrmList2=Frame(FrameB)
    FrmList2a=Frame(FrmList2)
    FrmList2b=Frame(FrmList2)
    FF1.pack()
    Frmtop1.pack(side=TOP)
    Frmtop1a.pack(side=LEFT, padx=65, pady=6)
    Frmtop1b.pack(side=RIGHT, padx=85, pady=6)
    Frmtop2.pack(side=BOTTOM)
    Frmtop2a.pack(side=LEFT, padx=65, pady=6)
    Frmtop2b.pack(side=RIGHT, padx=60, pady=6)
    FrmEntry.pack(side=BOTTOM)
    FrmEntrya.pack(side=LEFT)
    FrmEntryb.pack(side=RIGHT)
    FrameA.pack(side=TOP)
    FrameA1.pack(side=TOP)
    FrameA1T.pack(side=TOP)
    FrameA1B.pack(side=BOTTOM)
    FrameA2.pack(side=BOTTOM)
    FrameA2L.pack(side=LEFT, padx=15)
    FrameA2L1.pack(side=LEFT)
    FrameA2L2.pack(side=RIGHT)
    FrameA2R.pack(side=RIGHT)
    FrameA2RL.pack(side=LEFT)
    FrameA2RL1.pack(side=LEFT)
    FrameA2RL2.pack(side=RIGHT, padx=10)
    FrameA2RR.pack(side=RIGHT)
    FrameA2RR1.pack(side=LEFT)
    FrameA2RR2.pack(side=RIGHT, padx=10)

    FrameB.pack(side=BOTTOM)
    FrmAll1.pack(side=TOP)
    FrmAll2.pack(side=BOTTOM)
    FrmList1.pack(side=TOP, pady=10)
    FrmList2.pack(side=TOP, pady=12)

    FrmList2a.pack(side=TOP)
    FrmList2b.pack(side=BOTTOM)
    Label(Frmtop1a,text="总金额:",font=("Arial",15),padx=10,pady=10).pack(side=LEFT)
    var2=DoubleVar()
    var2.set(100)
    #Entry2readonly只可读 borderwidth无边框
    e2=Entry(Frmtop1a,textvariable=var2,font=("Arial",15),borderwidth=0,state="readonly").pack(side=RIGHT)
    l3=Label(Frmtop1b,text="盈利:",font=("Arial",15),padx=10,pady=10).pack(side=LEFT)
    #Entry3
    var3=DoubleVar()
    var3.set(0)
    e3 = Entry(Frmtop1b, textvariable=var3,font=("Arial",15), borderwidth=0, state="readonly").pack(side=RIGHT)

    # Frame2
    l4 = Label(Frmtop2a, text="成功收米:", font=("Arial", 15),padx=10,pady=20).pack(side=LEFT)
    var4 = IntVar()
    var4.set(0)
    e4 = Entry(Frmtop2a, textvariable=var4, font=("Arial", 15), borderwidth=0, state="readonly").pack(side=RIGHT)

    l5 = Label(Frmtop2b, text="失败自杀:", font=("Arial", 15), padx=10, pady=20).pack(side=LEFT)
    var5 = IntVar()
    var5.set(0)
    e5 = Entry(Frmtop2b, textvariable=var5, font=("Arial", 15), borderwidth=0, state="readonly").pack(side=RIGHT)
    #Frame输入框
    l6=Label(FrmEntrya,text="输入总投注金额:",font=("Arial",15),padx=10,pady=11).pack(side=LEFT)
    var1 = IntVar()
    var1.set(100)
    e1=Entry(FrmEntryb,show="",textvariable=var1).pack(side=LEFT)

    def confirmMoney():
        i=var1.get()
        var2.set(i)
    b1 = Button(FrmEntryb, text="确定", command=confirmMoney, padx=10).pack(side=RIGHT)

    #输入投注参数
    #前置次数
    qianzhiL=Label(FrameA2L1,text="前置次数:",font=("Arial",10),pady=10).pack(side=LEFT)
    var8=IntVar()
    var8.set(3)
    ETYqz=Entry(FrameA2L1,show="",textvariable=var8,width=10).pack(side=RIGHT)

    #投注次数
    touzhuL=Label(FrameA2L2,text="投注次数:",font=("Arial",10),pady=10).pack(side=LEFT)
    var9=IntVar()
    var9.set(3)
    ETYtz = Entry(FrameA2L2, show="", textvariable=var9,width=10).pack(side=RIGHT)

    #投注号码
        # 号码1
    num1=Label(FrameA2RL1,text="号码1:",font=("Arial",10),pady=10).pack(side=LEFT)
    varnm1=StringVar()
    varnm1.set("0")
    ETYnum1= Entry(FrameA2RL1, show="", textvariable=varnm1,width=6).pack(side=RIGHT)
        #号码2
    num2 = Label(FrameA2RL2, text="号码2:", font=("Arial", 10), pady=10).pack(side=LEFT)
    varnm2 = StringVar()
    varnm2.set("1")
    ETYnum2 = Entry(FrameA2RL2, show="", textvariable=varnm2,width=6).pack(side=RIGHT)
        #号码3
    num3 = Label(FrameA2RR1, text="号码3:", font=("Arial", 10), pady=10).pack(side=LEFT)
    varnm3 = StringVar()
    varnm3.set("9")
    ETYnum3 = Entry(FrameA2RR1, show="", textvariable=varnm3,width=6).pack(side=RIGHT)
    #倍数
    mutiply = Label(FrameA2RR2, text="倍数:", font=("Arial", 10), pady=10).pack(side=LEFT)
    mutti=IntVar()
    mutti.set(1)
    ETYmulti= Entry(FrameA2RR2, show="", textvariable=mutti,width=8).pack(side=RIGHT)
    #开奖信息
    var6=StringVar()
    l7=Label(FrmList1,text="开奖信息",font=("Arial",10),pady=5).pack(side=TOP)
    lb1=Listbox(FrmList1,listvariable=var6,width=100,height=10,font=("Arial",10),xscrollcommand=TRUE)
    var7=StringVar()
    l8 = Label(FrmList2a, text="中奖结果", font=("Arial",10), pady=5).pack(side=TOP)
    lb2=Listbox(FrmList2a, listvariable=var7, width=100, height=10, font=("Arial", 10))
    #结束后写出
    Label(FrameA1B, text="没事干别点:", font=("Arial", 18), pady=10).pack(side=LEFT)
    def write():
        if not os.path.exists("E:/go019"):
            os.mkdir("E:/go019")
        if not os.path.exists('E:/go019/%s'%str(datetime.datetime.now().date())):
            os.mkdir('E:/go019/%s'% str(datetime.datetime.now().date()))
        os.path.join('E:/go019/',str(datetime.datetime.now().date()))
        kj=open('E:/go019/%s/%s开奖记录%s分.txt'%(str(datetime.datetime.now().date()),vartext.get(),str(datetime.datetime.now().minute)), 'w')
        zj=open('E:/go019/%s/%s中奖记录%s分.txt'%(str(datetime.datetime.now().date()),vartext.get(),str(datetime.datetime.now().minute)), 'w')
        allzj=open('E:/go019/%s/%s完全版中奖记录%s分.txt'%(str(datetime.datetime.now().date()),vartext.get(),str(datetime.datetime.now().minute)), 'w')
        numwrite=open('E:/go019/%s/%s出现记录%s分.txt'%(str(datetime.datetime.now().date()),vartext.get(),str(datetime.datetime.now().minute)), 'w')
        kj.write(fileskj.getvalue())
        zj.write(fileszj.getvalue())
        allzj.write(fileallkj.getvalue())
        numwrite.write(filenumapper.getvalue())
        ws.save('E:/go019/%s/%s出现表格%s分.xls'%(str(datetime.datetime.now().date()),vartext.get(),str(datetime.datetime.now().minute)))
    b2 = Button(FrameA1B, text="输出日记", command=write, padx=10).pack(side=RIGHT)


    global flag
    flag = True

    global u019
    u019=Util019()
    global ws
    ws = Workbook(encoding="utf-8")
    global w1
    w1=ws.add_sheet("bet1Hour")
    global w2
    w2=ws.add_sheet("bet2Minute")
    #记录每次出现的号码 用于模拟

    global w4
    global w5
    w4 = ws.add_sheet("bet3tenMinute")
    w5 = ws.add_sheet("bet4halfMinute")
    global w3
    w3 = ws.add_sheet("betnum")







    def reflash():
        # 参数设置
        currentperiod, get019, benefit, tim, bettime, firstnum,\
        secnum, trdnum, multiple, losemoney, url, period, datalist,\
        betFlag, betwintime, nowintime, carnivalwin,\
        num0, num1, num2, num3, num4, num5, num6, num7, num8, num9, \
        paw,currentHour,currentMinute,currenttenMinute,currenthalfMinute, show019time, no019time\
            , minbetwintime,tenminbetwintime,halfminbetwintime,minnowintime,tenminnowintime,halfminnowintime\
            ,minpaw,numpaw,tenminpaw,halfminpaw,numList,isgobet,gobet,betovertime=u019.getconst(var8,var9,varnm1,varnm2,varnm3,mutti)
        while True:
            try:
                # print(datetime.datetime.now().hour)

                listkjx, period, kjxx,num1,num2,num3 = u019.requestData(url)

                dt=str(datetime.datetime.now())
                #每小时判断并写入一次
                currentHour,show019time,no019time,paw=u019.hourchangescount(currentHour,filenumapper,show019time,no019time,w1,paw)
                #5分钟的判断
                minpaw, minnowintime, minbetwintime, currentMinute=u019.countMinute(currentMinute,w2,minpaw,minbetwintime,minnowintime,5)
                #10分钟的判断
                tenminpaw, tenminnowintime, tenminbetwintime, currenttenMinute = u019.countMinute(currenttenMinute, w4, tenminpaw,
                                                                                               tenminbetwintime, tenminnowintime, 10)
                #30分钟的判断
                halfminpaw, halfminnowintime, halfminbetwintime, currenthalfMinute = u019.countMinute(currenthalfMinute, w5,
                                                                                               halfminpaw,
                                                                                                  halfminbetwintime,
                                                                                                  halfminnowintime, 30)



                ts = ("                    --------------------第%s期,开奖结果为:%s,时间为:%s--------------------" % (
                    period, kjxx,dt[0:20] ))
                #是否更新期数
                if u019.isUpdateperiod(currentperiod,period):
                    lb1.insert(0, ts)
                    fileskj.write(ts+"\n")
                    lb1.delete(49, 50)
                    print(num1, num2, num3)
                    currentperiod = int(period)
                    #记录0-9的数字
                    numList=u019.count0to9(num1,num2,num3,numList)
                    #记录开奖号码到xls
                    numpaw=u019.writenumws(w3,numpaw,num1,num2,num3,currentperiod)
                    if (u019.iswin(kjxx,firstnum,secnum,trdnum)):
                        #如果赢了 进入代码判断
                        no019time, minnowintime,halfminnowintime,tenminnowintime=u019.wincore(lb2,no019time,minnowintime,tenminnowintime,halfminnowintime)
                        if isgobet:

                            if u019.isnotToss(get019, tim):
                                if betFlag:
                                    get019 = 0
                                    result = "未满%s次就中奖，重新计数,时间%s" % (tim, str(dt[0:20]))
                                    u019.insertzjinfo(result, lb2, fileallkj)
                                else:
                                    # Tosslossway1
                                    # nowintime, get019, betwintime, betFlag=u019.TosslossWay1(betwintime,nowintime,u019,listkjxx,dt,lb2,fileallkj,get019,tim)
                                    betFlag, carnivalwin, get019, nowintime = u019.Tosslossway2(carnivalwin, betFlag,
                                                                                                lb2, dt, get019)

                            else:
                                # 中奖赢钱的参数以及界面修改
                                carnivalwin, benefit,betovertime = u019.winbet(var1, var2, var3, var4, get019, tim, multiple,
                                                                   carnivalwin,betovertime)
                                if betovertime>=8888888888888888888888:
                                    betovertime=0
                                    #8888888888888888888888
                                    isgobet=False
                                u019.insertinfo("恭喜中奖！！投注%0.2f元成功收米:%0.2f 元,当前余额:%s,当前盈利:%s,时间:%s" % (
                                    benefit, benefit * 2.84, var2.get(), var3.get(), dt[0:20]), lb2, fileszj, fileallkj)
                                # ver4新增
                                # 狂热时间结束
                                # carnivalwin, tim, bettime=u019.carnivaltimeover(carnivalwin,var8,var9,tim,bettime)
                                get019, losemoney, benefit = 0, 0, 0
                                u019.playvoice("win.wav")
                        else:
                            # 中间几次了我要开始了
                            if (gobet >= 4):
                                gobet = 0
                                isgobet = True
                                lb2.insert(0, "中奖次数达到规定次数开启购买模式")
                            else:
                                gobet=0
                                lb2.insert(0,"尚未满足条件就中奖")
                    else:

                        #开奖时没中奖进入的代码
                        show019time, minbetwintime,tenminbetwintime,halfminbetwintime=u019.losecore(lb2, show019time,minbetwintime,tenminbetwintime,halfminbetwintime)
                        print(show019time)
                        if isgobet:
                            if betFlag:
                                get019 = get019 + 1

                            # get019----019出现的次数
                            # tim 未中奖的前置次数
                            # bettime 投注x次
                            if u019.isfalureTost(get019, tim, bettime):
                                # 参与投注但是未中奖
                                losemoney, benefit = u019.betnowin(get019, tim, multiple, losemoney, var2)
                                u019.insertzjinfo("参与投注第%s次,投注金额%s,时间:%s" % (get019 - tim, benefit, str(dt[0:20])), lb2,
                                                  fileallkj)
                                # 支付
                                # u019.gopay(u019,(get019-tim+1))
                                # u019.gopay2(u019,(get019-tim+1))

                            elif u019.isFalure(get019, bettime, tim):
                                # 投注多次未中失败
                                get019, betFlag, benefit,isgobet= u019.addfalure(var1, var2, var3, var5, get019, tim, multiple)
                                u019.insertinfo("多次投注未中，放弃投注，共亏损%0.2f 元,当前余额:%s,当前盈利:%s,时间:%s" % (
                                    losemoney + benefit, var2.get(), var3.get(), str(dt[0:20])), lb2, fileszj,
                                                fileallkj)
                                betovertime=0

                                losemoney = 0
                                # firstnum,secnum,trdnum=u019.Tosslossway3(numList,varnm1,varnm2,varnm3)
                                varnm1.set(firstnum)
                                varnm2.set(secnum)
                                varnm3.set(trdnum)
                                u019.playvoice("lose.wav")
                            else:
                                # 没中但是没到开始投注时机
                                if betFlag:
                                    result = "开奖结果%s %s %s中包含%s %s %s,累计次数%s,时间:%s" % (
                                        num1, num2, num3, firstnum,
                                        secnum, trdnum, get019, str(dt[0:20]))
                                    u019.insertzjinfo(result, lb2, fileallkj)
                                    # 即将开始投注
                                    u019.beganGotobet(get019, tim, lb2, u019)
                                else:
                                    nowintime = nowintime + 1
                                    result = "还未中奖，暂不开始投注，累计%s次未中，时间：%s" % (nowintime, str(dt[0:20]))
                                    u019.insertzjinfo(result, lb2, fileallkj)
                                    get019 = 0
                        else:
                            gobet+=1
                            lb2.insert(0,"没中奖，此时累计%s次"%gobet)

            except error.URLError as e:
                print(e)
                url=u019.JudgeUrl(url)
            except json.JSONDecodeError as j:
                print("JSONDecodeError",j)
                url =u019.JudgeUrl(url)
            except ValueError as v:
                print("ValueError:",v)
                url =u019.JudgeUrl(url)
            except socket.timeout as s:
                print(s)
                url =u019.JudgeUrl(url)


            time.sleep(1)
    global threadd
    threadd=threading.Thread(target=reflash, name='BetThread')
    def start():
        threadd.start()
    def clear():
        fileskj.close()
        fileszj.close()
        python = sys.executable
        os.execl(python, python, *sys.argv)
    btn_start=Button(FrmList2b, text="开始",command=start, padx=80).pack(side=LEFT)
    btn_clear = Button(FrmList2b, text="清空", command=clear, padx=80).pack(side=RIGHT)
    lb1.pack(side=BOTTOM)
    lb2.pack(side=BOTTOM)
    # print(t["list"][1]["result"][4])
    root.mainloop()
    # 自签名的证书

# def _async_raise(tid, exctype):
#     """raises the exception, performs cleanup if needed"""
#     tid = ctypes.c_long(tid)
#     if not inspect.isclass(exctype):
#         exctype = type(exctype)
#     res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
#     if res == 0:
#         raise ValueError("invalid thread id")
#     elif res != 1:
#                # """if it returns a number greater than one, you're in trouble,
#                 # and you should call it again with exc=NULL to revert the effect"""
#         ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
#         raise SystemError("PyThreadState_SetAsyncExc failed")


#   # selenium:由于是js加载的更新，所以我们需要用chrome打开后来获取页面上爬的数据
#     browser = webdriver.Firefox(executable_path='\go019\geckodriver')
#     browser.get("http://www.10086020.com/txffc/kjls/txffckj.html")
#     print(browser.page_source)
#     browser.close()
#
#
# #
