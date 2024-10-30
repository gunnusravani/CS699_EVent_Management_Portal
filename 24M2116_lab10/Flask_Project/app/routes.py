from flask import Blueprint, render_template, request, redirect, url_for, session, flash

bp = Blueprint('main', __name__)

users = {
    'user1@gmail.com': 'password1',
    'user2@gmail.com': 'password2',
    'user3@gmail.com': 'password3',
    'user4@gmail.com': 'password4',
    'user5@gmail.com': 'password5',
    'user6@gmail.com': 'password6',
    'user7@gmail.com': 'password7',
    'user8@gmail.com': 'password8',
    'user9@gmail.com': 'password9',
    'user10@gmail.com': 'password10',
    'host1@gmail.com': 'password1',
    'host2@gmail.com': 'password2',
    'host3@gmail.com': 'password3'
}

# Set of host emails using Gmail
host_emails = {'host1@gmail.com', 'host2@gmail.com', 'host3@gmail.com'}

# Events with associated host emails
events = [
    {'id': 1, 'name': 'Tech Conference 2024', 'description': 'AI and ML innovations.', 'date': '2024-11-01', 'host_email': 'host1@gmail.com', 'image': 'tech_conference.jpeg'},
    {'id': 2, 'name': 'Art Workshop', 'description': 'Modern art techniques.', 'date': '2024-12-05', 'host_email': 'host2@gmail.com', 'image': 'art_workshop.jpeg'},
    {'id': 3, 'name': 'Music Fest', 'description': 'Annual music festival with live bands.', 'date': '2024-10-20', 'host_email': 'host3@gmail.com', 'image': 'music_fest.jpeg'},
    {'id': 4, 'name': 'Cooking Class', 'description': 'Hands-on cooking session.', 'date': '2024-10-22', 'host_email': 'host1@gmail.com', 'image': 'cooking_class.jpeg'},
    {'id': 5, 'name': 'Startup Pitch', 'description': 'Pitching session for startups.', 'date': '2024-11-05', 'host_email': 'host2@gmail.com', 'image': 'startup_pitch.jpeg'},
    {'id': 6, 'name': 'Dance Workshop', 'description': 'Learn various dance forms.', 'date': '2024-11-12', 'host_email': 'host3@gmail.com', 'image': 'dance_workshop.png'},
]


# Store registrations by user and by event
registrations_by_user = {}
registrations_by_event = {event['id']: [] for event in events}

@bp.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('main.home'))
    return redirect(url_for('main.login'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if users.get(email) == password:
            session['user'] = email
            session['is_host'] = email in host_emails
            return redirect(url_for('main.home'))
        else:
            flash('Invalid credentials, please try again.', 'danger')
    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.login'))

@bp.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('main.login'))
    return render_template('index.html', events=events)

@bp.route('/event/<int:event_id>')
def event_detail(event_id):
    event = next((e for e in events if e['id'] == event_id), None)
    return render_template('event.html', event=event)

@bp.route('/register/<int:event_id>', methods=['GET', 'POST'])
def register(event_id):
    # Ensure the user is logged in
    if 'user' not in session:
        return redirect(url_for('main.login'))
    
    # Find the event
    event = next((e for e in events if e['id'] == event_id), None)
    if not event:
        flash("Event not found.", "danger")
        return redirect(url_for('main.home'))

    # Get the user's email from the session
    user_email = session['user']

    # Check if the logged-in user is the host of the event
    if user_email == event['host_email']:
        flash("You cannot register for your own event.", "warning")
        return redirect(url_for('main.event_detail', event_id=event_id))

    # Check if the user is already registered for the event
    if user_email in registrations_by_event[event_id]:
        flash("You have already registered for this event.", "info")
        return redirect(url_for('main.event_detail', event_id=event_id))

    # Handle form submission if not already registered and not the host
    if request.method == 'POST':
        registrations_by_event[event_id].append(user_email)
        if user_email not in registrations_by_user:
            registrations_by_user[user_email] = []
        registrations_by_user[user_email].append(event)
        flash(f'Successfully registered for {event["name"]}!', 'success')
        
        return redirect(url_for('main.event_detail', event_id=event_id))

    # Display the registration form
    return render_template('register.html', event=event)


@bp.route('/my_events')
def my_events():
    # Ensure the user is logged in
    if 'user' not in session:
        return redirect(url_for('main.login'))
    
    # Get the user's email from the session
    user_email = session['user']
    
    # Retrieve the list of events the user has registered for
    user_events = registrations_by_user.get(user_email, [])
    
    # Render the my_events.html template with the list of registered events
    return render_template('myevents.html', user_events=user_events)

@bp.route('/hostdashboard')
def host_dashboard():
    if 'user' not in session or not session.get('is_host'):
        flash("Access denied: You do not have permission to view the host dashboard.", "danger")
        return redirect(url_for('main.home'))

    host_email = session['user']
    hosted_events = [event for event in events if event['host_email'] == host_email]
    return render_template('hostdashboard.html', hosted_events=hosted_events)

@bp.route('/host_event_dashboard/<int:event_id>')
def host_event_dashboard(event_id):
    if 'user' not in session or not session.get('is_host'):
        flash("Access denied: You do not have permission to view this dashboard.", "danger")
        return redirect(url_for('main.home'))

    host_email = session['user']
    event = next((e for e in events if e['id'] == event_id and e['host_email'] == host_email), None)
    if not event:
        flash("Event not found or access denied.", "danger")
        return redirect(url_for('main.host_dashboard'))

    registered_users = registrations_by_event[event_id]
    return render_template('host_event_dashboard.html', event=event, registered_users=registered_users)
