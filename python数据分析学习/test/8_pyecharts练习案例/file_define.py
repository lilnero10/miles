"""
和文件相关的类定义
"""
import json

from data_define import Records
#先定义一个抽象类用来做顶层设计，用来确认有哪些功能可以实现
class FileReader():
    """读取文件数据，读到的每条数据转换为Records对象"""
    def read_data(self) -> list[Records]:
        pass

class TextFileReader(FileReader):

    def __init__(self,path):
        self.path = path


    def read_data(self) ->list[Records]:
        f = open(self.path, 'r',encoding='utf-8')

        record_list :list[Records] = []
        for i in f.readlines():
            i = i.strip()
            data_list = i.split(",")
            record = Records(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)

            f.close()
            return record_list


class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Records]:
        f = open(self.path, 'r', encoding='utf-8')

        record_list: list[Records] = []
        for i in f.readlines():
            data_dict = json.loads(i)
            Record = Records(data_dict['date'],data_dict['order_id'],int(data_dict['money']))
            record_list.append(Record)

            f.close()
            return record_list



