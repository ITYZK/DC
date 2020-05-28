#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 该文件是对GUI界面功能的实现

import os, re
import do_SimHash as ds
import read_file as rf
import document_file as df
from PyQt5 import QtWidgets


simhash_index = None  #simhash索引
same_count = 0        #统计相似的数量
count = 0            #统计总的字符串数，不包含空白行


def choose_file(path_obj):
    """选择文件并显示在路径栏里"""
    try:
        # 设置弹窗
        messageBox = QtWidgets.QMessageBox()
        messageBox.setWindowTitle('文件目录选择')
        messageBox.setText('选择打开文件或文件夹')
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
        buttonY = messageBox.button(QtWidgets.QMessageBox.Yes)
        buttonY.setText("文件")
        buttonX = messageBox.button(QtWidgets.QMessageBox.Ok)
        buttonX.setText("文件夹")
        buttonN = messageBox.button(QtWidgets.QMessageBox.No)
        buttonN.setText("取消")
        messageBox.exec_()  # 关闭弹窗
        if messageBox.clickedButton() == buttonY:
            # 文件选择，返回文件路径和文件类型
            fname, _ = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QWidget(),
                                                             "文件选择",
                                                             "./",
                                                             "All Files (*)")
        elif messageBox.clickedButton() == buttonX:
            # 文件夹选择
            fname = QtWidgets.QFileDialog.getExistingDirectory(QtWidgets.QWidget(),
                                                               "文件夹选择",
                                                               "./")
        if fname:
            path_obj.clear()
            path_obj.setEditText(fname)   # 将路径显示出来
    except Exception as e:
        print(e)


def load_file(path1_obj, path2_obj, content1_obj, content2_obj, rate_obj):
    """加载文本"""
    content1_obj.clear()  # 清空文本框
    content2_obj.clear()
    # 获取当前路径框内容
    path1 = path1_obj.currentText()
    path2 = path2_obj.currentText()
    #过滤路径空格
    path1 = path1.strip()
    path2 = path2.strip()

    if path1 and path2:
        file_type = os.path.splitext(path2)[1]  # 获取文件后缀名
        if file_type:    # 单文件类型
            flag, data_dic, err = do_check_file(file_type, path2)  # 分别对不同文件类型解析
            show_mode_file(content1_obj, path1, flag)  # 显示模板文件
            show_check_file(data_dic, content2_obj, flag, err)  # 显示检测文本内容
            show_rate(rate_obj)  # 计算重复率
        if not file_type:    # 目录类型
            doc = df.Doct(path1, path2)
            doc.check_file()  # 检测目录
            show_rate(rate_obj, doc.get_same_rate())  # 计算文件重复率
            if doc.get_len() > 0:  # 判断重复的文件个数
                content1_obj.setText("<font style='color: black;font-size: 15pt;'>" + "请在下拉列表中选择文件查重。。。" + "</font><br>")
                content2_obj.setText("<font style='color: black;font-size: 15pt;'>" + "请在下拉列表中选择文件查重。。。" + "</font><br>")
                for i in range(doc.get_len()):
                    doc_path1, doc_path2 = doc.get_file_queue().get()
                    path1_obj.addItem(doc_path1)  # 添加文件目录到下拉列表中
                    content1_obj.append("<font style='color: red;font-size: 13pt;'>" + doc_path1 + "</font>")  # 显示相同文件
                    path2_obj.addItem(doc_path2)
                    content2_obj.append("<font style='color: red;font-size: 13pt;'>" + doc_path2 + "</font>")
            else:
                content1_obj.setText("<font style='color: red;font-size: 15pt;'>" + "没有重复的文件。。。" + "</font>")
    elif not path2 and path1:    # 空输入检测
        content2_obj.setText("<font style='color: red;font-size: 15pt;'>" + "请选择检测文件。。。" + "</font>")
    elif path2 and not path1:
        content1_obj.setText("<font style='color: red;font-size: 15pt;'>" + "请选择模板文件。。。" + "</font>")
    else:
        content1_obj.setText("<font style='color: red;font-size: 15pt;'>" + "请选择模板文件。。。" + "</font>")
        content2_obj.setText("<font style='color: red;font-size: 15pt;'>" + "请选择检测文件。。。" + "</font>")


