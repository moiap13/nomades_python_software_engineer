import hashlib
import string
import time

def brute_force_password(charset, length, target_hash):
    start_time = time.time()

    # Essayer toutes les combinaisons possibles en utilisant des boucles imbriquées
    for a in charset:
        for b in charset:
            for c in charset:
                for d in charset:
                    for e in charset:
                        password = a + b + c + d + e  # Combiner les caractères pour former le mot de passe
                        password_hash = hashlib.sha256(password.encode()).hexdigest()  # Calculer le hash du mot de passe actuel
                        
                        if password_hash == target_hash:  # Si le mot de passe est correct
                            return password, time.time() - start_time

    return None, time.time() - start_time

# Exemple d'utilisation :
charset = string.ascii_lowercase  # Ensemble des caractères possibles (lettres minuscules)
length = 5  # Longueur du mot de passe
target_hash = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"  # C'est le hash pour le mot de passe "hello"

password, time_taken = brute_force_password(charset, length, target_hash)

if password:
    print("Mot de passe trouvé :", password)
else:
    print("Mot de passe non trouvé.")
    
print("Temps écoulé :", time_taken)
