#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import chardet
from docx import Document


class Filer:
    def __init__(self):
        self.data = ""

    def file_read(self, file_path):
        """加载代码类文档"""
        err = None
        self.data = []
        try:
            with open(file_path, "rb") as f:
                data = f.readlines()
            for i in data:
                self.data.append(self.check_code(i))
        except FileNotFoundError:
            err = "文件找不到，请检查文件路径！"
        except Exception as e:
            # print("code read err: %s" % e)
            err = e
        return self.data, err

    def check_code(self, text):
        """检查文件编码格式"""
        adchar = chardet.detect(text)
        if adchar['encoding'] == 'gbk' or adchar['encoding'] == 'GBK' or adchar['encoding'] == 'GB2312':
            true_text = text.decode('GB2312', "ignore")
        else:
            true_text = text.decode('utf-8', "ignore")
        return true_text

    def docx_read(self, file_path):
        """加载word类文档"""
        err = None
        try:
            f = Document(file_path)
            self.data = f.paragraphs
        except Exception as e:
            # print("docx read err: %s" % e)
            err = "文件找不到，请检查文件路径！"
        return self.data, err

    def Test_Split(self, file_path):
        """按照标点符号和空格将文本分割为列表"""
        data_dic = {}  # 创建数据索引
        data, err = self.file_read(file_path)
        # data_list = re.split(r"[|,|.|;|\?|!|，|。|；|！|\?|\s]\s*", data)
        tem_len = len(data)
        for i in range(tem_len):
            data_dic[i] = data[i]
        # print(data_dic)
        return data, data_dic, err

    def Code_Split(self, file_path):
        """分割代码类文档"""
        data_dic = {}  # 创建数据索引
        data, err = self.file_read(file_path)
        tem_len = len(data)
        for i in range(tem_len):
            data_dic[i] = data[i]
        return data, data_dic, err

    def Docx_Split(self, file_path):
        """加载word文档"""
        data_dic = {}
        k = 0
        data, err = self.docx_read(file_path)
        for temp in data:
            data_list = re.split(r"[|,|.|;|\?|!|，|。|；|！|\?|\s]\s*", temp.text)
            for i in data_list:
                data_dic[k] = i
                k += 1
        return [i.text for i in data], data_dic, err

#text
# path = r"C:\Users\Fucker\Desktop\Learning\面向对象c++\文件读写.cpp"
# path = "read_file.py"
# # # path = "./test/doc1/test_1.txt"
# f = Filer()
# data, data2, err = f.Code_Split(path)
# print(data2)
# data, _, _ = f.Docx_Split(path)
# print(data[0])
