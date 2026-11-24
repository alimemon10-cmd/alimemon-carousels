import json
from pathlib import Path


def close(text, btn):
    return {"t": "close", "text": text, "btn": btn}


D = []

D.append(dict(day=11, date="2026-11-25", folder="day11", art="history", slides=[
    {"t": "cover", "tag": "UAE HISTORY", "title": "How the UAE was born:", "gold": "from Trucial States to one nation", "sub": "The story behind 2 December 1971."},
    {"t": "stat", "num": "1820", "label": "The Trucial States", "head": "Treaties at sea", "bullets": [
        "Britain signed maritime truces with the coastal sheikhdoms from 1820.",
        "The 1853 Perpetual Truce gave them the name Trucial States.",
        "From 1892, foreign affairs ran through Britain."]},
    {"t": "stat", "num": "1958", "label": "Oil", "head": "The discovery that changed everything", "bullets": [
        "Oil struck offshore at Umm Shaif, Abu Dhabi, in 1958.",
        "Abu Dhabi's first export left Das Island in 1962.",
        "Dubai found the Fateh field in 1966 and exported from 1969."]},
    {"t": "stat", "num": "1968", "label": "The handshake", "head": "A union is agreed", "bullets": [
        "In January 1968, Britain said it would leave the Gulf by 1971.",
        "On 18 February 1968, Sheikh Zayed and Sheikh Rashid agreed to unite.",
        "They invited the other rulers to join them."]},
    {"t": "stat", "num": "1971", "label": "2 December", "head": "Six emirates become one", "bullets": [
        "The UAE was declared at Union House, Dubai.",
        "Abu Dhabi, Dubai, Sharjah, Ajman, Umm Al Quwain and Fujairah.",
        "Ras Al Khaimah joined on 10 February 1972, making seven."]},
    {"t": "stat", "num": "55", "label": "Years later", "head": "From pearl diving to Mars", "bullets": [
        "Expo 2020 Dubai drew over 24 million visits.",
        "The Hope Probe reached Mars orbit in 2021.",
        "Barakah now supplies up to a quarter of the UAE's electricity."]},
    close("55 years from union to global city. Thinking about putting down roots here? I'll walk you through it.", 'DM "UAE" TO START'),
],
    caption="How the UAE was born 🇦🇪 From the Trucial States and the 1968 handshake to 2 December 1971, in 7 slides.\n\nSave it and share it with someone new to the UAE.\n\nDM \"UAE\" if you're thinking of putting down roots here.\n\n#UAE #UAEHistory #EidAlEtihad #DubaiRealEstate #AbuDhabi",
    linkedin_caption="In 1968, the Trucial States were a set of small sheikhdoms under British protection, with oil only just starting to flow. Three years later they were one country.\n\nA short history of how the UAE came together: the maritime truces of the 1800s, the oil discoveries of 1958 and 1966, the February 1968 agreement between Sheikh Zayed and Sheikh Rashid, and the declaration of the union on 2 December 1971.\n\n55 years on, it's worth remembering how recent and how deliberate all of this was."))

