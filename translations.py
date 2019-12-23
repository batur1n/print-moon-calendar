class Russian():

    translations = { 
                    'Aries': "Овен",
                    'Taurus': "Телец",
                    'Gemini': "Близнецы",
                    'Cancer': "Рак",
                    "Leo": "Лев",
                    'Virgo': "Дева",
                    'Libra': "Весы",
                    'Scorpio': "Скорпион",
                    'Sagittarius': "Стрелец",
                    'Capricorn': "Козерог",
                    'Aquarius': "Водолей",
                    'Pisces': "Рыбы",
                    'moon day': "лунный день",
                    'Mon': "Понедельник", 
                    'Tue': "Вторник", 
                    'Wed': "Среда", 
                    'Thu': "Четверг", 
                    'Fri': "Пятница", 
                    'Sat': "Суббота", 
                    'Sun': "Воскресенье",
                    'January': "Январь",
                    'February': "Февраль",
                    'March': "Март",
                    'April': "Апрель",
                    'May': "Май",
                    'June': "Июнь",
                    'July': "Июль",
                    'August': "Август",
                    'September': "Сентябрь",
                    'October': "Октябрь",
                    'November': "Ноябрь",
                    'December': "Декабрь"
                  }

    def traslate(self, input_string):
        # returns translated text
        if input_string in self.translations:
            return self.translations[input_string]
