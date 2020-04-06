# wordcloud-api
Wordcloud python api

### Endpoints

```
POST /api/wordcloud

Input:
{
    "words": [
        {
            "word": "string",
            "count": int,
        },
        ...
    ]
}

Output:
{
    "filename": "path..."
}
```

```
GET /api/file/{filename}
```
