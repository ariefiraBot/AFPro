# -*- coding: utf-8 -*-

import ARIEFIRA
from ARIEFIRA import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
import youtube_dl
 

botStart = time.time()

gye = LineClient(authToken="EwlOMRSdr3TytJZTBlwb.5TJ574/cd62CzBU10EXXsW.p4X6X57aZUw9cVZwhkL+Rs5zOTobTAxhAOXMWhx4tqI=")
ais = LineClient(authToken="EvMIrxy6K7pPzRlB2oef.Wg7X9UypxJoU9Ba7qNI/JW.Gzv49GgzQSNoVn0SOERVAu2HybT/aNjC30N6CCUuBmg=")
ki2 = LineClient(authToken="EvVs88oQboryDeNNnBU3.TbIH3XpUQAgLbH1XED8cyW.NxkBZutTbbt3LjjGYOMSd/CYn21jUmsaVQgIXQoHG4k=")
ki3 = LineClient(authToken="EvL0CaiUOGYwY64ie177.Ej8RQ9eha4DWzbeKsC7wnW.xU3TXHB0DWiwY5SiVEzSfwCjCNLQ083lKYoftstNXyo=")
ki4 = LineClient(authToken="EvihzxOOd5q7Mt6dE575.apNsaBy6aP3PigpnNpYr1q.wC/qPOja7JcRTkhoPHDjPHmC6+QehcUXLbt7cVNjXxo=")
ki5 = LineClient(authToken="EvgZBmfx50qdaed5lOYe.yVyeR0q6DDSJTQ5gNsmqxG.+pGvgIKYUpyrmTlcJ4mjGhyu27hkGPar2feQeU5V110=")
ki6 = LineClient(authToken="Ev9K5F2CJHqnzAXhBB86.D0aYYAS66mXgBmTu3T08LG.0YLUEaATKJJiacre/xDvnEkZai2Q87wTb/x4ND8I3Ec=")
ki7 = LineClient(authToken="Ev9FiVAOeCjNnqVIcOH5.2eA7gbwfLwnW1ji7QOOqLq./lxPYjZYK/dbp9EifUweT/hp8nsk4kcj96gl4PX14So=")
ki8 = LineClient(authToken="Evs1gl0C8fPUAenkMFp1.XAsTn39sGquizsesHUeQ0q.PSr2JMap29r4JWFChetW9mjrV9UY7r31v75G1mUW0CI=")
ki9 = LineClient(authToken="EveMzM7OfZHttCkCNrP4.ZAPgZ566N3LXrrYum1zyXa.0a2ZCmumwvDPMSBvOS8ycqMCbdakw0Af4ts6d8SIhQI=")
ki10 = LineClient(authToken="EvmeVH4ox0vL2cVZuypc.bWgwpyPMQ5hoceOLP7Dopa.aOpz7E4RXj1gmvhkyV8lgtA+kh7bRkwbGhdwglYD8bI=")
KAC = [gye,ais,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
GUE = [ais,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki9,ki10] 
gyeMID = gye.profile.mid
aisMID = ais.profile.mid
ki2MID = ki2.profile.mid
ki3MID = ki3.profile.mid
ki4MID = ki4.profile.mid
ki5MID = ki5.profile.mid
ki6MID = ki6.profile.mid
ki7MID = ki7.profile.mid
ki8MID = ki8.profile.mid
ki9MID = ki9.profile.mid
ki10MID = ki10.profile.mid
Bots = [gyeMID,aisMID,ki2MID,ki3MID,ki4MID,ki5MID,ki6MID,ki7MID,ki8MID,ki9MID,ki10MID] #ini jangan dinrubah Gunanya agar bot tidak saling kick
creator = ["ue6d8f9ef8f820fad9c65bbb5d1ec714b"]
Owner = ["ue6d8f9ef8f820fad9c65bbb5d1ec714b"]
admin = ["ue6d8f9ef8f820fad9c65bbb5d1ec714b"]

gyeProfile = gye.getProfile()
aisProfile = ais.getProfile()
ki2Profile = ki2.getProfile()
ki3Profile = ki3.getProfile()
ki4Profile = ki4.getProfile()
ki5Profile = ki5.getProfile()
ki6Profile = ki6.getProfile()
ki7Profile = ki7.getProfile()
ki8Profile = ki8.getProfile()
ki9Profile = ki9.getProfile()
ki10Profile = ki10.getProfile()

lineSettings = gye.getSettings()
aisSettings = ais.getSettings()
ki2Settings = ki2.getSettings()
ki3Settings = ki3.getSettings()
ki4Settings = ki4.getSettings()
ki5Settings = ki5.getSettings()
ki6Settings = ki6.getSettings()
ki7Settings = ki7.getSettings()
ki8Settings = ki8.getSettings()
ki9Settings = ki9.getSettings()
ki10Settings = ki10.getSettings()

poll = LinePoll(gye)
poll1 = LinePoll(ais)
poll2 = LinePoll(ki2)
poll3 = LinePoll(ki3)
poll4 = LinePoll(ki4)
poll5 = LinePoll(ki5)
poll6 = LinePoll(ki6)
poll7 = LinePoll(ki7)
poll8 = LinePoll(ki8)
poll9 = LinePoll(ki9)
poll10 = LinePoll(ki10)

responsename = gye.getProfile().displayName
responsename2 = ais.getProfile().displayName
responsename3 = ki2.getProfile().displayName
responsename2 = ki3.getProfile().displayName
responsename3 = ki4.getProfile().displayName
responsename5 = ki5.getProfile().displayName
responsename7 = ki6.getProfile().displayName
responsename8 = ki7.getProfile().displayName
responsename6 = ki8.getProfile().displayName
responsename10 = ki9.getProfile().displayName
responsename9 = ki10.getProfile().displayName
#==============================================================================#

with open('Owner.json', 'r') as fp:
    Owner = json.load(fp)
    
with open('admin.json', 'r') as fp:
    admin = json.load(fp)
    
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = gyeProfile.displayName
myProfile["statusMessage"] = gyeProfile.statusMessage
myProfile["pictureStatus"] = gyeProfile.pictureStatus

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

#==============================================================================#

read = json.load(readOpen)
settings = json.load(settingsOpen)

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    gye.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        gye.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def helpmessage():
    helpMessage = "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ ⭐️☀️Boy-FirA™️☀️⭐ BOTS" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ HELP      ❂  Boy-FirA™️" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ Help 1" + "\n" + \
                  "║͜͡☆➣ Help 2" + "\n" + \
                  "║͜͡☆➣ tagall" + "\n" + \
                  "║͜͡☆➣ Masuk( panggil bot ) " + "\n" + \
                  "║͜͡☆➣ Absen" + "\n" + \
                  "║͜͡☆➣ Pamit( usir bot ) " + "\n" + \
                  "║͜͡☆➣ Wassalam ( kluar semua ) " + "\n" + \
                  "║͜͡☆➣ Cekk ( cek semua bot )" + "\n" + \
                  "║͜͡☆➣ Me" + "\n" + \
                  "║͜͡☆➣ Sp" + "\n" + \
                  "║͜͡☆➣ Status" + "\n" + \
                  "║͜͡☆➣ Ciak @" + "\n" + \
                  "║͜͡☆➣ Kickallmember" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ ⭐️☀️Boy-FirA™️☀️⭐ BOTS" + "\n" + \
                  "╰════════╬♥╬════════╯"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ ⭐️☀️Boy-FirA™️☀️⭐ BOTS" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ HELP 2  ❂  Boy-FirA™️" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ Help 1" + "\n" + \
                  "║͜͡☆➣ Help 2" + "\n" + \
                  "║͜͡☆➣ Protect on/off" + "\n" + \
                  "║͜͡☆➣ QrProtect on/off" + "\n" + \
                  "║͜͡☆➣ InviteProtect on/off" + "\n" + \
                  "║͜͡☆➣ CancelProtect on/off" + "\n" + \
                  "║͜͡☆➣ AutoAdd on/off" + "\n" + \
                  "║͜͡☆➣ AutoJoin on/off" + "\n" + \
                  "║͜͡☆➣ AutoLeave on/off" + "\n" + \
                  "║͜͡☆➣ CheckSticker on/off" + "\n" + \
                  "║͜͡☆➣ AutoRead on/off" + "\n" + \
                  "║͜͡☆➣ DetectMention on/off" + "\n" + \
                  "║͜͡☆➣ Join link on/off" + "\n" + \
                  "║͜͡☆➣ GroupCreator" + "\n" + \
                  "║͜͡☆➣ GroupId" + "\n" + \
                  "║͜͡☆➣ GroupName" + "\n" + \
                  "║͜͡☆➣ GroupPicture" + "\n" + \
                  "║͜͡☆➣ GroupList" + "\n" + \
                  "║͜͡☆➣ GroupMemberList" + "\n" + \
                  "║͜͡☆➣ GroupInfo" + "\n" + \
                  "║͜͡☆➣ Gt" + "\n" + \
                  "║͜͡☆➣ Gt on/off" + "\n" + \
                  "║͜͡☆➣ Mimic on" + "\n" + \
                  "║͜͡☆➣ Mimic off" + "\n" + \
                  "║͜͡☆➣ MimicAdd" + "\n" + \
                  "║͜͡☆➣ MimicDel" + "\n" + \
                  "║͜͡☆➣ Lurking on/off" + "\n" + \
                  "║͜͡☆➣ Lurking" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ ⭐️☀️Boy-FirA™️☀️⭐ BOTS" + "\n" + \
                  "╰════════╬♥╬════════╯"
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate =    "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ ⭐️☀️Boy-FirA™️☀️⭐ BOTS" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ HELP 3  ❂   Boy-FirA™️" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ AdminLit" + "\n" + \
                  "║͜͡☆➣ OwnerList" + "\n" + \
                  "║͜͡☆➣ BanContact" + "\n" + \
                  "║͜͡☆➣ UnbanContact" + "\n" + \
                  "║͜͡☆➣ BanList" + "\n" + \
                  "║͜͡☆➣ Clearban" + "\n" + \
                  "║͜͡☆➣ Restart" + "\n" + \
                  "║͜͡☆➣ About" + "\n" + \
                  "║͜͡☆➣ Me" + "\n" + \
                  "║͜͡☆➣ MyMid" + "\n" + \
                  "║͜͡☆➣ Midnya @" + "\n" + \
                  "║͜͡☆➣ MyName" + "\n" + \
                  "║͜͡☆➣ MyBio" + "\n" + \
                  "║͜͡☆➣ MyPicture" + "\n" + \
                  "║͜͡☆➣ MyVideoProfile" + "\n" + \
                  "║͜͡☆➣ MyCover" + "\n" + \
                  "║͜͡☆➣ StealContact @" + "\n" + \
                  "║͜͡☆➣ StealMid @" + "\n" + \
                  "║͜͡☆➣ StealName「Mention」" + "\n" + \
                  "║͜͡☆➣ StealBio @" + "\n" + \
                  "║͜͡☆➣ StealPicture @" + "\n" + \
                  "║͜͡☆➣ StealVideoProfile @" + "\n" + \
                  "║͜͡☆➣ StealCover @" + "\n" + \
                  "║͜͡☆➣ CloneProfile @" + "\n" + \
                  "║͜͡☆➣ RestoreProfile" + "\n" + \
                  "║͜͡☆➣ GroupCreator" + "\n" + \
                  "║͜͡☆➣ GroupId" + "\n" + \
                  "║͜͡☆➣ GroupName" + "\n" + \
                  "║͜͡☆➣ GroupPicture" + "\n" + \
                  "║͜͡☆➣ Gt" + "\n" + \
                  "║͜͡☆➣ Gt「On/Off」" + "\n" + \
                  "║͜͡☆➣ GroupList" + "\n" + \
                  "║͜͡☆➣ GroupMemberList" + "\n" + \
                  "║͜͡☆➣ GroupInfo" + "\n" + \
                  "║͜͡☆➣ Ciak @" + "\n" + \
                  "║͜͡☆➣ KickAllMember"+ "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ ⭐️☀️Boy-FirA™️☀️⭐ BOTS" + "\n" + \
                  "╰════════╬♥╬════════╯"
    return helpTranslate
#==============================================================================#
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
        
def command(text):
    pesan = text.lower()
    if pesan.startswith(settings["keyCommand"]):
        cmd = pesan.replace(settings["keyCommand"],"")
    else:
        cmd = "Undefined command"
    return cmd        


def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] ⭐️☀️ARIEF☀️⭐ BOTS SATU")
            return
