from helpers import download
import re
import urlparse
import robotparser

rp=robotparser.RobotFileParser()
rp.set_url('http://example.webscraping.com/robots.txt')
rp.read()


def crawl_sitemap(url):
	sitemap=download(url)
	links=re.findall('<loc>(.*?)</loc>',sitemap)
	for link in links:
		html=download(link)

def crawl_sitemap_2(url):
	num_errors=0
	max_errors=5
	html=download(url)
	if html is None:
		num_errors+=1
		if num_errors == max_errors:
			break
	else:
		num_errors=0


def link_crawler(seed_url,link_regex,max_depth=2):
	crawl_queue=[seed_url]
	seen=set(crawl_queue)
	depth=seen[url]
	if depth != max_depth:
		while crawl_queue:
			url=crawl_queue.pop()
			if rp.can_fetch(user_agent,url):	
				pass
			else:
				print("Blocked by robotics.txt",url)
			html=download(url)
			for link in get_links(html):
				if re.match(link_regex,link):
					link=urlparse.urljoin(seed_url,link)
					if link not in seen:
						seen.add(link)
						crawl_queue.append(link)
	

def get_links(html):
	webpage_regex=re.compile('<a[^>]+href=["\'](.*?)["\"]',re.IGNORECASE)
	return webpage_regex.findall(html)
