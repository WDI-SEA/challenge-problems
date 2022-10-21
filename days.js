function dayOfWeek(day, count) {
    const days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ];
    const index = days.indexOf(day);
    return days[(index + count) % 7];
}
console.log(dayOfWeek("Monday", 27))