D.append(dict(day=12, date="2026-11-26", folder="day12", art="rehistory", slides=[
    {"t": "cover", "tag": "MARKET HISTORY", "title": "Dubai real estate:", "gold": "from 2002 to a record year", "sub": "How the market went from leasehold-only to AED 917bn."},
    {"t": "stat", "num": "2002", "label": "Freehold", "head": "The door opens", "bullets": [
        "Before 2002, foreigners could only lease, for up to 99 years.",
        "From May 2002, expats could buy freehold in Dubai.",
        "Emirates Hills, Arabian Ranches and Dubai Marina led the way."]},
    {"t": "stat", "num": "2006", "label": "The rulebook", "head": "Laws that protect buyers", "bullets": [
        "Law No. 7 of 2006 made property registration mandatory.",
        "2007: escrow accounts became law for off-plan projects.",
        "2007: RERA was set up to regulate the market."]},
    {"t": "stat", "num": "~60%", "label": "2008 to 2009", "head": "The crash", "bullets": [
        "Prices fell by up to around 60% from the peak.",
        "Many projects stalled or were cancelled.",
        "The escrow and RERA rules shaped the stronger market that followed."]},
    {"t": "stat", "num": "2019", "label": "New doors", "head": "Visas and a wider market", "bullets": [
        "Golden visas launched in 2019. Property worth AED 2M or more can now qualify.",
        "Abu Dhabi opened freehold in investment zones the same year.",
        "Expo 2020, won in 2013, put Dubai on the world stage."]},
    {"t": "stat", "num": "917", "label": "AED billion in 2025", "head": "A record year", "bullets": [
        "Over 270,000 Dubai property transactions in 2025.",
        "Value up 20% on 2024's AED 761bn.",
        "129,600 first-time investors entered the market."]},
    close("24 years from the first freehold sale to a record year. Want to know where the next chapter is? Let's talk.", 'DM "HISTORY" TO CHAT'),
],
    caption="Dubai real estate in 24 years 📈 2002 freehold, the 2008 crash, golden visas and a record AED 917bn in 2025.\n\nSave this for context the next time someone calls it a bubble.\n\nDM \"HISTORY\" to talk about where the market goes next.\n\n#DubaiRealEstate #DubaiProperty #UAE #InvestInDubai #DubaiHistory",
    linkedin_caption="Until 2002, a foreigner couldn't own a freehold home in Dubai. In 2025 the market recorded more than 270,000 transactions worth AED 917bn.\n\nWhat happened in between matters: the 2006 registration law, escrow and RERA in 2007, the 2008-09 correction, golden visas in 2019, and the run of records since.\n\nThe rules written after the crash are a big part of why today's market looks so different from 2008."))

D.append(dict(day=13, date="2026-11-27", folder="day13", art="metro", slides=[
    {"t": "cover", "tag": "INFRASTRUCTURE", "title": "Dubai Metro:", "gold": "today's lines and what's next", "sub": "Red, Green, Blue and the new Gold Line."},
    {"t": "stat", "num": "2", "label": "Lines today", "head": "The network now", "bullets": [
        "Red Line, open since 2009: 35 stations, including the branch to Expo City.",
        "Green Line, open since 2011: 20 stations.",
        "About 90 km in total, plus the Dubai Tram."]},
    {"t": "stat", "num": "295M", "label": "Metro trips in 2025", "head": "How busy it is", "bullets": [
        "294.7 million metro trips in 2025, up 7%.",
        "About 1 in 3 of all public transport trips in Dubai.",
        "Busiest station: BurJuman, with 17.8 million riders."]},
    {"t": "stat", "num": "2029", "label": "Blue Line", "head": "Opening 9 September 2029", "bullets": [
        "30 km and 14 stations, about 30% built.",
        "Mirdif, Al Warqa, International City, Silicon Oasis and Academic City.",
        "Plus Dubai Creek Harbour and Festival City."]},
    {"t": "stat", "num": "2032", "label": "Gold Line", "head": "Approved in April 2026", "bullets": [
        "42 km, fully underground, 18 stations.",
        "Al Ghubaiba to Jumeirah Golf Estates via Business Bay, Meydan and JVC.",
        "Due to open on 9 September 2032."]},
    {"t": "stat", "num": "140", "label": "Stations by 2040", "head": "Why it matters", "bullets": [
        "Dubai's 2040 plan targets 140 metro stations.",
        "RTA says property near Gold Line stations could gain up to 20% in value.",
        "The time to buy near a line is before it opens."]},
    close("Want options near the Blue Line or Gold Line before they open? I'll show you what's available at your budget.", 'DM "METRO" FOR OPTIONS'),
],
    caption="Dubai Metro: every line now and every line coming 🚇 Red, Green, the Blue Line in 2029 and the new 42 km Gold Line in 2032.\n\nSave it for the next time you're comparing areas.\n\nDM \"METRO\" for homes near the new stations.\n\n#DubaiMetro #GoldLine #BlueLine #DubaiRealEstate #DubaiProperty",
    linkedin_caption="Dubai Metro carried 294.7 million trips in 2025, and the network is about to grow fast.\n\nThe Blue Line (30 km, 14 stations) opens in September 2029 and is already about 30% built. The Gold Line, approved in April 2026, adds 42 km underground from Al Ghubaiba to Jumeirah Golf Estates via Business Bay, Meydan and JVC, opening in 2032.\n\nRTA itself estimates property near Gold Line stations could rise by up to 20%. Infrastructure usually gets priced in before the ribbon is cut."))

