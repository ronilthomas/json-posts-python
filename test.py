import sys
import json
import validators

#getting only the first 3 arguments 
args = sys.argv[1:4]

#checking if the arguments passed are correct
if args[0] == 'hackernews' and args[1] == '--posts' and type(int(args[2])) == int:
    print("The arguments passed are correct")
else:
    print("The arguments passed are incorrect")
    sys.exit()

#getting the number of posts to display
posts_to_display = int(args[2])
if posts_to_display >100:
    print("Cannot display more than 100 posts")
    sys.exit()

if posts_to_display <1:
    print("Cannot display less than 1 post")
    sys.exit()

#storing the JSON data in a variable
string = '''
{
    "posts":[{
        "title": "Web Scraping in 2016",
        "uri": "https://franciskim.co/2016/08/24/dont-need-no-stinking-api-web-scraping-2016-beyond/",
        "author": "franciskim",
        "points": 133,
        "comments": 80,
        "rank": 1
    },
    {
        "title": "Instapaper is joining Pinterest",
        "uri": "http://blog.instapaper.com/post/149374303661",
        "author": "ropiku",
        "points": 182,
        "comments": 99,
        "rank": 2
    },
    {
        "title": "joining Insta",
        "uri": "http://blog.paper.com/post/1493",
        "author": "hinoken",
        "points": 12,
        "comments": 89,
        "rank": 3
    },
    {
        "title": "testing Insta",
        "uri": "http://test.pages.com/post/1493",
        "author": "kevin",
        "points": 128,
        "comments": 49,
        "rank": 4
    }

]
}
'''
#Converting the data in the variable to python object
data = json.loads(string)

#validating the JSON data
for post in data['posts']:
    #getting the title
    title = post.get('title', 'Unavailable')
    title_len=len(title)
    #checking for valid title
    if (title_len>=256 or title == ''):
        post.update({'title':'Invalid title'})
    
    #getting the author
    author = post.get('author', 'Unavailable')
    author_len=len(author)
    #checking for valid author
    if (author_len>=256 or author == ''):
        post.update({'author':'Invalid author'})

    #getting the uri
    uri = post.get('uri', 'Unavailable')
    #checking for valid url
    checked_url = validators.url(uri)
    if checked_url != True:
        post.update({'uri':'Invalid uri'})
 
    #getting points
    points = post.get('points', 'Unavailable')
    #checking for valid points
    if (points<=0):
        post.update({'points':'Invalid points'})
    
    #getting comments
    comments = post.get('comments', 'Unavailable')
    #checking for valid comments
    if (comments<=0):
        post.update({'comments':'Invalid comments'})

    #getting rank
    rank = post.get('rank', 'Unavailable')
    #checking for valid rank
    if (rank<=0):
        post.update({'rank':'Invalid rank'})

available_posts = len(data['posts'])

#validated output
for i in range(0, posts_to_display):
    #to break the loop if number of posts available are less than the posts requested for display
    if (available_posts<=i):
        break
    #output JSON data    
    print(json.dumps(data['posts'][i], indent=2))