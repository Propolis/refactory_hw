from fastapi import Depends, HTTPException

from models import Post
from repositories import PostRepository


class PostService:
    def __init__(self, repository: PostRepository = Depends(PostRepository)):
        self.repository = repository

    def create_post(self, post_text: str, owner_id: int) -> Post:
        return self.repository.create(post_text, owner_id)

    def get_post(self, post_id: int) -> Post:
        post = self.repository.get_by_id(post_id)
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        return post

    def get_all_posts(self) -> list[Post]:
        return self.repository.get_all()

    def delete_post(self, post_id: int, current_user_id: int) -> Post:
        post = self.repository.get_by_id(post_id)
        if post is None:
            raise HTTPException(status_code=404, detail="Post not found")
        if post.owner_id != current_user_id:
            raise HTTPException(status_code=403, detail="You are not the owner of the post")
        self.repository.delete(post)