def do_check_file(file_type, file_path):
    """解析文本"""
    data_dic = {}
    flag = 1  # 标志文档的分词方式
    if file_type in ds.text_type:  # 解析txt
        _, data_dic, err = rf.Filer().Test_Split(file_path)
    elif file_type in ds.doc_type:  # 解析word文档
        data, _, err = rf.Filer().Docx_Split(file_path)
        for i in range(len(data)):
            data_dic[i] = data[i]
        flag = 2
    elif file_type in ds.code_type:  # 解析代码类
        flag = 3
        _, data_dic, err = rf.Filer().Code_Split(file_path)
    else:
        err = r"文件类型不支持。。。"
    return flag, data_dic, err


def show_mode_file(contant_obj1, path, flag):
    """显示模板文件内容"""
    global simhash_index
    contant_obj1.clear()
    index, data, err = ds.get_simHash(path)  # 计算simhash
    simhash_index = index
    row = 0
    if not err:
        # 显示模板文件内容
        if flag != 2:
            for d in data:
                row += 1
                contant_obj1.append("<pre>{}&nbsp;&nbsp; ".format(row) + d.replace("<", "&lt;").replace(" ", "&nbsp;") + "</pre>")
        else:
            for d in data:
                row += 1
                contant_obj1.append("<font>{}&nbsp;&nbsp;".format(row) + d.replace("<", "&lt;").replace(" ", "&nbsp;") + "</font><br>")
    else:
        # 显示错误提示
        contant_obj1.setText("<font style='color: red;font-size: 15pt;'>" + err + "</font>")


def show_check_file(data_dic, content_obj2, flag, err):
    """显示检测文本内容"""
    global same_count, count
    same_count = 0
    count = 0
    row = 0
    if err:
        content_obj2.setText("<font style='color: red;font-size: 15pt;'>" + err + "</font>")  # 显示错误提示
    else:
        for v in data_dic.values():
            if not v.strip():      # 遇到空行
                row += 1
                content_obj2.append(str(row)  + v)
                continue
            if flag != 2:
                if flag == 1:    # 文档类的解析
                    result = ds.get_sameStr(simhash_index, v)
                elif flag == 3:  # 代码类的解析
                    result = ds.get_sameStr_code(simhash_index, v)
                if result:
                    same_count += 1
                    row += 1
                    temp = "<pre style='background-color:#FFB5B5;'>{}&nbsp;&nbsp;".format(row) + v.replace("<", "&lt;") + "</pre>"  # 重复
                    content_obj2.append(temp)   # 显示内容
                else:
                    row += 1
                    temp = "<pre style='background-color:#66FF00;'>{}&nbsp;&nbsp;".format(row) + v.replace("<", "&lt;") + "</pre>"  # 无重复
                    content_obj2.append(temp)
                count += 1
            else:  # word类的解析
                str_list = re.split(r"[|,|.|;|\?|!|，|。|；|！|]*", v)
                # str_list = re.split(r'[\W]+', v)
                temp = "&nbsp;&nbsp;"
                for i in str_list:
                    count += 1
                    result = ds.get_sameStr(simhash_index, i)
                    if result:
                        same_count += 1
                        temp += "<font style='background-color:#FFB5B5;'>" + i + " </font>"  # 重复
                    else:
                        temp += "<font style='background-color:#66FF00;'>" + i + " </font>"  # 无重复
                row += 1
                content_obj2.append(str(row) + temp + "<br>")



def show_rate(rate_obj, rate_data=None):
    """显示重复率"""
    rate = 0
    global same_count, count
    if rate_data:
        same_count = rate_data[0]
        count = rate_data[1]
    if count <= 0:
       pass
    else:
        rate = int((same_count / count) * 100)
    # 不同分数段不同的颜色显示
    if rate <= 30:
        rate_obj.setText(r"<font style='color: rgb(15, 255, 11);font-size: 35pt'>{}%</font>".format(rate))  # 绿
    elif (rate > 30) and (rate <= 60):
        rate_obj.setText(r"<font style='color: orange;font-size: 35pt'>{}%</font>".format(rate))   # 橙
    else:
        rate_obj.setText(r"<font style='color: red;font-size: 35pt'>{}%</font>".format(rate))    # 红

