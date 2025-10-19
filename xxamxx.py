from pydub import AudioSegment
import argparse
import loguru
from sys import stdout

parser = argparse.ArgumentParser(description="enshittify audio")
parser.add_argument("input", help="input audio file")
parser.add_argument("output", help="output audio file location")
parser.add_argument("-f", "--fr", help="set multiplier of framerate (default is 1, this value can be a float)")
parser.add_argument("-g", "--grain", help="set level of grain ")
parser.add_argument("-d", "--disable_extras", help="disables extra non-listed modifiers", action='store_true')
args = parser.parse_args()
logger = loguru.logger
YELLO = "<fg #ffff00>"
YELLO_CLOSE = "</fg #ffff00>"
RED = "<fg #ff0000>"
BLU = "<fg #0000ff>"
MAGENTA = "<fg #ff00ff>"
logger.remove()
logger.add(stdout, colorize=True, format="<level>[{level}] {message}</level>")
logger.level("WARNING", color=YELLO)
logger.level("ERROR", color=RED)
logger.level("INFO", color=BLU)
logger.level("CRITICAL", color=MAGENTA)
gd = False
fd = False
try:
    logger.info(f"processing file '{args.input}', this might take a min..")
    if args.disable_extras:
        logger.info("disabled extra modifiers")
    if args.fr:
        if args.fr == "!":
            logger.info("framerate modifier disabled")
            fd = True
        else:
            logger.info("framerate changed to " + str(args.fr))
    else:
        logger.info("no framerate specified, defaulting to 1..")
        args.fr = 1
    if args.grain:
        if args.grain == "!":
            logger.info("grain disabled")
            gd = True
        else:
            logger.info("grain changed to "+str(args.grain))
    else:
        logger.info("no grain specified, defaulting to 1..")
        args.grain = 1
    inp = AudioSegment.from_file(args.input)
    p1 = inp.set_frame_rate(round(6900/float(args.fr)))
    if not args.disable_extras:
        p2 = p1.set_sample_width(1)
        p2 = p2.set_channels(1)
    else:
        p2 = p1
    if not gd:
        p3 = p2.apply_gain(round(4/float(args.grain)))
        p3.export(args.output)
    else:
        p2.export(args.output)
    logger.critical(f"exported to '{args.output}'!")
except Exception as e:
    logger.error("error enshittifying audio: "+str(e))