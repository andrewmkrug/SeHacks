var scrape = require('website-scraper');
phantomHtml = require('website-scraper-phantom');

scrape({
    urls: [
        'https://gitpitch.com/andrewmkrug/SeHacks#/'
    ],
    directory: '/Users/andrewkrug/Projects/lazycoder/sites/SeHacks/public2',
    httpResponseHandler: phantomHtml,
    filenameGenerator: 'bySiteStructure',
    subdirectories: [
        {directory: 'img', extensions: ['.jpg', '.png', '.svg']},
        {directory: 'js', extensions: ['.js']},
        {directory: 'css', extensions: ['.css']}
    ]
}).then(console.log).catch(console.log);