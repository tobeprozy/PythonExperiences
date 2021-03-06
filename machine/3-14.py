#!/usr/bin/env python  
# -*- coding: utf-8 -*-
#http://blog.csdn.net/myhaspl  
#code:myhaspl@qq.com
#3-14.py 
import wave
import pylab as pl
import numpy as np


def wavechange(x,dwmax,dwmin):
    if x!=0:
        if abs(x)>dwmax:
            x=x/abs(x)*dwmax
        elif abs(x)<dwmin:
            x=x/abs(x)*dwmin
        else:
            x=x*1.5
    return x


# 打开WAV文档
f = wave.open(r"back.wav", "rb")
fo = wave.open(r"jg.wav", "wb")
# 读取波形数据
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
print "read wav data...."
str_data = f.readframes(nframes)

#将波形数据转换为数组，并更改
print "update wav data...."
wave_data = np.fromstring(str_data, dtype=np.short)
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = f.readframes(nframes)

#放大声音
change_dwmax=wave_data.max()/100*88
change_dwmin=wave_data.max()/100*14
wave_change = np.frompyfunc(wavechange,3,1)
new_wave_data =wave_change(wave_data,change_dwmax,change_dwmin)
new_wave_data =new_wave_data.astype(wave_data.dtype)
new_str_data=new_wave_data.tostring()
#写波形数据参数
print "save new wav files...."
fo.setnchannels(nchannels)
fo.setframerate(framerate)
fo.setsampwidth(sampwidth)
fo.writeframes(new_str_data)


# 绘制波形
wave_data.shape = -1, 2
wave_data = wave_data.T
time = np.arange(0, nframes) * (1.0 / framerate)
pl.subplot(221)
pl.plot(time, wave_data[0])
pl.subplot(222)
pl.plot(time, wave_data[1], c="g")
pl.xlabel("time (seconds)")


# 绘制波形
new_wave_data.shape = -1, 2
new_wave_data =new_wave_data.T
new_time = np.arange(0, nframes) * (1.0 / framerate)
pl.subplot(223)
pl.plot(new_time,new_wave_data[0])
pl.subplot(224)
pl.plot(new_time, new_wave_data[1], c="g")
pl.xlabel("time (seconds)")
pl.show()