# Overview: The goal of this file include a simple python funtion 
# that can be tested for CI/CD in both Github Actions and Cloud Build
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--username', type=str, default='Unknown')



def greeting(name: str)->str:
    return 'Hello ' + name



if __name__ == "__main__":
    args = parser.parse_args()
    dict_args = vars(args)
    str_username = dict_args['username']
    g = greeting(str_username)
    print(g)
