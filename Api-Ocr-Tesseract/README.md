# Api-Ocr-Tesseract

# Process Execution

## Local

#### Environment

    conda create -n ocr python=3.7
    source activate ocr
    pip install -r requirements.txt

#### Run

     python main.py --port 9191 --version v1.0.0

# Docker

#### Build

    sudo docker build . -t api-ocr

#### Run

    sudo docker run -it -p 9191:9191 -e VERSION="v1.0.0" -e PORT=9191 api-ocr