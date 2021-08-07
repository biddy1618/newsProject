/*
 * Additional functions
 */
(function () {
  // Burger menu
  var burger = document.querySelector('.burger');
  var menu = document.querySelector('#' + burger.dataset.target);
  burger.addEventListener('click', function () {
    burger.classList.toggle('is-active');
    menu.classList.toggle('is-active');
  });

  // Modals
  var modal = document.querySelector('.modal');  // assuming you have only 1
  if (modal !== null) {
    modal.addEventListener('click', function (e) {
      e.preventDefault();
      modal.classList.remove('is-active');
    })
  };

  // Bulma calendar
  //// Initialize
  try {
    var calendar = new bulmaCalendar('#calendar', { showFooter: false, isRange: true, dateFormat: "DD-MM-YYYY" });
    
    //// Prevent default submit for calendar
    var calendarButtons = document.getElementById('calendar-div').getElementsByTagName('button');
    for (i = 0; i < calendarButtons.length; i++) {
      calendarButtons[i].setAttribute("type", "button");
    }
  } catch(error) {
    console.log('No calendar was found.');
  }
})();