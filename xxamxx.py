from pydub import AudioSegment
import argparse
import loguru
from sys import stdout

parser = argparse.ArgumentParser(description="enshittify audio")
parser.add_argument("input", help="input audio file")
parser.add_argument("output", help="output audio file location")
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
try:
    logger.info(f"processing file '{args.input}', this might take a min..")
    inp = AudioSegment.from_file(args.input)
    p1 = inp.set_frame_rate(6900)
    p2 = p1.set_sample_width(1)
    p2 = p2.set_channels(1)
    p3 = p2.apply_gain(4)
    p3.export(args.output)
    logger.critical(f"exported to '{args.output}'!")
except Exception as e:
    logger.error("error enshittifying audio: "+str(e))