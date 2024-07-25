from flask import Flask, jsonify

app = Flask(__name__)

# (1) 전체 게시글을 불러오는 API
@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    data = {'result':'success', 'data':{'feed1':'data1', 'feed2':'data2'}}

    return data

# (2) 특정 게시글을 불러오는 API
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    data = {
        'result':'success', 
        'data':{'feed_id':feed_id}
        }

    return data