import subprocess


def execute_command(cmd, pathget='C:'):
    # log("Executing command : {}".format(cmd))
    return subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True,
                            cwd=pathget).communicate()


def execute_command_output_file(cmd, file_fp, pathget='C:'):
    # log("Executing command : {}".format(cmd))
    # log("Output file path : {}".format(file_fp))
    return subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=file_fp, shell=True,
                            cwd=pathget).communicate()


def execute_and_return_output(cmd, pathget='C:'):
    lines = []
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True,
                            cwd=pathget)
    while True:
        line = proc.stdout.readline().decode('utf-8')
        if not line:
            break
        lines.append(line)
    return lines
