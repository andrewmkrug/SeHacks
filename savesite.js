var scrape = require('website-scraper');

scrape({
    urls: ['http://localhost:9000/gitpitch/desktop#/'],
    urlFilter: (url) => url.startsWith('localhost:9000'),
    recursive: true,
    maxRecursiveDepth: 1,
    filenameGenerator: 'bySiteStructure',
    directory: '/public',
    subdirectories: [
    {directory: 'img', extensions: ['.jpg', '.png', '.svg']},
    {directory: 'js', extensions: ['.js']},
    {directory: 'css', extensions: ['.css']}
]
}).then(console.log).catch(console.log);