"""Flask Stack Simulator starter: complete TODOs during the live demo.
Before class, preview templates/index.html directly in the browser.
Running this file starts a status page, not the completed simulator.
"""
from flask import Flask

# TODO P1: Extend the imports with render_template, request, redirect,
# url_for, session, and flash. Import secrets and the completed Stack class.
app = Flask(__name__)
# TODO P2: Set SECRET_KEY for the session and flash messages.
# This lesson uses short fictional stack values on localhost.


@app.route('/')
def index():
    # TODO P3: Replace this temporary response with render_template.
    # Start by displaying the static index.html through Flask.
    # TODO P6: Restore stack values from session, reverse for display,
    # and pass items, size, popped, and highlight to the template.
    return '<h1>Starter ready</h1><p>Complete the TODOs during the demo.</p>'


@app.route('/stack', methods=['POST'])
def operate():
    # TODO P4: Read action and value from request.form. Strip the value.
    # TODO P7: Restore the Stack and removed-item history from session.
    # TODO P8: Implement Push, Pop, Peek, and Clear with feedback.
    # Push accepts 1-24 characters and at most 20 current items.
    # Pop and Peek must handle an empty stack. Clear resets both lists.
    # Keep only the 20 most recently removed values.
    # TODO P9: Reassign session values, then redirect to the index route.
    # Use a peek flag when highlighting the top item.
    return 'TODO: stack operations will be completed during the demo.', 501


@app.route('/contact')
def contact():
    # TODO P5: Render contact.html as a placeholder landing page.
    # A validated contact form belongs to a later lesson.
    return 'TODO: connect the contact placeholder during the demo.', 501


if __name__ == '__main__':
    app.run()  # Local development only. Stop with Ctrl+C.
