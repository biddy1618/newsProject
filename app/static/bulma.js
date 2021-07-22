/*
 * The following code is based off a toggle menu by @Bradcomp
 * source: https://gist.github.com/Bradcomp/a9ef2ef322a8e8017443b626208999c1
 */
(function () {
  var burger = document.querySelector('.burger');
  var menu = document.querySelector('#' + burger.dataset.target);
  burger.addEventListener('click', function () {
    burger.classList.toggle('is-active');
    menu.classList.toggle('is-active');
  });

  var modal = document.querySelector('.modal');  // assuming you have only 1
  if (modal !== null) {
    modal.addEventListener('click', function (e) {
      e.preventDefault();
      modal.classList.remove('is-active');
    })
  };
})();

// Initialize all input of type date
var calendars = bulmaCalendar.attach('[type="date"]', {startDate: "2012-08-01", endDate: "2012-08-02", showClearButton: false});

// Loop on each calendar initialized
for(var i = 0; i < calendars.length; i++) {
	// Add listener to select event
	calendars[i].on('select', date => {
		// console.log(date);
	});
}

// To access to bulmaCalendar instance of an element
var element = document.querySelector('#calendar');
if (element) {
	// bulmaCalendar instance is available as element.bulmaCalendar
	element.bulmaCalendar.on('select', function(datepicker) {
		console.log(datepicker.data.value());
	});
}