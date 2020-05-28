#!/usr/bin/python3
# -*- coding: utf-8 -*-

import jieba
import os
import re
from simhash import Simhash, SimhashIndex
import read_file as rf

text_type = [".txt"]
doc_type = [".docx"]
code_type = [".c", ".h", ".java", ".py", ".html", ".css", ".js", ".cpp", ".php"]


def get_simHash(file_path):
    """
    功能：对语句进行分词并进行Simhash计算
    返回值：返回Simhash值索引对象和错误
    """
    simhash_list = []
    data = None

    file_type = os.path.splitext(file_path)[1]  # 后缀获取
    if file_type in text_type:
        data, data_dic, err = rf.Filer().Test_Split(file_path) #对文档类进行分割
        for i, v in data_dic.items():
            words = jieba.cut(v)
            smValue = Simhash(words) #计算simhash值
            simhash_list.append((i, smValue))
    elif file_type in doc_type:
        data, data_dic, err = rf.Filer().Docx_Split(file_path)  #对word类进行分割
        for i, v in data_dic.items():
            words = jieba.cut(v)
            smValue = Simhash(words)
            simhash_list.append((i, smValue))
    elif file_type in code_type:
        data, data_dic, err = rf.Filer().Code_Split(file_path)  #对代码类进行分割
        for i, v in data_dic.items():
            words = re.split(r"[|,|.|;|\?|!|，|。|；|！|>|(|)|:|%|\s]\s*", v.strip())
            smValue = Simhash(words) 
            simhash_list.append((i, smValue))
    else:
        err = "文件类型不支持"
    return get_simHashindex(simhash_list), data, err

def get_simHashindex(hash_list):
    """
    功能：创建Simhash索引
    参数：SimHash列表
    返回值：SimHash索
    """
    return SimhashIndex(hash_list, k=5)  #创建索引


def get_sameStr(obj, s):
    """
    功能：查找与目标相似的语句，一般文件
    参数：参照文本的simhash值索引对象和目标string
    返回：与目标string相似语句的索引
    """
    return obj.get_near_dups(Simhash(jieba.cut(s)))


def get_sameStr_code(obj, s):
    """
    功能：查找与目标相似的语句，代码类的文件
    参数：参照文本的simhash值索引对象和目标string
    返回：与目标string相似语句的索引
    """
    return obj.get_near_dups(Simhash(re.split(r"[|,|.|;|\?|!|，|。|；|！|>|(|)|:|%|-|\s]\s*", s.strip())))


#test
# File_path = "./test/test1.docx"
# index, data_list, err = get_simHash(File_path)
#
# l = get_sameStr(index, "生成器是创建迭代器的简单而强大的工具")
# for i in l:
#     print(data_list[int(i)])

