function get_current_date_info(testDate = new Date()) {
    let date = new Date(testDate);
    let year = date.getFullYear();
    let monthNames = ["January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
    ];
    let month = monthNames[date.getMonth()];
    let weekOfTheMonth = Math.ceil(date.getDate() / 7);
    let daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    let dayOfWeek = daysOfWeek[date.getDay()];
  
    return { 
        'year': year,
        'month': month,
        'week_of_the_month': weekOfTheMonth,
        'day_of_the_week': dayOfWeek
    };
}