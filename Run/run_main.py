#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import sys, os
from Util.handle_excel import handleExcel
from Base.base_request import request

base_path = os.getcwd()
sys.path.append(base_path)

class RunMain:
    def run_case(self):
        # 获取excel行数
        rows = handleExcel.get_rows()
        print(rows)
        for row in range(rows):
            cookie = None
            header = None
            # 获取行数据
            row_data = handleExcel.get_row_value(row+2)
            # 是否执行
            is_run = row_data[2]
            if is_run == "yes":
                url = row_data[5]
                method = row_data[6]
                data = json.loads(row_data[7])
                expect_status_code = row_data[10]
                # expect_result = row_data[11]
                res = request.run_main(method, url, data)
                status_code = res['status']
                if status_code == expect_status_code:
                    print("pass")
                    handleExcel.excel_write_data(row+2, 12, json.dumps(res["status"]))
                    handleExcel.excel_write_data(row+2, 13, "pass")
                else:
                    print("fial")
                    handleExcel.excel_write_data(row + 2, 12, json.dumps(res["status"]))
                    handleExcel.excel_write_data(row + 2, 13, "fail")

if __name__ == '__main__':
    run = RunMain()
    run.run_case()




