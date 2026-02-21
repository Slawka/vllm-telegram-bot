Edit file
./searxng/config/settings.yml
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
