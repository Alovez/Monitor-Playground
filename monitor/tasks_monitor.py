# Copyright (c) 2018 App Annie Inc. All rights reserved.
import psutil
import csv
import os

all_python_process = [psutil.Process(p) for p in psutil.pids() if 'python' in psutil.Process(p).exe()]

p_info = []

for p in all_python_process:
    p_dict = dict()
    p_dict['parent'] = p.parent()
    p_dict['cpu'] = p.cpu_percent()
    p_dict['mem'] = p.memory_percent()
    p_dict['create'] = p.create_time()
    p_dict['pid'] = p.pid
    p_info.append(p_dict)
header_flag = os.path.exists('task_monitor_log.csv')

with open('task_monitor_log.csv', 'a' if header_flag else 'w') as f:
    fieldnames = ['pid', 'parent', 'create', 'cpu', 'mem']
    writer = csv.DictWriter(f, fieldnames)
    if header_flag:
        writer.writeheader()
    for p in p_info:
        writer.wri

