import scrapelib

s = scrapelib.Scraper(requests_per_minute=10)

r = s.get('http://qiita.com/advent-calendar/2014')

print (type(r))

print (r.status_code)

while True:
	r = s.get('http://qiita.com/advent-calendar/2014')
	print (r.status_code)