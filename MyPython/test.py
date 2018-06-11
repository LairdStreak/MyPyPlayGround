"""This module does blah blah."""
import httplib2
resp, content = httplib2.Http().request("http://myip.dk")
#start = content.find("ipv4address")
#end = start + 100

print (content) #[start:end].strip())