D.append(dict(day=14, date="2026-11-28", folder="day14", art="rail", slides=[
    {"t": "cover", "tag": "INFRASTRUCTURE", "title": "Etihad Rail:", "gold": "the UAE by train", "sub": "Abu Dhabi to Dubai in about 57 minutes."},
    {"t": "stat", "num": "900", "label": "Kilometres", "head": "One network, seven emirates", "bullets": [
        "Runs from Ghuweifat on the Saudi border to Fujairah.",
        "Freight began on the first 264 km in 2016.",
        "The full freight network has run since 2023."]},
    {"t": "stat", "num": "2026", "label": "Passenger trains", "head": "Now carrying passengers", "bullets": [
        "Passenger service launched on 30 June 2026.",
        "Dubai's Al Yalayis station opened on 30 September 2026.",
        "Trains reach 200 km/h and carry up to 400 people."]},
    {"t": "stat", "num": "57", "label": "Minutes", "head": "Journey times", "bullets": [
        "Abu Dhabi to Dubai: about 57 min, fares from AED 39.",
        "Dubai to Fujairah: about 70 min.",
        "Abu Dhabi to Fujairah: about 1 hr 45 min."]},
    {"t": "stat", "num": "11", "label": "Cities and regions", "head": "Where it goes", "bullets": [
        "Open now: Abu Dhabi, Dubai, Fujairah and Al Dhaid.",
        "More Al Dhafra stations and Sharjah are rolling out through 2026 and 2027.",
        "Dubai's station links to Jumeirah Golf Estates metro."]},
    {"t": "stat", "num": "30", "label": "Minutes, high-speed", "head": "What's next", "bullets": [
        "A new high-speed line: Abu Dhabi to Dubai in about 30 min.",
        "Stations include Saadiyat, Yas, Abu Dhabi Airport and Al Jaddaf.",
        "Works are due to finish around 2030."]},
    close("Rail is redrawing the commute map. Want to see the communities closest to the new stations?", 'DM "RAIL" FOR OPTIONS'),
],
    caption="Etihad Rail is here 🚆 Abu Dhabi to Dubai in about 57 minutes from AED 39, and a 30-minute high-speed line on the way.\n\nSave it and tag someone who commutes between the two.\n\nDM \"RAIL\" for homes near the stations.\n\n#EtihadRail #UAE #Dubai #AbuDhabi #DubaiRealEstate",
    linkedin_caption="Since 30 June 2026 you can take a passenger train across the UAE. Abu Dhabi to Dubai takes about 57 minutes, with fares from AED 39, and Dubai's Al Yalayis station connects to the metro at Jumeirah Golf Estates.\n\nNext up is a dedicated high-speed line cutting Abu Dhabi to Dubai to about 30 minutes, with stations planned at Saadiyat, Yas, Abu Dhabi Airport and Al Jaddaf.\n\nWhen a two-city commute becomes a 30-minute ride, it changes where people choose to live."))

D.append(dict(day=15, date="2026-11-29", folder="day15", art="abudhabi", slides=[
    {"t": "cover", "tag": "ABU DHABI", "title": "Abu Dhabi real estate:", "gold": "the capital's breakout year", "sub": "AED 171bn in nine months, already past all of 2025."},
    {"t": "stat", "num": "142", "label": "AED billion in 2025", "head": "A record year", "bullets": [
        "Up 44% on 2024.",
        "42,814 transactions, up 52%.",
        "Buyers from more than 100 nationalities."]},
    {"t": "stat", "num": "171", "label": "AED billion, Jan to Sep 2026", "head": "And 2026 is bigger", "bullets": [
        "Up 76% on the same period last year.",
        "Sales alone: AED 119bn, more than double.",
        "Buyers from 121 nationalities."]},
    {"t": "bars", "label": "Jan to Sep 2026, by value", "head": "Where the money went", "bars": [
        ["Al Reem Island", 29.86, "AED 29.9bn"], ["Al Hudayriyat", 28.62, "AED 28.6bn"], ["Saadiyat Island", 18.69, "AED 18.7bn"],
        ["Yas Island", 13.4, "AED 13.4bn"], ["Zayed City", 5.36, "AED 5.4bn"]],
     "note": "Source: Abu Dhabi Real Estate Centre (ADREC)."},
    {"t": "stat", "num": "2019", "label": "Freehold for foreigners", "head": "Who can buy", "bullets": [
        "Since 2019, foreigners can own freehold in investment zones.",
        "There are now 50 investment zones.",
        "Foreign buyers made up 62% of residential sales value in 2025."]},
    {"t": "stat", "num": "+19%", "label": "Apartment prices in 2025", "head": "Demand beats supply", "bullets": [
        "Apartment prices rose 19% and villas 13% in 2025.",
        "New apartment rents were up 16%.",
        "Occupied homes have grown 6.6% a year since 2022, against 2.8% new supply."]},
    close("Looking at Abu Dhabi as well as Dubai? I'll compare both for your budget and goals.", 'DM "ABU DHABI" TO COMPARE'),
],
    caption="Abu Dhabi real estate just had its biggest year ever, in nine months 🏙️ AED 171bn from January to September 2026, up 76%.\n\nSave it if you're weighing Abu Dhabi against Dubai.\n\nDM \"ABU DHABI\" for a side-by-side comparison.\n\n#AbuDhabiRealEstate #AbuDhabi #SaadiyatIsland #YasIsland #AlReemIsland",
    linkedin_caption="Abu Dhabi recorded AED 171bn of real estate transactions in the first nine months of 2026, more than the whole of record-breaking 2025 (AED 142bn).\n\nAl Reem, Al Hudayriyat, Saadiyat and Yas led by value. Foreign buyers made up 62% of residential sales value last year, and apartment prices rose 19%.\n\nFor a long time Abu Dhabi was Dubai's quieter neighbour. The numbers say that's changing."))

