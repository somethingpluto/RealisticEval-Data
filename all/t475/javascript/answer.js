function safeFormat(template, ...args) {
    // Convert args into an object for easier access
    let obj = {};
    for(let i=0; i<args.length; i++) {
        if(typeof args[i] === 'object' && args[i] !== null){
            Object.assign(obj, args[i]);
        }
    }

    return template.replace(/{(\w+)}/g, function(match, key) {
        return key in obj ? obj[key] : match;
    });
}
