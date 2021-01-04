from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import DataConfig


class Data:
    def __init__(self, testcase_file, sheet_name):
    # 1、使用excel工具类，获取结果list
        # reader = ExcelReader("../data/data.xlsx","ims前台页面接口自动化测试")
        self.reader = ExcelReader(testcase_file, sheet_name)
        # print(reader.data())
    # 2、列是否运行内容，y

    def get_run_data(self):
        """
        根据是否运行列==y，获取执行测试用例
        :return:
        """
        run_list = list()
        for line in self.reader.data():
            if str(line[DataConfig().is_run]).lower() == "y":
                # print(line)
        # 3、保存要执行结果，放到新的列表。
                run_list.append(line)
        print(run_list)
        return run_list


# if __name__ == "__main__":
#     reader = Data("../data/data.xlsx","IMS前台接口自动化测试")
#     print(reader.get_run_data())

