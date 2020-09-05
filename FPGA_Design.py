from SyntheSys import Algorithm, Testbench, Synthesize
from SyntheSys.Library.SW.Processing.Math import Square

@Algorithm() # Mean that this method will be HighLevelModule algorithm to be synthesized.
def MyAlgorithm(a,b,c):
     Delta = Square(b)-4*a*c
     return Delta


@MyTestbench() # Mean that this method will be HighLevelModule algorithm to be synthesized.
def MyAlgorithm(a,b,c):
     Delta = Square(b)-4*a*c
     return Delta


def main(args):

    Synthesize(MyAlgorithm, MyTestbench, OutputPath="./MyOutputDirectory", a=float,b=float,c=float)

main(sys.argv)