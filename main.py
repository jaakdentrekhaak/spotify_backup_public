import requests
import base64
import json

def get_access_token(client_id, client_secret):
    """
    https://developer.spotify.com/documentation/general/guides/authorization/client-credentials/
    """

    authorization_string = f'{client_id}:{client_secret}'
    authorization_bytes = authorization_string.encode('ascii')
    authorization_base64_bytes = authorization_bytes
    authorization_base64_bytes = base64.b64encode(authorization_bytes)
    authorization_base64_string = authorization_base64_bytes.decode("ascii")

    body = {'grant_type': 'client_credentials'}
    headers = {
        'Authorization': f'Basic {authorization_base64_string}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    r = requests.post(
        'https://accounts.spotify.com/api/token',
        data=body,
        headers=headers
    )

    if r.status_code != 200:
        print(f'Failed with status code {r.status_code}')
        exit()

    return r.json()['access_token']


def get_playlists(access_token, user_id):
    """
    https://developer.spotify.com/documentation/web-api/reference/#/operations/get-list-users-playlists
    """
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    url = f'https://api.spotify.com/v1/users/{user_id}/playlists?offset=0&limit=50'
    next = 'dummy'

    playlists = []

    while next is not None:

        r = requests.get(
            url,
            headers=headers
        )

        if r.status_code != 200:
            print(f'Failed with status code {r.status_code}')
            exit()
        
        body = r.json()
        next = body['next']
        playlists.extend(body['items'])

    playlists = parse_playlists(playlists)
    
    return playlists


def parse_playlists(playlists):
    result = []
    for pl in playlists:
        result.append(
            {
                'description': pl['description'],
                'id': pl['id'],
                'name': pl['name'],
                'snapshot_id': pl['snapshot_id'],
                'tracks': pl['tracks']
            }
        )
    return result


if __name__ == '__main__':
    with open('config.json', 'r') as f:
        data = json.load(f)
        client_id = data['client_id']
        client_secret = data['client_secret']
        user_id = data['user_id']

    access_token = get_access_token(client_id, client_secret)
    playlists = get_playlists(access_token, user_id)
    # TODO: use track urls to get information about songs in playlist and store result in json
