from locust import task, between, TaskSet, User, HttpUser
from client import SocialMediaClient

class ExampleTaskSet(TaskSet):
    def __init__(self, user: User):
        super().__init__(user)
        self.social_media_client = SocialMediaClient(self.client)

    def on_start(self):
        self.social_media_client.login()

    @task
    def view_feed_api(self):
        self.social_media_client.view_feed()

    @task
    def create_post_api(self):
        self.social_media_client.create_post()

    @task
    def like_post_api(self):
        self.social_media_client.like_post()

class ExampleSocialMediaUser(HttpUser):
    wait_time = between(1, 5)
    tasks = [ExampleTaskSet]