from model import train
from cctv import update

import tensorflow as tf

def main():
	model = train()
	update(model)

if __name__ == '__main__':
	main()