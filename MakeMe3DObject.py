''' Creating a new 3D printable object'''

# find libraries of objects, blend them together in 3D, look for typical printable issue (e.g. too thin)
#   add typical simple solutions to each problem
import argparse

# import numpy as np
# import matplotlib.pyplot as plt
# from stl_tools import numpy2stl

class LibraryOfMeshes(object):
    ''' Managing a library of meshes '''

    def __init__(self):
        ''' Create a new library of meshes, eventually load a saved one '''
        pass

    # load user theme or parameters as keywords
    # renamed from find_meshes_from_keywords()
    def Extend(self, list_of_keywords):
        ''' Find a mesh based on keywords then add it '''
        pass

    def GetRandom(self):
        ''' Return a random mesh from the current library '''
        pass

class PrintableNewMesh(object):
    ''' Create a new mesh that can be 3D printed '''

    def __init__(self, mesh):
        ''' Create a new mesh based on an existing one '''
        pass

    # "conify" function would provide a good basis for a lamp from a 3D object
    #   simply by rotating a long flat object around an 2 axis and keeping a central point at the end
    # "tabletify" function would provide a good basis for a tablet or phone holder from a 3D object
    #   simply by substracting a rectangle from the approximate size (usually given in inches) to the top of it
    # function to transform a mesh to provide affordances (e.g. wearable on wrist, holding a tablet, etc)
    def ProvideAffordance(self, affordance):
        ''' Insure that a mesh has a shape that provide a useful function to its user '''
        if affordance == "hold_a_lightbulb":
            pass
        pass

    def IsNot3DPrintable(self):
        ''' Find problems related to 3D printing '''
        pass

    def FixPrintabilityIssues(self):
        ''' Fix problems related to 3D printing '''
        pass

    # can be blended along
        # center of each object (merging)
        # border of each object (chaining)
        # a solid axis (holding stick)
        # helix
        # other supporting structures
    def BlendWithOtherMeshes(self, list_of_meshes):
        ''' Blend multiple meshes with the current one '''
        pass

    def RenderPreview(self):
        ''' Render as images a mesh '''
        pass

    def ExportSTL(self, filename):
        ''' Export the current mesh to the STL format '''
        pass

# generate a bunch of models with 3D preview
#remember own experience with the ouroboros orb

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Module to create a new 3D-printable object.")
    parser.add_argument("-v", "--verbose", action="store_true", default=False,
                        help="Verbose, display plenty of debugging and testing information")
    parser.add_argument("-t", "--theme", default="cube",
                        help="Theme to be used as inspiration")
    parser.add_argument("-a", "--affordance", default="hold_a_lightbulb",
                        help="Affordance to use for the object, what can it must be able to do. For the moment only hold_a_lightbulb is available.")
    parser.add_argument("-f", "--filename", default="NewObject",
                        help="Filename of the exported 3D printable file both in preview image and STL for printing.")

    args = parser.parse_args()

    if args.verbose:
        print("Verbose mode")

    MyLibrary = LibraryOfMeshes()
    MyLibrary.Extend(args.theme)
    MyMesh = PrintableNewMesh(MyLibrary.GetRandom)
    MyMesh.BlendWithOtherMeshes(MyLibrary.GetRandom)
    MyMesh.ProvideAffordance(args.affordance)
    while MyMesh.IsNot3DPrintable():
        MyMesh.FixPrintabilityIssues()
    MyMesh.RenderPreview()
    MyMesh.ExportSTL(args.filename)
