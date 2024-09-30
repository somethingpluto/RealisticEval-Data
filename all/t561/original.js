const getLogTypeIcon = function(type) {
    if(!['text', 'image'].includes(type)) return false;

    const iconMap = {
        'text': 'article-ph.svg',
        'image': 'image-ph.svg'
    };

    return `assets/icons/${iconMap[type]}`;
}