from io import StringIO
from urllib import request
import json
import ssl
import winsound
import win32api
import time
from ctypes import *
import win32gui
from xlwt import  *
import win32con
import datetime

class Util019(object):
    #常数控制
    def getconst(self,var8,var9,varnm1,varnm2,varnm3,mutti):
        # 当前期数
        currentperiod = 0
        # 019几次88了
        get019 = 0
        # 出钱和收益
        benefit = 0
        # 几次开始掏钱
        tim = var8.get()
        # 需要投注几次
        bettime = var9.get()
        # 第一个号码
        firstnum = varnm1.get()
        # 第二个号码
        secnum = varnm2.get()
        # 第三个号码
        trdnum = varnm3.get()
        # 倍数
        multiple = mutti.get()
        # 数字出现次数
        num0, num1, num2, num3, num4, num5, num6, num7, num8, num9 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        # 每次投注失败时的总共的亏损
        losemoney = 0
        currentHour=0
        currentMinute=0
        currenttenMinute=0
        currenthalfMinute=0
        show019time=0
        no019time=0
        url = 'https://www.150106.com/api/lastOpenedIssues.php?id=1&issueCount=50'
        period = "period"
        datalist = "list"
        betFlag = True
        betwintime = 0
        minbetwintime=0
        tenminbetwintime = 0
        halfminbetwintime = 0
        nowintime = 0
        minnowintime=0
        tenminnowintime = 0
        halfminnowintime=0
        carnivalwin = 0
        minpaw=0
        tenminpaw = 0
        halfminpaw = 0
        numpaw=0
        numList=[num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
        #xls的行数
        paw=0
        #是否开始失败x次后开始投注选项！8888888888888888
        isgobet=False
        gobet=0
        betovertime=0
        return currentperiod,get019,benefit,tim,bettime,firstnum,secnum,trdnum,multiple\
            ,losemoney,url,period,datalist,betFlag,betwintime,nowintime,carnivalwin,\
               num0, num1, num2, num3, num4, num5, num6, num7, num8, num9,\
               paw,currentHour,currentMinute,currenttenMinute,currenthalfMinute,show019time,no019time,\
               minbetwintime,tenminbetwintime,halfminbetwintime,minnowintime,tenminnowintime,halfminnowintime,minpaw,tenminpaw,halfminpaw,numpaw,numList,\
               isgobet,gobet,betovertime
    #判断链接转换
    def JudgeUrl(self,url):
        if url == "http://www.tongling8.com/kj/txffc/cate.php":
            return "https://www.150106.com/api/lastOpenedIssues.php?id=1&issueCount=50"
        elif url=="https://www.150106.com/api/lastOpenedIssues.php?id=1&issueCount=50":
            return "http://www.10086020.com/txffc/kjls/kj.php"
        elif url == "http://www.10086020.com/txffc/kjls/kj.php":
            return "http://www.tongling8.com/kj/txffc/cate.php"

    def JudgeUrl2(self,url):
        if url == 'http://www.10086020.com/txffc/kjls/kj.php':
            return "period","list"
        elif url == "http://www.tongling8.com/kj/txffc/cate.php":
            return "issue","data"
        elif url=="https://www.150106.com/api/lastOpenedIssues.php?id=1&issueCount=50":
            return ""
    def requestData(self,url):
        if url == 'http://www.10086020.com/txffc/kjls/kj.php':
            time= "period"
            datalist ="list"
            context = ssl._create_unverified_context()
            f = request.urlopen(url, context=context, timeout=7)
            data = f.read()
            d = data.decode('UTF-8')
            t = json.loads(d)
            listx = t[datalist][0]
            period=listx[time]
            kjxx=listx["result"]
            num1=kjxx[4]
            num2=kjxx[6]
            num3=kjxx[8]

        elif url == "http://www.tongling8.com/kj/txffc/cate.php":
            time= "issue"
            datalist="data"
            context = ssl._create_unverified_context()
            f = request.urlopen(url, context=context, timeout=7)
            data = f.read()
            d = data.decode('UTF-8')
            t = json.loads(d)
            listx = t[datalist][0]
            period = listx[time]
            kjxx=listx["result"]
            num1 = kjxx[4]
            num2 = kjxx[6]
            num3 = kjxx[8]
        elif url=="https://www.150106.com/api/lastOpenedIssues.php?id=1&issueCount=50":
            datalist="result"
            context = ssl._create_unverified_context()
            f = request.urlopen(url, context=context, timeout=7)
            data = f.read()
            d = data.decode('UTF-8')
            t = json.loads(d)
            listx = t[datalist]
            listxx=str(listx).split(",")[0].split("|")
            period = listxx[0].replace("-", "")

            l = list(listxx[1])
            s = StringIO()
            for x in range(0, 5):
                s.write(l[x])
                if x != 4:
                    s.write(",")
            kjxx=s.getvalue()
            num1 = kjxx[4]
            num2 = kjxx[6]
            num3 = kjxx[8]



        return listx,period,kjxx,num1,num2,num3

    # 打印全开奖信息
    def insertinfo(self,str,lb2,filezj,fileallkj):
        lb2.insert(0,str)
        filezj.write(str+ "\n")
        fileallkj.write(str+ "\n")
    #打印仅仅中奖信息
    def insertzjinfo(self,str,lb2,filezj):
        lb2.insert(0, str)
        filezj.write(str + "\n")
    #判断是否中奖
    def iswin(self,listx,firstnum,secnum,tirdnum):
        if (listx[4:].find(firstnum) < 0 and
                listx[4:].find(secnum) < 0 and
                listx[4:].find(tirdnum) < 0):
            return True
        else:
            return False
    #投注失败
    def addfalure(self,var1,var2,var3,var5,get019,tim,multiple):
        currentmoney = var2.get()
        benefit = pow(2, (get019 - tim - 1)) * 0.343 * multiple
        var2.set(currentmoney - benefit)
        get019 = 0
        #修改这个即可恢复正常版666666666666666666666666666
        betFlag = True
        #8888888888888888
        isgobet=False
        failvar = var5.get()
        failvar = failvar + 1
        var5.set(failvar)
        money = var2.get()
        var3.set(money - var1.get())
        return get019,betFlag,benefit,isgobet
    # #参与投注但是未中奖
    def betnowin(self,get019,tim,multiple,losemoney,var2):
        benefit = pow(2, (get019 - tim - 1)) * 0.343 * multiple
        currentmoney = var2.get()
        losemoney = losemoney + benefit
        print(benefit)
        var2.set(currentmoney - benefit)
        return losemoney,benefit
    #是否不投钱
    def isnotToss(self,get019,tim):
        if get019 < tim:
            return True
        else:
            return False
    #失败后开启投注的参数修改
    def betwinandopenbet(self):
            betwintime = 0
            #狂欢赢钱的投注次数
            # tim = 1
            # bettime = 4
            # #狂欢赢钱次数清零
            # carnivalwin = 0
            nowintime = 0
            betFlag = True
            return betwintime,nowintime,betFlag
    #准备开始投注1
    def beganGotobet(self,get019,tim,lb2,u019):
        if (get019 == tim):
            lb2.insert(0, "即将开始投注")
            # u019.gopay(u019,1)
            # u019.gopay2(u019,1)
            u019.playvoice("wait.wav")
    #播放声音
    def playvoice(self,name):

        # winsound.PlaySound(name, winsound.SND_FILENAME)
        pass

    #是否开启投注
    def isopentoBet(self,betwintime,nowintime):
        #betwintime为赢钱次数大于2 ，连续不赢的次数nowintime大于5
        #
        if betwintime >= 2 and nowintime >= 5:
            return True
        else:
            return False


    #投注成功收米
    def winbet(self,var1,var2,var3,var4,get019,tim,multiple,carnivalwin,betovertime):
        shoumi = var4.get()
        shoumi = shoumi + 1
        var4.set(shoumi)
        money = var2.get()
        # 获得收益
        benefit = pow(2, (get019 - tim)) * 0.343 * multiple
        print("收益：%0.2f" % (benefit * 2.84))
        money = money + benefit * 1.84
        var2.set(money)
        var3.set(money - var1.get())
        betovertime = betovertime + 1
        # carnivalwin=carnivalwin+ 1
        return carnivalwin,benefit,betovertime
    def carnivaltimeover(self,carnivalwin,var8,var9,tim,bettime):
        if (carnivalwin >= 4):
            carnivalwin = 0
            tim = var8.get()
            bettime = var9.get()
        return carnivalwin,tim,bettime


    #get019----019出现的次数
    #tim 未中奖的前置次数
    #bettime 投注x次
    def isfalureTost(self,get019,tim,bettime):
        if get019 > tim and get019 <= bettime+tim-1:
            return True
        else:
            return False
    def isFalure(self,get019,bettime,tim):
        if get019 > bettime+tim-1:
            return True
        else:
            return False


    def isUpdateperiod(self,currentperiod,period):
        if currentperiod < int(period):
            return True
        else:
            return False
    #每小时记录一次
        # 每小时记录一次
    def hourchangescount(self, currentHour, filenumapper, show019time, no019time, ws, paw):
        if (datetime.datetime.now().hour == 0 and currentHour != 0):
            currentHour = -1
        if (currentHour < datetime.datetime.now().hour):
                # print(datetime.datetime.now().hour)
            currentHour = datetime.datetime.now().hour
            ws.write(paw, 0, currentHour)
            ws.write(paw, 1, show019time)
            ws.write(paw, 2, no019time)
            paw = paw + 1
            show019time = 0
            # print(paw)
            no019time = 0

            # print(paw)
        return currentHour, show019time, no019time, paw

    def wincore(self,lb2,no019time,minnowintime,tenminnowintime,halfminnowintime):
        # 避免listbox行数过多
        lb2.delete(49, 50)
        no019time+=1
        minnowintime+=1
        tenminnowintime+=1
        halfminnowintime+=1
        # print(no019time)
        return no019time,minnowintime,halfminnowintime,tenminnowintime
    def losecore(self,lb2,show019time,minbetwintime,tenminbetwintime,halfminbetwintime):
        lb2.delete(49, 50)
        show019time += 1
        minbetwintime+=1
        tenminbetwintime+=1
        halfminbetwintime+=1
        # print(show019time)
        return show019time,minbetwintime,tenminbetwintime,halfminbetwintime
    # 记录每5分钟赢的次数和输的次数
    def countMinute(self,currentMinute,ws,minpaw,minbetwintime,minnowintime,passminute):
        # 过去的分钟数

        if currentMinute-30>=datetime.datetime.now().minute:
            currentMinute=datetime.datetime.now().minute-passminute
        if currentMinute+passminute<=datetime.datetime.now().minute:
            currentMinute=datetime.datetime.now().minute
            ws.write(minpaw, 0, str(datetime.datetime.now().hour)+":"+str(currentMinute))
            ws.write(minpaw, 1, minbetwintime)
            ws.write(minpaw, 2, minnowintime)
            minpaw+=1
            minnowintime=0
            minbetwintime=0
        return minpaw,minnowintime,minbetwintime,currentMinute

    def writenumws(self,ws,numpaw,num1,num2,num3,currentperiod):
        ws.write(numpaw,0,currentperiod)
        ws.write(numpaw,1,num1)
        ws.write(numpaw,2,num2)
        ws.write(numpaw, 3, num3)
        numpaw+=1
        return numpaw



    #失败后进行连续失败2次 且第二次失败要连续5次以上
    def TosslossWay1(self,betwintime,nowintime,u019,listkjxx,dt,lb2,fileallkj,get019,tim):
        betwintime = betwintime + 1
        # 赢钱次数大于betwintime，连续不赢的次数大于nowintime
        if u019.isopentoBet(betwintime, nowintime):
            # 狂热时间开启 （目前已注释）
            betwintime, nowintime, betFlag = u019.betwinandopenbet()
            result = "终于尼玛中奖了,号码为%s %s %s,投注开启！！时间:%s" % (
                listkjxx["result"][4], listkjxx["result"][6], listkjxx["result"][8],
                str(dt[0:20]))
            u019.insertzjinfo(result, lb2, fileallkj)
            # 准备开始投注
            u019.beganGotobet(get019, tim, lb2)
        else:
            # 中奖了但是还没有满足连赢条件
            result = "终于尼玛中奖了,号码为%s %s %s,开启条件未满！！！！时间:%s" % (
                listkjxx["result"][4], listkjxx["result"][6], listkjxx["result"][8],
                str(dt[0:20]))
            u019.insertzjinfo(result, lb2, fileallkj)
            nowintime, get019 = 0, 0
        return nowintime, get019,betwintime,betFlag

    #出现5次没有019才能复活
    def Tosslossway2(self,carnivalwin,betFlag,lb2,dt,nowintime):
        bettime=3
        carnivalwin+=1
        if carnivalwin>=bettime:
            betFlag=True
            carnivalwin=0
            nowintime=0
            get019=0
            lb2.insert(0,"中了%s次啦！解放啦！！！s时间:%s"%(bettime,str(dt[0:20])))

        else:
            lb2.insert(0,"中奖次数不足，当前已经%s次,时间：%s"%(carnivalwin,str(dt[0:20])))
            get019=0
        return betFlag,carnivalwin,get019,nowintime

    def judgenum(self,num, numList, newList):
        maxflag = 0
        for n in numList:
            if num - n < 0:
                maxflag += 1
        if maxflag < 3:
            newList.append(num)

    def Tosslossway3(self,numList,varnm1,varnm2,varnm3):
        newList=[]
        posList=[]
        pos=[]
        for n in numList:
            newList.append(n)
        pos1 =max(newList)
        newList.remove(pos1)
        pos2 = max(newList)
        newList.remove(pos2)
        pos3 = max(newList)
        newList.remove(pos3)
        maxpos1=numList.index(pos1)
        maxpos2 = numList.index(pos2)
        maxpos3= numList.index(pos3)
        posList.append(maxpos1)
        posList.append(maxpos2)
        posList.append(maxpos3)
        posList.sort()
        for id in posList:
            if id not in pos:
                pos.append(id)
            elif id + 1 not in pos:
                pos.append(id + 1)
            elif id + 2 not in pos:
                pos.append(id + 2)
            elif id + 3 not in pos:
                pos.append(id + 3)
            elif id + 4 not in pos:
                pos.append(id + 4)

        varnm1.set(str(maxpos1))
        varnm2.set(str(maxpos2))
        varnm3.set(str(maxpos3))
        print(maxpos1,maxpos2,maxpos3)
        return str(maxpos1),str(maxpos2),str(maxpos3)

    def Tosslossway4(self):
        pass

    def count0to9(self,num1,num2,num3,numList):
        for n in range(0,10):
            if int(num1)==n:
                numList[n]+=1
            if int(num2)==n:
                numList[n]+=1
            if int(num3)==n:
                numList[n]+=1
        print(numList)
        return numList

    def mouse_click(self,x=None, y=None):
        if not x is None and not y is None:
            windll.user32.SetCursorPos(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def mouse_dclick(self,x=None, y=None):
        if not x is None and not y is None:
            windll.user32.SetCursorPos(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def key_input(self,num):
        win32api.keybd_event(num, 0, 0, 0)
        win32api.keybd_event(num, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.01)

    def inputtimes(self,u019,times,passtime):
        if(times==1):
            time.sleep(passtime)
            u019.key_input(0x33)
        elif times==2:
            time.sleep(passtime)
            u019.key_input(0x36)
        elif times==3:
            time.sleep(passtime)
            u019.key_input(0x31)
            time.sleep(passtime)
            u019.key_input(0x32)
        elif times ==4:
            time.sleep(passtime)
            u019.key_input(0x32)
            time.sleep(passtime)
            u019.key_input(0x34)
        elif times ==5:
            time.sleep(passtime)
            u019.key_input(0x34)
            time.sleep(passtime)
            u019.key_input(0x38)
        elif times ==6:
            time.sleep(passtime)
            u019.key_input(0x39)
            time.sleep(passtime)
            u019.key_input(0x36)
        elif times ==7:
            u019.key_input(0x31)
            time.sleep(passtime)
            u019.key_input(0x39)
            time.sleep(passtime)
            u019.key_input(0x32)
            time.sleep(passtime)
    #自己的支付
    def gopay(self,u019,times,mul=1,hmul=1):
        passtime=0.3
        u019.key_input(0x1B)
        time.sleep(passtime)
        u019.mouse_click(1403,359)
        time.sleep(passtime)
        u019.mouse_click(int(1400*mul),int(600*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1400*mul),int(660*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1400*mul),int(720*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(715*mul),int(600*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(715*mul),int(660*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(715*mul),int(720*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(780*mul),int(600*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(780*mul),int(660*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(780*mul),int(720*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1260*mul),int(600*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1260*mul),int(660*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1260*mul),int(720*hmul))
        time.sleep(passtime)

        u019.mouse_dclick(int(1102 * mul), int(770 * hmul))
        time.sleep(passtime*2)
        u019.inputtimes(u019,times,passtime*2)

        time.sleep(passtime)
        u019.mouse_click(int(930*mul),int(805*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(910*mul),int(780*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1400*mul),int(780*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1550*mul),int(860*hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1270*mul),int(520*hmul))
        time.sleep(passtime)
        u019.key_input(0x1B)
        time.sleep(passtime)


    def gopay2(self, u019,times):
        #forps
        passtime=0.3
        mul = 1
        hmul = 1
        u019.key_input(0x1B)
        time.sleep(passtime)
        u019.mouse_click(int(1118 * mul), int(628 * hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1345 * mul), int(300 * hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1357 * mul), int(546 * hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1357 * mul), int(602 * hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1357 * mul), int(655 * hmul))
        time.sleep(passtime)
        #019
        u019.mouse_click(int(670 * mul), int(545 * hmul))
        time.sleep(passtime)
        u019.mouse_click(int(670 * mul), int(602 * hmul))
        time.sleep(passtime)
        u019.mouse_click(int(670 * mul), int(655 * hmul))
        time.sleep(passtime)
        u019.mouse_click(int(728 * mul), int(545 * hmul))
        time.sleep(passtime)
        u019.mouse_click(int(728 * mul), int(602 * hmul))
        time.sleep(passtime)
        u019.mouse_click(int(728 * mul), int(655 * hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1206 * mul), int(545 * hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1206 * mul), int(602 * hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1206 * mul), int(655 * hmul))
        time.sleep(passtime)

        u019.mouse_click(int(874 * mul), int(744 * hmul))
        time.sleep(passtime)
        u019.mouse_click(int(860 * mul), int(715 * hmul))
        time.sleep(passtime)

        u019.mouse_dclick(int(1048 * mul), int(715 * hmul))
        time.sleep(passtime)
        u019.inputtimes(u019, times,passtime)
        time.sleep(passtime)


        u019.mouse_click(int(1355 * mul), int(715 * hmul))
        time.sleep(passtime)
        u019.mouse_click(int(1515 * mul), int(800 * hmul))
        time.sleep(passtime)

        u019.mouse_click(int(1192 * mul), int(463 * hmul))
        time.sleep(passtime)
        u019.key_input(0x1B)
        time.sleep(passtime)


















