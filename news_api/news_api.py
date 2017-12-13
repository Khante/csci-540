from flask import (Flask, render_template, request, flash, abort)
import redis
import sys
from wtforms import Form, TextField, validators
from collections import defaultdict

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'super_secret_key'

redis_db = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)
pubsub = redis_db.pubsub(ignore_subscribe_messages=True)
messages = defaultdict(list)


class SubscribeForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    channel = TextField('Game Channel:', validators=[validators.required()])


class PublishForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    channel = TextField('Game Channel:', validators=[validators.required()])
    news = TextField('News:', validators=[validators.required()])


def pubsubHandler(message):
    print("News Published! " + str(message['data']) + " published to " +
          str(message['channel']), file=sys.stderr)
    messages[message['channel']].append(message['data'])


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/subscribe/", methods=['GET', 'POST'])
def subscribe():
    thread = pubsub.run_in_thread(sleep_time=1)
    form = SubscribeForm(request.form)
    subscriptions = redis_db.pubsub_channels()

    if request.method == 'POST':
        # print(request.headers.get('Content-Type'), file=sys.stderr)
        if request.headers.get('Content-Type') == 'application/json':
            data = request.get_json(force=True)
            if 'name' not in data or 'channel' not in data:
                abort(400)
            name = data['name']
            channel = data['channel']
        else:
            if form.validate():
                name = request.form['name']
                channel = request.form['channel']
            else:
                flash('Error: all fields are required')
                return render_template('subscribe.html', form=form)

        # do stuff with redis
        if channel not in subscriptions:
            messages[channel]
            pubsub.subscribe(**{channel: pubsubHandler})
            flash(str(name) + ' subscribed to ' + str(channel))
            thread = pubsub.run_in_thread(sleep_time=1)
        else:
            flash(str(name) + ' is already subscribed to ' + str(channel))

    return render_template('subscribe.html', form=form,
                           subs=redis_db.pubsub_channels())


@app.route('/publish/', methods=['GET', 'POST'])
def publish():
    form = PublishForm(request.form)

    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            data = request.get_json(force=True)
            if 'name' not in data or 'channel' not in data or 'news' not in data:
                abort(400)
            else:
                name = data['name']
                channel = data['channel']
                news = data['news']
        else:
            if form.validate():
                name = request.form['name']
                channel = request.form['channel']
                news = request.form['news']
            else:
                flash('Error: all fields are required')
                return render_template('publish.html', form=form,
                                       msgs=messages)

        # do stuff with redis
        redis_db.publish(channel, news)
        flash('Published!')

    return render_template('publish.html', form=form, msgs=messages)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
