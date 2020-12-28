
from blog import Blog

MENU_PROMPT = """ 
Enter the letter according to the option you want to execute: 
    - 'C' to create a blog.
    - 'L' list blogs.
    - 'R' read a blog.
    - 'P' create a post.
    - 'Q' exit.
"""

blogs = dict()

def menu():
    # Show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection.upper() != 'Q':
        if selection.upper() == 'C':
            create_blog()
        elif selection.upper() == 'L':
            print_blogs()
        elif selection.upper() == 'R':
            read_blogs()
        elif selection.upper() == 'P':
            create_post()
        else 
            print("Incorrect option, closing the app")
            break
        selection = input(MENU_PROMPT)

def create_blog():
    new_blog_title = input('Enter the new blog title: ')
    new_blog_author = input('Enter the new blog author: ')

    blogs[new_blog_title] = Blog(new_blog_title, new_blog_author)

def print_blogs():
    for key, blog in blogs.items():     #this is how you iterate a dict
        print('- {}'.format(blog))

def read_blogs():
    enter_title = input('Please enter the title of the blog: ')
    if blogs[enter_title]:
        print_posts(blogs[enter_title])
    else:
        print("Blog wasn't found.")

def create_post():

def print_posts(title):
    for post in blog.posts: #.post is like .item and is to get the elements of a dict, post will have key and value.
        print_post(post)

def print_post(post):
    print("""
    --- {} ---

    {}

    """.format(post.title, post.content))



            
