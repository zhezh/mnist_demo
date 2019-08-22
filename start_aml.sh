set -x
DATA_DIR=$PWD
LOG_DIR=$PWD/log
MODEL_DIR=$PWD/output

# parsing command line arguments:
while [[ $# > 0 ]]
do
key="$1"

case $key in
    -h|--help)
    echo "Usage: toolkit-execute [run_options]"
    echo "Options:"
    echo "  -d|--dataDir <path> - directory path to input files (default NONE)"
    echo "  -l|--logDir <path> - directory path to save the log files (default \$PWD)"
    echo "  -m|--modelDir <path> - directory path to save the model files (default NONE)"
    exit 1
    ;;
    -d|--dataDir)
    DATA_DIR="$2"
    shift # pass argument
    ;;
    -l|--logDir)
    LOG_DIR="$2"
    shift # pass argument
    ;;
    -m|--modelDir)
    MODEL_DIR="$2"
    shift # pass argument
    ;;
    *)
    EXTRA_ARGS="$EXTRA_ARGS $1"
    ;;
esac
shift # past argument or value
done

git clone https://github.com/zhezh/mnist_demo.git
cd mnist_demo
python main.py --save-model --data-path $DATA_DIR --out-path $MODEL_DIR

