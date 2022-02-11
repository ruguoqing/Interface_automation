import json
import os
import allure

import pytest
from libs.login import Login
from tools.ymalcontrol import get_yaml_data
from tools.getmd5 import get_md5


class TestLogin:

    # # 测试类级开始
    # def setup_class(self):
    #     print("------->setup_class")
    #
    # # 测试类级结束
    # def teardown_class(self):
    #     print("------->teardown_class")
    #
    # # 函数级开始
    # def setup(self):
    #     print("------->setup_method")
    #
    # # 函数级结束
    # def teardown(self):
    #     print("------->teardown_method")

    @pytest.mark.parametrize('indata, resexp', get_yaml_data("../data/logincase.yaml"))
    def test_login(self, indata, resexp):
        indata["password"] = get_md5(indata["password"])
        resq = Login().login(indata)
        resq = json.loads(resq)
        # print(indata["password"])
        assert resq["message"] == resexp["message"]


if __name__ == '__main__':
    pytest.main(['test_login.py', '-s']) # 运行该文件下所有用例，-s 打印输出

    # 运行并生成脚本文件用于生成测试报告
    # pytest.main(['test_login.py', '-s', '--alluredir', '../reports/tmp'])
    # 本地启动一个服务，并生成报告，运行完自动打开，关掉服务就看不到了
    # os.system("allure serve ../reports/tmp")
    #在本地路径下生成
    # os.system("allure generate ../reports/tmp -o ../reports/tmp/html")
