import requests
import hashlib
import sys
def request_api_data(query):
	url = "https://api.pwnedpasswords.com/range/"+ query #hello123
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError (f"Error fetching {res.status_code}, check the api and try again!")
	return res
# def read_response(response):
# 	print(response.text)	
def pass_leaks_count(hashes, hashes_to_check):
	hashes = (line.split(":") for line in hashes.text.splitlines())
	for h,count in hashes :
		if h == hashes_to_check:
			return count

	return 0


def pwned_api_check(password):
	# print(hashlib.sha1(password.encode("utf-8")).hexdigest().upper())	
	sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
	first5_ , tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_)
	# return sha1password
	# print(response)
	return pass_leaks_count(response,tail)

def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f"{password} was found {count} times...  ")
		else:
			print("password doesn't found")
	return "well done"
	


if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))



# request_api_data("12567")
# pwned_api_check("urvishjat")
