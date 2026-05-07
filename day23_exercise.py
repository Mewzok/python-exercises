def most_visited_page(page_visits):
    top_page = None
    most_visited = {}

    for page in page_visits:
        most_visited[page] = most_visited.get(page, 0) + 1
        if top_page is None or most_visited[page] > most_visited[top_page]:
            top_page = page

    return top_page, most_visited[top_page]

page_visits = [
    "home",
    "about",
    "home",
    "products",
    "home",
    "about"
]

print(most_visited_page(page_visits))