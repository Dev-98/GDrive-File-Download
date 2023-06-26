import gdown, sys

url = sys.argv[1]

file_id = url.split('/')[-2]

prefix = "https://drive.google.com/uc?id="

gdown.download(prefix+file_id,quiet=False)