D.append(dict(day=16, date="2026-11-30", folder="day16", art="culture", slides=[
    {"t": "cover", "tag": "ABU DHABI", "title": "Saadiyat and Yas:", "gold": "what's open and what's coming", "sub": "The Guggenheim opens on 11 December."},
    {"t": "stat", "num": "2017", "label": "Louvre Abu Dhabi", "head": "Where it started", "bullets": [
        "Opened in November 2017, designed by Jean Nouvel.",
        "More than 5 million visitors by 2024.",
        "The first of Saadiyat's big museums."]},
    {"t": "stat", "num": "2025", "label": "Three openings", "head": "A big year for Saadiyat", "bullets": [
        "teamLab Phenomena Abu Dhabi, April 2025.",
        "Natural History Museum Abu Dhabi, November 2025.",
        "Zayed National Museum by Foster + Partners, December 2025."]},
    {"t": "stat", "num": "11 DEC", "label": "Guggenheim Abu Dhabi", "head": "Opening in December", "bullets": [
        "Frank Gehry's design opens on 11 December 2026.",
        "30 galleries, with cones rising up to 88 m.",
        "The fourth Guggenheim, after New York, Venice and Bilbao."]},
    {"t": "stat", "num": "7th", "label": "Disney resort", "head": "Disneyland Abu Dhabi", "bullets": [
        "Planned for Yas Island, developed with Miral.",
        "Disney's first theme park in the Middle East.",
        "No opening date yet. Disney is planning on years of design and construction."]},
    {"t": "stat", "num": "2029", "label": "More on Yas", "head": "The pipeline keeps growing", "bullets": [
        "Sphere Abu Dhabi, a USD 1.7bn venue, due by end-2029.",
        "A Harry Potter area at Warner Bros. World, set for 2029.",
        "Miral plans AED 12bn more on Yas hotels and attractions."]},
    close("Homes near world-class culture and theme parks hold their appeal. Want to see what's available on Saadiyat and Yas?", 'DM "SAADIYAT" FOR OPTIONS'),
],
    caption="Saadiyat and Yas: Abu Dhabi's culture and theme park capital 🏛️ Louvre, Zayed National Museum, the Guggenheim on 11 December, and Disneyland on the way.\n\nSave this for your next Abu Dhabi weekend.\n\nDM \"SAADIYAT\" for homes on Saadiyat and Yas.\n\n#SaadiyatIsland #YasIsland #GuggenheimAbuDhabi #DisneylandAbuDhabi #AbuDhabiRealEstate",
    linkedin_caption="In one year Saadiyat Cultural District added teamLab Phenomena, the Natural History Museum and the Zayed National Museum. On 11 December 2026, Frank Gehry's Guggenheim Abu Dhabi opens beside the Louvre.\n\nNext door on Yas, Disney is planning its first Middle East park with Miral, and Sphere Abu Dhabi is due by the end of 2029.\n\nThis kind of anchor investment tends to show up in demand for homes nearby long before the doors open."))

