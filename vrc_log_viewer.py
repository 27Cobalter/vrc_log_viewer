import glob
import os
import re
import sys
import time
import yaml


def tail(thefile, past):
    if not past:
        thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.5)
            continue
        line = line.rstrip("\n").rstrip("\r")
        if line != "":
            yield repr(line)[1:-1]


if __name__ == "__main__":
    with open("config.yml", "r") as config:
        conf = yaml.load(config, Loader=yaml.SafeLoader)
    print("load config")
    reg = []
    for pattern in conf["reg"]:
        print("  " + pattern)
        reg.append(re.compile(pattern))

    vrcdir = os.environ["USERPROFILE"] + "\\AppData\\LocalLow\\VRChat\\VRChat\\"
    logfile = vrcdir + conf["logfile"]
    if len(sys.argv) > 1:
        logfile = sys.argv[1]
    if logfile == vrcdir:
        logfiles = glob.glob(vrcdir + "output_log_*.txt")
        logfiles.sort(key=os.path.getctime, reverse=True)
        logfile = logfiles[0]

    with open(logfile, "r", encoding="utf-8") as f:
        print("open logfile : ", logfile)
        loglines = tail(f, conf["past"])

        for line in loglines:
            for pattern in reg:
                match = pattern.match(line)
                if not match:
                    continue
                message = ""
                for group in match.groups():
                    message = message + group + " "
                print(message)
