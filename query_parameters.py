from requests.models import PreparedRequest
req = PreparedRequest()

url = "http://www.neo4j.com"
params = {'ref':"mark-blog"}
req.prepare_url(url, params)

req.url

# We can also use this approach to add parameters to URLs that already have existing ones. 
# For example, we could update this YouTube URL:

url = "https://www.youtube.com/watch?v=Y-Wqna-hC2Y&list=RDhlznpxNGFGQ&index=2"
params = {'ref':"mark-blog"}
req.prepare_url(url, params)

req.url
