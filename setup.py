from setuptools import setup, Command
import os, shutil, subprocess, glob

class GeosphereClean(Command):
    user_options = []
    def initialize_options(self):
        pass 
    def finalize_options(self):
        pass
    def run(self):
        for dir in ['build', 'dist', 'geosphere.egg-info', '__pycache__']:
            shutil.rmtree(dir, ignore_errors=True)
        for file in glob.glob('*.pyc'):
            if os.path.exists(file):
                os.remove(file)
        for file in os.listdir('doc'):
            if os.path.splitext(file)[-1] != '.tex':
                os.unlink(os.path.join('doc', file))

class GeosphereBuildDocs(Command):
    user_options = []
    def initialize_options(self):
        pass 
    def finalize_options(self):
        pass
    def run(self):
        os.chdir('doc')
        subprocess.call(['pdflatex', 'geosphere'])
        os.chdir(os.path.pardir)

setup(cmdclass={'clean': GeosphereClean,
                'build_docs': GeosphereBuildDocs})
