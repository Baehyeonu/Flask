from flask import request, jsonify
from flask_smorest import Blueprint, abort

def create_posts_blueprint(mysql):
    posts_blp = Blueprint("psosts", __name__, description="posts API", url_prefix="/posts")

    @posts_blp.route('/', methods=['GET','POST']) #POST 오타수정
    def posts():
        cursor = mysql.connection.cursor()
        if request.method == 'GET':
            sql = "SELECT * FROM posts"
            cursor.execute(sql)
            
            posts = cursor.fetchall()
            cursor.close()
            
            post_list = []
            
            for post in posts:
                post_list.append({
                    'id': post[0],
                    'title': post[1],
                    'content': post[2]
                })
            return jsonify(post_list)
        
        # 게시글 생성
        elif request.method == "POST":
            title = request.json.get("title")
            content = request.json.get("content")

            if not title or not content:
                abort(400, message="title 또는 content가 없습니다.")

            sql = "INSERT INTO posts(title, content) VALUES(%s, %s)"
            cursor.execute(sql, (title, content))
            mysql.connection.commit()

            
            return jsonify({'msg':"Successfully created post data"}), 201
        
    # 게시글 수정 및 삭제
    @posts_blp.route('/<int:id>', methods=['GET','PUT','DELETE'])   
    def post(id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM posts WHERE id = {id}"
        cursor.execute(sql)
        post = cursor.fetchone()
            
        if request.method == 'GET':

            
            if not post:
                abort(404, "Post not found")
            return ({
                    'id': post[0],
                    'title': post[1],
                    'content': post[2]
                    })
            
        elif request.method == "PUT":  # 인자수의 개수가 맞지 않아 PUT관련 오류 수정
            title = request.json.get("title")
            content = request.json.get("content")

            if not title or not content:
                abort(400, message="title 또는 content가 없습니다.")

            sql = "SELECT * FROM posts WHERE id=%s"
            cursor.execute(sql, (id,))
            post = cursor.fetchone()

            if not post:
                abort(404, message="해당 게시글이 없습니다.")

            sql = "UPDATE posts SET title=%s, content=%s WHERE id=%s"
            cursor.execute(sql, (title, content, id))
            mysql.connection.commit()

            return jsonify({"message": "Successfully updated title & content"})
            
        elif request.method == 'DELETE':
            if not post:
                abort(400, "Not found title, content")
                
            sql = f"DELETE FROM posts WHERE id={id}"
            cursor.execute(sql)
            mysql.connection.commit()
            
            return jsonify({'msg':"Successfully deleted post data"})
        
    return posts_blp