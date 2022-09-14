input_params = {
 "Subscription":"date",
 "add_subscription":{"Music":"Personal","Video":"Premium","Podcast":"Free"},
 "add_topup":{"Four_Device":"3","Ten_Device":"6"},
 "print_renewal":"yes"
}

input_params["add_subscription"]["Music"] = {"Personal"}

subscription_category -> Music, video, podcast
subscription_type -> personal, premium, free
topup -> four_device, ten_device

TRIAL = 1 month datetime object
PERSONAL = 1 month datetime object
PREMIUM = 3 month datetime object

{
"TRIAL":{"music":0,"video":200,"podcast":100}
"PERSONAL":{"music":100,"video":200,"podcast":100},
"PREMIUM":{"music":250,"video":500,"podcast":300}
}

class music:
	def __init__(self, )

class subs_cat:
	def __init__(self, input_params: Dict):
		self.input_params = input_params
		
	def calc_amount(self):
		music = int(input_params["Add_subscription"]["music"])
		videos = int(input_params["Add_subscription"]["video"])
		podcast = int(input_params["Add_subscription"]["Podcast"])
		days = get_days(input_params['Subscription'])
