# Ubicoustics Label Definition
labels = {
    'dog-bark':0,
    'drill':1,
    'hazard-alarm':2,
    'phone-ring':3,
    'speech':4,
    'vacuum':5,
    'baby-cry':6,
    'chopping':7,
    'cough':8,
    'door':9,
    'water-running':10,
    'knock':11,
    'microwave':12,
    'shaver':13,
    'toothbrush':14,
    'blender':15,
    'dishwasher':16,
    'doorbell':17,
    'flush':18,
    'hair-dryer':19,
    'laugh':20,
    'snore':21,
    'typing':22,
    'hammer':23,
    'car-horn':24,
    'engine':25,
    'saw':26,
    'cat-meow':27,
    'alarm-clock':28,
    'cooking':29,
}

dummy = ['snore', 'saw']
bathroom = ['water-running','flush','toothbrush','shaver','hair-dryer']
kitchen = ['water-running','chopping','cooking','microwave','blender','hazard-alarm','dishwasher','speech']
bedroom = ['alarm-clock','snore','cough','baby-cry','speech']
office = ['knock','typing','phone-ring','door','cough','speech']
entrance = ['knock','door','doorbell','speech','laugh']
workshop = ['hammer','saw','drill','vacuum','hazard-alarm','speech']
outdoor = ['dog-bark','cat-meow','engine','car-horn','speech','hazard-alarm']
everything = [
    'dog-bark', 'drill', 'hazard-alarm', 'phone-ring', 'speech', 
    'vacuum', 'baby-cry', 'chopping', 'cough', 'door', 
    'water-running', 'knock', 'microwave', 'shaver', 'toothbrush', 
    'blender', 'dishwasher', 'doorbell', 'flush', 'hair-dryer', 
    'laugh', 'snore', 'typing', 'hammer', 'car-horn', 
    'engine', 'saw', 'cat-meow', 'alarm-clock', 'cooking'
]

context_mapping = {
    'kitchen': kitchen, 
    'bathroom': bathroom, 
    'bedroom': bedroom, 
    'office': office, 
    'entrance': entrance, 
    'workshop':workshop, 
    'outdoor':outdoor, 
    'everything': everything
}

to_human_labels = {
    'dog-bark': "Dog Barking",
    'drill': "Drill In-Use",
    'hazard-alarm': "Hazard Alarm",
    'phone-ring': "Phone Ringing",
    'speech': "Person Talking",
    'vacuum': "Vacuum In-Use",
    'baby-cry': "Baby Crying",
    'chopping': "Chopping",
    'cough': "Coughing",
    'door': "Door In-Use",
    'water-running': "Water Running",
    'knock': "Knocking",
    'microwave': "Microwave In-Use",
    'shaver': "Shaver In-Use",
    'toothbrush': "Toothbrushing",
    'blender': "Blender In-Use",
    'dishwasher': "Dishwasher In-Use",
    'doorbell': "Doorbel In-Use",
    'flush': "Toilet Flushing",
    'hair-dryer': "Hair Dryer In-Use",
    'laugh': "Laughing",
    'snore': "Snoring",
    'typing': "Typing",
    'hammer': "Hammering",
    'car-horn': "Car Honking",
    'engine': "Vehicle Running",
    'saw': "Saw In-Use",
    'cat-meow': "Cat Meowing",
    'alarm-clock': "Alarm Clock",
    'cooking': "Utensils and Cutlery",
}