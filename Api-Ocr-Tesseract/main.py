import uvicorn
from v1.app import app
from settings import Settings
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Select the mode process [prod, dev]')
    parser.add_argument('--port', dest='port', default=8080, help='Mode to run')
    parser.add_argument('--debug', dest='debug', default=0, help='Mode to run')
    parser.add_argument('--version', dest='version', default="v0.0.0", help='Mode to run')
    args = parser.parse_args()

    cfg = Settings()
    cfg.set_version(args.version)

    if args.debug == 0:
        uvicorn.run(app, host="0.0.0.0", port=int(args.port))
    else:
        uvicorn.run("main:app", host="0.0.0.0", port=int(args.port), reload=True, debug=True)



