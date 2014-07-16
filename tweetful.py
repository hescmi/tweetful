import json
import argparse
from urls import *
import authorization
import requests

def main():
    """ Main function """
    auth = authorization.authorize()

    parser = argparse.ArgumentParser()
    parser.add_argument("resource", type=str, help="specific resource to be queried (Timeline, Messages, Friends, Followers)")
    parser.add_argument("user", type=str, help="user to be queried about", nargs='?')
    args = vars(parser.parse_args())

    if args["resource"]=="Timeline":
        response = requests.get(TIMELINE_URL, auth=auth)
        print json.dumps((response.json()), sort_keys=True, indent=4, separators=(',',':'))
    elif args["resource"]=="Messages":
        response = requests.get(MESSAGES_URL, auth=auth)
        print json.dumps((response.json()), sort_keys=True, indent=4, separators=(',',':'))
    elif args["resource"]=="Followers":
        response = requests.get(FOLLOWERS_URL + args["user"], auth=auth)
        print json.dumps((response.json()), sort_keys=True, indent=4, separators=(',',':'))
    elif args["resource"]=="Friends":
        response = requests.get(FOLLOWERS_URL + args["user"], auth=auth)
        print json.dumps((response.json()), sort_keys=True, indent=4, separators=(',',':'))

if __name__ == "__main__":
    main()