D.append(dict(day=17, date="2026-12-01", folder="day17", art="rulers", slides=[
    {"t": "cover", "tag": "LEADERSHIP", "title": "The seven rulers", "gold": "of the UAE", "sub": "Who leads each emirate, and since when."},
    {"t": "stat", "num": "7", "label": "Federal Supreme Council", "head": "How the UAE is led", "bullets": [
        "The seven rulers form the Federal Supreme Council, the UAE's highest authority.",
        "President: Sheikh Mohamed bin Zayed Al Nahyan, since 2022.",
        "Vice President and Prime Minister: Sheikh Mohammed bin Rashid Al Maktoum."]},
    {"t": "rulers", "label": "The rulers", "head": "Abu Dhabi, Dubai, Sharjah, Ajman", "items": [
        {"flag": "abudhabi", "emirate": "Abu Dhabi", "name": "Sheikh Mohamed bin Zayed Al Nahyan", "since": "Ruler since 2022"},
        {"flag": "dubai", "emirate": "Dubai", "name": "Sheikh Mohammed bin Rashid Al Maktoum", "since": "Ruler since 2006"},
        {"flag": "sharjah", "emirate": "Sharjah", "name": "Sheikh Dr Sultan bin Mohammed Al Qasimi", "since": "Ruler since 1972"},
        {"flag": "ajman", "emirate": "Ajman", "name": "Sheikh Humaid bin Rashid Al Nuaimi", "since": "Ruler since 1981"}]},
    {"t": "rulers", "label": "The rulers", "head": "Umm Al Quwain, Ras Al Khaimah, Fujairah", "items": [
        {"flag": "uaq", "emirate": "Umm Al Quwain", "name": "Sheikh Saud bin Rashid Al Mualla", "since": "Ruler since 2009"},
        {"flag": "rak", "emirate": "Ras Al Khaimah", "name": "Sheikh Saud bin Saqr Al Qasimi", "since": "Ruler since 2010"},
        {"flag": "fujairah", "emirate": "Fujairah", "name": "Sheikh Hamad bin Mohammed Al Sharqi", "since": "Ruler since 1974"}],
     "note": "Fujairah has flown the UAE flag since 1975."},
    {"t": "list", "label": "The next generation", "head": "Crown princes and deputies", "bullets": [
        "Crown Prince of Abu Dhabi: Sheikh Khaled bin Mohamed bin Zayed, since 2023.",
        "Crown Prince of Dubai: Sheikh Hamdan bin Mohammed bin Rashid, since 2008.",
        "Vice President: Sheikh Mansour bin Zayed Al Nahyan, since 2023."]},
    {"t": "stat", "num": "1972", "label": "Longest reign today", "head": "Sharjah's ruler", "bullets": [
        "Sheikh Dr Sultan bin Mohammed Al Qasimi has ruled Sharjah since January 1972.",
        "That's more than 54 years, the longest of the current rulers.",
        "Sharjah is known as the UAE's cultural capital."]},
    close("Seven emirates, one country. Whichever emirate you're looking at, I can help you find the right home.", 'DM "UAE" TO START'),
],
    caption="The seven rulers of the UAE 🇦🇪 Who leads each emirate, and since when, ahead of Eid Al Etihad.\n\nSave it and share it with someone who's new to the UAE.\n\n#UAE #EidAlEtihad #UAELeadership #SevenEmirates #DubaiRealEstate",
    linkedin_caption="Ahead of Eid Al Etihad, a quick guide to how the UAE is led.\n\nThe rulers of the seven emirates make up the Federal Supreme Council, the country's highest authority. Sheikh Mohamed bin Zayed is President and Ruler of Abu Dhabi. Sheikh Mohammed bin Rashid is Vice President, Prime Minister and Ruler of Dubai. Sheikh Dr Sultan bin Mohammed Al Qasimi has ruled Sharjah since 1972.\n\nUseful context for anyone new to the country, or anyone investing here."))

