function formatAllDates() {
    // Select all elements with the class "date-to-format"
    var elements = document.querySelectorAll('.date-to-format');

    elements.forEach(function(element) {
        var date = element.getAttribute('data-date');
        var format = element.getAttribute('data-format');

        formattedDate = getFormattedDate(date, format);

        element.textContent = formattedDate;
    });
}

function getFormattedDate(date, format) {
     var dateInCET = moment(date).tz('Europe/Berlin');
     return dateInCET.format(format);
}

function getAllDividerAnchors() {
    return document.querySelectorAll('.date_divider a');
}

function jumpToCurrentDateAnchor(dateDividers) {

    var urlPath = new URL(window.location.href).pathname;
    if (!urlPath) {
        return;
    }
    if (!urlPath.indexOf('date')) {
        return;
    }
    if (urlPath.includes('#')) {
        return;
    }

    var currentDate = urlPath.split('/').pop();
    [...dateDividers].forEach(function(dateDivider) {
        anchorDate = dateDivider.dataset.date.split(' ')[0];
        if (anchorDate == currentDate) {
            console.log('scrolling to ' + currentDate);
            dateDivider.scrollIntoView();
        }
    });
}

function generateScrollShortcuts(dateDividers) {
    target = document.getElementById('scroll-shortcuts');
    target.innerHTML = '';

    bodyElement = document.querySelector('body');
    appendAnchorLink(target, bodyElement, 'Top');

    shortcuts = [];

    [...dateDividers].forEach(function(dateDivider) {
        anchorDate = dateDivider.dataset.date.split(' ')[0];
        anchorFormat = 'dddd DD. MMMM';
        formattedDate = getFormattedDate(anchorDate, anchorFormat);
        button = appendAnchorLink(target, dateDivider, formattedDate);
        shortcuts.push({shortcut: button, dateDivider: dateDivider});
    });

    return shortcuts;
}

function appendAnchorLink(target, anchorTarget, text) {
        var p = document.createElement('p');
        var button = document.createElement('a');
        button.onclick = function() {
            anchorTarget.scrollIntoView();
        };
        button.textContent = text;
        p.append(button);
        target.appendChild(p);
        return button;
}


document.addEventListener("DOMContentLoaded", function() {
        formatAllDates();
        dateDividers = getAllDividerAnchors();
        jumpToCurrentDateAnchor(dateDividers);
        shortcuts = generateScrollShortcuts(dateDividers);

        addEventListener("scroll", function(){
            var scrollPosition = window.scrollY;
            const scrollOffset = 300;

            lastCurrentShortcut = undefined;
            [...shortcuts].forEach(function({shortcut, dateDivider}){
                shortcut.classList.remove('current');
                var dateDividerPosition = dateDivider.getBoundingClientRect().top;
                if (dateDividerPosition < scrollOffset) {
                    lastCurrentShortcut = shortcut;
                }
            });

            if (lastCurrentShortcut) {
                lastCurrentShortcut.classList.add('current');
            }
        });
});