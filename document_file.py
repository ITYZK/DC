import os
import queue

same_count = 0        #统计相似文件的数量
count = 0            #统计所有的文件数

class Doct():
    """对两个文件夹的操作"""
    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2
        self.Q = queue.Queue()  # 存储相同文件名的路径

    def check_file(self):
        """检查两个文件夹相同的文件，以文件名是否相同判断"""
        global same_count, count
        same_count = 0
        count = 0
        dir1 = {}
        for root, _, files in os.walk(self.path1):
            for file in files:
                dir1[file] = root
        count = len(dir1)
        for root, _, files in os.walk(self.path2):
            for file in files:
                if dir1.get(file):
                    # 将两个相同文件的路径加到队列中
                    self.Q.put([os.path.join(dir1.get(file) + "/", file), os.path.join(root + "/", file)])
                    same_count += 1

    def get_len(self):
        """返回符合结果的数目"""
        return self.Q.qsize()

    def get_file_queue(self):
        """返回队列对象"""
        return self.Q

    def get_same_rate(self):
        if count == 0:
            return [0, 1]
        return [same_count, count]

# # test
# d = Doct(r"C:/Users/Fucker/Desktop/毕设/殷质琨/demo/test/doc1", r"C:/Users/Fucker/Desktop/毕设/殷质琨/demo/test/doc2")
# d.check_file()
# print(d.get_len())
# ln = d.get_len()
# ls = d.get_file_queue()
# for i in range(ln):
#     print(ls.get())
