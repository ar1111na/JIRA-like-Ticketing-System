/*
Author       : Dreamguys
Template Name: SmartHR - Bootstrap Admin Template
Version      : 3.6
*/






$(document).ready(function() {



    if ($('.kanban-wrap').length > 0) {
        $(".kanban-wrap").sortable({
            connectWith: ".kanban-wrap",
            handle: ".kanban-box",
            placeholder: "drag-placeholder",
            stop: function(event, ui) {
                saveBoardState(); // Call save function after drag and drop
            }
        });
    }

    // Load board state
    loadBoardState();

    // Save the board state to localStorage
    function saveBoardState() {
        $('.kanban-list').each(function () {
            const listClass = $(this).attr('class').split(' ')[1]; // e.g., kanban-list-to-do
            $(this).find('.kanban-box').each(function () {
                const ticketId = $(this).attr('id').replace('ticket-', ''); // Remove "ticket-" prefix from ID
                const newStatus = listClass.replace('kanban-list-', ''); // Extract the new status from the class name
                
                // Send an AJAX request to update the ticket's status in the database
                $.ajax({
                   // url: '/update-ticket-status/',
                    url: '/dashboard/update_ticket_status/',
                    method: 'GET',
                    data: JSON.stringify({ ticket_id: ticketId, new_status: newStatus }),
                    contentType: 'application/json',
                    headers: {
                        'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val() // Add CSRF token for security
                    },
                    success: function (response) {
                        if (response.status !== "success") {
                            console.error("Error updating ticket:", response.message);
                        }
                    },
                    error: function (error) {
                        console.error("AJAX error:", error);
                    }
                });
            });
        });
    }
    

    // Load the board state from localStorage
    function loadBoardState() {
        const boardState = JSON.parse(localStorage.getItem('kanbanBoardState'));
        if (boardState) {
            for (const listClass in boardState) {
                const ids = boardState[listClass];
                const $list = $('.' + listClass + ' .kanban-wrap');
                $list.empty(); // Clear current items

                // Append items based on saved order
                ids.forEach(id => {
                    const $card = $('#' + id);
                    if ($card.length) {
                        $list.append($card); // Move the card back to the list
                    }
                });
            }
        }
    }


    if ($('.datetimepicker').length > 0) {
        $('.datetimepicker').datetimepicker({
            format: 'DD/MM/YYYY',
            icons: {
                up: "bx bx-chevron-up",
                down: "bx bx-chevron-down",
                next: 'bx bx-chevron-right',
                previous: 'bx bx-chevron-left'
            }
        });
    }

});

// Loader

$(window).on('load', function() {
    $('#loader').delay(100).fadeOut('slow');
    $('#loader-wrapper').delay(500).fadeOut('slow');
});



// var $a = self.$widget.find('a[data-rating-value="' + ratingValue() + '"]');


// resetStyle();


// $a.addClass('br-selected br-current')[nextAllorPreviousAll()]()
//     .addClass('br-selected');

// if (!getData('ratingMade') && $.isNumeric(initialRating)) {
//     if ((initialRating <= baseValue) || !f) {
//         return;
//     }

//     $all = self.$widget.find('a');

//     $fractional = ($a.length) ?
//         $a[(getData('userOptions').reverse) ? 'prev' : 'next']() :
//         $all[(getData('userOptions').reverse) ? 'last' : 'first']();

//     $fractional.addClass('br-fractional');
//     $fractional.addClass('br-fractional-' + f);
// }