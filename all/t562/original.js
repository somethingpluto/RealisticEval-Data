const getStatusIcon = function(status) {
    if(!['success', 'fail'].includes(status)) return false;

    const iconMap = {
        'success': 'checks-ph.svg',
        'fail': 'x-ph.svg'
    };

    return `assets/icons/${iconMap[status]}`;
}