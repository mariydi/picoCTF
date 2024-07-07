import hashlib

username_trial = "MORTON"
bUsername_trial = b"MORTON"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"


key = [4,5,3,6,2,7,1,8]

for i in key:
    key_part_static1_trial += hashlib.sha256(bUsername_trial).hexdigest()[i]

key_part_static1_trial += key_part_static2_trial

print(key_part_static1_trial)