D.append(dict(day=18, date="2026-12-02", folder="day18", art="national", slides=[
    {"t": "cover", "tag": "EID AL ETIHAD", "title": "Happy 55th", "gold": "Eid Al Etihad", "sub": "2 December 1971 to 2 December 2026."},
    {"t": "stat", "num": "55", "label": "Years of union", "head": "What we celebrate today", "bullets": [
        "On 2 December 1971, six emirates united at Union House, Dubai.",
        "Ras Al Khaimah joined in February 1972.",
        "Eid Al Etihad means the Festival of the Union."]},
    {"t": "stat", "num": "19", "label": "Years old", "head": "The flag's designer", "bullets": [
        "Abdullah Mohammed Al Maainah designed the flag at 19.",
        "His design was picked from about 1,030 entries.",
        "Sheikh Zayed first raised it on 2 December 1971."]},
    {"t": "flag", "label": "Four colours", "head": "The UAE flag", "swatches": [
        ["#C8102E", "#fff", "Red", "Courage"], ["#00843D", "#fff", "Green", "Growth"],
        ["#ffffff", "#1b2838", "White", "Peace"], ["#111111", "#fff", "Black", "Strength"]],
     "note": "These are the meanings most often given. The colours are the pan-Arab colours."},
    {"t": "cal", "label": "The calendar", "head": "Three dates to know", "rows": [
        ["3", "NOV", "Flag Day", "Flags raised nationwide to mark the leadership."],
        ["30", "NOV", "Commemoration Day", "Honouring the nation's martyrs."],
        ["2", "DEC", "Eid Al Etihad", "Holiday: 2 to 3 Dec private sector, 2 to 4 Dec government."]]},
    {"t": "stat", "num": "2026", "label": "This year's theme", "head": "A family of families", "bullets": [
        "This year's celebrations centre on family, in the UAE's Year of Family.",
        "The official identity is inspired by a family photo album.",
        "Generations of Emiratis and residents, one home."]},
    close("Wishing everyone who calls the UAE home a happy Eid Al Etihad, from my family to yours.", "EID AL ETIHAD MUBARAK"),
],
    caption="Happy 55th Eid Al Etihad 🇦🇪 On 2 December 1971, six emirates became one nation. Here's the story of the day and the flag.\n\nEid Al Etihad Mubarak to everyone who calls the UAE home.\n\n#EidAlEtihad #UAENationalDay #UAE55 #UAE #Dubai",
    linkedin_caption="Today is the UAE's 55th Eid Al Etihad. On 2 December 1971, six emirates united at Union House in Dubai, and Ras Al Khaimah joined two months later.\n\nThe flag raised that day was designed by Abdullah Mohammed Al Maainah, aged 19, from about 1,030 entries. This year's celebrations centre on family, as part of the UAE's Year of Family.\n\nEid Al Etihad Mubarak to everyone who calls this country home."))

D.append(dict(day=19, date="2026-12-03", folder="day19", art="adgm", slides=[
    {"t": "cover", "tag": "FINANCE", "title": "Wall Street is", "gold": "moving to Al Maryah", "sub": "Why the world's biggest money managers chose ADGM."},
    {"t": "stat", "num": "2015", "label": "ADGM", "head": "Abu Dhabi's financial centre", "bullets": [
        "Abu Dhabi Global Market opened for business in 2015.",
        "It applies English common law and has its own courts and regulator.",
        "It now covers Al Maryah and Al Reem islands."]},
    {"t": "stat", "num": "13,974", "label": "Active licences, mid-2026", "head": "Growing fast", "bullets": [
        "Assets under management up 54% in a year.",
        "49,027 people work there, up 34%.",
        "190 asset managers running 276 funds."]},
    {"t": "chips", "label": "Who's here", "head": "Big names with an ADGM presence", "chips": [
        "BlackRock", "Blackstone", "J.P. Morgan", "Goldman Sachs", "Apollo", "KKR", "Brevan Howard", "Marshall Wace",
        "Man Group", "Capital Group", "Bain Capital", "Fortress"],
     "note": "Licensed or registered entities, per ADGM's public register and announcements."},
    {"t": "stat", "num": "60", "label": "AED billion", "head": "Al Maryah is expanding", "bullets": [
        "Mubadala and Aldar's north Al Maryah expansion: AED 60bn+.",
        "450,000+ sqm of Grade A offices, roughly doubling the island's supply.",
        "3,000+ waterfront homes, hotels and a marina."]},
    {"t": "stat", "num": "50K", "label": "Professionals", "head": "Why it matters for property", "bullets": [
        "Nearly 50,000 people now work in ADGM.",
        "High earners need homes close to the office.",
        "Al Reem was Abu Dhabi's top area by sales value in 2026 so far."]},
    close("Funds are arriving and they need homes. Want to see what's available on Al Reem and Al Maryah?", 'DM "ADGM" FOR OPTIONS'),
],
    caption="Wall Street is moving to Al Maryah Island 💼 BlackRock, Blackstone, J.P. Morgan, Goldman Sachs, Brevan Howard and more now have a presence in ADGM.\n\nSave it and send it to someone in finance.\n\nDM \"ADGM\" for homes on Al Reem and Al Maryah.\n\n#ADGM #AbuDhabi #AlMaryahIsland #AlReemIsland #AbuDhabiRealEstate",
    linkedin_caption="ADGM ended H1 2026 with 13,974 active licences, a workforce of 49,027 (up 34%) and assets under management up 54% year on year.\n\nThe names on its register include BlackRock, Blackstone, J.P. Morgan, Goldman Sachs, Apollo, Brevan Howard and Marshall Wace. To keep up, Mubadala and Aldar have announced an AED 60bn+ expansion of Al Maryah Island that roughly doubles its Grade A office supply and adds 3,000+ homes.\n\nWhere the financial industry goes, demand for quality housing follows."))

