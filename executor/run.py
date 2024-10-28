import subprocess


def execute_commands(command_list):
    for command in command_list:
        try:
            # 使用Popen执行命令，并捕获标准输出和标准错误
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # 等待命令执行完成，并获取输出
            stdout, stderr = process.communicate()

            # 检查命令执行是否成功（返回码为0）
            if process.returncode != 0:
                print(f"命令执行错误：{stderr.decode()}")
                process.kill()  # 命令执行错误时杀死进程
            else:
                print(f"命令执行输出：\n{stdout.decode()}")

        except Exception as e:
            print(f"执行命令时发生异常：{str(e)}")
            if process.poll() is None:  # 如果进程仍在运行，则杀死它
                process.kill()


# 定义要执行的命令列表
command_list = [
    "/home/whut/anaconda3/envs/codegen25/bin/python /home/whut/chx/llm/codegen25/main.py --languages python --type pass1",
    "/home/whut/anaconda3/envs/codegen25/bin/python /home/whut/chx/llm/codegen25/main.py --languages javascript --type pass1",
    "/home/whut/anaconda3/envs/codegen25/bin/python /home/whut/chx/llm/codegen25/main.py --languages typescript --type pass1",
    "/home/whut/anaconda3/envs/codegen25/bin/python /home/whut/chx/llm/codegen25/main.py --languages 'c&cpp' --type pass1",
    "/home/whut/anaconda3/envs/codegen25/bin/python /home/whut/chx/llm/codegen25/main.py --languages java --type pass1",
]

# 执行命令列表
execute_commands(command_list)
