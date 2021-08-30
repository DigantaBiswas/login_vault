import re

from bs4 import BeautifulSoup
import requests

# def text_formatter(text):
#     if text.startswith("\n"):
#         text = text.replace("\n", "")
#     if text.startswith(" "):
#         text.replace()
#     return text
from blog.models import Tag, Post


def get_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def scrape_data():
    count = 0
    for page_num in range(1):
        soup = get_page("http://staffslogin.com/?page={}".format(page_num))
        div_body = soup.find("div", class_="body")
        parents = div_body.findAll("li")

        for parent in parents:
            a_child = parent.find("a")

            # parent tag is the name of the tag we will create later
            parent_tag = a_child.find("div").text.strip()

            tag = Tag.objects.filter(name=parent_tag).last()
            if not tag:
                tag = Tag.objects.create(name=parent_tag)

            child_url = a_child["href"]

            # scrape nested iteams
            child_soup = get_page(child_url)
            all_cards = child_soup.findAll("div", class_="card")
            for card in all_cards:
                image_url = card.find("img")["src"]
                h3_result = card.find("h3", class_="results")
                title = h3_result.text.strip()
                login_url = h3_result.find("a")["href"]

                # details_div = soup.find('div', attrs={"style": "font-size: 13px;color:#00000085;"})
                details = h3_result.findNext("div").text.strip()

                new_post = Post()
                new_post.title = title
                new_post.image_url = image_url
                new_post.login_url = login_url
                new_post.detail = details
                new_post.save()
                new_post.tag.add(tag)

                print("parent:{}".format(parent_tag))
                print("Child-image:{}".format(image_url))
                print("Child-login:{}".format(login_url))
                print("Child-title:{}".format(title))
                print("Child-detail:{}".format(details))
                print("\n")
                print("\n")

                count += 1

                if count % 200 == 0:
                    print("total items copied {}".format(count))
    print("Finished Copy. Total Copied : {}".format(count))
