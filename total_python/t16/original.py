# mostly written by CHATGPT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import utils


def plot_eeg_with_event_markers(eeg_file_path, markers_file_path):
    # Load the EEG data file
    eeg_data = pd.read_csv(eeg_file_path)

    # Load the Markers data file
    markers_data = pd.read_csv(markers_file_path)

    # Plotting the EEG data with event markers
    plt.figure(figsize=(18, 20))

    # Plot each EEG channel with actual event names as labels
    for i, column in enumerate(eeg_data.columns[1:], start=1):
        plt.subplot(len(eeg_data.columns) - 1, 1, i)
        plt.plot(eeg_data['Timestamp'], eeg_data[column], label=f'{column}')
        plt.ylabel('Amplitude')

        # Adding markers with actual event names from the second column
        for _, row in markers_data.iterrows():
            plt.axvline(x=row['Timestamp'], color='r', linestyle='--')
            marker_id = np.rint(row['Channel_1']).astype(int)  # obtain marker id
            eventName = utils.get_marker_name(marker_id)  # convert id to name (string)
            plt.text(row['Timestamp'], plt.ylim()[1], eventName, color='r', verticalalignment='bottom', rotation=45)

        plt.legend()

    plt.xlabel('Timestamp')
    plt.suptitle('EEG Data with Event Markers Labeled by Event Names')
    plt.tight_layout(rect=[0, 0.03, 1, 0.97])  # Adjust layout to make room for the title
    plt.show()


# Replace 'path_to_your_eeg_data.csv' and 'path_to_your_markers_data.csv' with the actual paths to your files

plot_eeg_with_event_markers('./xdf-results/test0_data.csv', './xdf-results/test0_markers.csv')