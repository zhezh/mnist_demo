from __future__ import print_function
import argparse
import os
import pathlib
import subprocess
import logging


def main():
    # Training settings
    parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
    parser.add_argument('--data-path', type=str, default='.',
                        help='')
    parser.add_argument('--out-path', type=str, default='.',
                        help='')
    args = parser.parse_args()

    runlog_path = pathlib.Path(args.out_path) / 'run_log.txt'
    fh = logging.FileHandler(runlog_path)
    logging.basicConfig(level=logging.DEBUG, filename=runlog_path)
    logger = logging.getLogger(__name__)

    out_path = pathlib.Path(args.out_path)
    if not out_path.exists():
        os.makedirs(out_path)
    logf = open(args.out_path + '/app_log.txt', 'w')

    subprocess.Popen('nvidia-smi'.format(args.data_path), shell=True, stdout=logf)
    subprocess.Popen('df', shell=True)
    logger.info(args.data_path)
    logger.info(args.out_path)
    p = subprocess.Popen(
        "python main.py --save-model --data-path {} --out-path {} --epochs 2".format(args.data_path, args.out_path),
        shell=True, stdout=logf, stderr=logf, env=my_env)
    p.wait()
    # os.system("python main.py --save-model --data-path {} --out-path {} --epochs 2".format(args.data_path, args.out_path))


if __name__ == '__main__':
    my_env = os.environ.copy()
    main()
