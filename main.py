import subprocess
import time
import argparse
import csv
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
    args_parser.add_argument(
        '-l', '--log',
        type=str,
        help='path to save log file',
        default='log.csv',
    )

    args = args_parser.parse_args()
    interval = args.interval
    program = args.program.split()
    log_path = args.log

    proc = subprocess.Popen(program)
    python_process = psutil.Process(proc.pid)

    with open(log_path, 'w', newline='') as log_file:
        log_writer = csv.writer(log_file, dialect='excel', delimiter=',')
        log_writer.writerow([
            'CPU load',
            'Working set memory',
            'Private memory',
            'Open handles',
        ])
        while psutil.pid_exists(proc.pid):
            cpu_load = python_process.cpu_percent()
            working_set = python_process.memory_info().rss
            private_bytes = python_process.memory_info().private
            file_handles = len(python_process.open_files())
            log_writer.writerow([
                cpu_load,
                working_set,
                private_bytes,
                file_handles,
            ])

            time.sleep(interval)


if __name__ == '__main__':
    main()
