from TikTokApi import TikTokApi
api = TikTokApi.get_instance(custom_verifyFp="")
# If playwright doesn't work for you try to use selenium
# api = TikTokApi.get_instance(use_selenium=True)
from rich.console import Console
from random import randint
import secrets
import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# from spotipy.oauth2 import SpotifyImplicitGrant
import requests

console = Console()
username = ''
while username == '':
    try:
        username = input('Enter your username:\n')
        user_id = api.getUser(username)['userInfo']['user']['id']
    except:
        username = ''
        console.log("Username not found...Please try again.")

playlist = set()
loop = 0
while len(playlist) < 14 and loop < 1:
    # with console.status("[bold green]Gathering songs from trending...",'dots') as status:
        # trending = api.trending(count=5-len(playlist), custom_verifyFp="verify_kk0jgayg_3lgunWm5_sK7O_4Yf6_8sgx_dgzrQZwWQQnr")
    with console.status("[bold green]Gathering songs from you and similar users...",'dots') as status:
        songs = api.getSuggestedMusicIDCrawler(count=14-len(playlist), startingId=user_id, custom_verifyFp="")
    with console.status("[bold green]Gathering songs from TikTok Discover...",'dots') as status:
        discover = api.discoverMusic()
    liked_priv = input('Are your likes private?(y/n)\n').lower()
    if liked_priv == 'n':
        with console.status("[bold green]Gathering songs from your liked videos...",'dots') as status:
            tiktoks = api.userLikedbyUsername(username,count=14-len(playlist))
    with console.status("[bold green]Gathering songs from your posted videos...",'dots') as status:
        posted = api.byUsername(username,count=50)

    with console.status("[bold green]Randomizing and removing extraneous songs...",'dots') as status:
        for i in range(5):
            if len(songs) > 2:
                songs.pop(randint(0,len(songs)-1))
            # trending.pop(randint(0,len(trending)-1))
            # if len(tiktoks) > 5:
                # tiktoks.pop(randint(0,len(tiktoks)-1))
            filtered_list = []
            for tiktok in posted:
                if tiktok['music']['original'] == False:
                    filtered_list.append(tiktok)
            if len(filtered_list) > 10:
                for i in range(4):
                    filtered_list.pop(randint(0,len(filtered_list)-1))

        printed = []
        for song in songs:
            playlist.add(song['title']+" "+song['description'])
            if song['title']+" "+song['description'] not in printed:
                printed.append(song['title']+" "+song['description'])
                console.log("{} by {}".format(song['title'],song['description']))
        # for tiktok in trending:
            # if tiktok['music']['original'] == False:
                # console.log("{} by {}".format(tiktok['music']['title'],tiktok['music']['authorName']))
                # playlist.add(tiktok['music']['title']+tiktok['music']['authorName'])
        for song in discover:
            playlist.add(song['cardItem']['title']+" "+song['cardItem']['description'])
            if song['cardItem']['title']+" "+song['cardItem']['description'] not in printed:
                printed.append(song['cardItem']['title']+" "+song['cardItem']['description'])
                console.log("{} by {}".format(song['cardItem']['title'],song['cardItem']['description']))
        if liked_priv == 'n':
            for tiktok in tiktoks:
                if tiktok['music']['original'] == False:
                    playlist.add(tiktok['music']['title']+" "+tiktok['music']['authorName'])
                    if tiktok['music']['title']+" "+tiktok['music']['authorName'] not in printed:
                        printed.append(tiktok['music']['title']+" "+tiktok['music']['authorName'])
                        console.log("{} by {}".format(tiktok['music']['title'],tiktok['music']['authorName']))
        for tiktok in filtered_list:
            playlist.add(tiktok['music']['title']+" "+tiktok['music']['authorName'])
            if tiktok['music']['title']+" "+tiktok['music']['authorName'] not in printed:
                printed.append(tiktok['music']['title']+" "+tiktok['music']['authorName'])
                console.log("{} by {}".format(tiktok['music']['title'],tiktok['music']['authorName']))
    loop+=1

print("\nCome try again tomorrow or in a couple of days if your results look too similar.")
print("It's because tiktok's trends haven't shifted yet and neither has your discovery.\n")

cont = input("Do you want to continue?(y/n)\n").lower()
while cont != 'y' and cont != 'n':
    print("Incorrect response. Try again.")
    cont = input("Do you want to continue?(y/n)\n")

if cont == 'y':
    # sp = spotipy.Spotify(spotipy.SpotifyOAuth(secrets.YOUR_APP_CLIENT_ID,
    #                                            secrets.YOUR_APP_CLIENT_SECRET,
    #                                            secrets.YOUR_APP_REDIRECT_URI,
    #                                            "playlist-modify-public"))

    # sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(secrets.YOUR_APP_CLIENT_ID,
    #                                             secrets.YOUR_APP_CLIENT_SECRET))

    sp = spotipy.Spotify(auth_manager=SpotifyImplicitGrant())

    # new_playlist = input("Do you want to make a new playlist(y) or add to an old one?(n)")
    # while new_playlist != 'y' and new_playlist == 'n':
    #     print("Not a valid answer, try again.")
    #     new_playlist = input("Do you want to make a new playlist(y) or add to an old one?(n)")

    # spot_name = ''
    # while spot_name == '':
    #     name_test = input("Enter your spotify username:")
    #     try:
    #         spot_name = sp.user(name_test)['display_name']
    #     except:
    #         console.log('Invalid username, try again.')

    # if new_playlist == 'y':
    #     playlist_name = input("Name your new playlist:")
    #     sp.user_playlist_create(spot_name,playlist_name,"(Auto-generated playlist by TikTokToSpotify)")
    #     spot_playlist = sp.user_playlist(spot_name['display_name'], playlist_name)
    # else:
    #     playlist_name = input("Name the playlist that you want to add to:")
    #     spot_playlist = None
    #     while spot_playlist == None:
    #         try:
    #             spot_playlist = sp.user_playlist(spot_name, playlist_name)
    #         except:
    #             print('Invalid playlist name, try again.')
    #             playlist_name = input("Name the playlist that you want to add to:")

    # for song in playlist:
    #     results = sp.search(q=song, limit=1)
    #     for idx, track in enumerate(results['tracks']['items']):
    #         console.log('[bold green]Song found! '+track['name'])
    #     # sp.user_playlist_add_tracks(spot_name,spot_playlist)
    
