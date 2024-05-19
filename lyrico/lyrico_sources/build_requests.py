
from __future__ import print_function
from __future__ import unicode_literals

import copy
import random


user_agents = [
	'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
]

request_headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
	'DNT': '1',
}

# randint inculdes both upper and lower bounds

def get_lyrico_headers(site_name=None):

	# Since each module requesting from different souce uses the same
	# request headers for a lyrico operation, make deep copies of base headers
	# before giving it to modules.

	headers_copy = copy.deepcopy(request_headers)
	headers_copy['User-Agent'] = user_agents[random.randint(0, (len(user_agents) - 1))]
	return headers_copy

def test_req_dic():
	print(request_headers)
