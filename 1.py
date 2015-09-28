#!/usr/bin/python
import sys
import pbl
import spotipy
import spotipy.util as util

scope = 'user-library-read'

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print "Usage: %s username" % (sys.argv[0],)
        sys.exit()

    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        main()
    else:
        print "Can't get token for", username


def main():
    playlists = sp.user_playlists(username);
    for playlist in playlists:
        print(playlist['name'])