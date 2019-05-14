import threading
import time
class htmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success")
        self.sem.release() # 内部维护的计数器加1，并通知内部维护的conditon通知acquire

class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire() # 内部维护的计数器减1，到0就会阻塞
            html_thread = htmlSpider("http://baidu.com/{}".format(i), self.sem)
            html_thread.start()

if __name__ == "__main__":
    sem = threading.Semaphore(3) #设置同时最多3个
    url_producer = UrlProducer(sem)
    url_producer.start()
