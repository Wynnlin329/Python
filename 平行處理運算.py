#==========建立程序=================
# import subprocess,time
#
# calcproc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
#
# while True:
#     print(calcproc.poll())#polling 輪詢
#     if calcproc.poll() != None:
#         print('小算盤已開啟')
#         break
#
# time.sleep(3)
#
# proc = subprocess.Popen('Taskkill/IM Calculator.exe /F')
#===========================

#=======Multiprocessing====================

import multiprocessing as mp
import  os,random,time

counter = 0

def pm(task_id,task_queue):
    task=[0,'']
    task_type = random.sample(['Level A Task','Level B Task','Level C Task','Level S Task'],k=1)
    task[0]=task_id; task[1]=task_type
    print('PM 接到了一項',task[1],'編號',task[0])
    task_queue.put(task)

def worker(worker_id,task_queue):
    global counter
    while True:
        task = list(task_queue.get())
        time.sleep(random.randrange(2))
        print('worker',worker_id,' 處理了一項',task[1],'編號',task[0],' PID=',os.getpid(),counter)
        counter = counter + 1
        task_queue.task_done()

def main():
    #任務佇列
    task_queue = mp.JoinableQueue()

    #工作程序1
    worker1 = mp.Process(target=worker,args=(1,task_queue))
    worker1.daemon =True

    # 工作程序2
    worker2 = mp.Process(target=worker, args=(2, task_queue))
    worker2.daemon = True

    #專案經理程序更新100個任務到任務佇列
    for id  in range(100):
        pm(id,task_queue)
    #task_queue.join()

    worker1.start()
    worker2.start()

    worker1.join()
    worker2.join()

if __name__ == "__main__":
    main()
#=============================================
# import threading,queue
# import  os,random,time
#
# counter = 0
#
# def pm(task_id,task_queue):
#     task=[0,'']
#     task_type = random.sample(['Level A Task','Level B Task','Level C Task','Level S Task'],k=1)
#     task[0]=task_id; task[1]=task_type
#     print('PM 接到了一項',task[1],'編號',task[0])
#     task_queue.put(task)
#
# def worker(worker_id,task_queue):
#     global counter
#     while True:
#         task = list(task_queue.get())
#         time.sleep(random.randrange(2))
#         print('worker',worker_id,' 處理了一項',task[1],'編號',task[0],' PID=',os.getpid(),counter)
#         counter = counter + 1
#         task_queue.task_done()
#
# def main():
#     #任務佇列
#     task_queue = queue.Queue()
#     #工作執行緒1
#     worker1 = threading.Thread(target=worker, args=(1,task_queue))
#     #worker1.start()
#
#     #工作執行緒2
#     worker2 = threading.Thread(target=worker, args=(2,task_queue))
#     #worker2.start()
#
#     #專案經理程序更新100個任務到任務佇列
#     for id  in range(100):
#         pm(id,task_queue)
#     #task_queue.join() #等待PM已經交付完畢
#
#     worker1.start()
#     worker2.start()
#
#     worker1.join()
#     worker2.join()
#
# if __name__ == "__main__":
#    main()













