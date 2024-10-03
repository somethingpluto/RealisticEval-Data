// written by chatgpt, lesgo
	private int findIndex(double target) {
		int left = 0;
	    int right = totalMassUpToCurrentIndex.length - 1;

	    while (left < right) {
	        int mid = left + (right - left) / 2;

	        // Check if the middle element is the target
	        if (totalMassUpToCurrentIndex[mid] == target) {
	            return mid;
	        }

	        // Check if the target is in the left half of the array
	        if (totalMassUpToCurrentIndex[mid] > target) {
	            right = mid - 1;
	        }
	        // Check if the target is in the right half of the array
	        else {
	            left = mid + 1;
	        }
	    }
