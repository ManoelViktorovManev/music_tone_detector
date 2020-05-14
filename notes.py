# Code to generate Piano key frequencies. Work for every other instrument.

def get_basics_of_notes():
    return {
        "La":[27.5], 
        "La#/Si_bemol":[29.13524], 
        "Si":[30.86771],
        "Do":[32.70320], 
        "Do#,Re_bemol":[34.64783], 
        "Re":[36.70810],
        "Re#,Mi_bemol":[38.89087],
        "Mi":[41.20344],
        "Fa":[43.65353],
        "Fa#/Sol_bemol":[46.24930],
        "Sol":[48.99943],
        "Sol#/La_bemol":[51.91309],  
    }
def create_piano_key_freq(dict):
    for element in dict:
        if element == "La" or element == "La#/Si_bemol" or element == "Si":
            for x in range(7):
                dict[element].append(dict[element][-1]*2)
        else:
            for x in range(6):
                dict[element].append(dict[element][-1]*2)
    return dict




asdf=get_basics_of_notes()
create_piano_key_freq(asdf)
for i in asdf:
    print asdf[i]