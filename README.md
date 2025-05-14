launch: uvicorn main:app --reload

add user:
http POST http://127.0.0.1:8000/user/add name="name" age:=age

add post:
http POST http://12zzz.1:8000/posts/addtitle="title"body="body"author_id:=id


get all posts:
http GET http://127.0.0.1:8000/posts


get one post by id:
http GET http://127.0.0.1:8000/posts/1


