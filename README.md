Vllm 
searxng 
openwebui 
telegram-bot

Edit file **./searxng/config/settings.yml**
```
  # remove format to deny access, use lower case.
  # formats: [html, csv, json, rss]
  formats:
    - html
```
to
```
  # remove format to deny access, use lower case.
  # formats: [html, csv, json, rss]
  formats:
    - html
    - json
```

Rename .env_Configure_and_Rename to .env

and edit .env and add key
```
TG_TOKEN=
HF_TOKEN=
```

And start
```
docker-compose up -d --build
```
