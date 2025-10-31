import numpy as np
import plotly.graph_objects as go

# ----------- USER SETTINGS ------------
faces = [1, 2, 3, 4, 5, 6,7]             # Die faces
probabilities = [0.5,0.05,0.05,0.025,0.025,0.05,0.3]                # Change to uneven, e.g. [0.05,0.1,0.1,0.2,0.25,0.3]
n_throws = 10                          # Number of throws per sample
n_samples = 100000                       # Number of samples (frames in animation)
frame_step = 1000                        # How many samples per frame (for speed)
# -------------------------------------

assert np.isclose(sum(probabilities), 1), "Probabilities must sum to 1."
assert len(faces) == len(probabilities), "Number of faces must equal number of probabilities."

# Calculating Theoretical Values
expectation_single = np.dot(faces, probabilities)
variance_single = np.dot(probabilities, (np.array(faces) - expectation_single)**2)
expectation_sum = n_throws * expectation_single
variance_sum = n_throws * variance_single
std_sum = np.sqrt(variance_sum)

# Generate all sample sums
sample_sums = [np.sum(np.random.choice(faces, size=n_throws, p=probabilities))
               for _ in range(n_samples)]

# Create frames for animation
frames = []
bins = np.arange(n_throws * min(faces), n_throws * max(faces) + 2)
'''
Setting up 'buckets' for our histogram: Think of this as creating the empty boxes we'll put our results into.
If we're throwing dice with faces 1-6, and we throw 10 dice, the total can range from 10 to 60.
This creates boxes for every possible total score
'''

for i in range(frame_step, n_samples + frame_step, frame_step): #start, stop (+step because range doesn't include last val), step
    hist, edges = np.histogram(sample_sums[:i], bins=bins, density=False) #adds {frame_step} samples to the histogram with bins defined
    centers = (edges[:-1] + edges[1:]) / 2  # center of the bins will in between its edges
    frames.append(go.Frame(
        data=[go.Bar(x=centers, y=hist, marker_color='skyblue', opacity=0.7)],
        name=f"{i}"
    ))

# Gaussian for overlay
x_vals = np.linspace(min(sample_sums), max(sample_sums), 400)
gaussian = (1 / (std_sum * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_vals - expectation_sum) / std_sum) ** 2)
gaussian_scaled = gaussian * n_samples * (bins[1] - bins[0])

# Create figure
fig = go.Figure(
    data=[go.Bar(x=[], y=[], marker_color='skyblue', opacity=0.7),
          go.Scatter(x=x_vals, y=gaussian_scaled, mode='lines', line=dict(color='red', width=2),
                     name='Gaussian Approximation')],
    layout=go.Layout(
        title="Central Limit Theorem Visualizer (Animated)",
        xaxis=dict(title='Sum of Throws'),
        yaxis=dict(title='Frequency'),
        template='plotly_white',
        updatemenus=[{
            "buttons": [
                {"args": [None, {"frame": {"duration": 50, "redraw": True},
                                 "fromcurrent": True, "mode": "immediate"}],
                 "label": "Play",
                 "method": "animate"},
                {"args": [[None], {"frame": {"duration": 0, "redraw": False},
                                   "mode": "immediate"}],
                 "label": "Pause",
                 "method": "animate"}
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 70},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top"
        }]
    ),
    frames=frames
)

# Now show the plot
fig.show()
