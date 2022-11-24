from users.models import UserProfile
import random
movie_list = ['batman', 'superman', 'marvel', 'spy', 'tom and jerry', 'micky mouse', 'ghost']

def get_home_page_content():
    return movie_list[random.randint(0, len(movie_list))-1]


