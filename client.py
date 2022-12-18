import requests
import argparse

url = "http://localhost:8080/predict"

#init parser
parser = argparse.ArgumentParser(description='post from client image to server')
# add argument to parser
parser.add_argument('-d','--dir',type=str,default='test_images/cat2.jpg',help='directory to image')
# create arguments
args = parser.parse_args()

if __name__ == "__main__":

    file = {"file":open(args.dir,'rb')}
    res = requests.post(url,files =file)
    print(res.text)