D.append(dict(day=20, date="2026-12-04", folder="day20", art="difc", slides=[
    {"t": "cover", "tag": "FINANCE", "title": "DIFC 2.0:", "gold": "the AED 100bn Zabeel District", "sub": "Dubai's financial centre is doubling down."},
    {"t": "stat", "num": "10,018", "label": "Active companies, mid-2026", "head": "DIFC today", "bullets": [
        "Over 10,000 companies for the first time.",
        "1,134 regulated financial firms.",
        "102 hedge funds at the end of 2025, the most in the region."]},
    {"t": "stat", "num": "17.7M", "label": "Sq ft of floor space", "head": "Zabeel District", "bullets": [
        "Launched by Sheikh Mohammed bin Rashid in January 2026.",
        "More than AED 100bn in development value.",
        "Room for 42,000+ companies and 125,000+ workers."]},
    {"t": "list", "label": "What's planned", "head": "Inside Zabeel District", "bullets": [
        "Offices, homes and hotels along a central boulevard.",
        "An AI Campus, plus over 1M sq ft for AI and future tech.",
        "A bigger DIFC Academy, a conference centre and retail.",
        "An art pavilion, green spaces and a bridge to the Gate District."]},
    {"t": "stat", "num": "2030", "label": "Timeline", "head": "When it opens", "bullets": [
        "Phase 1: about AED 20bn and 3.7M sq ft, finishing in 2029 to 2030.",
        "Public opening expected in 2030.",
        "Six phases, with the full masterplan by 2040."]},
    {"t": "stat", "num": "463", "label": "Homes", "head": "Sold out at launch", "bullets": [
        "The Residences, Zabeel District's first homes, sold out in February 2026.",
        "1 to 4 bedroom apartments, duplexes and penthouses.",
        "Homes near DIFC remain some of the most sought after in Dubai."]},
    close("DIFC is growing and the homes around it are in demand. Want first look at the next launches nearby?", 'DM "DIFC" FOR EARLY ACCESS'),
],
    caption="DIFC 2.0: the AED 100bn Zabeel District 🏦 17.7M sq ft, room for 125,000+ workers, and its first homes sold out at launch.\n\nSave it and share it with someone who works in DIFC.\n\nDM \"DIFC\" for early access to launches nearby.\n\n#DIFC #ZabeelDistrict #DubaiRealEstate #Dubai #DubaiProperty",
    linkedin_caption="DIFC passed 10,000 active companies in H1 2026, and in January Sheikh Mohammed bin Rashid launched its next chapter: Zabeel District, an AED 100bn+, 17.7M sq ft expansion with room for 42,000+ companies and 125,000+ workers.\n\nPhase 1 (about AED 20bn) is due in 2029-30, with an AI Campus, a much larger DIFC Academy, hotels and homes. The first residential launch, The Residences (463 homes), sold out on launch day.\n\nDubai's two financial centres are expanding at the same time. That says a lot about where demand is heading."))

for d in D:
    d["slides_count"] = len(d["slides"])
Path(__file__).with_name("content.json").write_text(json.dumps(D, ensure_ascii=False, indent=1))
print(len(D), [d["slides_count"] for d in D])