#-------------------------------------------------------------------------------
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        gye.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        gye.sendMessage(msg.to,"Itu tidak berkomentar")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        gye.sendMessage(msg.to,"Done")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        gye.sendMessage(msg.to,"Tidak ada dalam daftar hitam")
#-------------------------------------------------------------------------------
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        gye.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        gye.sendMessage(msg.to,"Done")
                        
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        gye.sendMessage(msg.to,"Done")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        gye.sendMessage(msg.to,"Done")
                        
                       
#-------------------------------------------------------------------------------
        if op.type == 25:
            print ("[ 25 ] ⭐️☀️ARIEF☀️⭐ BOTS TIGA")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != gye.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    gye.sendMessage(to, str(helpMessage))
                    gye.sendContact(to, "ue6d8f9ef8f820fad9c65bbb5d1ec714b")
                    gye.sendMessage(to,"█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
                elif text.lower() == 'help 1':
                    helpTextToSpeech = helptexttospeech()
                    gye.sendMessage(to, str(helpTextToSpeech))
                    gye.sendMessage(to, "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
                elif text.lower() == 'help 2':
                    helpTranslate = helptranslate()
                    gye.sendMessage(to, str(helpTranslate))
                    gye.sendMessage(to, "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
#==============================================================================#
                elif text.lower() == 'sp':
                    start = time.time()
                    gye.sendMessage(to, "Cek Speed...")
                    elapsed_time = time.time() - start
                    gye.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'restart':    
                    gye.sendMessage(to, "Please Wait...")
                    time.sleep(5)
                    gye.sendMessage(to, "Restart Sukses")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    gye.sendMessage(to, "login bot selama {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "ue6d8f9ef8f820fad9c65bbb5d1ec714b"
                        creator = gye.getContact(owner)
                        contact = gye.getContact(gyeMID)
                        grouplist = gye.getGroupIdsJoined()
                        contactlist = gye.getAllContactIds()
                        blockedlist = gye.getBlockedContactIds()
                        ret_ = "╭════════╬♥╬════════╮\nStatus Bots\n ╰════════╬♥╬════════╯\n ╭════════╬♥╬════════╮\n"
                        ret_ += "\n╠ akun : {}".format(contact.displayName)
                        ret_ += "\n╠ group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ teman : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blokir : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ About Selfbot ]"
                        ret_ += "\n╠ Version : Premium"
                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                        ret_ += "\n╰════════╬♥╬════════╯\n\n⭐️☀️ARIEF☀️⭐ BOTS╭════════╬♥╬════════╮\n╰════════╬♥╬════════╯"
                        gye.sendMessage(to, str(ret_))
                    except Exception as e:
                        gye.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'status':
                    try:
                        ret_ = "╭════════╬♥╬════════╮\n ║͜͡☆➣ ♥ Status Bots ♥\n ╰════════╬♥╬════════╯\n ╭════════╬♥╬════════╮\n"
                        if settings["protect"] == True: ret_ += "║͜͡☆➣ Protect ✅"
                        else: ret_ += "║͜͡☆➣  Protect ❌"
                        if settings["qrprotect"] == True: ret_ += "\n║͜͡☆➣ Qr Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Qr Protect ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n║͜͡☆➣ Invite Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Invite Protect ❌"
                        if settings["cancelprotect"] == True: ret_ += "\n║͜͡☆➣ Cancel Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Cancel Protect ❌"
                        if settings["autoAdd"] == True: ret_ += "\n║͜͡☆➣ Auto Add ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n║͜͡☆➣ Auto Join ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n║͜͡☆➣ Auto Leave ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n║͜͡☆➣ Auto Read ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n║͜͡☆➣ Check Sticker ✅"
                        else: ret_ += "\n║͜͡☆➣ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n║͜͡☆➣ Detect Mention ✅"
                        else: ret_ += "\n║͜͡☆➣ Detect Mention ❌"
                        ret_ += "\n╰════════╬♥╬════════╯\n╭════════╬♥╬════════╮\n  ║͜͡☆➣ ♥ ⭐️☀️ARIEF☀️⭐ BOTS ♥\n╰════════╬♥╬════════╯"
                        gye.sendMessage(to, str(ret_))
                    except Exception as e:
                        gye.sendMessage(msg.to, str(e))
                        
                elif msg.text.lower().startswith("spaminvite "):
                   #if msg._from in admin:
                    dan = text.split("|")
                    userid = dan[0]
                    namagrup = dan[0]
                    jumlah = int(dan[0])
                    grups = gye.groups
                    tgb = gye.findContactsByUserid(userid)
                    if jumlah <= 1000:
                        for var in range(0,jumlah):
                            try:
                                gye.createGroup(str(namagrup), [tgb.mid])
                                for i in grups:
                                    grup = gye.getGroup(i)
                                    if grup.name == namagrup:
                                        gye.inviteIntoGroup(grup.id, [tgb.mid])
                                        gye.sendMessage(to, "@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                            except Exception as Nigga:
                                gye.sendMessage(to, str(Nigga))
                            #else:
                                gye.sendMessage(to, "@! kebanyakan njer!!", [sender])
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("owneradd "):
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                Owner[target] = True
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Owner ☢-Bot-☢\nAdd\nExecuted")
                            except:
                                pass
                    
                elif msg.text.lower().startswith("ownerdel "):
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del Owner[target]
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Owner ☢-Bot-☢\nRemove\nExecuted")
                            except:
                                pass
#-------------------------------------------------------------------------------
                elif text.lower() == 'ownerlist':
                        if Owner == []:
                            gye.sendMessage(msg.to,"The Ownerlist is empty")
                        else:
                            gye.sendMessage(msg.to,"Tunggu...")
                            mc = "╔═══════════════\n╠⭐️☀️ARIEF☀️⭐ \n╠══✪〘 Owner List 〙✪═══\n"
                            for mi_d in admin:
                                mc += "╠✪ " +gye.getContact(mi_d).displayName + "\n"
                            gye.sendMessage(msg.to,mc + "╠═══════════════\n╠✪〘 ⭐️☀️ARIEF☀️⭐ 〙\n╚═══════════════")
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("adminadd "):
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                admin[target] = True
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Admin ☢-Bot-☢\nAdd\nExecuted")
                                break
                            except:
                                gye.sendMessage(msg.to,"Added Target Fail !")
                                break
                    
                elif msg.text.lower().startswith("admindel "):
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del admin[target]
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Admin ☢-Bot-☢\nRemove\nExecuted")
                                break
                            except:
                                gye.sendMessage(msg.to,"Deleted Target Fail !")
                            break
              #      else:
               #         gye.sendMessage(msg.to,"Owner Permission Required")
#-------------------------------------------------------------------------------
                elif text.lower() == 'adminlist':
                #    if msg._from in Owner:
                        if admin == []:
                            gye.sendMessage(msg.to,"The Adminlist is empty")
                        else:
                            gye.sendMessage(msg.to,"Tunggu...")
                            mc = "╔═══════════════\n╠⭐️☀️ARIEF☀️⭐ \n╠══✪〘 Admin List 〙✪═══\n"
                            for mi_d in admin:
                                mc += "╠✪ " +gye.getContact(mi_d).displayName + "\n"
                            gye.sendMessage(msg.to,mc + "╠═══════════════\n╠✪〘 ⭐️☀️ARIEF☀️⭐ 〙\n╚═══════════════")
#-------------------------------------------------------------------------------
                elif text.lower() == 'protect on':
                        if settings["protect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Already On")
                        else:
                            settings["protect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Set To On")
                                
                elif text.lower() == 'protect off':
                        if settings["protect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Already Off")
                        else:
                            settings["protect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Set To Off")
#----------------------------------------------------------------------------------------                        
                elif text.lower() == 'qrprotect on':
                        if settings["qrprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Qr Already On")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Qr Set To On")
                        else:
                            settings["qrprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Qr Set To On")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Qr Already On")
                                
                elif text.lower() == 'qrprotect off':
                        if settings["qrprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Qr Already Off")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Qr Set To Off")
                        else:
                            settings["qrprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Qr Set To Off")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Qr Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'inviteprotect on':
                        if settings["inviteprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Invite Already On")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Invite Set To On")
                        else:
                            settings["inviteprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Invite Set To On")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Invite Already On")
                                
                elif text.lower() == 'inviteprotect off':
                        if settings["inviteprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Invite Already Off")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Invite Set To Off")
                        else:
                            settings["inviteprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Invite Set To Off")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Invite Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'cancelprotect on':
                        if settings["cancelprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Already On")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Set To On")
                        else:
                            settings["cancelprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Set To On")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Already On")
                                
                elif text.lower() == 'cancelprotect off':
                        if settings["cancelprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Already Off")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Set To Off")
                        else:
                            settings["cancelprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Set To Off")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Already Off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'pro on':
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        settings["join link"] = True
                        #gye.sendMessage(msg.to,"Join link on")
                        #gye.sendMessage(msg.to,"Qrprotect on")
                        #gye.sendMessage(msg.to,"Protect on")
                        #gye.sendMessage(msg.to,"Inviteprotect on")
                        #gye.sendMessage(msg.to,"Cancelprotect on")
                        gye.sendMessage(msg.to,"➲ All Protect Set To On")
                        		            
                elif text.lower() == 'pro off':
             #       if msg._from in Owner:
                        settings["protect"] = False
                        settings["qrprotect"] = False
                        settings["inviteprotect"] = False
                        settings["cancelprotect"] = False
                        #gye.sendMessage(msg.to,"Qrprotect Off")
                        #gye.sendMessage(msg.to,"Protect Off")
                        #gye.sendMessage(msg.to,"Inviteprotect Off")
                        #gye.sendMessage(msg.to,"Cancelprotect Off")
                        gye.sendMessage(msg.to,"➲ All Protect Set To Modar")
            #        else:
             #           gye.sendMessage(msg.to,"Just for Owner")
#-------------------------------------------------------------------------------
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Add")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Add")
                elif text.lower() == 'autojoin on':
             #     if msg._from in Owner:    
                    settings["autoJoin"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Join")
                elif text.lower() == 'autojoin off':
                #  if msg._from in Owner:    
                    settings["autoJoin"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Join")
                elif text.lower() == 'autoleave on':
               #   if msg._from in Owner:
                    settings["autoLeave"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Leave")
                elif text.lower() == 'autoleave off':
             #     if msg._from in Owner:
                    settings["autoLeave"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Leave")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Read")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Read")
                elif text.lower() == 'checksticker on':
                    settings["checkSticker"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Check Details Sticker")
                elif text.lower() == 'checksticker off':
                    settings["checkSticker"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Check Details Sticker")
                elif text.lower() == 'detectmention on':
                    settings["datectMention"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Detect Mention")
                elif text.lower() == 'detectmention off':
                    settings["datectMention"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Detect Mention")
                elif text.lower() == 'join link on':
                    settings["autoJoinTicket"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Join Link")
                elif text.lower() == 'join link off':
                    settings["autoJoinTicket"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Join Link")                    
#==============================================================================#
                elif msg.text.lower() == 'cekk':
                        gye.sendContact(to, gyeMID)
                        ais.sendContact(to, aisMID)
                        ki2.sendContact(to, ki2MID)
                        ki3.sendContact(to, ki3MID)
                        ki4.sendContact(to, ki4MID)
                        ki5.sendContact(to, ki5MID) 
                elif text.lower() in ["pamit"]:    
                    #gye.leaveGroup(msg.to)
                    ais.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
                    ki3.leaveGroup(msg.to)
                    ki4.leaveGroup(msg.to)
                    ki5.leaveGroup(msg.to)
                    ki6.leaveGroup(msg.to)
                    ki7.leaveGroup(msg.to)
                    ki8.leaveGroup(msg.to)
                    ki9.leaveGroup(msg.to)
                    ki10.leaveGroup(msg.to)
                elif text.lower() in ["wassalam"]:    
                    gye.leaveGroup(msg.to)
                    ais.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
                    ki3.leaveGroup(msg.to)
                    ki4.leaveGroup(msg.to)
                    ki5.leaveGroup(msg.to)
                    ki6.leaveGroup(msg.to)
                    ki7.leaveGroup(msg.to)
                    ki8.leaveGroup(msg.to)
                    ki9.leaveGroup(msg.to)
                    ki10.leaveGroup(msg.to)
  
                elif text.lower() in ["masuk"]:    
                    G = gye.getGroup(msg.to)
                    ginfo = gye.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    gye.updateGroup(G)
                    invsend = 0
                    Ticket = gye.reissueGroupTicket(msg.to)
                    ais.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = gye.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    gye.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    gye.updateGroup(G)
                
                elif text.lower() == 'me':
                    sendMessageWithMention(to, gyeMID)
                    gye.sendContact(to, gyeMID)
                  #  gye.sendMessage(msg.to,"➲ Jangan Songong Pake Sc Orang")
                elif text.lower() == 'mymid':
                    gye.sendMessage(msg.to,"[MID]\n" +  gyeMID)
                elif text.lower() == 'myname':
                    me = gye.getContact(gyeMID)
                    gye.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = gye.getContact(gyeMID)
                    gye.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = gye.getContact(gyeMID)
                    gye.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    me = gye.getContact(gyeMID)
                    gye.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = gye.getContact(gyeMID)
                    cover = gye.getProfileCoverURL(gyeMID)    
                    gye.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("stealcontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            mi_d = contact.mid
                            gye.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("midnya "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        gye.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("stealname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            gye.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("stealbio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            gye.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("stealpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.gye.naver.jp/" + gye.getContact(ls).pictureStatus
                            gye.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealvideoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.gye.naver.jp/" + gye.getContact(ls).pictureStatus + "/vp"
                            gye.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealcover "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = gye.getProfileCoverURL(ls)
                                gye.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cloneprofile "):    
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            gye.cloneContactProfile(contact)
                            gye.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                        except:
                            gye.sendMessage(msg.to, "Gagal clone member")
                elif text.lower() == 'restoreprofile':    
                    try:
                        gyeProfile.displayName = str(myProfile["displayName"])
                        gyeProfile.statusMessage = str(myProfile["statusMessage"])
                        gyeProfile.pictureStatus = str(myProfile["pictureStatus"])
                        gye.updateProfileAttribute(8, gyeProfile.pictureStatus)
                        gye.updateProfile(gyeProfile)
                        gye.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                    except:
                        gye.sendMessage(msg.to, "Gagal restore profile")
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            gye.sendMessage(msg.to,"Target ditambahkan!")
                            break
                        except:
                            gye.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            gye.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            gye.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        gye.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+gye.getContact(mi_d).displayName
                        gye.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            gye.sendMessage(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            gye.sendMessage(msg.to,"Reply Message off")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = gye.getGroup(to)
                    GS = group.creator.mid
                    gye.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = gye.getGroup(to)
                    gye.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = gye.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    gye.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = gye.getGroup(to)
                    gye.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'gt':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = gye.reissueGroupTicket(to)
                            gye.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            gye.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'gt on':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            gye.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            gye.updateGroup(group)
                            gye.sendMessage(to, "Berhasil membuka grup qr")
                elif text.lower() == 'gt off':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            gye.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            gye.updateGroup(group)
                            gye.sendMessage(to, "Berhasil menutup grup qr")
                elif text.lower() == 'groupinfo':
                    group = gye.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(gye.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    gye.sendMessage(to, str(ret_))
                    gye.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        gye.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = gye.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = gye.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        gye.sendMessage(to, str(ret_))
#-------------------------------------------------------------------------------
                elif text.lower() == 'clearban':
                        settings["blacklist"] = {}
                        gye.sendMessage(msg.to,"➲ Done")
                        ais.sendMessage(msg.to,"➲ Done")
                        ki2.sendMessage(msg.to,"➲ Done")
                        ki3.sendMessage(msg.to,"➲ Done")
                        ki4.sendMessage(msg.to,"➲ Done")
                        ki5.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki6.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki7.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki8.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki9.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki10.sendMessage(msg.to,"➲ Jangan Jadi Penjahat yah kakak Agar Tak Masuk Blaclist ku")
                        
                elif text.lower() == 'absen':
                        ais.sendMessage(msg.to,"➲  Kicker on 1")
                        ki2.sendMessage(msg.to,"➲ Kicker on 2")
                        ki3.sendMessage(msg.to,"➲ Kicker on 3")
                        ki4.sendMessage(msg.to,"➲ Kicker on 4")
                        ki5.sendMessage(msg.to,"➲ Kicker on 5")
                        ki6.sendMessage(msg.to,"➲ Kicker on 6")
                        ki7.sendMessage(msg.to,"➲ Kicker on 7")
                        ki8.sendMessage(msg.to,"➲ Kicker on 8")
                        ki9.sendMessage(msg.to,"➲ Kicker on 9")
                        ki10.sendMessage(msg.to,"➲ Kicker on 10")
                        ais.sendMessage(msg.to,"➲  Lengkap Bossq... ")
                        
                elif text.lower() == 'bancontact':
                        settings["wblacklist"] = True
                        gye.sendMessage(msg.to,"Send Contact")
                        
                elif msg.text in ["unbancontact"]:
                        settings["dblacklist"] = True
                        gye.sendMessage(msg.to,"Send Contact")
#-------------------------------------------------------------------------------
                elif text.lower() == 'banlist':
                        if settings["blacklist"] == {}:
                            gye.sendMessage(msg.to,"Tidak Ada Banlist")
                        else:
                            gye.sendMessage(msg.to,"Daftar Banlist")
                            num=1
                            msgs="═══T E R S A N G K A═══"
                            for mi_d in settings["blacklist"]:
                                msgs+="\n[%i] %s" % (num, gye.getContact(mi_d).displayName)
                                num=(num+1)
                            msgs+="\n═══T E R S A N G K A═══\n\nTotal Tersangka :  %i" % len(settings["blacklist"])
                            gye.sendMessage(msg.to, msgs)
#=======================================================================================
                elif msg.text.lower().startswith("ciak "):
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(GUE).kickoutFromGroup(msg.to,[target])
                           except:
                               random.choice(GUE).sendText(msg.to,"Error")
#-------------------------------------------------------------------------------
                elif text.lower() == 'kickallmember':
                 #   if msg._from in Owner:
                        if msg.toType == 2:
                            print ("[ 19 ] ⭐️☀️ARIEF☀️⭐ ALL MEMBER")
                            _name = msg.text.replace("kickallmember","")
                            gs = gye.getGroup(msg.to)
                            gs = ais.getGroup(msg.to)
                            gs = ki2.getGroup(msg.to)
                            gs = ki3.getGroup(msg.to)
                            gs = ki4.getGroup(msg.to)
                           #gye.sendMessage(msg.to,"「 Bye All 」")
                           #gye.sendMessage(msg.to,"「 Sory guys 」")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                gye.sendMessage(msg.to,"Not Found")
                            else:
                                for target in targets:
                                    if not target in Bots:
                                        if not target in Owner:
                                            if not target in admin:
                                                try:
                                                    klist=[ais,ki2,ki3,ki4]
                                                    kicker=random.choice(klist)
                                                    kicker.kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    gye.sendMessage(msg.to,"") 
#==============================================================================#          
                elif text.lower() == 'tagall':
                    group = gye.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+0):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        gye.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        gye.sendMessage(to, "Total {} Mention".format(str(len(nama))))          
                elif text.lower() == 'lurking on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                gye.sendMessage(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            gye.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            #gye.sendMessage(msg.to,"➲ Jangan Songong Pake Sc Orang")
                            
                elif text.lower() == 'lurking off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        gye.sendMessage(msg.to,"Lurking already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        gye.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        gye.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        gye.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'lurking':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            gye.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = gye.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            gye.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        gye.sendMessage(receiver,"Lurking has not been set.")
                        
#===============================================================================[gyeMID - kiMID]
        if op.type == 19:
            print ("[ 19 ] ⭐️☀️ARIEF☀️⭐ BOTS KICK")
            try:
                if op.param3 in gyeMID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
                        ginfo = ais.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[gyeMID - ki2MID]
                elif op.param3 in gyeMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[gyeMID - ki3MID]
                elif op.param3 in gyeMID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[gyeMID - ki4MID]
                elif op.param3 in gyeMID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[kiMID gyeMID]
                if op.param3 in aisMID:
                    if op.param2 in gyeMID:
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)
                        ki5.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki5.updateGroup(G)
                        invsend = 0
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki5.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki5.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki5.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki2MID]
                elif op.param3 in aisMID:
                    if op.param2 in ki2MID:
                        G = ki7.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki7.updateGroup(G)
                        invsend = 0
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki7.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki7.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki7.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)
                        ginfo = ki2.getGroup(op.param1)
                        ki7.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki7.updateGroup(G)
                        invsend = 0
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki7.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki7.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki7.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki3MID]
                elif op.param3 in aisMID:
                    if op.param2 in ki3MID:
                        G = ki9.getGroup(op.param1)
                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki9.updateGroup(G)
                        invsend = 0
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki9.getGroup(op.param1)
                        ginfo = ki3.getGroup(op.param1)
                        ki9.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki9.updateGroup(G)
                        invsend = 0
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki9.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki9.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki9.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki4MID]
                elif op.param3 in aisMID:
                    if op.param2 in ki4MID:
                        G = ki6.getGroup(op.param1)
                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki6.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)
                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki6.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki6.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki6.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki2MID gyeMID]
                if op.param3 in ki2MID:
                    if op.param2 in gyeMID:
                        G = ki10.getGroup(op.param1)
                        ginfo = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki10.updateGroup(G)
                        invsend = 0
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki10.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki10.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki10.updateGroup(G)
                    else:
                        G = ki10.getGroup(op.param1)
                        ginfo = gye.getGroup(op.param1)
                        ki10.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki10.updateGroup(G)
                        invsend = 0
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki10.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki10.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki10.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID kiMID]
                elif op.param3 in ki2MID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
                        ginfo = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID ki3MID]
                elif op.param3 in ki2MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID ki4MID]
                elif op.param3 in ki2MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki3MID gyeMID]
                if op.param3 in ki3MID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
                        ginfo = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
                        ginfo = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID kiMID]
                elif op.param3 in ki3MID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
                        ginfo = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
                        ginfo = ais.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID ki2MID]
                elif op.param3 in ki3MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID ki4MID]
                elif op.param3 in ki3MID:
                    if op.param2 in ki4MID:
                        G = ki4.getGroup(op.param1)
                        ginfo = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        ginfo = ki4.getGroup(op.param1)
                        ki4.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        invsend = 0
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#===============================================================================[ki4MID gyeMID]
                if op.param3 in ki4MID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
                        ginfo = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
                        ginfo = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID kiMID]
                elif op.param3 in ki4MID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
                        ginfo = ais.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID ki2MID]
                elif op.param3 in ki4MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        ginfo = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ginfo = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID ki3MID]
                elif op.param3 in ki4MID:
                    if op.param2 in ki3MID:
                        G = ki3.getGroup(op.param1)
                        ginfo = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ginfo = ki3.getGroup(op.param1)
                        ki3.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki3.updateGroup(G)
                        invsend = 0
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki3.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                        
                elif op.param2 not in Bots:
                    if op.param2 in admin:
                        pass
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(KAC).sendText(op.param1,"Don't Play bro...!")
                        
                else:
                    pass
            except:
                pass
#==============================================================================#
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in admin:
                    pass
                elif settings["inviteprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            settings["blacklist"][op.param2] = True
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])	
#-------------------------------------------------------------------------------
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in admin and Bots and Owner:
                    pass
                elif settings["qrprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    G = ais.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    ais.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    gye.sendMessage(op.param1,"Jangan Buka Qr")
            else:
                gye.sendMessage(op.param1,"Maaf gue kick nih lu pea ngapain buka Qr vekok🤔🤔")
#==============================================================================#
       # if op.type == 55:
        #    print ("[ 55 ] GYEVHA BOTS EMPAT")
         #   if op.param1 in read["readPoint"]:
          #      _name = gye.getContact(op.param2).displayName
           #     tz = pytz.timezone("Asia/Jakarta")
           #     timeNow = datetime.now(tz=tz)
            #    timeHours = datetime.strftime(timeNow," (%H:%M)")
             #   read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)
     #   backupData()
    #except Exception as error:
     #   logError(error)
#==============================================================================#
        if op.type == 25:
            msg = op.message
            if text.lower() == '/ti/g/':    
                if settings["join ticket"] == True:
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        group = gye.findGroupByTicket(ticket_id)
                        gye.acceptGroupInvitationByTicket(group.id,ticket_id)
                        gye.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
                        
    except Exception as error:
        logError(error)
#==============================================================================#
# Auto join if BOT invited to group
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        gye.acceptGroupInvitation(op.param1)
        ais.acceptGroupInvitation(op.param1)
        ki2.acceptGroupInvitation(op.param1)
        ki3.acceptGroupInvitation(op.param1)
        ki4.acceptGroupInvitation(op.param1)
        ki5.acceptGroupInvitation(op.param1)
        ki6.acceptGroupInvitation(op.param1)
        ki7.acceptGroupInvitation(op.param1)
        ki8.acceptGroupInvitation(op.param1)
        ki9.acceptGroupInvitation(op.param1)
        ki10.acceptGroupInvitation(op.param1)
    except Exception as e:
        gye.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
# Auto kick if BOT out to group
def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,op.param2)
        else:
            pass
    except Exception as e:
        gye.log("[NOTIFIED_KICKOUT_FROM_GROUP] ERROR : " + str(e))

while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
