import sys

try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")
color.write("Some test",color)
