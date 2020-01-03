function calculate_days(){

    var from_date = document.getElementById("from_date").value
    var to_date = document.getElementById("to_date").value

    var time_diff = Date.parse(to_date) - Date.parse(from_date)
    var total_days = Math.round( time_diff / (1000*60*60*24) ) + 1

    document.getElementById("total_days").value = total_days
}
