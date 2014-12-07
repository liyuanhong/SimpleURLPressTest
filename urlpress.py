#-*- coding: UTF-8 -*-

import os
import threading
import time

#将要进行压力测试的网址
url = 'http://www.baidu.com/'
#url = 'www.github.com'
#线程总数量，根据数量访问（mult_openurl_nums）
thread_num = 300
#并发数量
user_nums = 10
#并发压力测试时间（秒）
pr_time = 10
#设置线程之间的间隔时间（秒）
space_time = 0
#显示结束的线程数


#访问网址线程
class openurl(threading.Thread):
    def __init__(self,name,num):
        threading.Thread.__init__(self)
        self.setName(name)
        self.num = num
        self.num.append(name)

    def run(self):
        #设置请求超时时间（秒）
        cmd = 'curl -m 5 ' + url
        #没有设置请求超时时间
        #cmd = 'curl ' + url
        contents = os.popen(cmd).readlines()
        length = len(contents)
        #print contents
        if length == 0:
            print '线程：'.decode('utf-8') + self.getName() + '连接超时！！！'.decode('utf-8')
        elif length < 10:
            print '线程：'.decode('utf-8') + self.getName() + '服务器响应异常'.decode('utf-8')
        #else:
            #print str(len(contents)) + '   '
            #print contents
        self.num.pop()
        print "线程:".decode('utf-8') + self.getName() + '结束；'.decode('utf-8')
        
        
        
#并发发访问线程（根据总数量）
class mult_openurl_nums(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #定义并发数量
        self.ctr_num = 1

    def run(self):
        for i in range(0,thread_num):
            openurl(str(i),num=[]).start()
            time.sleep(space_time)
            print "线程:".decode('utf-8') + str(i) + '开始；'.decode('utf-8')
        num = 1

#并发发访问线程（根据总时间）
class mult_openurl_time(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        #定义并发数量
        self.ctr_num = []

    def run(self):
        time_start = time.time()
        time_end = time.time()
        i = 0
        while time_end - time_start < pr_time:
            time_end = time.time()
            if len(self.ctr_num) <  user_nums:
                print "线程:".decode('utf-8') + str(i) + '开始；'.decode('utf-8')
                openurl(str(i),self.ctr_num).start()
                time.sleep(space_time)               
                i = i + 1
        print 'end'
                

#启用并发发访问线程（根据总数量）          
#mult_openurl_nums().run()
#启用并发发访问线程（根据总数量）
mult_openurl_time().run()



