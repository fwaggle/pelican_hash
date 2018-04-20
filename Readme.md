# Hash

A collection of common hash filters for hashing strings in Jinja templates under Pelican.

Absolutely nothing to this, simply pipe anything through the filter, for example:

```
{{ article.url | sha256 }}
```

Simple Gravatar implementation (there's probably better ways to accomplish this):

```
{{ "MyEmailAddress@example.com" | lower | md5 }}
```

So far only SHA-256 and MD5 are supported (with MD5 depending on your hashlib supporting it).
Adding more should be fairly trivial.
