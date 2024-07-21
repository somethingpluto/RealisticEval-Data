import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data(eeg_file_path, markers_file_path):
    """Load EEG and markers data from CSV files."""
    try:
        eeg_data = pd.read_csv(eeg_file_path)
        markers_data = pd.read_csv(markers_file_path)
        return eeg_data, markers_data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None


def plot_eeg_data(eeg_data, markers_data):
    """Plot EEG data with event markers."""
    plt.figure(figsize=(18, 20))

    num_channels = len(eeg_data.columns) - 1
    timestamp_col = 'Timestamp'

    for i, column in enumerate(eeg_data.columns[1:], start=1):
        plt.subplot(num_channels, 1, i)
        plt.plot(eeg_data[timestamp_col], eeg_data[column], label=f'{column}')
        plt.ylabel('Amplitude')

        add_event_markers(markers_data, timestamp_col)

        plt.legend()

    plt.xlabel('Timestamp')
    plt.suptitle('EEG Data with Event Markers Labeled by Event Names')
    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    plt.show()


def add_event_markers(markers_data, timestamp_col):
    """Add event markers to the plot."""
    for _, row in markers_data.iterrows():
        marker_time = row[timestamp_col]
        plt.axvline(x=marker_time, color='r', linestyle='--')
        marker_id = np.rint(row['Channel_1']).astype(int)
        event_name = utils.get_marker_name(marker_id)
        plt.text(marker_time, plt.ylim()[1], event_name, color='r', verticalalignment='bottom', rotation=45)


def plot_eeg_with_event_markers(eeg_file_path, markers_file_path):
    """High-level function to plot EEG data with markers."""
    eeg_data, markers_data = load_data(eeg_file_path, markers_file_path)
    if eeg_data is not None and markers_data is not None:
        plot_eeg_data(eeg_data, markers_data)


# Example usage
plot_eeg_with_event_markers('./xdf-results/test0_data.csv', './xdf-results/test0_markers.csv')
