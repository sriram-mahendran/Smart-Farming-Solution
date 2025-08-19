import csv

# Your data (assuming it's stored in commodity_info)
commodity_info = {
    "bajra": {
        "season": "Kharif",
        "locations": ["Rajasthan", "Uttar Pradesh", "Haryana", "Gujarat", "Maharashtra"],
        "exported_to": ["Saudi Arabia", "UAE", "Yemen", "USA"]
    },
    "barley": {
        "season": "Rabi",
        "locations": ["Rajasthan", "Uttar Pradesh", "Haryana", "Madhya Pradesh", "Punjab"],
        "exported_to": ["Saudi Arabia", "UAE", "Nepal", "Japan"]
    },
    "jowar": {
        "season": "Both",  # Kharif in north, Rabi in south
        "locations": ["Maharashtra", "Karnataka", "Madhya Pradesh", "Andhra Pradesh", "Tamil Nadu"],
        "exported_to": ["USA", "UAE", "Nepal", "China"]
    },
    "maize": {
        "season": "Both",  # Mainly Kharif but also Rabi in some regions
        "locations": ["Karnataka", "Andhra Pradesh", "Maharashtra", "Rajasthan", "Madhya Pradesh"],
        "exported_to": ["Vietnam", "Malaysia", "Sri Lanka", "Bangladesh", "UAE"]
    },
    "paddy": {
        "season": "Kharif",  # Mainly Kharif, though some Rabi varieties exist
        "locations": ["West Bengal", "Punjab", "Uttar Pradesh", "Andhra Pradesh", "Tamil Nadu"],
        "exported_to": ["Bangladesh", "Saudi Arabia", "Iran", "Nepal", "UAE"]
    },
    "ragi": {
        "season": "Kharif",
        "locations": ["Karnataka", "Tamil Nadu", "Andhra Pradesh", "Odisha", "Maharashtra"],
        "exported_to": ["USA", "UK", "Germany", "Australia"]
    },
    "wheat": {
        "season": "Rabi",
        "locations": ["Punjab", "Haryana", "Uttar Pradesh", "Madhya Pradesh", "Bihar"],
        "exported_to": ["Bangladesh", "Sri Lanka", "UAE", "Indonesia", "Afghanistan"]
    },
    "betelnut_arceanut": {
        "season": "Perennial",
        "locations": ["Karnataka", "Kerala", "Assam", "Tamil Nadu", "Meghalaya"],
        "exported_to": ["Nepal", "Pakistan", "Bangladesh", "UAE"]
    },
    "black_pepper": {
        "season": "Perennial",
        "locations": ["Kerala", "Karnataka", "Tamil Nadu"],
        "exported_to": ["USA", "Germany", "UK", "Vietnam", "UAE"]
    },
    "cardamom": {
        "season": "Perennial",
        "locations": ["Kerala", "Karnataka", "Tamil Nadu"],
        "exported_to": ["Saudi Arabia", "UAE", "Kuwait", "Qatar", "Japan"]
    },
    "chillies_dry": {
        "season": "Both",
        "locations": ["Andhra Pradesh", "Telangana", "Madhya Pradesh", "Karnataka", "Odisha"],
        "exported_to": ["Vietnam", "Thailand", "Sri Lanka", "Bangladesh", "USA"]
    },
    "coriander": {
        "season": "Rabi",
        "locations": ["Rajasthan", "Madhya Pradesh", "Gujarat", "Uttar Pradesh", "Tamil Nadu"],
        "exported_to": ["Malaysia", "Pakistan", "Bangladesh", "UAE", "UK"]
    },
    "cumin": {
        "season": "Rabi",
        "locations": ["Rajasthan", "Gujarat"],
        "exported_to": ["Vietnam", "USA", "Bangladesh", "UAE", "UK"]
    },
    "garlic": {
        "season": "Rabi",
        "locations": ["Madhya Pradesh", "Gujarat", "Uttar Pradesh", "Rajasthan", "Odisha"],
        "exported_to": ["Bangladesh", "Nepal", "Malaysia", "Sri Lanka", "UAE"]
    },
    "ginger_dry": {
        "season": "Kharif",
        "locations": ["Kerala", "Karnataka", "Orissa", "Assam", "Meghalaya"],
        "exported_to": ["USA", "UK", "Netherlands", "Saudi Arabia", "UAE"]
    },
    "tamarind": {
        "season": "Perennial",
        "locations": ["Tamil Nadu", "Maharashtra", "Karnataka", "Andhra Pradesh", "Odisha"],
        "exported_to": ["USA", "UK", "UAE", "Saudi Arabia", "Germany"]
    },
    "turmeric": {
        "season": "Kharif",
        "locations": ["Telangana", "Andhra Pradesh", "Tamil Nadu", "Odisha", "Maharashtra"],
        "exported_to": ["UAE", "USA", "Iran", "Japan", "Malaysia"]
    },
    "coir_fibre": {
        "season": "Perennial",
        "locations": ["Kerala", "Tamil Nadu", "Karnataka", "Andhra Pradesh", "Odisha"],
        "exported_to": ["USA", "UK", "Germany", "Netherlands", "Australia"]
    },
    "mesta": {
        "season": "Kharif",
        "locations": ["West Bengal", "Bihar", "Assam", "Andhra Pradesh", "Odisha"],
        "exported_to": ["Nepal", "Bangladesh", "Thailand", "Vietnam", "Philippines"]
    },
    "raw_cotton": {
        "season": "Kharif",
        "locations": ["Gujarat", "Maharashtra", "Telangana", "Andhra Pradesh", "Punjab"],
        "exported_to": ["Bangladesh", "China", "Vietnam", "Pakistan", "Indonesia"]
    },
    "raw_jute": {
        "season": "Kharif",
        "locations": ["West Bengal", "Bihar", "Assam", "Meghalaya", "Odisha"],
        "exported_to": ["Nepal", "Bangladesh", "UK", "USA", "Australia"]
    },
    "raw_silk": {
        "season": "Perennial",
        "locations": ["Karnataka", "West Bengal", "Jammu & Kashmir", "Tamil Nadu", "Assam"],
        "exported_to": ["USA", "UK", "Italy", "France", "Germany"]
    },
    
        "raw_wool": {
        "season": "Perennial",
        "locations": ["Rajasthan", "Jammu & Kashmir", "Himachal Pradesh", "Uttarakhand", "Gujarat"],
        "exported_to": ["UK", "Italy", "Germany", "China", "USA"]
    },
    "jasmine": {
        "season": "Perennial",
        "locations": ["Tamil Nadu", "Karnataka", "Andhra Pradesh", "West Bengal"],
        "exported_to": ["UAE", "Saudi Arabia", "USA", "Singapore"]
    },
    "marigold": {
        "season": "Both",
        "locations": ["Karnataka", "Tamil Nadu", "West Bengal", "Maharashtra", "Andhra Pradesh"],
        "exported_to": ["Nepal", "Malaysia", "Sri Lanka"]
    },
    "rose": {
        "season": "Perennial",
        "locations": ["Maharashtra", "Karnataka", "Tamil Nadu", "West Bengal", "Uttar Pradesh"],
        "exported_to": ["UAE", "Saudi Arabia", "Netherlands", "Germany"]
    },
    "almonds": {
        "season": "Perennial",
        "locations": ["Jammu & Kashmir", "Himachal Pradesh"],
        "exported_to": ["UAE", "Saudi Arabia", "Nepal"]
    },
    "amla": {
        "season": "Perennial",
        "locations": ["Uttar Pradesh", "Madhya Pradesh", "Bihar", "Rajasthan", "Tamil Nadu"],
        "exported_to": ["USA", "UK", "Bangladesh", "Nepal"]
    },
    "apple": {
        "season": "Perennial",
        "locations": ["Jammu & Kashmir", "Himachal Pradesh", "Uttarakhand"],
        "exported_to": ["Nepal", "Bangladesh", "UAE", "Saudi Arabia"]
    },
    "banana": {
        "season": "Perennial",
        "locations": ["Tamil Nadu", "Maharashtra", "Gujarat", "Andhra Pradesh", "Karnataka"],
        "exported_to": ["UAE", "Saudi Arabia", "Oman", "Iran", "Bangladesh"]
    },
    "cashew_nut": {
        "season": "Perennial",
        "locations": ["Kerala", "Karnataka", "Goa", "Maharashtra", "Odisha"],
        "exported_to": ["UAE", "USA", "Japan", "Netherlands", "UK"]
    },
    "coconut_fresh": {
        "season": "Perennial",
        "locations": ["Kerala", "Tamil Nadu", "Karnataka", "Andhra Pradesh"],
        "exported_to": ["UAE", "Saudi Arabia", "Malaysia", "Sri Lanka"]
    },
    "grapes": {
        "season": "Perennial",
        "locations": ["Maharashtra", "Karnataka", "Andhra Pradesh", "Tamil Nadu"],
        "exported_to": ["Netherlands", "Russia", "UK", "UAE", "Bangladesh"]
    },
    "guava": {
        "season": "Perennial",
        "locations": ["Uttar Pradesh", "Bihar", "Maharashtra", "Tamil Nadu", "Andhra Pradesh"],
        "exported_to": ["UAE", "Nepal", "Bangladesh", "Saudi Arabia"]
    },
    "jackfruit": {
        "season": "Perennial",
        "locations": ["Kerala", "Tamil Nadu", "Assam", "West Bengal", "Karnataka"],
        "exported_to": ["UK", "USA", "Germany", "Singapore"]
    },
    "lemon": {
        "season": "Perennial",
        "locations": ["Andhra Pradesh", "Tamil Nadu", "Maharashtra", "Gujarat", "Rajasthan"],
        "exported_to": ["UAE", "Bangladesh", "Nepal", "Sri Lanka"]
    },
    "sweet_orange": {
        "season": "Perennial",
        "locations": ["Maharashtra", "Andhra Pradesh", "Punjab", "Karnataka"],
        "exported_to": ["Bangladesh", "Nepal", "UAE", "Sri Lanka"]
    },
    "orange": {
        "season": "Perennial",
        "locations": ["Maharashtra (Nagpur)", "Punjab", "Madhya Pradesh"],
        "exported_to": ["Bangladesh", "UAE", "Sri Lanka", "Nepal"]
    },
    "papaya": {
        "season": "Perennial",
        "locations": ["Andhra Pradesh", "Karnataka", "Maharashtra", "Gujarat", "West Bengal"],
        "exported_to": ["UAE", "Qatar", "Nepal", "Saudi Arabia"]
    },
    "pear": {
        "season": "Perennial",
        "locations": ["Jammu & Kashmir", "Himachal Pradesh", "Uttarakhand"],
        "exported_to": ["Nepal", "Bangladesh", "UAE"]
    },
    "pineapple": {
        "season": "Perennial",
        "locations": ["West Bengal", "Assam", "Kerala", "Tripura", "Meghalaya"],
        "exported_to": ["UAE", "Qatar", "Saudi Arabia", "Nepal"]
    },
    "pomengranate": {
        "season": "Perennial",
        "locations": ["Maharashtra", "Karnataka", "Andhra Pradesh", "Tamil Nadu", "Gujarat"],
        "exported_to": ["Bangladesh", "UAE", "Saudi Arabia", "Netherlands"]
    },
    "sapota": {
        "season": "Perennial",
        "locations": ["Karnataka", "Gujarat", "Maharashtra", "Tamil Nadu", "Andhra Pradesh"],
        "exported_to": ["UAE", "Saudi Arabia", "Bangladesh"]
    },
    "walnut": {
        "season": "Perennial",
        "locations": ["Jammu & Kashmir", "Himachal Pradesh", "Uttarakhand"],
        "exported_to": ["USA", "UK", "Germany", "UAE"]
    },

        "fodder": {
        "season": "Both",
        "locations": ["Punjab", "Haryana", "Uttar Pradesh", "Maharashtra", "Rajasthan"],
        "exported_to": ["Nepal", "Bangladesh"]
    },
    "gaur_seed": {
        "season": "Kharif",
        "locations": ["Rajasthan", "Gujarat", "Haryana"],
        "exported_to": ["USA", "Germany", "China", "Japan"]
    },
    "industrial_wood": {
        "season": "Perennial",
        "locations": ["Andhra Pradesh", "Telangana", "Odisha", "Madhya Pradesh"],
        "exported_to": ["Nepal", "Bangladesh", "Sri Lanka"]
    },
    "raw_rubber": {
        "season": "Perennial",
        "locations": ["Kerala", "Tripura", "Karnataka", "Tamil Nadu", "Assam"],
        "exported_to": ["USA", "Germany", "Japan", "Sri Lanka"]
    },
    "tobacco": {
        "season": "Both",
        "locations": ["Andhra Pradesh", "Karnataka", "Telangana", "Gujarat"],
        "exported_to": ["Belgium", "Egypt", "Russia", "Indonesia", "USA"]
    },
    "castor_seed": {
        "season": "Both",
        "locations": ["Gujarat", "Rajasthan", "Andhra Pradesh"],
        "exported_to": ["China", "Thailand", "USA", "Netherlands"]
    },
    "copra_coconut": {
        "season": "Perennial",
        "locations": ["Kerala", "Tamil Nadu", "Karnataka", "Andhra Pradesh"],
        "exported_to": ["USA", "UK", "Germany", "Malaysia", "Sri Lanka"]
    },
    "cotton_seed": {
        "season": "Kharif",
        "locations": ["Gujarat", "Maharashtra", "Punjab", "Haryana", "Telangana"],
        "exported_to": ["Bangladesh", "Vietnam", "Pakistan", "China"]
    },
    "gingelly_seed_sesamum": {
        "season": "Kharif",
        "locations": ["Uttar Pradesh", "Rajasthan", "Madhya Pradesh", "Tamil Nadu", "Andhra Pradesh"],
        "exported_to": ["Japan", "South Korea", "USA", "Vietnam"]
    },
    "groundnut_seed": {
        "season": "Kharif",
        "locations": ["Gujarat", "Andhra Pradesh", "Tamil Nadu", "Maharashtra", "Karnataka"],
        "exported_to": ["Indonesia", "Vietnam", "Philippines", "Malaysia"]
    },
    "linseed": {
        "season": "Rabi",
        "locations": ["Madhya Pradesh", "Uttar Pradesh", "Chhattisgarh", "Bihar"],
        "exported_to": ["Nepal", "Bangladesh"]
    },
    "niger_seed": {
        "season": "Kharif",
        "locations": ["Odisha", "Chhattisgarh", "Andhra Pradesh", "Madhya Pradesh"],
        "exported_to": ["USA", "UK", "Germany"]
    },
    "rape_mustard_seed": {
        "season": "Rabi",
        "locations": ["Rajasthan", "Uttar Pradesh", "Haryana", "Madhya Pradesh"],
        "exported_to": ["Nepal", "Bangladesh", "UAE"]
    },
    "safflower_kardi_seed": {
        "season": "Rabi",
        "locations": ["Maharashtra", "Karnataka", "Andhra Pradesh"],
        "exported_to": ["USA", "Germany", "UK"]
    },
    "soyabean": {
        "season": "Kharif",
        "locations": ["Madhya Pradesh", "Maharashtra", "Rajasthan"],
        "exported_to": ["Iran", "Bangladesh", "Vietnam", "Thailand", "Nepal"]
    },
    "sunflower": {
        "season": "Both",
        "locations": ["Karnataka", "Andhra Pradesh", "Maharashtra", "Punjab"],
        "exported_to": ["Nepal", "Bangladesh", "UAE"]
    },
    "betel_leaves": {
        "season": "Perennial",
        "locations": ["West Bengal", "Odisha", "Tamil Nadu", "Andhra Pradesh"],
        "exported_to": ["UK", "USA", "Singapore", "UAE"]
    },
    "coffee": {
        "season": "Perennial",
        "locations": ["Karnataka", "Kerala", "Tamil Nadu"],
        "exported_to": ["Italy", "Germany", "Russia", "Belgium", "USA"]
    },
    "honey": {
        "season": "Perennial",
        "locations": ["Punjab", "Haryana", "West Bengal", "Bihar", "Uttar Pradesh"],
        "exported_to": ["USA", "Saudi Arabia", "UAE", "Bangladesh"]
    },
    "sugarcane": {
        "season": "Perennial",
        "locations": ["Uttar Pradesh", "Maharashtra", "Karnataka", "Tamil Nadu", "Bihar"],
        "exported_to": ["Sri Lanka", "Nepal", "Bangladesh", "Indonesia"]
    },
    "tea": {
        "season": "Perennial",
        "locations": ["Assam", "West Bengal", "Tamil Nadu", "Kerala"],
        "exported_to": ["Russia", "Iran", "UK", "USA", "UAE"]
    },
    "arhar": {
        "season": "Kharif",
        "locations": ["Maharashtra", "Karnataka", "Uttar Pradesh", "Madhya Pradesh"],
        "exported_to": ["Sri Lanka", "Bangladesh", "Nepal"]
    },
    "gram": {
        "season": "Rabi",
        "locations": ["Madhya Pradesh", "Maharashtra", "Rajasthan", "Uttar Pradesh"],
        "exported_to": ["Bangladesh", "Nepal", "Pakistan"]
    },
    "masur": {
        "season": "Rabi",
        "locations": ["Uttar Pradesh", "Madhya Pradesh", "Bihar", "West Bengal"],
        "exported_to": ["Bangladesh", "Nepal"]
    },
    "moong": {
        "season": "Kharif",
        "locations": ["Rajasthan", "Maharashtra", "Karnataka", "Andhra Pradesh"],
        "exported_to": ["Bangladesh", "Nepal", "Sri Lanka"]
    },
    "peas_chawali": {
        "season": "Rabi",
        "locations": ["Uttar Pradesh", "Madhya Pradesh", "Bihar", "West Bengal"],
        "exported_to": ["Nepal", "Bangladesh"]
    },
    "rajma": {
        "season": "Kharif",
        "locations": ["Jammu & Kashmir", "Uttarakhand", "Himachal Pradesh"],
        "exported_to": ["USA", "UK", "UAE"]
    },
    "urad": {
        "season": "Kharif",
        "locations": ["Maharashtra", "Andhra Pradesh", "Madhya Pradesh", "Tamil Nadu"],
        "exported_to": ["Nepal", "Bangladesh", "Sri Lanka"]
    },
    "cotton_yarn": {
        "season": "Perennial",
        "locations": ["Tamil Nadu", "Gujarat", "Maharashtra", "Punjab"],
        "exported_to": ["China", "Bangladesh", "Vietnam", "Sri Lanka"]
    },
    "woollen_yarn": {
        "season": "Perennial",
        "locations": ["Rajasthan", "Punjab", "Uttar Pradesh", "Himachal Pradesh"],
        "exported_to": ["USA", "UK", "Germany"]
    },
    "beans": {
        "season": "Rabi",
        "locations": ["Karnataka", "Maharashtra", "Himachal Pradesh"],
        "exported_to": ["UAE", "UK", "Bangladesh"]
    },
    "bittergourd": {
        "season": "Kharif",
        "locations": ["Uttar Pradesh", "Maharashtra", "West Bengal"],
        "exported_to": ["UAE", "UK", "Malaysia"]
    },
    "bottlegourd": {
        "season": "Kharif",
        "locations": ["Uttar Pradesh", "Bihar", "West Bengal"],
        "exported_to": ["UAE", "Nepal", "Bangladesh"]
    },
    "brinjal": {
        "season": "Both",
        "locations": ["West Bengal", "Odisha", "Bihar", "Maharashtra"],
        "exported_to": ["Nepal", "Bangladesh", "UAE"]
    },
    "cabbage": {
        "season": "Rabi",
        "locations": ["West Bengal", "Bihar", "Odisha", "Karnataka"],
        "exported_to": ["Nepal", "Bangladesh", "UAE"]
    },
    "carrot": {
        "season": "Rabi",
        "locations": ["Punjab", "Haryana", "Karnataka", "Uttar Pradesh"],
        "exported_to": ["UAE", "Qatar", "Nepal"]
    },
    "cauliflower": {
        "season": "Rabi",
        "locations": ["West Bengal", "Bihar", "Uttar Pradesh"],
        "exported_to": ["Nepal", "Bangladesh"]
    },
    "cucumber": {
        "season": "Kharif",
        "locations": ["Uttar Pradesh", "Punjab", "Haryana"],
        "exported_to": ["UAE", "Oman"]
    },
    "drumstick": {
        "season": "Perennial",
        "locations": ["Tamil Nadu", "Andhra Pradesh", "Karnataka"],
        "exported_to": ["USA", "UK", "Malaysia", "Singapore"]
    },
    "gingerfresh": {
        "season": "Kharif",
        "locations": ["Kerala", "Karnataka", "Assam", "Meghalaya"],
        "exported_to": ["USA", "UK", "Germany"]
    },
    "ladyfinger": {
        "season": "Kharif",
        "locations": ["Uttar Pradesh", "West Bengal", "Bihar"],
        "exported_to": ["UAE", "UK", "Saudi Arabia"]
    },
    "onion": {
        "season": "Rabi",
        "locations": ["Maharashtra", "Karnataka", "Madhya Pradesh", "Gujarat"],
        "exported_to": ["Bangladesh", "Malaysia", "Sri Lanka", "UAE"]
    },
    "peasgreen": {
        "season": "Rabi",
        "locations": ["Uttar Pradesh", "Bihar", "Madhya Pradesh"],
        "exported_to": ["Nepal", "UAE", "Bangladesh"]
    },
    "pointedgourd": {
        "season": "Kharif",
        "locations": ["West Bengal", "Bihar", "Assam"],
        "exported_to": ["Nepal", "Bangladesh"]
    },
    "potato": {
        "season": "Rabi",
        "locations": ["Uttar Pradesh", "West Bengal", "Bihar", "Punjab"],
        "exported_to": ["Nepal", "Sri Lanka", "Bangladesh", "UAE"]
    },
    "pumpkin": {
        "season": "Kharif",
        "locations": ["West Bengal", "Odisha", "Bihar", "Uttar Pradesh"],
        "exported_to": ["Nepal", "Bangladesh"]
    },
    "radish": {
        "season": "Rabi",
        "locations": ["Punjab", "Haryana", "Uttar Pradesh", "West Bengal"],
        "exported_to": ["UAE", "Qatar"]
    },
    "sweetpotato": {
        "season": "Kharif",
        "locations": ["Odisha", "Uttar Pradesh", "West Bengal"],
        "exported_to": ["Nepal", "Bangladesh"]
    },
    "tapioca": {
        "season": "Perennial",
        "locations": ["Kerala", "Tamil Nadu", "Andhra Pradesh"],
        "exported_to": ["USA", "UK", "Malaysia"]
    },
    "tomato": {
        "season": "Both",
        "locations": ["Andhra Pradesh", "Karnataka", "Maharashtra", "Odisha"],
        "exported_to": ["UAE", "Sri Lanka", "Nepal", "Bangladesh"]
    }
}


with open("commodity_data.csv", "w", newline='', encoding='utf-8') as csvfile:
    fieldnames = ["commodity", "locations", "season", "exported_to"]
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    # Write header
    writer.writerow(fieldnames)

    for commodity, info in commodity_info.items():
        row = [
            commodity,
            ", ".join(info["locations"]),
            info["season"],
            ", ".join(info["exported_to"])
        ]
        writer.writerow(row)

print("CSV file generated with simple double quotes around each value.")