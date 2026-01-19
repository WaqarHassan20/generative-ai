from pydantic import BaseModel
from typing import Optional


class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[list["Comment"]] = None  # Self-referential field


Comment.model_rebuild()  # Required to resolve forward references

comment = Comment(
    id=1,
    content="This is first comment",
    replies=[
        Comment(id=2, content="This is a reply to first comment"),
        Comment(id=3, content="This is another reply to first comment"),
    ],
)
from pydantic import BaseModel
from typing import Optional


class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[list["Comment"]] = None  # Self-referential field


Comment.model_rebuild()  # Required to resolve forward references

comment = Comment(
    id=1,
    content="This is first comment",
    replies=[
        Comment(id=2, content="This is a reply to first comment"),
        Comment(id=3, content="This is another reply to first comment"),
        Comment(
            id=4,
            content="This is another reply to first comment",
            replies=[
                Comment(id=5, content="This is a nested reply"),
            ],
        ),
    ],
)

print(comment)