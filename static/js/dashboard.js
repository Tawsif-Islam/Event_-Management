document.addEventListener('DOMContentLoaded', function() {
    // Function to fetch and display today's events
    function fetchTodaysEvents() {
        const today = new Date().toISOString().split('T')[0];
        fetch(`/events/today/${today}/`)
            .then(response => response.json())
            .then(data => {
                const eventsList = document.getElementById('todays-events-list');
                eventsList.innerHTML = '';
                data.forEach(event => {
                    const listItem = document.createElement('li');
                    listItem.textContent = `${event.name} - ${event.location}`;
                    eventsList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Error fetching today\'s events:', error));
    }

    // Function to update stats dynamically
    function updateStats(statType) {
        fetch(`/events/stats/${statType}/`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('total-participants').textContent = data.total_participants;
                document.getElementById('total-events').textContent = data.total_events;
                document.getElementById('upcoming-events').textContent = data.upcoming_events;
                document.getElementById('past-events').textContent = data.past_events;
            })
            .catch(error => console.error('Error updating stats:', error));
    }

    // Event listeners for stats buttons
    document.getElementById('total-events-btn').addEventListener('click', function() {
        updateStats('total');
    });

    document.getElementById('upcoming-events-btn').addEventListener('click', function() {
        updateStats('upcoming');
    });

    document.getElementById('past-events-btn').addEventListener('click', function() {
        updateStats('past');
    });

    // Initial fetch for today's events
    fetchTodaysEvents();
});