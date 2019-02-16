#coding:utf-8

import commands
import re

PACKAGE_NAME = "com.yixia.videoeditor"
MEMORY_MOBILE = "adb shell 'cat /proc/meminfo'"
MEMORY = "adb shell 'dumpsys meminfo' | grep RAM"
MEMORY_APP = "adb shell 'dumpsys meminfo " + PACKAGE_NAME + " | grep TOTAL:'"
CPUUSED_APP = "adb shell 'top -d 1 -n 1 | grep " + PACKAGE_NAME +"'"
CPU_INFO = "adb shell cat  /proc/cpuinfo | grep 'CPU architecture'"

#手机总内存
memTotal = 0
#手机空闲内存
memFree = 0
#被监控应用的总内存
appMemTotal = 0
#被监控应用的内存使用情况
cpuused = 0


status,result = commands.getstatusoutput(MEMORY_MOBILE)
listResult = result.split("\n")
mapMemResult = {}
mapResult = {}
totalRam = 0
freeRam = 0
usedRam = 0

for i in listResult:
    key = re.search('^(.+):',i).group(1)
    val = re.search('\d+', i).group()
    mapMemResult[key] = val

print "MemTotal=" + mapMemResult["MemTotal"] + " kb"
print "MemFree=" + mapMemResult["MemFree"] + " kb"


status,result = commands.getstatusoutput(MEMORY_APP)
appMemTotal =  re.search('\d+', result).group()

status,result = commands.getstatusoutput(CPUUSED_APP)
print CPUUSED_APP
print result
listResult = result.split("\n")
cpuused = re.search(' (\d+)%', listResult[0]).group(1)

print PACKAGE_NAME + "cpu is used :" + cpuused + "%"

status,result = commands.getstatusoutput(MEMORY)
listResult = result.split("\n")
for i in listResult:
    key = re.search('^(.+):', i).group(1)
    val = re.search('\d+', i).group()
    mapResult[key] = val

print "Total RAM = " + mapResult["Total RAM"] + "kb"
print " Free RAM = " + mapResult[" Free RAM"] + "kb"
print " Used RAM = " + mapResult[" Used RAM"] + "kb"
