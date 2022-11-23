from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from pages.models import Page
from .utils import state_choices
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    # profile_pic = models.ImageField(upload_to='profile_pics', blank=True, default='profile_default.jpeg')
    profile_pic = models.TextField(null=True, blank=True,
     default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_640.png")
    dob = models.DateField(blank=True, null=True)
    full_name = models.CharField(max_length=55)
   
    bio = models.TextField(blank=True)
    api_key = models.CharField(max_length=100, null=True, blank=True)
   
    Address     = models.TextField(default=None, blank=True, null=True)
    State       = models.CharField(choices=state_choices,max_length=255, null=True, blank=True)
    Country     = models.CharField(max_length=20, default='India')

    whatsapp    = models.CharField(max_length=10, blank=True) 
    instagram_username = models.CharField(max_length=50 ,blank = True)
    facebook    = models.URLField(blank = True)
    linkdin_profile_link = models.URLField(blank = True)
    gmail       = models.EmailField(blank=True)

    def __str__(self):
        return f'{self.user} Profile'




class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return f'{self.following}' 



class UserPost(models.Model):
    posted_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    title = models.CharField(max_length=100)
    # img = models.ImageField(upload_to='user_post_images', blank=True)
    img = models.TextField(null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f'{self.title} by {self.posted_user}'
    
    class Meta:
        ordering = ['-updated', '-created']

    def get_absolute_url(self):
        return reverse('user-post-detail', kwargs={'pk': self.pk})


class UserSavePost(models.Model):
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name='user_save_Post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_user_post')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f'{self.user} Save {self.post} '


class Messages(models.Model):
    req_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="req_user") # request user
    user_other = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_other")
    msg_data = models.CharField(max_length=500, blank=True)
    # msg_img = models.ImageField(upload_to='chatings')
    sent = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.req_user} - {self.user_other}'