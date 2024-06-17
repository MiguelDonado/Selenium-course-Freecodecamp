from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.close_cookies()
    bot.close_genius_pop_up()
    bot.change_currency(currency="EUR")
    bot.close_genius_pop_up()
    bot.select_place_to_go(input("Where do you like to go ? "))
    bot.select_dates(
        check_in_date=input("What is the check in day? "),
        check_out_date=input("What is the check out day? "),
    )
    bot.select_adults(count=int(input("How many people?")))
    bot.click_search()
    bot.apply_filtrations()
    bot.refresh()  # A workaround to let our bot to grab the data properly
    bot.report_results()
