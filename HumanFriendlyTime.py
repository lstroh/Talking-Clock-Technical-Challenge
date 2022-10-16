import time as modtime


class HumanFriendlyTime:
    def __init__(self):
        # dicts used to convert from int to string
        self._intToString11 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
                               8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven'}
        self._hours = {12: 'noon', 13: 'one', 14: 'two', 15: 'three', 16: 'four', 17: 'five', 18: 'six',
                       19: 'seven', 20: 'eight', 21: 'nine', 22: 'ten', 23: 'eleven', 24: 'midnight',
                       0: 'midnight'}
        self._min = {12: 'twelve', 13: "thirteen", 20: 'twenty', 30: 'half'}
        self._minTeen = "teen"

    def _get_hours_string(self, hours):  # method to get hours string from int
        if 0 < hours <= 11:
            return self._intToString11[hours]
        elif 12 <= hours <= 24:
            return self._hours[hours]
        elif hours == 0:
            return self._hours[hours]
        else:
            return ""

    def _get_min_string(self, minutes):  # method to get minutes string from int
        working_min = minutes
        if minutes < 0:
            return ""
        if minutes > 60:
            return ""
        if working_min == 60:  # 60 minutes is the same as 0 minutes
            working_min = 0
        if working_min > 30:  # if minutes > 30 then we want to reduce it from 60 and use it
            working_min = 60 - working_min
        if working_min == 0:   # 0 minutes
            return ""
        elif working_min <= 11:
            return self._intToString11[working_min]
        elif working_min == 12 or working_min == 13 or working_min == 20 or working_min == 30:
            return self._min[working_min]
        #  build minutes string in case it is not a special case ( 0 - 12, 20 or 30 )
        low_digit = working_min % 10
        high_digit = working_min - low_digit
        if high_digit == 10:  # in case minutes > 12 but < 20
            return self._intToString11[low_digit] + self._minTeen
        else:  # in case minutes > 20 and < 30
            return self._min[high_digit] + " " + self._intToString11[low_digit]

    def _check_int_input(self, hours, minutes):  # method to verify int inputs are as expected
        if not isinstance(hours, int):
            raise TypeError("hours should of type int")
        if not isinstance(minutes, int):
            raise TypeError("minutes should of type int")
        if hours < 0 or hours > 24:
            raise ValueError("Hours should be in 0 - 24 range")
        if minutes < 0 or minutes > 60:
            raise ValueError("minutes should be in 0 - 60 range")

    def _check_string_input(self, string):  # method to verify string input is as expected
        if not isinstance(string, str):
            raise TypeError("string should of type str")
        data = string.split(":")
        if len(data) != 2:
            raise ValueError("str format should be HH:MM. For example 01:20 or 1:20")
        return data[0], data[1]

    def get_human_friendly_time_int(self, hours, minutes):
        # main method to convert from hours and minutes to human friendly time string as expected
        self._check_int_input(hours, minutes)
        if minutes == 0 or minutes == 60:
            res = self._get_hours_string(hours) + " o'clock"
        elif minutes <= 30:
            res = self._get_min_string(minutes) + " past " + self._get_hours_string(hours)
        else:
            res = self._get_min_string(minutes) + " to " + self._get_hours_string(hours)
        return res.capitalize()

    def get_human_friendly_time_string(self, time_string):
        # method to convert from string input to human friendly time string as expected
        hours, minutes = self._check_string_input(time_string)
        try:
            hours_int = int(hours)
        except ValueError:
            raise ValueError("Cannot convert hours str " + hours + " to int")
        try:
            min_int = int(minutes)
        except ValueError:
            raise ValueError("Cannot convert minutes str " + minutes + " to int")
        return self.get_human_friendly_time_int(hours_int, min_int)

    def get_human_friendly_time_now(self):
        # method to return the current time as a human friendly time string as expected
        time_now = modtime.localtime(modtime.time())
        return self.get_human_friendly_time_int(time_now.tm_hour, time_now.tm_min)
