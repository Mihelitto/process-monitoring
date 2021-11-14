import subprocess
import time
import argparse
import psutil


def main():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument(
        'program',
        type=str,
        help='path to the program',
    )
    args_parser.add_argument(
        '-i', '--interval',
        type=float,
        help='statistics collection interval',
        default=0.5,
    )

    args = args_parser.parse_args()
    interval = args.interval
    program = args.program.split()

    proc = subprocess.Popen(program)
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
        time.sleep(interval)


if __name__ == '__main__':
    main()
