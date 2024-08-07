def read_hmm_emissions(hmm_file_path) -> Tuple[np.ndarray, List[str]]:
    """
    NOTE: This subroutine has largely been written by GPT-4 and was debugged and modified by the author.
    """
    with open(hmm_file_path, 'r') as file:
        lines = file.readlines()

    # Find where the HMM matrix starts and ends
    start = next(i for i, line in enumerate(lines) if line.startswith('HMM '))
    end = next(i for i, line in enumerate(lines[start:], start) if line.startswith('//'))

    # Read the emission probabilities
    emissions = []
    aa_mapping = lines[start].split()[1:21] # In what order do our AAs occur
    for line in lines[start+2:end]:  # Skip header lines
        parts = line.split()
        if not parts[0].isnumeric(): # Only process lines starting with a match state index
            continue 
        # Each match state has 20 emissions followed by 20 insert emissions; we'll take just the first 20
        match_emissions = list(map(float, parts[1:21]))
        emissions.append(match_emissions)
    emissions = np.array(emissions)
    return emissions, aa_mapping