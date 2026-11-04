
"""Flask Stack Simulator starter: complete TODOs during the live demo.
Before class, preview templates/index.html directly in the browser.
Running this file starts a status page, not the completed simulator.
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
import secrets
from stack_model import Stack

# TODO P1: Extend the imports with render_template, request, redirect,
# url_for, session, and flash. Import secrets and the completed Stack class.
app = Flask(__name__)

# TODO P2: Set SECRET_KEY for the session and flash messages.
# This lesson uses short fictional stack values on localhost.
app.secret_key = secrets.token_hex(16)


@app.route('/')
def index():
    # TODO P3: Replace this temporary response with render_template.
    # Start by displaying the static index.html through Flask.

    # TODO P6: Restore stack values from session, reverse for display,
    # and pass items, size, popped, and highlight to the template.
    stack = Stack(session.get('stack', []))
    items = list(reversed(stack.items))
    popped = session.get('popped', [])
    highlight = session.pop('highlight', False)

    return render_template(
        'index.html',
        items=items,
        size=stack.size(),
        popped=popped,
        highlight=highlight
    )


@app.route('/stack', methods=['POST'])
def operate():
    # TODO P4: Read action and value from request.form. Strip the value.
    action = request.form.get('action', '').strip().lower()
    value = request.form.get('value', '').strip()

    # TODO P7: Restore the Stack and removed-item history from session.
    stack = Stack(session.get('stack', []))
    popped = session.get('popped', [])

    # TODO P8: Implement Push, Pop, Peek, and Clear with feedback.
    # Push accepts 1-24 characters and at most 20 current items.
    # Pop and Peek must handle an empty stack. Clear resets both lists.
    # Keep only the 20 most recently removed values.
    # Use a peek flag when highlighting the top item.

    session['highlight'] = False

    if action == 'push':
        if not value:
            flash('Please enter a value.', 'warning')
        elif len(value) > 24:
            flash('Value must not exceed 24 characters.', 'warning')
        elif stack.size() >= 20:
            flash('Stack is full. Maximum is 20 items.', 'warning')
        else:
            stack.push(value)
            flash(f'{value} added to the stack.', 'success')

    elif action == 'pop':
        removed = stack.pop()

        if removed is None:
            flash('The stack is empty. Nothing to remove.', 'warning')
        else:
            popped.append(removed)
            popped = popped[-20:]
            flash(f'{removed} removed from the stack.', 'success')

    elif action == 'peek':
        top = stack.peek()

        if top is None:
            flash('The stack is empty. Nothing to peek.', 'warning')
        else:
            session['highlight'] = True
            flash(f'Top value is {top}.', 'info')

    elif action == 'clear':
        stack.clear()
        popped.clear()
        flash('Stack and removed items cleared.', 'success')

    else:
        flash('Invalid operation.', 'warning')

    # TODO P9: Reassign session values, then redirect to the index route.
    session['stack'] = stack.items
    session['popped'] = popped

    return redirect(url_for('index'))


@app.route('/contact')
def contact():
    # TODO P5: Render contact.html as a placeholder landing page.
    # A validated contact form belongs to a later lesson.
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()  # Local development only. Stop with Ctrl+C.