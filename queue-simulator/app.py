from flask import Flask, render_template, request, redirect, url_for, session, flash
from queue_model import Queue

app = Flask(__name__)
app.secret_key = 'dev-only-change-me'


@app.route('/')
def index():
    queue = Queue(session.get('queue', []))
    items = queue.items  # Huwag i-reverse: Front ang una.
    popped = session.get('popped', [])
    highlight = session.pop('highlight', False)

    return render_template(
        'index.html',
        items=items,
        size=queue.size(),
        popped=popped,
        highlight=highlight
    )


@app.route('/queue', methods=['POST'])
def operate():
    action = request.form.get('action', '').strip().lower()
    value = request.form.get('value', '').strip()

    queue = Queue(session.get('queue', []))
    popped = session.get('popped', [])
    session['highlight'] = False

    if action == 'enqueue':
        if not value:
            flash('Please enter a value.', 'warning')
        elif len(value) > 24:
            flash('Value must not exceed 24 characters.', 'warning')
        elif queue.size() >= 20:
            flash('Queue is full. Maximum is 20 items.', 'warning')
        else:
            queue.enqueue(value)
            flash(f'{value} added to the rear of the queue.', 'success')

    elif action == 'dequeue':
        removed = queue.dequeue()
        if removed is None:
            flash('The queue is empty. Nothing to dequeue.', 'warning')
        else:
            popped.append(removed)
            popped = popped[-20:]
            flash(f'{removed} removed from the front.', 'success')

    elif action == 'peek':
        front = queue.peek()
        if front is None:
            flash('The queue is empty. Nothing to peek.', 'warning')
        else:
            session['highlight'] = True
            flash(f'Front value is {front}.', 'info')

    elif action == 'clear':
        queue.clear()
        popped.clear()
        flash('Queue and removed items cleared.', 'success')

    else:
        flash('Invalid operation.', 'warning')

    session['queue'] = queue.items
    session['popped'] = popped
    return redirect(url_for('index'))


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()