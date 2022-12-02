# Prerequisites
Make a `config.json` file in the same directory as the `main.py` file with a client id and client secret which you can get from a Spotify application: https://developer.spotify.com/dashboard/applications. You should also provide your user id, which can be found by going to your Spotify profile, right clicking your name and choosing "Copy link to profile". If you paste this link, it will look something like `https://open.spotify.com/user/your_id?si=123456789` where `your_id` is your user id, which you need to put in the `config.json`.

```json
{
    "client_id": "replace_me",
    "client_secret": "replace_me",
    "user_id": "replace_me"
}
```

# Run program
In the terminal: 
`python3 main.py`
