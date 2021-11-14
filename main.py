import subprocess
import time
import psutil


def main():
    proc = subprocess.Popen(['python', 'test_process.py'])
    python_process = psutil.Process(proc.pid)
    while psutil.pid_exists(proc.pid):
        cpu_load = python_process.cpu_percent()
        working_set = python_process.memory_info().rss
        private_bytes = python_process.memory_info().private
        file_handles = len(python_process.open_files())
        print('CPU load: ', cpu_load)
        print('Working set memory: ', working_set)
        print('Private memory: ', private_bytes)
        print('Open handles: ', file_handles)
        time.sleep(0.1)


if __name__ == '__main__':
    main()
