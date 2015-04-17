# find libraries of objects, blend them together in 3D, look for typical printable issue (e.g. too thin)
#   add typical simple solutions to each problem
import sys
import argparse

# import numpy as np
# import matplotlib.pyplot as plt
# from stl_tools import numpy2stl

class library_of_meshes(object):

    def __init__(self):
        pass

    # load user theme or parameters as keywords
    # renamed from find_meshes_from_keywords()
    def extend(self, list_of_keywords):
        pass

    def get_random(self):
        pass

class printable_new_mesh(object):

    def __init__(self, mesh):
        pass

    # "conify" function would provide a good basis for a lamp from a 3D object
    #   simply by rotating a long flat object around an 2 axis and keeping a central point at the end
    # "tabletify" function would provide a good basis for a tablet or phone holder from a 3D object
    #   simply by substracting a rectangle from the approximate size (usually given in inches) to the top of it
    # function to transform a mesh to provide affordances (e.g. wearable on wrist, holding a tablet, etc)
    def provide_affordance(self, affordance):
        pass

    def is_not_3Dprintable(self):
        pass 

    def fix_printability_issues(self):
        pass

    def blend_with_other_meshes(self, list_of_meshes):
        pass

    def render_preview(self):
        pass

    def export_STL(self, filename):
        pass

# generate a bunch of models with 3D preview
#remember own experience with the ouroboros orb

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Module to create a new 3D-printable object.")
    parser.add_argument("-v", "--verbose", action="store_true", default = False, 
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

    MyLibrary = library_of_meshes()
    MyLibrary.extend(args.theme)
    MyMesh = printable_new_mesh(MyLibrary.get_random)
    MyMesh.blend_with_other_meshes(MyLibrary.get_random)
    MyMesh.provide_affordance(args.affordance)
    while MyMesh.is_not_3Dprintable():
        MyMesh.fix_printability_issues()
    MyMesh.render_preview()
    MyMesh.export_STL(args.filename)
