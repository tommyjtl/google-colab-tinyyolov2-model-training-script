import os

os.system("git submodule update --init")
os.system("cd ./tools/darknet-colab/ && make && cd ../../")
os.system("cd ./tools/darkflow-colab/ && python3 setup.py build_ext --inplace && cd ../../")