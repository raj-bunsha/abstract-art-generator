from cx_Freeze import setup, Executable 
import sys
#not for anything with program just built to freeze the code so that non-programmers can run
#buildOptions = dict(include_files = [(absolute_path_to_your_file,'final_filename')]) #single file, absolute path.

buildOptions = dict(include_files=['assets','examples','color_palettes.py','Basic-Regular.ttf']) #folder,relative path. Use tuple like in the single file to set a absolute path.

executables = [
    Executable('art_generator.py'),
]
setup(
         name = "abstract_art_generator",
         version = "1.0",
         description = "description",
         author = "raj",
         options = dict(build_exe = buildOptions),
         executables = executables)
